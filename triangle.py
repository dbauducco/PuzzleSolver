class Triangle:
    corners = (0,0,0)
    values = (0,0,0)
    isEmpty = True

    def __init__(self, corns):
        self.corners = corns

    def setValues(self, vals):
        self.isEmpty = False
        self.values = vals