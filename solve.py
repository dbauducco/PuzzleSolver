import copy

class Solve:

    def __init__(self, puzzle):

    def run(self):
        print("++ " + str(len(self.pieces)))

        if len(self.pieces) > 0:
            self.newBranches()
        else:
            self.kill()

    def newBranches(self):
        for x in range(len(self.pieces)):
            p1 = self.pieces[x]
            print(p1)
            p2 = self.rotate(p1)
            p3 = self.rotate(p2)
            Solve(self.tris, self.pieces.pop(x))

    def kill(self):
        print("-- Killed")

    ## Util Methods
    def rotate(self, o):
        x = o[0]
        y = o[1]
        z = o[2]

        return (y, z, x)

    ## Checks to make sure all the corners add up ( -> Bool )
    ## True - Everything checks out
    ## False - A corner doesn't add up
    ## Could be optimized to check sum every time a new corner is added, but that is for later
    ## TODO: Optimize
    def checksum(self):


        
        vals = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        for t in self.tris:
            vals[t.corners[0]] += t.values[0]
            vals[t.corners[1]] += t.values[1]
            vals[t.corners[2]] += t.values[2]
        for x in range(len(vals)):
            if (x + 1) < vals[x]:
                return False
        return True