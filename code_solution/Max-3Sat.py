import itertools
from timeit import default_timer as timer
import math


def max_3Sat(num_variables, clauses):
    # Fill default list
    variables = [1 for _ in range(num_variables)]
    max = 0
    # Make all combinations to get the correct answer
    all_combinations = itertools.product([1, -1], repeat=num_variables)
    for combination in all_combinations:
        clauses_satisfied = max_3Sat_helper(combination, clauses)
        if clauses_satisfied == len(clauses):
            # Return the answer if all clauses are satisfied
            return combination, clauses_satisfied
        elif clauses_satisfied > max:
            variables = combination
            max = clauses_satisfied

    return variables, max


def greedy_3sat(num_variables, clauses):
    # Fill default list
    variables = [1 for _ in range(num_variables)]
    # variables = [random.choice([-1, 1]) for _ in range(num_variables)]
    satisfied = max_3Sat_helper(variables, clauses)

    for _ in range(math.ceil((2 ** num_variables) / num_variables)):
    # for _ in range(2 ** num_variables):
    # for _ in range((2 ** num_variables)):
    # for _ in range(10):
        for i in range(num_variables):
            # Flip the value of variable i
            variables[i] *= -1
            new_satisfied = max_3Sat_helper(variables, clauses)
            if new_satisfied == len(clauses):
                return variables, new_satisfied
            # If flipping improves the count, keep it
            if new_satisfied > satisfied:
                satisfied = new_satisfied
            else:
                # Revert value if it doesn't improve
                variables[i] *= -1

    return variables, satisfied


def max_3Sat_helper(variables, clauses):
    clauses_satisfied = 0

    for i in range(len(clauses)):
        for j in range(len(clauses[i])):
            variable_index = abs(clauses[i][j]) - 1
            if clauses[i][j] * variables[variable_index] > 0:
                clauses_satisfied += 1
                break

    return clauses_satisfied


def format_time(seconds):
    minutes = round(seconds // 60)
    return f"Time: {minutes} {'Minute' if minutes == 1 else 'Minutes'} {round(seconds % 60, 2)} Seconds\n"


def format_variables(variables):
    for i in range(len(variables)):
        print(i + 1, 'T' if variables[i] > 0 else 'F')


def main():
    num_variables, num_clauses = [int(x) for x in input().split()]
    clauses = []

    for _ in range(num_clauses):
        clause = [int(x) for x in input().split()]
        clauses.append(clause)

    print(f"\n\n{num_variables} Variables {num_clauses} Clauses")
    print("-" * 50)
    print("\nOPTIMIZED\n")
    startO = timer()
    variables, max = max_3Sat(num_variables, clauses)
    endO = timer()

    print(format_time(endO - startO))
    # print(endO - startO)
    print(max)

    format_variables(variables)

    print("\nGREEDY\n")

    startG = timer()
    variables, max = greedy_3sat(num_variables, clauses)
    endG = timer()

    print(format_time(endG - startG))
    # print(endG - startG)
    print(max)

    format_variables(variables)


if __name__ == "__main__":
    main()