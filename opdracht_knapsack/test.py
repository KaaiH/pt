import random
import copy
from classes import Knapsack, Item, Solver_Random, Solver_Optimal_Recursive, Solver_Optimal_Iterative_Deepcopy

# class Solver_Random:

#     def __init__(self, iterations):
#         self.iterations = int(iterations)

#     def run(self, knapsack, items):
#         for _ in range(self.iterations):
#             test_knapsack = knapsack.copy_empty()
#             test_knapsack.items = []
#             index = list(range(len(items)))
#             random.shuffle(index)
#             while(test_knapsack.add(items[index.pop(0)])):
#                 pass
#             if test_knapsack.get_points() > knapsack.get_points():
#                 knapsack = test_knapsack.copy()
#         return knapsack



# class Solver_Random_improved(Solver_Random):
#     def run(self, knapsack, items):
#         pass
#     # kutzooi deze moet ik nog maken

# class Solver_Optimal_Recursive:
#     def run(self, knapsack, items)



# fix dubbele iteratie
def load_knapsack(knapsack_file):
    with open(knapsack_file) as file:
        data = []
        kkr = 0
        # next(file)
        for line in file:
            if kkr == 0:
                kkr = 1
                continue
            values = Item(line.replace('\n', '').split(', '))
            data.append(values)
        item = data.pop(0)
        knapsack = Knapsack(item.get_weight(), item.get_volume())
    return knapsack, data


# def random_solver(knapsack: Knapsack, items: list[Item], iterations: int) -> Knapsack:
#     for _ in range(iterations):
#         test_knapsack = knapsack.copy_empty()
#         index = list(range(len(items)))
#         random.shuffle(index)
#         while(test_knapsack.add(items[index.pop(0)])):
#             pass
#         if test_knapsack.get_points() > knapsack.get_points():
#             knapsack = test_knapsack.copy()
#     return knapsack





def dfs_show(s, depth):
    print(s)
    if not len(s) == depth:
        # for i in ['L', 'R']:
        #     s.append(i)
        #     dfs_show(s, depth)
        #     s.pop()
        s.append('L' + str(len(s)))
        dfs_show(s, depth)
        s.pop()
        s.append('R' + str(len(s)))
        dfs_show(s, depth)
        s.pop()
# dfs_show([], 4)



def solver_optimal_recursive1(knapsack: Knapsack, items: Item) -> Knapsack:
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

    # dfs(index, items, knapsack)

    def dfs2(knapsack, items):
        nonlocal best_knapsack
        if not items:
            return
        i = items.pop()
        dfs2(knapsack.copy(), items[:])
        if knapsack.add(i):
            if knapsack.get_points() > best_knapsack.get_points():
                best_knapsack = knapsack.copy()
            dfs2(knapsack.copy(), items[:])
            knapsack.pop()

    def dfs3(knapsack, items, index):
        nonlocal best_knapsack
        if not index:
            return
        i = items[index.pop()]
        dfs3(knapsack.copy(), items, index[:])
        if knapsack.add(i):
            if knapsack.get_points() > best_knapsack.get_points():
                best_knapsack = knapsack.copy()
            dfs3(knapsack.copy(), items, index[:])
            knapsack.pop()


    dfs2(knapsack, items)
    # dfs3(knapsack, items, index)
    return best_knapsack


def dfs4(knapsack, items):
    best_knapsack = knapsack.copy_empty()
    stack = []
    stack.append([knapsack.copy(), items])

    while stack:
        current_knapsack, current_items = stack.pop()
        if not current_items:
            continue

        i = current_items.pop()
        stack.append([knapsack.copy(), current_items[:]])

        if current_knapsack.add(i):
            if current_knapsack.get_points() > best_knapsack.get_points():
                best_knapsack = current_knapsack.copy()
            stack.append([current_knapsack.copy(), current_items[:]])

    return best_knapsack


def solver_optimal_iterative1(knapsack: Knapsack, items: Item) -> Knapsack:
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

    return best_knapsack








def solve(solver, knapsack_file, solution_file):
    """ Uses 'solver' to solve the knapsack problem in file
    'knapsack_file' and writes the best solution to 'solution_file'.
    """
    knapsack, items = load_knapsack(knapsack_file)
    solver.solve(knapsack, items)
    knapsack = solver.get_best_knapsack()
    knapsack.save(solution_file)

solver_random = Solver_Random(1000)
solver_optimal_recursive = Solver_Optimal_Recursive()
solver_optimal_iterative = Solver_Optimal_Iterative_Deepcopy()
# solve(solver_optimal_iterative, "knapsack_large.csv", "solutions.csv")

knapsack, items = load_knapsack("knapsack_large.csv")
# best_knapsack = dfs4(knapsack, items)
best_knapsack = solver_optimal_iterative1(knapsack, items)
# best_knapsack = solver_optimal_recursive1(knapsack, items)
best_knapsack.save("solutions.csv")