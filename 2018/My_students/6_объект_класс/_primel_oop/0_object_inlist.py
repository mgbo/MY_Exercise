class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __lt__(self, other):
        return self.x, self.y < other.x, other.y

    def __eq__(self, other):
        return self.x, self.y == other.x, other.y


points = [Point(x, y) for x in range(2, 0, -1) for y in range(3, 0, -1)]

print('Not sorted:', ', '.join(map('({0.x}, {0.y})'.format, points)))
print('Sorted:', ', '.join(map('({0.x}, {0.y})'.format, sorted(points))))
