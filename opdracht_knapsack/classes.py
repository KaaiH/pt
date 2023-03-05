import copy
import random

class Item:
    def __init__(self, values):
        self.name = values[0]
        self.points = int(values[1])
        self.weight = int(values[2])
        self.volume = int(values[3])

    def get_points(self):
        return int(self.points)

    def get_weight(self):
        return int(self.weight)

    def get_volume(self):
        return int(self.volume)

class Knapsack(Item):
    items = []
    points = 0
    weight = 0
    volume = 0
    max_weight = 0
    max_volume = 0


    def __init__(self, max_weight, max_volume):
        self.max_weight = max_weight
        self.max_volume = max_volume


    # def get_max_weight(self):
    #     return int(self.max_weight)

    # def get_max_volume(self):
    #     return self.max_volume


    def add(self, item):

        if self.weight + item.get_weight() > self.max_weight:
            return False
        if self.volume + item.get_volume() > self.max_volume:
            return False
        self.points += item.points
        self.weight += item.weight
        self.volume += item.volume
        self.items.append(item)
        return True

    def pop(self):
        item = self.items.pop()
        self.weight -= item.get_weight()
        self.volume -= item.get_weight()

    def save(self, solution_file):
        file = open(solution_file, "w")
        file.write("points:"+str(self.points)+"\n")
        for item in self.items:
            file.write(item.name+"\n")
        file.close


    def stats(self):
        return self.points, self.weight, self.volume, self.items

    def fill(self, points, weight, volume, items):
        self.points = points
        self.weight = weight
        self.volume = volume
        self.items = items[:]

    def copy_empty(self):
        return Knapsack(self.max_weight, self.max_volume)

    def copy(self):
        copy = self.copy_empty()
        copy.fill(*self.stats())
        return copy

class Solver:
    knapsack = None

    def get_best_knapsack(self):
        return self.knapsack

class Solver_Random(Solver):

    def __init__(self, iterations):
        self.iterations = iterations

    def solve(self, knapsack: Knapsack, items: list[Item]) -> Knapsack:
        for _ in range(self.iterations):
            test_knapsack = knapsack.copy_empty()
            test_knapsack.items = []
            index = list(range(len(items)))
            random.shuffle(index)
            while(test_knapsack.add(items[index.pop(0)])):
                pass
            if test_knapsack.get_points() > knapsack.get_points():
                knapsack = test_knapsack.copy()
        self.knapsack = knapsack

class Solver_Random_improved(Solver_Random):
    def solve(self, knapsack: Knapsack, items: list[Item]) -> Knapsack:
        pass
    pass

class Solver_Optimal_Recursive(Solver):
    def solve(self, knapsack: Knapsack, items: list[Item]) -> Knapsack:
        index = list(range(len(items)))
        best_knapsack = knapsack.copy_empty()
        def dfs(index, items, knapsack):
            nonlocal best_knapsack
            # print(knapsack.get_points())
            if not index:
                return

            i = index.pop()
            dfs(index[:], items, knapsack.copy())

            if knapsack.add(items[i]):
                if knapsack.get_points() > best_knapsack.get_points():
                    best_knapsack = knapsack.copy()
                dfs(index[:], items, knapsack.copy())
                knapsack.pop()

        dfs(index, items, knapsack)
        self.knapsack = best_knapsack


class Solver_Optimal_Iterative_Deepcopy(Solver):
    def solve(self, knapsack: Knapsack, items: list[Item]) -> Knapsack:
        best_knapsack = knapsack.copy_empty()
        stack = [(list(range(len(items))), knapsack.copy())]

        while stack:
            index, current_knapsack = stack.pop()

            if not index:
                continue

            i = index.pop()
            stack.append((index[:], current_knapsack.copy()))

            if current_knapsack.add(items[i]):
                if current_knapsack.get_points() > best_knapsack.get_points():
                    best_knapsack = current_knapsack.copy()
                stack.append((index[:], current_knapsack.copy()))
                current_knapsack.pop()

        self.knapsack = best_knapsack


class Solver_Optimal_Iterative(Solver):

    def solve(knapsack: Knapsack, items: list[Item]) -> Knapsack:
        pass
