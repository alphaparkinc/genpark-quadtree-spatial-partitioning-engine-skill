"""Recursive 2D Quadtree Spatial Partitioning Engine.
100% Python Standard Library.
"""

class Quadtree:
    """Recursive 2D Quadtree spatial decomposition."""
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self, pt):
        x, y, w, h = self.boundary
        px, py = pt
        if not (x <= px <= x + w and y <= py <= y + h):
            return False
        if len(self.points) < self.capacity and not self.divided:
            self.points.append(pt)
            return True
        if not self.divided:
            self._subdivide()
        return (self.nw.insert(pt) or self.ne.insert(pt) or
                self.sw.insert(pt) or self.se.insert(pt))

    def _subdivide(self):
        x, y, w, h = self.boundary
        hw, hh = w / 2, h / 2
        self.nw = Quadtree((x, y, hw, hh), self.capacity)
        self.ne = Quadtree((x + hw, y, hw, hh), self.capacity)
        self.sw = Quadtree((x, y + hh, hw, hh), self.capacity)
        self.se = Quadtree((x + hw, y + hh, hw, hh), self.capacity)
        self.divided = True
        for pt in self.points:
            self.nw.insert(pt) or self.ne.insert(pt) or self.sw.insert(pt) or self.se.insert(pt)
        self.points = []
