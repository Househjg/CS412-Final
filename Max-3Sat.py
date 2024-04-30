import itertools


def max_3Sat(num_variables, clauses):
    variables = [1 for _ in range(num_variables)]
    max = 0
    all_combinations = itertools.product([1, -1], repeat=num_variables)
    for combination in all_combinations:
        clauses_satisfied = max_3Sat_helper(combination, clauses)
        if clauses_satisfied == clauses:
            return combination, clauses_satisfied
        elif clauses_satisfied > max:
            variables = combination
            max = clauses_satisfied

    return variables, max


def max_3Sat_helper(variables, clauses):
    clauses_satisfied = 0

    for i in range(len(clauses)):
        for j in range(len(variables)):
            if clauses[i][j] * variables[j] > 0:
                clauses_satisfied += 1
                break

    return clauses_satisfied


def main():
    num_variables, num_clauses = [int(x) for x in input().split()]
    clauses = []

    for _ in range(num_clauses):
        clause = [int(x) for x in input().split()]
        clauses.append(clause)

    variables, max = max_3Sat(num_variables, clauses)
    print(max)

    for i in range(len(variables)):
        print(i + 1, 'T' if variables[i] > 0 else 'F')


if __name__ == "__main__":
    main()