# def main():
#     clauses = [[1, -2, 3], [-1, 2, -3]]
#     variables = [-1, 1, -1]
#     print(max_3Sat_helper(variables, clauses))

# def max_3Sat_helper(variables, clauses):
#     clauses_satisfied = 0
#     for i in range(len(clauses)):
#         for j in range(len(variables)):
#             if clauses[i][j] * variables[j] > 0:
#                 clauses_satisfied += 1
#                 break
#     return clauses_satisfied

# if __name__ == "__main__":
#     main()
from timeit import default_timer as timer
import itertools


def main():
    num_variables, num_clauses = [int(x) for x in input().split()]
    clauses = []

    for _ in range(num_clauses):
        clause = [int(x) for x in input().split()]
        clauses.append(clause)

    print("\nCOMBINATIONS\n")

    startC = timer()
    combinations = max_3Sat_combinations(num_variables)
    total = 0
    for combination in combinations:
        total += 1
        # print(combination)
    endC = timer()
    print(total)
    combination_time = endC - startC
    print(combination_time)

    print("\nLOOP\n")

    startB = timer()
    variables, max = max_3Sat_loop(num_variables, clauses)
    endB = timer()
    body_time = endB - startB
    print(body_time)

    print(f"{round((combination_time / body_time) * 100, 2)}%")

    print("\nRESULTS\n")

    print(max)

    for i in range(len(variables)):
        print(i + 1, 'T' if variables[i] > 0 else 'F')


def max_3Sat_loop(num_variables, clauses):
    variables = [1 for _ in range(num_variables)]
    max = 0
    # Make all combinations to get the correct answer
    all_combinations = itertools.product([1, -1], repeat=num_variables)
    for combination in all_combinations:
        # print(combination)
        clauses_satisfied = max_3Sat_helper(combination, clauses)
        if clauses_satisfied == clauses:
            # Return the answer if all clauses are satisfied
            return combination, clauses_satisfied
        elif clauses_satisfied > max:
            variables = combination
            max = clauses_satisfied

    return variables, max




def max_3Sat_combinations(num_variables):
    return itertools.product([1, -1], repeat=num_variables)

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


def max_3Sat_helper(variables, clauses):
    clauses_satisfied = 0

    for i in range(len(clauses)):
        for j in range(len(clauses[i])):
            variable_index = abs(clauses[i][j]) - 1
            if clauses[i][j] * variables[variable_index] > 0:
                clauses_satisfied += 1
                break

    return clauses_satisfied

if __name__ == "__main__":
    main()