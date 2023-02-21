import copy

class Item:
    def __init__(self, values):
        self.name = values[0]
        self.points = int(values[1])
        self.weight = int(values[2])
        self.volume = int(values[3])
        # self.name = None
        # self.points = None
        # self.weight = None
        # self.volume = None

    def get_points(self):
        return int(self.points)

class Knapsack(Item):
    items = []
    points = 0
    weight = 0
    volume = 0


    def __init__(self, max_weight, max_volume):
        self.max_weight = max_weight
        self.max_volume = max_volume

    def test_add(self, item):
        if self.weight + item.weight > self.max_weight:
            return False
        elif self.volume + item.volume > self.max_volume:
            return False
        else:
            return True

    def add(self, item):
        if self.test_add(item) == False:
            return False

        self.points += item.points
        self.weight += item.weight
        self.volume += item.volume
        self.items.append(item)
        return True

    def save(self, solution_file):
        file = open(solution_file, "w")
        file.write("points:"+str(self.points)+"\n")
        for item in self.items:
            file.write(item.name+"\n")
        file.close

    def copy(self):
        return Knapsack(self.max_weight, self.max_volume)

    def empty(self):
        self.items = []
        self.points = self.weight = self.volume = 0
    def pop(self):
        return self.items.pop()


class Solver:
    knapsack = None
    iterations = 3


    def __init__(self, alg):
        self.alg = alg

    def test_knapsack(self, knapsack):
        if self.knapsack == None:
            self.knapsack = copy.deepcopy(knapsack)
        elif self.knapsack.points < knapsack.points:
            self.knapsack = copy.deepcopy(knapsack)


    def solve(self, knapsack, items):
        for _ in range(self.iterations):
            test_knapsack = self.alg(knapsack, items)
            self.test_knapsack(test_knapsack)
            test_knapsack.empty()

    def get_best_knapsack(self):
        return self.knapsack
