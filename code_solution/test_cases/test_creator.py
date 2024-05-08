import random

def generate_test_case(num_vars, num_clauses):
    variables = list(range(1, num_vars + 1))
    clauses = []

    for _ in range(num_clauses):
        clause = []
        while len(clause) < 3:
            var = random.choice(variables)
            if random.random() < 0.5:
                clause.append(var)
            else:
                clause.append(-var)
            clause = list(set(clause))
        clauses.append(clause)

    return clauses

def write_test_case(filename, test_case, num_vars):
    with open(filename, 'w') as f:
        f.write(f"{num_vars} {len(test_case)}\n")
        for clause in test_case:
            f.write(" ".join(map(str, clause)) + "\n")

if __name__ == "__main__":
    num_vars = 10
    num_clauses = 1000

    test_case = generate_test_case(num_vars, num_clauses)
    write_test_case("10_1000.txt", test_case, num_vars)
    print("Test case generated and saved as 'large_test_case.txt'")
