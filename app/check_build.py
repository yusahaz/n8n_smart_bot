import os
import importlib

REQUIRED_MODULES = [
    "app.main",
    "app.core.signal_engine",
    "app.core.patterns.base",
    "app.core.patterns.head_and_shoulders",
    "app.core.patterns.descending_triangle"
]

def check_imports():
    print("🔍 Import path kontrolü başlıyor...\n")
    for module_name in REQUIRED_MODULES:
        try:
            importlib.import_module(module_name)
            print(f"✅ Başarılı: {module_name}")
        except Exception as e:
            print(f"❌ Hata: {module_name} -> {e}")

def check_files():
    print("\n🔍 Dosya varlık kontrolü başlıyor...\n")
    files = [
        "app/__init__.py",
        "app/core/__init__.py",
        "app/core/patterns/__init__.py",
        "app/core/patterns/base.py",
        "app/core/patterns/head_and_shoulders.py",
        "app/core/patterns/descending_triangle.py",
        "app/core/signal_engine.py"
    ]
    for f in files:
        if os.path.exists(f):
            print(f"✅ Var: {f}")
        else:
            print(f"❌ Eksik: {f}")

if __name__ == "__main__":
    check_imports()
    check_files()
