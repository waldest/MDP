class ValueIterateAlgorithm():
    def __init__(self, n, m, r, d, a, b, g, gb, ns):
        self.a = float(a)
        self.b = float(b)
        self.discounting = float(d)
        self.n = int(n)
        self.m = int(m)
        self.u = [[0 for i in range(self.n)] for j in range(self.m)]
        self.new_u = list(self.u)
        self.r = r
        self.move = 'UP DOWN LEFT RIGHT'.split()
        self.g = float(g)
        self.gb = float(gb)
        self.ns = float(ns)

    def usability_table(self):
        for pos_y in range(self.m):
            for pos_x in range(self.n):
                if self.r[pos_y][pos_x] == '*':
                    self.usability((pos_x, pos_y))
                elif self.r[pos_y][pos_x] == 'F':
                    self.new_u[pos_y][pos_x] = 0
                elif self.r[pos_y][pos_x] == 'G':
                    self.new_u[pos_y][pos_x] = self.g
                elif self.r[pos_y][pos_x] == 'GB':
                    self.new_u[pos_y][pos_x] = self.gb
        self.new_u, self.u = self.u, self.new_u

    def usability(self, s):
        x, y = s[0], s[1]
        self.new_u[y][x] = round(self.value_of_r(x, y) + self.discounting * max(
            [sum([p * self.u[np[1]][np[0]] for np, p in self.outcomes(a, x, y)])
             for a in self.move]), 3)

    def outcomes(self, a, x, y):
        if a == "UP":
            n = self.neighbours(x, y)
            return [(n[1], self.a), (n[0], self.b), (n[3], self.a)]
        if a == "LEFT":
            n = self.neighbours(x, y)
            return [(n[2], self.a), (n[1], self.b), (n[0], self.a)]
        if a == "DOWN":
            n = self.neighbours(x, y)
            return [(n[3], self.a), (n[2], self.b), (n[1], self.a)]
        if a == "RIGHT":
            n = self.neighbours(x, y)
            return [(n[0], self.a), (n[3], self.b), (n[2], self.a)]

    def neighbours(self, x, y):
        """
        return [up, left, down, right]
        """
        if x == 0 and y == 0:
            res = [(x, y), (x, y), (x, y + 1), (x + 1, y)]
        elif x == self.n - 1 and y == self.m - 1:
            res = [(x, y - 1), (x - 1, y), (x, y), (x, y)]
        elif x == 0 and y == self.m - 1:
            res = [(x, y - 1), (x, y), (x, y), (x + 1, y)]
        elif x == self.n - 1 and y == 0:
            res = [(x, y), (x - 1, y), (x, y + 1), (x, y)]
        elif x == 0:
            res = [(x, y - 1), (x, y), (x, y + 1), (x + 1, y)]
        elif y == 0:
            res = [(x, y), (x - 1, y), (x, y + 1), (x + 1, y)]
        elif x == self.n - 1:
            res = [(x, y - 1), (x - 1, y), (x, y + 1), (x, y)]
        elif y == self.m - 1:
            res = [(x, y - 1), (x - 1, y), (x, y), (x + 1, y)]
        else:
            res = [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]
        return [pos if self.r[pos[1]][pos[0]] != 'F' else (x, y) for pos in res]


    def value_of_r(self, x, y):
        if self.r[y][x] == '*':
            return self.ns
        elif self.r[y][x] == 'F':
            return 0
        elif self.r[y][x] == 'G':
            return self.g
        elif self.r[y][x] == 'GB':
            return self.gb
