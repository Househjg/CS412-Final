import itertools
from timeit import default_timer as timer


# def max_3Sat(num_variables, clauses):
#     # Fill default list
#     variables = [1 for _ in range(num_variables)]
#     max = 0
#     # Make all combinations to get the correct answer
#     all_combinations = itertools.product([1, -1], repeat=num_variables)
#     for combination in all_combinations:
#         clauses_satisfied = max_3Sat_helper(combination, clauses)
#         if clauses_satisfied == clauses:
#             # Return the answer if all clauses are satisfied
#             return combination, clauses_satisfied
#         elif clauses_satisfied > max:
#             variables = combination
#             max = clauses_satisfied

#     return variables, max

def max_3Sat(num_variables, clauses):
    # Fill default list
    variables = [1 for _ in range(num_variables)]
    max = 0
    # Make all combinations to get the correct answer
    all_combinations = itertools.product([1, -1], repeat=num_variables)
    for combination in all_combinations:
        clauses_satisfied = max_3Sat_helper(combination, clauses)
        if clauses_satisfied == clauses:
            # Return the answer if all clauses are satisfied
            return combination, clauses_satisfied
        elif clauses_satisfied > max:
            variables = combination
            max = clauses_satisfied

    return variables, max


# def greedy_3sat(n, clauses):
#     # Fill default list
#     variables = [-1 for _ in range(n)]
#     satisfied = max_3Sat_helper(variables, clauses)

#     for _ in range(2 ** n):
#         for i in range(n):
#             # Flip the value of variable i
#             variables[i] = 1
#             new_satisfied = max_3Sat_helper(variables, clauses)
#             # If flipping improves the count, keep it
#             if new_satisfied > satisfied:
#                 satisfied = new_satisfied
#             else:
#                 # Revert value if it doesn't improve
#                 variables[i] = -1

#     return variables, satisfied

def greedy_3sat(n, clauses):
    # Fill default list
    variables = [-1 for _ in range(n)]
    satisfied = max_3Sat_helper(variables, clauses)

    for _ in range(2 ** n):
        for i in range(n):
            # Flip the value of variable i
            variables[i] = 1
            new_satisfied = max_3Sat_helper(variables, clauses)
            # If flipping improves the count, keep it
            if new_satisfied > satisfied:
                satisfied = new_satisfied
            else:
                # Revert value if it doesn't improve
                variables[i] = -1

    return variables, satisfied


# def max_3Sat_helper(variables, clauses):
#     clauses_satisfied = 0

#     for i in range(len(clauses)):
#         for j in range(len(variables)):
#             if clauses[i][j] * variables[j] > 0:
#                 clauses_satisfied += 1
#                 break

#     return clauses_satisfied

def max_3Sat_helper(variables, clauses):
    clauses_satisfied = 0

    for i in range(len(clauses)):
        for j in range(len(clauses[i])):
            variable_index = abs(clauses[i][j]) - 1
            if clauses[i][j] * variables[variable_index] > 0:
                clauses_satisfied += 1
                break

    return clauses_satisfied


def main():
    num_variables, num_clauses = [int(x) for x in input().split()]
    clauses = []

    for _ in range(num_clauses):
        clause = [int(x) for x in input().split()]
        clauses.append(clause)

    print()
    print()
    print("OPTIMIZED\n")
    start = timer()
    variables, max = max_3Sat(num_variables, clauses)
    end = timer()
    print(end - start)
    print()
    print(max)

    for i in range(len(variables)):
        print(i + 1, 'T' if variables[i] > 0 else 'F')

    print("\nGREEDY\n")

    start = timer()
    variables, max = greedy_3sat(num_variables, clauses)
    end = timer()
    print(end - start)
    print()
    print(max)

    for i in range(len(variables)):
        print(i + 1, 'T' if variables[i] > 0 else 'F')


if __name__ == "__main__":
    main()