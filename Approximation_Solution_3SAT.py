def evaluate_clause(clause, values):
    return any(values[abs(x)-1] == (x > 0) for x in clause)

def simple_greedy_sat(n, clauses):
    # Start with random values
    values = [1 for _ in range(n)]
    satisfied = sum(evaluate_clause(clause, values) for clause in clauses)

    for _ in range(2 ** n):
        for i in range(n):
            # Flip the value of variable i
            values[i] = -1
            new_satisfied = sum(evaluate_clause(clause, values) for clause in clauses)
            # If flipping improves the count, keep it
            if new_satisfied > satisfied:
                satisfied = new_satisfied
            else:
                # Revert value if it doesn't improve
                values[i] = 1

    return satisfied, values

def main():
    num_variables, num_clauses = [int(x) for x in input().split()]
    clauses = []

    for _ in range(num_clauses):
        clause = [int(x) for x in input().split()]
        clauses.append(clause)
    
    satisfied, values = simple_greedy_sat(num_variables, clauses)
    print(satisfied)
    for index, value in enumerate(values):
        print(index + 1, 'T' if value > 0 else 'F')

if __name__ == "__main__":
    main()