def main():
    num_variables, num_clauses = [int(x) for x in input().split()]
    # print(num_variables)
    # print(num_clauses)
    clauses = []
    for _ in range(num_clauses):
        clause = [int(x) for x in input().split()]
        clauses.append(clause)
    # print(clauses)
    variables, max = max_3Sat(num_variables, clauses)
    print(max)
    # print(variables)
    for i in range(len(variables)):
        print(f"{i + 1} {variables[i]}")

def max_3Sat(num_variables, clauses):
    variables = [1 for _ in range(num_variables)]
    max = 0

    # Go through and call helper function on every possible way of having the variables (T, T, T), (T, T, F)...
    return variables, max

def max_3Sat_helper(variables, clauses):
    return "Number of satisfied clauses"


if __name__ == "__main__":
    main()