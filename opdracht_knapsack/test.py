import random
import copy
from classes import Knapsack, Item, Solver





# fix dubbele iteratie
def load_knapsack(knapsack_file):
    with open(knapsack_file) as file:
        data = []
        kkr = 0
        for line in file:
            if kkr == 0:
                kkr = 1
                continue
            values = Item(line.replace('\n', '').split(', '))
            data.append(values)
        item = data.pop(0)
        knapsack = Knapsack(item.weight, item.volume)
    return knapsack, data


def random_solver(knapsack, items):

    index = list(range(len(items)))
    random.shuffle(index)
    while(knapsack.add(items[index.pop(0)])):
        pass
    return knapsack


def solver_optimal_recursive(knapsack, items):
    stack = copy.deepcopy(items)
    # list of items in the current branch
    stack = []
    index = 0
    start = 0
    points = 0
    most_points = 0
    count = 0
    index = list(range(len(items)))
    branch = []

    def recursive_dfs(index, items, knapsack):
        nonlocal points
        nonlocal most_points
        nonlocal branch

        if len(index) == 0:
            branch.pop
            return

        current_index = index.pop()
        recursive_dfs(index, items, knapsack)

        item = items[current_index]
        if knapsack.test_add(item):
            branch.append(current_index)
            points += item.get_points()
            if points > most_points:
                most_points = points
            recursive_dfs(index, items, knapsack)


        # if knapsack.add(items[current_index]):
        #     print("true")
        #     if knapsack.get_points() > best_score:
        #         best_score = knapsack.get_points()
        #         print("best score:" + str(best_score))
        #     recursive_dfs(index, items, knapsack)
        # else:
        #     knapsack.pop
        #     return

    recursive_dfs(index, items, knapsack)
    print(most_points)
    return most_points







knapsack_file = 'knapsack_medium.csv'
# knapsack_file = 'knapsack_small.csv'
knapsack, items = load_knapsack(knapsack_file)

solver_optimal_recursive(knapsack, items)

solution_file = "solutions.txt"
solver = Solver(random_solver)


solver.solve(knapsack, items)
best_knapsack = solver.get_best_knapsack()

best_knapsack.save(solution_file)
