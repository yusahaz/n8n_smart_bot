import os

PROJECT_ROOT = "app"
EXCLUDE_EXT = [".pyc", ".pyo", ".log", ".txt"]
EXCLUDE_FILES = ["__init__.py"]

def find_py_files():
    py_files = []
    for dirpath, _, filenames in os.walk(PROJECT_ROOT):
        for file in filenames:
            if file.endswith(".py") and file not in EXCLUDE_FILES:
                path = os.path.join(dirpath, file)
                py_files.append(path.replace("\\", "/"))
    return py_files

def search_imports(py_files):
    all_imports = set()
    for path in py_files:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if "import" in line or "from" in line:
                    all_imports.add(line.strip())
    return all_imports

def detect_unused(py_files, all_imports):
    unused = []
    for file in py_files:
        file_name = os.path.basename(file).replace(".py", "")
        # Dosya ismi import edilmiş mi kontrol et
        if not any(file_name in imp for imp in all_imports):
            unused.append(file)
    return unused

if __name__ == "__main__":
    print("🔍 Proje gereksiz dosya kontrolü başlıyor...\n")
    py_files = find_py_files()
    imports = search_imports(py_files)
    unused_files = detect_unused(py_files, imports)

    if unused_files:
        print("⚠ Tespit edilen kullanılmayan dosyalar:")
        for uf in unused_files:
            print(f"❌ {uf}")
    else:
        print("✅ Gereksiz dosya tespit edilmedi!")
