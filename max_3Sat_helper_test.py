def main():
    clauses = [[1, -2, 3], [-1, 2, -3]]
    variables = [-1, 1, -1]
    print(max_3Sat_helper(variables, clauses))

def max_3Sat_helper(variables, clauses):
    clauses_satisfied = 0
    for i in range(len(clauses)):
        for j in range(len(variables)):
            if clauses[i][j] * variables[j] > 0:
                clauses_satisfied += 1
                break
    return clauses_satisfied

if __name__ == "__main__":
    main()