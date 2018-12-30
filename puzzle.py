import copy

class Puzzle:
    t = []
    p = []

    def __init__(self, t1, p1):
        self.t = t1
        self.p = p1

    def copy(self):
        tc = copy.deepcopy(self.t)
        pc = copy.copy(self.p)

        c = Puzzle(tc, pc)
        return c

    def setPiece(self, x, i):
        self.t[x].setValues(self.p[i])
        self.p.pop(i)

    def checksum(self):
        vals = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        for x in self.t:
            vals[x.corners[0]] += x.values[0]
            vals[x.corners[1]] += x.values[1]
            vals[x.corners[2]] += x.values[2]
        for y in range(len(vals)):
            if y + 1 < vals[y + 1]:
                return False
        return True

    def nextemptytriangle(self):
        for x in range(len(self.t)):
            if self.t[x].isEmpty:
                return x