def main():
    variables, n = [int(x) for x in input().split()]
    print(variables)
    print(n)
    clauses = []
    for _ in range(n):
        clauses.append(input())

    print(clauses)


if __name__ == "__main__":
    main()