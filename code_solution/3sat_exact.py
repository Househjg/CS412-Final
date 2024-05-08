import itertools
from timeit import default_timer as timer


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

# def max_3Sat_helper2(variables, clauses):
#     clauses_satisfied = 0
#     # Iterate through each clause
#     for clause in clauses:
#         # Check if any literal in the clause is satisfied
#         if any((variables[abs(var) - 1] * var) > 0 for var in clause):
#             clauses_satisfied += 1
#     return clauses_satisfied



def main():
    
    num_variables, num_clauses = [int(x) for x in input().split()]
    clauses = []

    for _ in range(num_clauses):
        clause = [int(x) for x in input().split()]
        clauses.append(clause)
    
    start1 = timer()
    variables, max = max_3Sat(num_variables, clauses)
    end1 = timer()

    print(end1 - start1)
    print(max)

    for i in range(len(variables)):
        print(i + 1, 'T' if variables[i] > 0 else 'F')

    
if __name__ == "__main__":
    main()