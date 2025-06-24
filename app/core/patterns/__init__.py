from .head_and_shoulders import HeadAndShoulders
from .descending_triangle import DescendingTriangle

def get_all_detectors():
    return [
        HeadAndShoulders(),
        DescendingTriangle()
    ]
