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

# Reduction

**Idea**: Use known algs to solve new problems.

## 3-sum
sum 3 distinct = 0

Trivial3Sum \\(O(n^3)\\)

Improved3Sum: sort, then binary search \\(-B_i-B_j\\). \\(O(n\log n+n^2\log n)=O(n^2\log n)\\).

Quadratic3Sum:
- sort
- given \\(B[i]\\), simultaneously scan from both ends of \\(A\\) looking for \\(B[j] + B[k] = -B[i]\\).
- start wit \\(j=i+1\\) and \\(k=n\\)
- \\(O(n\log n+n^2)=O(n^2)\\)

Recursion is a special type of reduction, where we reduce the original problem to the same problem, but on a smaller input.

## target3sum
sum 3 distinct = T

\\[
(A[i]-T/3)+(A[j]-T/3)+(A[k]-T/3)=0
\\]

Then let \\(B[i]=A[i]-T/3\\).

## 3array3SUM
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
