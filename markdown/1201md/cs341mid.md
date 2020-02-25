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

little-\\(o\\).
\\[
\lim_{n\to\infty} {f(n)\over g(n)}=0 \implies f=o(g)
\\]
