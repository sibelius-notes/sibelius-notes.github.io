title: CS 341 - Algorithms (midterm)
---

Check my [scattered notes](../cs341)

# Pre
**Algorithm**: effective unambiguous finite

**solve a problem**: Every instance I of problem P, when alg runs, it outputs a valid soln to P.

- **Line-code model**: Each line takes 1 time step.
- **Bit-cost model**: single bit take 1 step.

Neither is ideal.

**Word Ram model**: The Word RAM model is the computational model
in which for an algorithm run on an input of size \\(n\\),
- the memory of the algorithm is broken up into words of length \\(w=\log n\\), and
- any elementary operation (read, write, add, multiply, AND, etc.) on any single word
in memory takes 1 time step.

Big \\(O, \Omega, \Theta\\) notation.

little-\\(o,\omega\\).
\\[
\lim_{n\to\infty} {f(n)\over g(n)}=0 \implies f=o(g)
\\]

## Reduction

**Idea**: Use known algs to solve new problems.

### 3-sum
sum 3 distinct = 0

Trivial3Sum \\(O(n^3)\\)

Improved3Sum: sort, then binary search \\(-B_i-B_j\\). \\(O(n\log n+n^2\log n)=O(n^2\log n)\\).

Quadratic3Sum:
- sort
- given \\(B[i]\\), simultaneously scan from both ends of \\(A\\) looking for \\(B[j] + B[k] = -B[i]\\).
- start wit \\(j=i+1\\) and \\(k=n\\)
- \\(O(n\log n+n^2)=O(n^2)\\)



### target3sum
sum 3 distinct = T

\\[
(A[i]-T/3)+(A[j]-T/3)+(A[k]-T/3)=0
\\]

Then let \\(B[i]=A[i]-T/3\\).

### 3array3SUM
three arrays of \\(n\\) distinct integers, one from each \\(A,B,C\\) whose sum equals 0.

color them:
\\[
\left \\\\{
\begin{array}{l}
D[i]\gets 10A[i]+1\\\\
E[i]\gets 10B[i]+2\\\\
F[i]\gets 10C[i]-3
\end{array}\right.
\\]

To show ... is a reduction, we show that \\(\alpha\\) is a solution to instance \\(A'\\) **if and only if** \\(\alpha'\\) is a solution to \\(A\\) of ... .
## Terminology
**Running time** can only be determined by implementing a program and
running it on a specic computer.

Running time is influenced by many factors, including the programming
language, processor, operating system, etc.

**Complexity** (AKA growth rate) can be analyzed by high-level
mathematical analysis. It is independent of the above-mentioned factors
aecting running time.
## Loop Analysis
1. Theta-bounds throughout the analysis
2. O and Omega separately

**unit cost model**: where we assume that
arithmetic operations such as \\(+,-,\times\\) and integer division take time \\(\Theta(1)\\).

If we want to consider the complexity of arithmetic operation on integers
of arbitrary size, we need to consider **bit complexity**, where we express the
complexity as a function of the length of the integers (as measured in bits).


# Divide and Conquer
## Recursion
Recursion is a special type of reduction, where we reduce the original problem to the same problem, but on a smaller input.

guess-and-check and recursion tree method.

Use recursion tree, we propose master theorem:
\\(a\\ge 1, b> 1\\). Consider the recurrence
\\[T(n)=aT\\left({n\\over b}\\right) + \\Theta(n^y)\\]
where n is a power of b.

Denote \\(x=\\log_b a\\). Then
\\[
T(n)\\in
\\begin{cases}
\Theta(n^x) &amp; \\text{if}~y&lt;x \\\\
\Theta(n^x\log n) &amp; \text{if} ~y=x \\\\
\Theta(n^y) &amp; \text{if}~y&gt;x.
\\end{cases}
\\]

\\(y<x\\): heavy leaves: the value of the recursion tree is dominated by
the values of the leaf nodes.

balanced: the values of the levels of the recursion tree are
constant (except for the last level).

heavy top: the value of the recursion tree is dominated by the
value of the root node.
