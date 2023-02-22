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
    index = list(range(len(items)))
    stack = list()
    points = 0
    most_points = 0
    def recursive(knapsack, items, stack, index, points):
        if not index:
            return

        nonlocal most_points
        current = index.pop()
        print(stack)
        recursive(knapsack, items, stack[:], index[:], points)
        # returns always true
        if knapsack.test_add(items[current]):
            points += items[current].get_points()
            print(stack, points)
            if points > most_points:
                most_points = points




            stack.append(current)
            recursive(knapsack, items, stack[:], index[:], points)


    recursive(knapsack, items, stack, index, 0)
    print(most_points)


# knapsack_file = 'knapsack_medium.csv'
knapsack_file = 'knapsack_small.csv'
knapsack, items = load_knapsack(knapsack_file)

solver_optimal_recursive(knapsack, items)

# solver_optimal_recursive(knapsack, items)







# def solver_optimal_recursive(knapsack, items):
#     index = list(range(len(items)))
#     print(index)
#     branch = []
#     best_branch = []
#     most_points = 0
#     points = 0
#     def recursive_dfs(knapsack, items, index, branch, best_branch, points):
#         nonlocal most_points
#         if not index:
#             return
#         current_index = index.pop()
#         recursive_dfs(knapsack, items, index[:], branch, best_branch, points)
#         item = items[current_index]
#         if knapsack.test_add(item):
#             points += item.get_points()
#             branch.append(current_index)
#             if points > most_points:
#                 most_points = points
#                 best_branch = branch[:]
#             recursive_dfs(knapsack, items, index[:], branch[:], best_branch, points)

#         # return most_points
#     recursive_dfs(knapsack, items, index, branch, best_branch, points)
#     print(most_points)



# def solver_optimal_recursive(knapsack, items):
#     stack = copy.deepcopy(items)
#     # list of items in the current branch
#     best_branch = []
#     index = 0
#     start = 0
#     points = 0
#     most_points = 0

#     index = list(range(len(items)))
#     branch = []

#     def recursive_dfs(index, items, knapsack):
#         nonlocal points
#         nonlocal most_points
#         nonlocal branch
#         nonlocal best_branch

#         if len(index) == 0:
#             branch.pop
#             return#         item = items[current_index]
#         if knapsack.test_add(item):
#             branch.append(current_index)
#             print(branch)
#             points += item.get_points()
#             if points > most_points:
#                 most_points = points
#                 best_branch = branch[:]

#             recursive_dfs(index, items, knapsack)


#         current_index = index.pop()
#         recursive_dfs(index, items, knapsack)

        # item = items[current_index]
        # if knapsack.test_add(item):
        #     branch.append(current_index)
        #     # print(branch)
        #     points += item.get_points()
        #     if points > most_points:
        #         most_points = points
        #         best_branch = branch[:]

        #     recursive_dfs(index, items, knapsack)


#     recursive_dfs(index, items, knapsack)
#     print(most_points)
#     for i in best_branch:
#         print(items[i].name)
#         knapsack.add(items[i])

#     return knapsack








# solution_file = "solutions.txt"
# solver = Solver(random_solver)
# # solver = Solver(solver_optimal_recursive)

# solver.solve(knapsack, items)
# best_knapsack = solver.get_best_knapsack()

# best_knapsack.save(solution_file)
