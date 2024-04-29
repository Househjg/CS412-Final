# CS412-Final
Max 3SAT
The first line of input specifies n the number of variables and m the number of clauses. The n variables are numbered 1 through n. The clauses are encoded as three indices with a minus sign (-) denoting negation (this is why they are numbered from 1 to n, since -0 is well, trouble).

So the clause
### (x1 or !x2 or x3) and (!x1 or x2 or !x3) ###

Would be encoded as:
```
3 2
1 -2 3
-1 2 -3
```
The first line of the output is the number of clauses satisfied, followed by n lines of output give an assignment of T/F to the variables that achieves this count.

Sample Output:
```
2
1 T
2 T
3 F
```
This output corresponds to the claim that if we set x0 to true, x1 to true, and x2 to false, we satisfy two clauses. 
