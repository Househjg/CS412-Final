# CS412-Final
Max 3SAT
The first line of input specifies n the number of variables and m the number of clauses. The n variables are numbered 1 through n. The clauses are encoded as three indices with a minus sign (-) denoting negation (this is why they are numbered from 1 to n, since -0 is well, trouble).

So the clause
### (x1 or !x2 or x3) and (!x1 or x2 or !x3) ###

Would be encoded as:

3 2
1 -2 3
-1 2 -3

The first line of the output is the number of clauses satisfied, followed by n lines of output give an assignment of T/F to the variables that achieves this count.

Sample Output:

2
1 T
2 T
3 F

This output corresponds to the claim that if we set x0 to true, x1 to true, and x2 to false, we satisfy two clauses. 


NP-Complete Project Description
This is a placeholder for the entire description of the final project.  Individual assignments will be created for all submission pieces (or they will be submitted in Github and an assignment will be created in Canvas to represent your grade).

This project will explore an known NP-complete problem and will consist of the following components:

    Problem presentation explaining the problem to be solved and its reduction to another accepted NP-complete problem.
    Solution Code -- develop code that solves the problem with the optimal answer (no approximation).
    Approximation presentation -- show an approximation algorithm for this problem and analyze it.
    Approximation code --  develop code that performs this approximation
    Evaluation of Other Projects  -- you will submit 1 review of other projects.   


Part 1: Problem and Group Selection
-----------------------------------

This is a group project that can have up to 2 members.  If you want to work in a group of 1 or 3, please contact me.  A group of 3 may require additional work.  You will need to select an NP-complete problem for this project.  You should do some research before just selecting one of these problems to make sure you see a way of doing the approximation, etc.  Ideally, we will get a nice distribution of projects across these problems.

    Max 3-Sat
    Max clique
    Traveling Saleman Problem (TSP) with a complete graph
    Longest Path
    Vertex Cover
    Min Graph Coloring

The expectation is that each person in the group will be responsible and be graded on a subset of the following categories.

Part 2: Coding
--------------

    Exact Solution Code

        Develop Python code that provides the optimal solution to the problem you are studying.  You must develop test cases of varying sizes and illustrate how the runtime (wall clock) of your program varies for different size input.  Your test cases must include at least one instance that causes your program to run for more than 20 minutes.

        Make sure you cite in the comments of your program ALL external sources used in the development of your code.

    Approximation Solution Code

        Develop Python code that provides an approximation of the solution. You are allowed to use approximation methods developed by others as long as you cite your sources.  In other words, you do not need to design the approximation yourself (but you will need to write the code yourself).

    Submission 
        Create a folder named code_solution with the GIT repository.  Place your exact solution and approximate solution in this folder including a README file that provides instructions and exact commands to run your code.  Within the code_solution folder, create a test_cases folder that contains all test cases.  Create a shell script named run_test_cases.sh that executes your program on all test cases. 

        You will also need to submit both the exact solution and approximate solution to Gradescope. 
 

Part 3: Presentation
--------------------

    You will present the problem you are solving in class.  This presentation must include:
        
        BOTH the decision problem being solved and the optimization problem

        Example inputs and outputs

        why the problem is important (some applications that use this problem)

        an explanation of the certifier process being polynomial

        a reduction from a known/accepted NP-hard problem  (with examples graphically shown)

        explanation of the coded solution in pseudocode: both the exact and the approximate solutions

        An analytical (big-O) runtime analysis of your coded solution and showcase the code that is the dominant term (the section that drives the highest order term).

        A wallclock (empirical) runtime analysis of your code on your test cases.  This analysis must show input size on the X axis and runtime on the Y axis.

        Plots that illustrate the run-time (wall clock) performance of your exact solution versus the approximation solution on your test cases

        Plots that compare the result/solution of your exact solution versus the approximation on your test cases.
    

    Submission 
        Create a folder named presentations with the GIT repository.  This presentation should use slides in either PowerPoint, Keynote, or Google slides (other slides formats can be requested, but are subject to instructor approval).   The slides (or a file with a link to the google slides) should be placed in the git repository. 
 

Rubrics:
--------

    Common Rubric (15 points): Regardless of the role of the student, everyone will have the following rubric items:
        Team formation and problem selection (3 points)

        Student participates in the in-class discussion and supports his team mates (6 points).  1 point for arriving and 1 point for your group submitting to Github each class period.  Students not present in class will be docked 2 points per day unless their absence is coordinated with me in advance.

        Student submits review of other teams project  with constructive and meaningful feedback (4 points)
        Overall project (2 points).

    Exact Solution (18 points):
        Exact solution runs and executes on provided test cases.  Some form of correctness is shown (for small examples, the program produces the correct/expected output).   Examples of how to run these test cases as well as "expected output" files are submitted. (18 points)

    Presenting the exact solution (18 points):
        Problem description and input (w/pictures if possible) (4 points)

        slide shows reduction and student provides a small example to illustrate the reduction (5 points)

        For longest path, student explains why taking the negative weights on all the edges and using bellman-ford does not work (3 points).  

        Sketch Exact Solution (3 points)

        Test Case Generation (3 point)

    Approximation solution (18 points):
        Specify program type in your comments (anytime, random, greedy, etc) (2 points)
        
        Program runs in polynomial time (10 points)
        
        Program makes a reasonable approximation (6 points)
        
        Test cases show that approximation does not always produce optimal solution (and that the approximation "worked" as expected).
    
    Presenting the Approximation solution (18 points):
        explain how the solution works (4 points) and the strategy utilized (anytime, random, greedy, etc.)
        
        provide an example of when the program may not make the optimal choice (6 points).  This involves shown a specific input, the optimal answer and the approximation made by your approach.  This should be one of the test cases from the approximation solution (see above).
        
        provide run time results (exact versus approximation).  If your approximation includes randomness, run your algorithm at least 10 times for each case and showcase the variance in your solutions.  These data should be provided in the form of: (8 points)
            approximation ratio if possible
            a script to run the tests
            a table of results (in a PDF)
            and a plot/graphic for the slides

    Report the progress of your project(5 points)
        Attend the class on Wednesday to report. 
        
    Evaluation of Other Projects (8 points) 
        You need to attend class to evaluate the presentations of other students. 