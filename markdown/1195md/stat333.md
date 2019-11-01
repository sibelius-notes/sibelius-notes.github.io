title: Applied Probability
---



# Lecture 2

* Prob model
* independence

## Introduction

### Basic concepts of prob theory

#### **Prob model**

it has three components: sample space, events, prob function

* **Sample space**: all possible outcomes of a random experiment

Eg: toss a die once. sample space = {1,2,3,4,5,6}

**Events**: roughly speaking: event = subset of sample space
Eg: E = {2,4,6} = outcome is even

**prob function**: Notation $P$
prob function is a function of event & it satisfies 3 conditions

1. $0\le P(E)\le 1$  for any event $E$

2. $P(sample ~space) = 1$

3. additivity
   Suppose we have a sequence of disjoint events, $E_1, E_2, \ldots$, i.e. $E_i\cap E_j=\emptyset, i\neq j$, then $P(\bigcup_{i=1}^\infty E_i) = \sum_{i=1}^\infty P(E_i)$


   Eg: toss a dice and define $P(E) = {\text{# of outcoms in E} \over 6} \implies P$ is prob function

**properties of prob function **

1. If $E_1 \subset E_2$, then $P(E_1) \leq P(E_2)$
2. If $E_1\cap E_2 = \emptyset$, then $P(E_1\cup E_2) = P(E_1) + P(E_2)$
3. $P(\emptyset) = 0$
4. $P(E)+P(E^C) = 1$ ($E^C$: complementary set of $E$)
5. $P(E_1\cup E_2) = P(E_1)+P(E_2)-P(E_1\cap E_2)$

#### **Indepdence**

Suppose we have two events $E \& F$. They are independent if $$\underbrace{P( E\cap F) }_{joint ~ prob} = P(E) * P(F)$$

The latter one is marginal probs or unconditional probs.



Independent $\implies$ joint = product of marginals.
More than two envents will not be covered.



**A simple and useful fact**

Suppose we have a sequence of independent trials and a sequence of events $E_1,E_2,\ldots$

Now: $E_i$ only depends on its trial

Then: $E_1, E_2,\ldots$ are independent
and $$\displaystyle P\left(\bigcap_{i=1}^\infty E_i\right) = \prod_{i=1}^\infty P(E_i) \qquad P\left(\bigcap_{i=1}^m E_i\right) = \prod_{i=1}^m P(E_i) $$



# Lecture 3

## conditional prob

**defn**: Suppose we have two events: $E\& F \& P(F)>0$, then $P(E|F) = \dfrac{P(E\cap F)}{P(F)}$

* Result1: $P(E\cap F) = P(E|F) P(F)$ [multiplication rule]
* Result2: If $E\&F$ are independent, the $P(E|F)=P(E)$

## Bayesian formula

Suppose  we have a sequence of events $F_1,F_2,\ldots$, such that
$$
\begin{cases}
\bigcup_i F_i = \text{sample space} \\
F_i\cap F_j = \emptyset &i\neq j \\
P(F_i)>0
\end{cases}
$$
Then
$$
\begin{equation*}
\begin{split}
P(E) &=\sum_iP(E\cap F_i) \\
&=\sum_i P(E|F_i)P(F_i) \\
\end{split}
\implies
P(E)=\sum_iP(E|F_i) P(F_i)
\end{equation*}
$$
Law of total prob. [divide and conquer method]

Next:
$$
\begin{equation}
\begin{split}
P(F_k|E) &= {P(E\cap F_k) \over P(E)} \\
&= {P(E|F_k) P(F_k) \over \sum_i P(E|F_i)P(F_i)}
\end{split}
\end{equation}
$$

## random variables

**Def**: A rv is a function defined on sample space to real time

X: sample space (domain) -> real time (range)

### two types of rvs in this course

1. Discrete: all possible values are at most countable (possion rv)
2. Conitinuous: all possible values contain an interval (exponential distribution)

Next: important rvs

# Lec 4

## Bernulli Trails

(1) each trail has 2 outcomes: $S$ & $F$.
(2) all trails are independent
(3) prob of $S$ on each trial are the same.

**Notation** $p = Pr(``S") ~~ ~~q = 1-p=Pr(``F")$

**Bernoulli rvs** Notation Bernoulli (p)

Let
$$
I_i=\begin{cases}
1 & \text{if S appears on the ith trail} \\
0 & \text{otherwise}
\end{cases}
$$
Then $Pr(I_i=1)=p$ & $P_r(I_i=0)=q$  & $I_1,I_2,\ldots,I_n,\ldots$ are a sequence of iid (independent identically distributed) Bernoulli rvs.

## Binomial rv

Notation $Bin(n,p)$

$X=$# of "S" in $n$ Bernoullli trials $\sim Bin(n,p)$
n = # of Bernoulli trials [fixed]          p is prob of "S"

**Range** $\{0,1,\ldots,n\}$         $P(X=k)=\underbrace{\binom{n}{k}p^k(1-p)^{n-k}}_{\text{prob mass function}}$     $k=0,1,2,\ldots, n$



* Result 1:$X=\sum_{i=1}^n I_i$ where $I_1,\ldots, I_n$ are iid Bernoulli rvs, $X$ is binomial
* Result 2: If $X_1\sim Bin(n_1,p), X_2\sim Bin(n_2,p)$ and they are independent, then $X_1+X_2 \sim Bin(n_1+n+2,p)$

Why?

$X_1=$ # of "S" in first $n_1$ trials (Bernoulli trials)
$X_2=$ # of "S" in next $n_2$ trials (Bernoulli trials)

**Indepdent** no overlaps between two groups of trials

## Geometric rv

Geo(p)

First waiting time rv

$X=$ # of **_trials_** to get first "S" in the sequence of Bernoulli trials

Range of $X=\{1,2,\ldots\}$       $E[X]={1\over p}$

prob mas function $P(X=k)=(1-p)^{k-1} p$      $k=1,2,3,\ldots$

**property** No-memory property

$P(X>n+m|X>m)=P(X>n)=P(X-m>n|X>m)$

* $X>m$ : at time $m$ , we don't observe "S"
* $X-m$ : remaining time

**Formula tells us**  given that we don't observe the event "S", the remaining time $\sim Geo(p)$

**That is** As long as we don't observe the event, remaining time and original time have same distribution $Geo(p)$ s

# Lec 5

## Negtive Binomial


$NegBin(r, p)$ & $X=\sum_{i=1}^v X_i:$ $X_1, \ldots, X_v$ are iid Geo(p) rvs

## Possion rv: pois ($\lambda$)

Range of X = {0, 1, 2, ...}

pmf: $P(X=k)= {\lambda^k e^{-\lambda} \over k!}$  $k=0,1,2,\ldots$

**Here** $\lambda$ (1)rate parameter (2) $\lambda=E(X)$

**Property** Suppose $X_1\sim pois(\lambda_1) \& X_2\sim pois (\lambda_2)$ and they are independent, then $X_1+X_2 \sim pois(\lambda_1+\lambda_2)$

## Exponential rv: $\exp(\lambda)$

The continuous waiting time rv.

probability density function (pdf):
$$
f(x)=\begin{cases}
\lambda e^{-\lambda x} & x>0 \\
0 & otherwise
\end{cases}
$$
**properties **: (a) $\lambda$: rate parameter = ${1\over expectation}$     
               $E(x)={1\over \lambda}$ if $X\sim \exp(\lambda)$

​                 (b) tail prob: $P(X >t) = e^{-\lambda t}\qquad t>0$  (at time t, we don't observe the event)

​					(c) No-memory property: missing pic


**No memory property meaning** : As long as we don't observe the event, Remaining time $k$ original time both $\sim \exp(\lambda)$

## Expectation & Variance

**Discrete rv**: $X$ with range $\{x_0, x_1,\ldots, x_n, \ldots\}$
Then $E(x)= \sum_{i=0}^\infty \underbrace{x_i}_{value} \times P(X=x_i)$

**Continous rv**: $X$ with pdf f(x), then $\displaystyle E(x)= \int_{-\infty}^\infty x f(x)dx$

**General case**: $E[g(x)]$       $g(x)$ is a real-function
$$
E[g(x)]=\begin{cases}
\sum_{i=0}^\infty g(x_i)P(X=x_i) & \text{discrete case} \\
\int_{-\infty}^\infty g(x) f(x)dx & \text{continuous case}
\end{cases}
$$
**variance**: $var[X]=E[(X-E(X))^2] = E(X^2)-E^2(X)$

**covariance** $cov(X,Y)=E[(X-E(X))(Y - E(Y))] = E(XY)-E(X)E(Y)$

If X and Y are independent, then $cov(X,Y)=0$

**Properties**:

1. $E[\sum_{i=1}^n a_i X_i] = \sum_{i=1}^n a_i E(X_i)$   Linearity
   $a_1, \ldots, a_n$ are constants and $X_1,\ldots, X_n$ are rvs

2. If $X_1, \ldots, X_n$ are independent, $var(\sum_{i=1}^n a_i X_i) = \sum_{i=1}^n a_i^2 ~~var(X_i)$

3. In general:
   $$
   var(\sum_{i=1}^n a_i X_i) = \sum{i=1}^n a_i^2 ~~var(X_i) + \sum_{i\neq j} a_i a_j ~cov (X_i, X_j) \\
   =\sum{i=1}^n a_i^2 ~~var(X_i) + 2\sum_{i< j} a_i a_j ~cov (X_i, X_j)
   $$


# Lec 6

## indicator rvs

**Indication rv** only two variables 0 & 1

For a given event A, we define
$$
I_A =\begin{cases}
1 & \text{if A occurs} \\
0 & otherwise
\end{cases}
$$
Let $P(A)=p \implies P(I_A=1)= p \qquad \& \qquad P(I_A=0)=q=1-p$

## chapter 2 waiting time rcs

Suppose we have a sequence of trials & we are interested in observing event E based on trials.



$T_E$ = # of trials or waiting time to observe first E.

Range of $T_E=\underbrace{\{1,2,\ldots\}}_{we~can~observe~E}\cup \underbrace{\{\infty\}}_{we~can't}$

We are intersted in

1. If $P(T_E < \infty) < 1$ or $P(T_E=\infty)>0$
2. If $P(T_E < \infty) = 1$ , what is $E(T_E)$?

**Classification of $T_E$**

1. If  $P(T_E < \infty) < 1$ , then $T_E$ is improper

2. If $P(T_E < \infty) =1$, then $T_E$ is proper

   2.1 If $E(T_E)=\infty$, $T_E$ is NULL proper

   2.2 If $E(T_E)<\infty$, $T_E$ is short proper

# Lec 7

1. If $T_E$ is improper, then $E(T_E)=\infty$  . since
   $$
   E(T_E) = \\1*P(T_E=1)+2*P(T_E=2)+\ldots+\underbrace{\infty*P(T_E=\infty)}_{=\infty} = \infty
   $$

2. If $E(T_E)<\infty$, then $T_E$ is short proper, we do not need to verify $P(T_E<\infty)=1$



**Aside**
$$
\sum_{n=1}^\infty a_n = \lim_{m\to\infty} \sum_{n=1}^m a_n \\
\prod_{n=1}^\infty a_n = \lim_{m\to\infty}\prod_{n=1}^ma_n
$$
Note, in $\sum_{n=1}^\infty a_n \& \prod_{n=1}^\infty a_n $, we do not include $\infty$ term. Hence, $P(T_E<\infty)= \sum_{n=1}^\infty P(T_E=n)$



## Chapter 3 Conditional expectation

### 3.1 joint rvs

We consider 2rvs

#### Joint discrete: X & Y

If X & Y are two discrete rvs, then X & Y together is called joint discrete.

* Joint pmf: $f_{X,Y}(x,y)=P(X=x, Y=y)$

* Properties

  * Joint pmf is pmf $\begin{cases} f_{X,Y}(x,y)\ge 0 \\ \sum_x \sum_y  f_{X,Y}(x,y) = 1\end{cases}$

  *

  * $$
    f_X(x)=P(X=x)=\sum_y f_{X,Y}(x,y) \qquad \text{marginal pmf of X}
    \\
    f_Y(y)=P(Y=y)=\sum_x f_{X,Y}(x,y) \qquad \text{marginal pmf of Y}
    $$

* Joint expectation: $E[h(X,Y)]$    $h(x,y)$ is a real function
  $E[h(X,Y)]=\sum_x\sum_y h(x,y)*f_{X,Y}(x,y)$

**EG**  $E(XY)=\sum_x\sum_y xy f_{X,Y}(x,y)$
       $E(X)= \sum_x\sum_y x f_{X,Y}(x,y) = \sum_x x f_X(x)$

#### joint continuous

If X & Y are two continuous rvs and
$$
P(X\le x, Y\le y)=\int_{-\infty}^x\left[\int_{-\infty}^y f_{X,Y}(s,t) dt\right] ds
$$
**properties**

1. $f_{X,Y}(x,y)$ is a pdf

   * $f_{X,Y}(x,y) \ge 0$
   * $\int_{-\infty}^\infty\int_{-\infty}^\infty f_{X,Y}(x,y) dxdy = 1$

2. $\text{}$
   $$
   f_X(x)=\int_{-\infty}^\infty f_{X,Y}(x,y) dy \qquad marginal~pdf~of~X \\
   f_Y(y)=\int_{-\infty}^\infty f_{X,Y}(x,y) dx \qquad marginal~pdf~of~Y
   $$


**expectation**
$$
E[h(X,Y)]=f_X(x)=\int_{-\infty}^\infty \int_{-\infty}^\infty h(x,y) f_{X,Y}(x,y) dx dy \\
E[X]=\int_{-\infty}^\infty \int_{-\infty}^\infty x f_{X,Y}(x,y) dx dy= \int_{-\infty}^\infty x f_X(x)dx
$$
**independence** both discrete and continuous

If $f_{X,Y}(x,y)=f_X(x)f_Y(y)$, then X and Y are independent. i.e. joint = product of marginal

**property** If X and Y are indepdent, $g(X)\& h(Y)$ are independent

# Lec 8

**property**

1. If X & Y are independent, then $g(X)\&h(Y)$ are independent.
2. If X & Y are independent, then $E[g(X)h(Y)]=E[g(X)]E[h(Y)]$

**Note** $Cov(X,Y)=0$ does not imply X & Y are independent.

## 3.2 Conditional distribution & Conditional expectation

* discrete case: notation: $f_{X,Y}(x,y)\to$ joint pmfs

* **Def** For a given $y$, the conditional pmf of $x$ given $Y=y$ is
  $$
  f_{X|Y}(x|y)={f_{X,Y}(x,y)\over f_Y(y)}={Joint\over marginal} \quad f_Y(y)>0
  $$

* Property: $f_{X|Y}(x|y)$ is a pmf
  *That is* (1) $f_{X|Y}(x|y)\ge 0$,  (2) $\sum_x f_{X|Y}(x|y) = 1$

Proof is trivial

**Conditional Expectation**

The conditional expectation of $x$ given $Y=y$ is
$$
E(X|Y=y)=\sum_x*f_{X|Y}(x|y)
$$
The conditional expectation of $g(x)$ given $Y=y$ is
$$
E[g(x)|Y=y]=\sum_x g(x)*f_{X|Y}(x|y)
$$


# Lec 9

### properties of conditional expectation

1. Conditional expectation has all properties of expectation. Eg
   $$
   E(\sum_{i=1}^na_iX_i|Y)=\sum_{i=1}^na_iE(X_i|Y)
   $$

2. Substitution rule
   $$
   E[X*g(Y)|Y=y]=E[X*g(y)|Y=y]\\=g(y)*E(X|Y=y)
   $$
   Eg: $E(X*Y|Y=y)=y*E(X|Y=y)$

   In general: $E(h(X,Y)|Y=y)=E(h(X,y)|Y=y)$

3. Independence property. If X & Y are independent, then
   $$
   f_{X|Y}(x|y)={f_{X,Y}(x,y)\over f_Y(y)}={f_X(x)f_Y(y)\over f_Y(y)}=f_X(x)
   $$

   $$
   \implies E(X|Y=y)=E(x)~~\&\\ E[g(X)|Y=y]=E[g(X)]
   $$



## 3.3 Calculating expectation by conditioning

This section we cover: $E(X)=E[E(X|Y)]$  

​				Law of total expectation/double expectation

**step 1** what is $E(X|Y)?$

(a) $E(X|Y)$ is a rv & dependents on $Y$. say $E(X|Y)=g(Y)\to$ $E(X|Y)$ depends on $Y$.

(b) given $Y=y$, the function of $g(Y)$, $\underbrace{g(y)=E(X|Y=y)}_{\text{in section 3.2}}$

​	**eg** eg3.1: $E(X|Y=y)=y{\lambda_1\over \lambda_1+\lambda_2}\implies g(y)=y{\lambda_1\over \lambda_1+\lambda_2}$

​	  	eg3.2: $E(X|Y=y)={2\over y}\implies g(y)={2\over y}$

**step2** How to get $E(X|Y)$?

(a) figure out $g(y)=E(X|Y=y)$ first by definitions/by properties

(b) $E(X|Y)$ is just $g(Y)$.

**step 3** how to apply $E(X)=E(E(X|Y))$
$$
E(X)=E(E(X|Y))=E[g(Y)]\\
=\begin{cases}
\sum_y g(y)*f_Y(y) & discrete~case\\
\int_{-\infty}^\infty g(y)*f_Y(y)dy & continuous~case
\end{cases}
\\
=\begin{cases}
\sum_y E(X|Y=y)f_Y(y) & discrete~case\\
\int_{-\infty}^\infty E(X|Y=y)*f_Y(y)dy & continuous~case
\end{cases}
$$
**comments:** $E(X)=E[E(X|Y)]$ is applicable to all expectations

# Lec 10

## 3.4 computing prob by conditioning

Suppose A is an event and we are interested in $P(A)$

Let $I_A= \begin{cases} 1 & \text{if A occurs } \\ 0 &\text{otherwise}\end{cases}$
$$
P(A)=E(I_A)=E(E(I_A|Y))\\= \begin{cases}
\sum_y E(I_A|Y=y)f_Y(y)&discrete~Y \\
\int_{-\infty}^\infty E(I_A|Y=y)f_Y(y)dy & continuous~Y
\end{cases} \\
=\begin{cases}
\sum_y E(A|Y=y)f_Y(y)&discrete~Y \\
\int_{-\infty}^\infty E(A|Y=y)f_Y(y)dy & continuous~Y
\end{cases}
$$

# Lec 12

## 3.5 Calculating variance by conditioning

**Method1** By defn

Recall
$$
Var(X)=E(X^2)-[E(X)]^2\\
E(X^2)=E[E(X^2|Y)]\\
E(X)=E[E(X|Y)]
$$
This method has been covered before.

**Method2** Conditional variance.

Given $Y=y$, the coditional variance of $X$ is given as
$$
Var(X|Y=y)=E(X^2|Y=y)-[E(X|Y=y)]^2
$$
**Note** $Var(X|Y=y)$ depends on $y$ and is a function $y$, say
$$
Var(X|Y=y)=h(y)
$$
**EG** $X|Y=y \sim pois(y) \implies Var(X|Y=y)=y \implies h(y)=y$
Then, apply $h(y)$ to $Y$, we get a r.v. This rv is denoted as $Var(X|Y)=h(Y)$

Basically: $Var(X|Y)=h(Y)=E(X^2|Y)-[E(X|Y)]^2$ conditional variance variance of $X$ given $Y$.



Two steps to find $Var(X|Y)$

* Step1: find $h(y)=Var(X|Y=y)$
* Step 2: apply $h(y)$ to $Y$ to get $var(X|Y)=h(Y)$

Comments:

1. Substitution rule is still applcable
2. If X & Y are independent, then $var(X|Y=y)=var(X)$

**THEOREM**
$$
Var(X)=E[\underbrace{var(X|Y)}_{\ge 0}]+var[E(X|Y)]
$$
From $X$ to $E(X|Y)$

1st $E(X)=E(E(X|Y))$

2nd $Var(X)\ge Var(E(X|Y))$

**PROOF**

*LHS* $Var(X)=E(X^2)-[E(X)]^2$
$$
\begin{split}
RHS =& E(var(X|Y)) + var[E(X|Y)]\\
=& E[E(X^2|Y) - \cancel{ \{E(X|Y\}^2}] \\&+ E[\cancel{\{E(X|Y\}^2\}}]-\{E[E(X|Y)]\}^2 \\
=& E(X^2)-[E(X)]^2=LHS
\end{split}
$$


**Method3** Compound rv formula: [random sum of iid rvs]

Suppose $X_1, X_2,\ldots, X_n, \ldots$ are a sequence of iid res.

N: a rv only takes non-negative integers.

**Further** N & $X_1, \ldots$ are independent.

Then $W=\sum_{i=1}^N X_i$: compound rv.  [If $N=0$, then $W=0$]

**Thm**: $E(W)=E(N)* E(X_1) \quad \& \quad var(W)=E(N)* var(X_1)+var(N)*[E(X_1)]^2$

**PROOF**
$$
E(W)=E(E(W|N))\\
\begin{split}
E(W|N=n)&= E\left(\sum_{i=1}^NX_i|N=n\right)\\
&=E\left(\sum_{i=1}^nX_i|N=n\right)\\
&=E\left(\sum_{i=1}^nX_i\right)\\
&= n*E(X_1)
\end{split}
$$

$$
\implies E(W|N)=N*E(X_1)\\
\implies E(W)=E(E(W|N))=E(N*E(X_1))=E(N)*E(X_1)\\
Var(W)=E[Var(W|N)]+Var[\underbrace{E(W|N)}_{N*E(X_1)}]
$$

$Var(W|N)?$
$$
\begin{aligned}
Var(W|N=n)&= var\left(\sum_{i=1}^N X_i |N=n\right) \\
&= var\left(\sum_{i=1}^n X_i |N=n\right) \\
&= var\left( \sum_{i=1}^n X_i\right) \quad X_1,\ldots, X_n\&N~indepdent \\
&= \sum_{i=1}^n var(X_i) \qquad X_1,\ldots, X_n~are~i.i.d\\
&=n*var(X_1)
\end{aligned}
$$

$$
\implies Var(W|N)=N*var(X_1)
$$

**Next**
$$
\begin{split}
Var(W)&=E[var(W|N)]+var[E(W|N)]\\
&=E[N*var(X_1)]+var(N*E(X_1))\\
&=E(N)*var(X_1)+var(N)*[E(X_1)]^2
\end{split}
$$

# Lec 13

examples & advice on midterm1

## ch 4 probability generating function (pgf)

### 4.1 generating function (gf)

**defn** given a sequence of real # $s$ $\{a_n\}_{n=0}^\infty$, define
$$
A(s)=\sum_{n=0}^\infty a_n s^n
$$

### power series

According to values of $\{a_n\}_{n=0}^\infty$, we have 3 situations:

1. $A(s)$ converges only at $s=0$
2. $A(s)$ converges when $|s|<R$ for some $R>0$ & diverges when $|s|>R$.
3. $A(s)$ converges when $|s|<\infty$, here $R=\infty$



When we have cases 2 & 3, $A(s)$ is called generating function of $\{a_n\}_{n=0}^\infty$ and $R$ is called convergence radius

**eg** (1) $a_n=1$ for $n\ge 0$, $A(s)=\sum_{n=0}^\infty s^n = \begin{cases}{1\over 1-s} & |s|<1 \\ diverges & |s|>1 \end{cases} \implies R=1$

(2) $a_n={1\over n!}$ for $n\ge 0$, $A(s)=\sum_{n=0}^\infty {1\over n!}s^n=e^s$ for $|s|<\infty \implies R=\infty$



**THeorem** There is a one-to-one correspondence between $\{a_n\}_{n=0}^\infty$ and $A(s)$

(1) Given $\{a_n\}_{n=0}^\infty$, $A(s)$ is uniquely defined

(2) Given $A(s)$, then $\{a_n\}_{n=0}^\infty$ is uniquely determined.

**uniquely determined** given $A(s)$ $\begin{cases}a_0=A(0) \\ a_n={A^{(n)}(0) \over n!} & for ~n\ge 1 \end{cases}$

#### commonly used power series

1. Geometric: $A(s)=\sum_{n=0}^\infty s^n = {1\over 1-s}, \quad R=1$. $a_n=1$ for $n\ge 0$
2. Altenative Geometric $A(s)=\sum_{n=0}^\infty (-1)^ns^n = {1\over 1+s}$   $R=1$.  $a_n=(-1)^n$  for $n\ge 0$.
3. Exponential $A(s)=\sum_{n=0}^\infty {1\over n!}s^n$  $R=\infty$.  $a_n={1\over n!}, n\ge 0$
4. Binomial $A(s)=(1+s)^n = \sum_{R=0}^n\binom{n}{R}s^R$
   $\begin{cases}a_R=\binom{n}{R} & R=0,1,2\ldots, n\\a_k=0 & R\ge n+1\end{cases}$
   $n$ is postive integer, $R=\infty$
5. general binomial
   $(1+s)^\alpha = \sum_{n=0}^\infty\binom{\alpha}{n}s^n$,  $\alpha$ is a real # (not postive integer)
   $\binom{\alpha}{n}={\alpha(\alpha-1)\ldots(\alpha-n+1)\over n!}$  &  $R=1$

# Lec 14

$$
\binom{-1\over 2}{n}=\left(-{1\over 4}\right)^n\binom{2n}{n}
$$

Properties of gf
$$
A(s)=\sum_{n=0}^\infty a_n s^n \qquad B(s)=\sum_{n=0}b_ns^n
$$
Let $R_A, R_B$ be convergence radius

1. Summation
   $$
   C(s)=A(s)+B(s)=\sum_{n=0}^\infty a_n s^n + \sum_{n=0}^\infty s^n =\sum_{n=0}^\infty(a_n+b_n)s^n
   $$
   $c_n = a_n+b_n$     $R_C = \min(R_A,R_B)$
   $$
   C(s)=A(s)-B(s)=\sum_{n=0}^\infty(a_n-b_n)s^n
   $$
   $c_n=a_n-b_n$     $R(c)=\min(R_A,R_B)$

2. Product
   $$
   C(s)=A(s)*B(s)=\sum_{n=0}^\infty c_ns^n
   $$
   $c_n=\underbrace{\sum_{k=0}^n a_kb_{n-k}}_{n+1~terms} \ne a_nb_n$

   $R_C=\min (R_A,R_B)$

   That is
   $$
   \left(\sum_{n=0}^\infty a_n s^n\right)\left(\sum_{n=0}^\infty b_n s^n\right)
   =\sum_{n=0}^\infty \left(\sum_{k=0}^n a_k b_{n-k}s^n\right)
   $$
   [convolution of $A(s)$ & $B(s)$]

**e.g.** find $\{c_n\}_{n=0}^\infty$ & $R_C$

1. $C(s)={1\over 1-s}*{1\over 1+s}$     2. $C(s)={1\over (1-s)^2}$

**soln**

(1) $C(s)={1\over 2}\left[{1\over 1-s}+{1\over 1+s}\right]={1\over 2}[a_n+b_n]$
then $a_n=1, R_A=1$, $b_n=(-1)^n, R_B=1$  $n\ge 0$
$C(s)={1\over 2}\sum_{n=0}^\infty (1+(-1)^n)s^n$
Hence
$$
\begin{cases}
c_n={1\over 2}(1+(-1)^n)& n\ge 0\\
R_C=1 = \min(R_A,R_B)
\end{cases}
$$
(2)

* Method1: $C(s)={1\over 1-s}{1\over 1-s}$
  then $B(s)=A(s)=\sum_{n=0}^\infty s^n, \quad a_n=b_n=1, R_A=R_B=1, n\ge 0$

  $c_n=\sum_{k=0}^n a_k b_{n-k}=n+1$  $R_C=\min(R_A,R_B)=1$

* Method2: $C(s)=(1+(-s))^{-2} = \sum_{n=0}^\infty (-1)^n\binom{-2}{n}s^n$
  $$
  \begin{split}
  c_n &= (-1)^n\binom{-2}{n}, \quad R_C=1\\
  &= (-1)^n {(-2)(-2-1)\ldots(-2-n+1)\over n!}\\
  &=(-1)^n(-1)^n {2*3*\ldots*(n+1)\over n!}=n+1
  \end{split}
  $$

## 4.2 Probablity generating function (pgf)

**Defn** Suppose $x$ is non-negative integer rv with range =$\{0,1,2,\ldots\}\cup\{\infty\}$. Let $P_n=P(x=n)$ for $n=0,1,2,\ldots$

Then $G_X(s)=\sum_{n=0}^\infty P_ns^n = \sum_{n=0}^\infty P(X=n)s^n$ is called pgf of $X$

If $X$ is a proper rv,  then $\begin{cases}P(x=\infty)=0\\P(x<\infty)=1\end{cases}$  , then $G_X(s)=\sum_{n=0}^\infty P(X=n)s^n=E[s^X]$

**Comments**

1. $G_X(1)=\sum_{n=0}^\infty P(X=n)=P(X<\infty) \le 1$
   $$
   |G_X(s)|=\left|\sum_{n=0}^\infty p_n s^n \right|\le \sum_{n=0}^\infty p_n |s|^n \le \sum_{n=0}^\infty p_n <\infty
   $$
   if $|s|\le 1$

**Property of pgf**

1. why pgf?
   If we have $G_X(s)$, we can recover $\{P_n=P(X=n)\}_{n=0}^\infty$
   Method 1:
   $\begin{cases}P_0=G_X(0) \\ P_n={G_X^{(n)}(0)\over n! }&n\ge 1\end{cases}$
   Method 2: use properties of gfs & commonly used gfs to recover $\{P_n\}_{n=0}^\infty$

   Reason for pgf:

   1. pgf helps to find $P_n = P(X=n)$ for rv $x$ [discrete rv]
   2. mgf(moment generating function) helps to find $E(X^k)$ for $k\ge 1$. [for both discrete & discrete continuous rvs]

2. Property 2
   we can check if  $X$ is proper or not.
   Note: $P(x<\infty)=\sum_{n=0}^\infty P(X=n)=\sum_{n=0}^\infty P_n=G_X(1)$
               and Recall $G_X(s)=\sum_{n=0}^\infty P_ns^n$

   ​			If $G_X(1)=1\implies $proper.

   ​			If $G_X(1)<1 \implies$ improper

   ​			If $G_X(1)>1\implies$ you did sth wrong

# Lec 15

3. Property #3
   If $x$ is proper, then
   $$
   E(x)= G_x'(1)\\
   var(x)=\underbrace{G_x''(1)+G_x'(1)}_{E(x^2)}-[\underbrace{G_x'(1)}_{E(x)}]^2
   $$

4. Property #4: Uniqness Theorem
   Two random variables X and Y have the same distribution iff $G_X(s)=G_Y(s)$  $\implies$ use pgf to determine distribution type

5. Property #5 Indepedence Property
   If X and Y are independent with ranges = {0, 1, 2, …} $\cup \{\infty\}$

   Argument:
   $$
   \begin{aligned}
   G_{X+Y}(s)&\stackrel{proper}{=}E[s^{X+Y}]\\
   &=E[s^X*s^Y]\\
   &\stackrel{indepdent}{=}E[s^X]E[s^Y] \\
   &= G_X(s)*G_Y(s)
   \end{aligned}
   $$





# Lec 16

useless examples

## 4.3 Simple random walk

Background:

* suppose we have a particle staring from $x_0$ (eg, $x_0=0$)
* At each step, the particle $\begin{cases}\text{can move to right by 1 unit with prob $= p$}\\
  \text{can move to right by 1 unit with prob $q=1- p$} \end{cases}$



**eg** toss a coin

* H: move to right by 1 unit
* T: move to left by 1 unit

Suppose we toss a coin 5 times and get HHTTH



**Def** Simple random walk: Let $x_0$ be the starting point of the process (eg: $x_0=0$) & $x_n$ be the position of the process after $n$ steps. Then $\{x_n\}_{n=0}^\infty$ is called a simple random walk or ordinary random walk.

**Our interest**

$\lambda_{0,0}=$ Returning to 0, given the process stars with 0

$\lambda_{0,k}=$ visiting $k$, given the process starts with 0

**LET** $T_{0,0}=$ waiting time for observing 1st $\lambda_{0,0}$  $=\min\{n\ge 1, x_n=0| x_0=0 \}$

For example, $k=1$, in the example above, $T_{0,1}=1$.

We would like to find

1. $P(T_{0,0}<\infty) \& E(T_{0,0})$
2. $P(T_{0,k}<\infty) \& E(T_{0,k})$

# Lec 17

* $T_{0,0}=$ waiting time for observing 1st $\lambda_{0,0}$  $=\min\{n\ge 1, x_n=0| x_0=0 \}$
* $T_{0,k}=$ waiting time for observing 1st $\lambda_{0,k}$  $=\min\{n\ge 1, x_n=0| x_0=0 \}$

**Notation**
$$
G_{0,0}(s)=\sum_{n=0}^\infty P(T_{0,0}=n) s^n ~~ pgf~of ~T_{0,0} \\
G_{0,k}(s)=\sum_{n=0}^\infty P(T_{0,k}=n) s^n ~~ pgf~of ~T_{0,k}
$$
Preparation: 1st for $k>0$, positive integer $k$

$ T_{0,k}=T_{0,1}+T_{1,2}+\ldots+T_{k-1,k}$

$T_{i,j}$ = waiting time for visiting $j$, starting from $i$ = $\min\{n\ge 1, x_n=j | x_0 = i\}$



**Claim** $T_{0,1}, T_{1,2},\ldots, T_{k-1,k}$ are $k$ iid rvs since all mean moving to right by 1 unit.

**That is** $T_{0,k}=\sum_{i=1}^k T_{i-1,i}$             all $T_{i-1,i}$ are iid & have same distribution as $T_{0,1}$.
$$
\implies G_{0,k}(s)=pgf~of~T_{0,k} = \prod_{i=1}^k \underbrace{G_{T_{i-1,i}}(s)}_{pgf~of~T_{i-1,i}} \\
\implies G_{0,k}(s)=[G_{0,1}(s)]^k \qquad \text{for $k>0$}
$$
2nd: In general:

* $T_{0,1}\& T_{-1,0}$ have same distribution [move to right by 1 unit]
* $T_{1,0}\&T_{0,-1}$  … [left by 1]

they are all in simple random walk.



**Next** move to pgf of $T_{0,1}$ then $T_{0,k}$ for $k>0$.

**by def** $G_{0,1}(s)=\sum_{n=0}^\infty P(T_{0,1}=n)s^n = pgf~of~ T_{0,1}$

$n=0, P(T_{0,1}=0)=0;~~ n=1, P(T_{0,1}=1)=P(\text{move to right by 1})=p$

For $n\ge 2$
$$
\begin{aligned}
P(T_{0,1}=n) &\stackrel{\substack{\text{condition on}\\\text{1st argument}}}{=}\\
&\underbrace{P(T_{0,1}=n|\text{1st stop = right})}_0 *
\underbrace{P(\text{1st stop = right})}_p \\
&+\underbrace{P(T_{0,1}=n|\text{1st stop = left})}_0 *
\underbrace{P(\text{1st stop = left})}_1
\end{aligned}
$$

1st stop = right $\implies T_{0,1}=1\ne n$  for $n\ge 2$
1st stop = left $\implies$ we are in position "-1" & $T_{0,1}=n$ means $T_{-1,1}=n-1$



Hence $P(T_{0,1}=n)=P(T_{-1,1}=n-1)*q = P(T_{0,2}=n-1)*q$
