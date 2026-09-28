from client import Quadtree

qt = Quadtree((0, 0, 100, 100), capacity=2)
for pt in [(10, 10), (12, 12), (15, 15), (70, 80)]:
    qt.insert(pt)

print("Quadtree subdivided:", qt.divided)
