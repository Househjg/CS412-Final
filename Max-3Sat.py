def main():
    num_variables, num_clauses = [int(x) for x in input().split()]
    print(num_variables)
    print(num_clauses)
    clauses = []
    for _ in range(num_clauses):
        clauses.append(input())
    print(clauses)
    print(max_3Sat(num_variables, clauses))

def max_3Sat(num_variables, clauses):
    variables = [True for _ in range(num_variables)]
    return variables


if __name__ == "__main__":
    main()