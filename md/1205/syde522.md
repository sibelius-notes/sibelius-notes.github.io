---
title: SYDE 522 - Machine Intelligence
layout: mdtoc
---
# Lecture 1
Objectives of this course:
- basic concepts of AI
- different methods for function approximation
- select the right learning scheme
- difference between shallow & deep learning
- verify the learning capability
- run and evaluate experiments
- write a scientific paper

Lecture Topics:
1. Encoding/embedding: data compression, PCA, t-SNE, Fisher Vector, ..., <span>&#92;(k &#92;)</span>-fold cross validation, leave-one-out
2. Classification/clustering: K-means, FCM, SVM, self-organizing maps
3. Learning: Perceptron, backpropagation, CNN, AEs
4. Reinforcement learning: check [CS 885](/cs/885)
5. Uncertain vs. vague: Probability, FuzzyLogic, DTs, RFs

*Why interest in AI?*
- Recent progress in algorithms
- Availability of data
- Computational power

## History of AI
1901 - PCA (K. Pearson)

1933 - PCA development (H. Hotelling)

1958 - Perceptron (F. Rosenblatt)

1965 - Fuzzy Sets (L. Zadeh)

1969 - Limitation of Perceptron (Minsky/Papert)

1982 - SOM (T. Kohonen)

1986 - Backpropation ([Rumelhart](https://en.wikipedia.org/wiki/David_Rumelhart)/Hinton)

1986 - ID3 algorithm ([J.R. Quinlan](https://en.wikipedia.org/wiki/Ross_Quinlan))

1993 - C 4.5 algorithm (J.R. Quinlan)

1995 - SVM (Cortes/Vapnik)

1995/2001 - Random Forest (T.K.Ho/L.Breiman)

1995 - CNN (LeCunn/Bengio)

2006 - Fast learning for deep belief Nets (Hinton et al.)

2007 - Greedy layer-wise training for deep Nets (Bengio et al.)

2012 - AlexNet

## Main Tasks for AI
- Classification
- Estimation/Prediction
- Search
- Optimization
- Inference

All these is approximation: you have a black box <span>&#92;(f(x) &#92;)</span>, some <span>&#92;(x &#92;)</span> goes in and some <span>&#92;(y &#92;)</span> goes out. <span>&#92;(f &#92;)</span> is unknown. The simplest approach is regression.

![there should be a image...](/pics/522/AI.svg)

*What is intelligence?*

"the act of knowing" <span>&#92;(\implies &#92;)</span> intelligence <span>&#92;(\stackrel{?}{=} &#92;)</span> knowledge

"the exercise of understanding" <span>&#92;(\implies &#92;)</span> intelligence = understanding

|   | humans | machines     |
|:--| :------------- | :------------- |
|thought | reason       | rational decisions       |
|actions | act | rational actions (AI) |

*Can we measure intelligence?*

![there should be a image...](/pics/522/tguess.svg)

# Lecture 2
Check [this paper](https://www.csee.umbc.edu/courses/471/papers/turing.pdf)

*Can machine think?*

Alan Turing assumed we can build intelligent machines. Measuring intelligence is what he is proposing.

Turing anticipated all AI fields:
- searching. Not like browsing, and you type sth in search engine. We are talking about explicit ones: whenever you see sb and remember the face, that is a search. The challenge is the visual info is stored in a highly complicated way, and search mechanism is very sophisticated.
- reasoning. That's where we failed Turing test. We cannot search intelligently, and we cannot reason based on the knowledge you acquired.
- knowledge representation
- NLP
- computer vision
- learning

## The Chinese Room
J. R. Searle

![there should be a image...](https://miro.medium.com/max/348/0*zA6_zLOjyt0zDeQG)

In the room, the person is non-Chinese. Two books inside: rule and dictionary. From outside, people come, put in Chinese text, and come out (flawless) English text.

*Can this person understand Chinese? Can the room understand Chinese?*

Let's look at an example.

## Tic-Tac-Toe
Version 1: Look-Up Table  [Answer for each situation is hard-coded]

Version 2:
- A: Attempt to place two marks in row
- B: If opponent has two marks in a row, then place a mark in the third position.

Version 3: Represent the **state**(understanding) of the game
- Current board position?
- next legal moves?

Use an evaluation function.
- Rate the next move! (how likely to win?)
- Look-ahead of possible opponent's move!


```
<-----Stupid ----------------------- intelligent----->
Version 1                   2                         3
```

AI = Function Approximation

We need "data" for any approximation. For example, linear regression.

AI = Operation intelligently on data to extract the relationship between in- and outputs.
*  Training data for learning.
*  testing data for validation.

**Problems**
1. Not enough data <span>&#92;(\to &#92;)</span> Augmentation
2. Too much data <span>&#92;(\to &#92;)</span> Dimensionality reduction

**Desired**
1. no correlation
2. high variance

## PCA
<span>&#92;(x' &#92;)</span> passes through the "mean" and delivers max variance when samples are projected into it. Process is repeated until we find <span>&#92;(n &#92;)</span> such axes <span>&#92;(\langle x_1,x_2,\ldots,x_n\rangle &#92;)</span>. intelligent: <span>&#92;(x\in \mathbb R^d \implies n \ll d &#92;)</span>.

Principal Component Analysis (PCA) is the algorithm to find orthogonal axes that diagonalize the covariance matrix. What does this mean?

First let's get used to some notations...

- <span>&#92;(x &#92;)</span>: scalar.
- <span>&#92;(\boldsymbol x &#92;)</span>: vector.
- <span>&#92;(X &#92;)</span>: set.
- <span>&#92;(\boldsymbol X &#92;)</span>: matrix.

Covariance matrix
<span>&#92;[
\Sigma = \operatorname{cov}(\underbrace{x_i} _ {i\text{-th input}}, \underbrace{x_j} _ {j\text{-th input}})
= \mathbb E \left[ (x_ i - \mu _ i) (x _ j - \mu _ j) \right]
&#92;]
</span>
where <span>&#92;(\mu _ i = \mathbb E[ x _ i], \mu _ j = \mathbb E[ x _ j] &#92;)</span>.

Are <span>&#92;(x_i &#92;)</span> and <span>&#92;(x_j &#92;)</span> changing together? (correlated)

Generalization of Covariance: <span>&#92;(\Sigma = E[(\boldsymbol x - E[\boldsymbol x]) (\boldsymbol x - E[\boldsymbol x])^T  ] &#92;)</span>

# Lecture 3
## PCA
main features selection. Which components (=features) are important to keep?
- Significance = variance.
- Intelligence = recognizing the significance

Staring point is a file with a table: where the columns: <span>&#92;(x_ 1, x_ 2,\ldots &#92;)</span> are features and rows: (1, 2, 3, ...) are observations.

Covariance matrix <span>&#92;(C = E[ x x^T] &#92;)</span>

Diagonalizing <span>&#92;(C &#92;)</span> using a suitable orthogonal transformation matrix <span>&#92;(A &#92;)</span> by obtaining <span>&#92;(N &#92;)</span> orthogonal "special vectors" <span>&#92;(u_ i &#92;)</span> with "special parameters" <span>&#92;(\lambda _ i &#92;)</span>

![there should be a image...](https://blog.bioturing.com/wp-content/uploads/2018/11/Blog_pca_6b.png)

[src](https://blog.bioturing.com/2018/06/14/principal-component-analysis-explained-simply/)

Principal components: <span>&#92;(\lambda_ 1 &#92;)</span> most important, <span>&#92;(\lambda _  N &#92;)</span> least important. Pick <span>&#92;(N' \ll N &#92;)</span>, so-called dimensionality reduction.

PCA is
- a linear transformation
- unsupervised
- uses statistics and calculus
- dimensionality reduction algorithm
- a visualization algorithm
- intelligent because it recognizes significance

## AI & Data
**Data types**: numbers/symbols/text/images/videos/audio files...

**Pre-processing**: filtering/normalization/outlier detection/dimensionality reduction/augmentation/...

**Data representation**:
- Hand-crafted features (e.g., stats, [SIFT](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform))
- automatic feature extraction (e.g. deep features)

**Encoding**: (compression/embedding)
- no learning
    - PCA
    - [Fisher Vector](https://en.wikipedia.org/wiki/Fisher_kernel)
    - [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)
    - VLAD (vector of locally aggregated descriptors)
    - ...
- with learning
    - Auto-Encoders. [ML DDoS Detection :)](https://www.sibeliusp.com/research/)
    - t-SNE

Applications of PCA
- Data reduction
- Data visualization
- Data classification
- Factor analysis
- Trend analysis
- Noise removal

A meaningful chain:

![there should be a image...](/pics/522/chain.svg)

You will see that this is not always desirable.

## Project
(not sure if this helps...)
1. Find a problem
2. Analyze the problem (input/output/knowledge)
3. Select approach (architecture, parameters, ...)
4. Design the approach
5. Training
6. Re-train if necessary
7. Recall phrase (unseen data)
8. Compare against other methods

# Lecture 4
## LDA
linear discriminant analysis (operates of feature subspace, linear method, supervised)
- Data <span>&#92;(\langle x _ 1,\ldots,x _ n \rangle &#92;)</span>
- <span>&#92;(N _ 1 (N _ 2) &#92;)</span> samples belonging to class <span>&#92;(C_1 (C _ 2) &#92;)</span>
- Find a line that maximizes the class separation

![there should be a image...](https://sebastianraschka.com/images/blog/2014/linear-discriminant-analysis/lda_1.png)

[src](https://sebastianraschka.com/Articles/2014_python_lda.html)

![there should be a image...](/pics/522/wtx.png)
- Define a good separation measure
- Mean vector

<span>&#92;[
    \mu _ i = {1\over N _ i }\sum _ {x\in C _ i} x, \quad \tilde \mu _ i = { 1\over N _ i}\sum _ {y\in C _ i }y = w^T \mu _ i
&#92;]</span>

- Driving force for separation: <span>&#92;(\operatorname{argmax}_ w &#124;\tilde \mu _ 1 - \tilde \mu _ 2 &#124; &#92;)</span>
- But we are ignoring the **variability inside** classes

Fisher's Approach: Normalize the distance (difference) between the means by intra-class scatter.

scatter = variance: <span>&#92;(\tilde s _ i ^ 2 = \sum _ {y\in C _ i} (y - \tilde \mu _ i)^2 &#92;)</span>

intra-class scatter <span>&#92;(\tilde s _ 1^2 + \tilde s _ 2^2 &#92;)</span>

Fisher Linear Discriminant: <span>&#92;(\dfrac {&#124; \tilde \mu _ 1-\tilde\mu _ 2 &#124;^2} {\tilde s _ 1^2 + \tilde s _ 2^2} &#92;)</span>. To be maximized!

## t-SNE
t-Distributed stochastic neighbor embeddings.
- non-linear data visualizer
- t-test. t-distribution (normal distribution)

t-SNE does not use any norm (=distance metric). It uses Kullback-Leibler Divergence. Given two probability distributions <span>&#92;(p,q &#92;)</span>, the KL divergence  measures the distance
<span>&#92;[
    D(p\&#124;q)= \sum _ {x\in X} p(x)\log {p(x)\over q(x)}
&#92;]</span>
However, <span>&#92;(D (p \&#124; q) \ne D(q \&#124; p) &#92;)</span>. Therefore, KL divergence is not a metric!

Relation to entropy <span>&#92;(H(X) &#92;)</span>.

<span>&#92;[H(X)=\sum _ {x\in X}p(x)\log {1\over p(x)}
= \log N - D(\underbrace{p(x)} _ {\text{true dist'n}} \&#124; p _ U(x))
&#92;]</span>
where <span>&#92;(U &#92;)</span>: uniform.

The Shannon entropy is the number of bits necessary to identify <span>&#92;(X &#92;)</span> from <span>&#92;(N &#92;)</span> equally likely possibilities, less the KL divergence of the uniform distribution from the true distribution.

t-SNE idea: hyper-dimensions <span>&#92;(\to &#92;)</span> two dimensions. Similarity in high dimensions corresponds to short distance in low dimensions.

Challenge: perplexing!

t-SNE minimizes the sum of KL divergences over all data points using a gradient descent method.

<span>&#92;[
    Objective = \sum _ i D(P _ i \&#124; Q  _ i) = \sum _ i \sum _ j p _ {j &#124; i} \log { p _ {j &#124; i}\over q _ {j &#124; i}}
&#92;]</span>

![there should be a image...](/pics/522/pq.png)

# Lecture 5
We'll start by saying: AI is vision! Intelligence is to recognize people/scenes/objects/patters/...
- Face recognition
- object recognition
- Auto-captioning of images
- robot navigation
- ...

Given a digital image, two possible ways for recognition:
1. AI approach: given an image, then pass to some sort of AI black box, then there it comes out classes/text
2. CV/AI approach: given an image, then give it to whitebox (CV), which gives you some features, then goes to blackbox of AI, then classes/text

Feature Extraction:
1. Keypoint-oriented (SIFT, SURF, ...): Several hundreds/thousands features
2. Histogram-oriented (LBP, HOG, ELF ...): one histogram

Example: Harris Corner Detection

![there should be a image...](https://miro.medium.com/max/469/0*gTbWMTKvNF-jLJrM.jpg)

For SIFT, you get many feature vectors of length 128. Thus
<span>&#92;[
    Image = \bigcup _ {i=1} ^ { n \text{ key points}} v _ i
&#92;]</span>
Challenge:
- Data is too large
- Data may not be descriptive

Solution: embedding/pooling/encoding
- Fisher Vectors (embedding/pooling)
- VLAD (encoding/increasing discrimination)

##  Fisher Vectors

We have our dataset: <span>&#92;(X = &#92;left&#92;{ x _ t &#124; t = 1,\ldots, T &#92;right&#92;} &#92;)</span>. And <span>&#92;(u _ \lambda &#92;)</span> = probability density function which models the generative process of elements of <span>&#92;(X &#92;)</span>. And we have <span>&#92;(\lambda \in \mathbb R^M &#92;)</span> which are parameters of <span>&#92;(u_ \lambda &#92;)</span>

In statistics, the "score function" is the gradient (partial derivative) w.r.t. parameter <span>&#92;(\lambda &#92;)</span> of the natural log of the likelihood function. Score function <span>&#92;(= \nabla _ \lambda \log u_ \lambda (X) = \nabla _ \lambda \log P(x | u _ \lambda) &#92;)</span>

Let <span>&#92;(X &#92;)</span> be the set of D-dimensional local descriptors extracted from an image (e.g. SIFT)

<span>&#92;[
    g _ \lambda^X = \sum _ {t=1}^T L _ \lambda \nabla _ \lambda \log u _ \lambda (x _ t)
&#92;]</span>
This is called Fisher Vector. Fisher Vector is a sum of normalized gradients statistics computed for each descriptor (= feature vector). The operation
<span>&#92;[
    x _ t \to f _ {FK}(x _ t) = L _ \lambda \nabla _ \lambda \log u _ \lambda ( x _ t)
&#92;]</span>
is an embedding of local descriptors <span>&#92;(x _ t &#92;)</span> in a higher dimensional space which is easier for classifier.

<span>&#92;(L _ \lambda &#92;)</span>: Cholesky Decomposition
<span>&#92;[
    F _ \lambda ^{-1} = L _ \lambda ^ T L _ \lambda, \qquad K _ {FK}(X,Y) = G _ \lambda ^{X^T} F _ \lambda G _ \lambda ^{X}
&#92;]</span>
where <span>&#92;(K _ {FK} &#92;)</span> is the Fisher Kernel.

## VLAD
Vector for locally aggregated descriptors

How to recognize images? Bag of Visual Words (BoVW)

![there should be a image...](/pics/522/vword.png)

Given an image <span>&#92;(I &#92;)</span>, divide it into small cell/windows of size <span>&#92;(n \times n &#92;)</span> (i.e. 16x16). We vectorize visual words for convenient calculations.

**Theory**: you got a image, apply BoVW, and get millions of visual words, and give that to a classifier, and classifier says that's a cat

**Practice**:
- too many vectors
- redundancy
- noise

**General Approach**: Build a codebook (dictionary) <span>&#92;(C = &#92;left&#92;{ c _ 1,\ldots,c _ n &#92;right&#92;} &#92;)</span> from <span>&#92;(m\gg n &#92;)</span> feature vectors (vectorized visual words)

**Idea**: Use a clustering algorithm like k-means. (<span>&#92;(C _ i &#92;)</span>) is the centre of <span>&#92;(n &#92;)</span> classes found in the data.

**Core Idea of VLAD**: Accumulate, for each visual word <span>&#92;(C _ i &#92;)</span>, the difference of the vectors <span>&#92;(X &#92;)</span> assigned to <span>&#92;(C _ i &#92;)</span>, <span>&#92;(X - C _ i &#92;)</span>, i.e., distribution of data w.r.t. the class centers.

<span>&#92;[
    V _ {i,j}=\sum _ {NN(X)=C_i} X _ j - C _ {i,j}
&#92;]</span>
Here NN is the nearest neighbor. <span>&#92;(X _ j &#92;)</span> is the <span>&#92;(j &#92;)</span>-th component of descriptor. <span>&#92;(C _ {i,j} &#92;)</span> is the corresponding center

Here we do a <span>&#92;(L _ 2 &#92;)</span> normalization.
<span>&#92;(
    V : = {V\over \&#124; V\&#124; _ 2}
&#92;)</span>

Final Chain
![there should be a image...](/pics/522/finalchain.png)

# Lecture 6
How to validate AI algorithms? [How do I use Turing Test in practice?]
- We get the data
- We train our algorithms:
    - how do we know it has learned what is was supposed to learn?
    - We should test it! If good enough, then release it! How do we make sure of this?

First factor to make sure that is good enough is to have target/objective function:
- error (minimize)
- reward (maximize)
- fitness (maximize)
- punishment (minimize)

Given the entire data <span>&#92;(X = &#92;left&#92;{ x _ t &#92;right&#92;} &#92;)</span>

![there should be a image...](/pics/522/super.png)

Given the set of all hypotheses <span>&#92;(H &#92;)</span> (set of all possible solutions), find <span>&#92;(h\in H &#92;)</span> such that
<span>&#92;[
    \sum _ {x _ t\in X} (x _ t^* - x _ t ^ d) = \epsilon \to 0
&#92;]</span>
which is supervised. This constitutes a good fit for the model <span>&#92;(h &#92;)</span> into <span>&#92;(X &#92;)</span>. Any concern?

**Scenario #1**: you have your complex data and simple solution, then you train. It does not converge. Problem is big/non-linear/non-stationary. Solution (hypothesis) is not capable of capturing the complexity.
![there should be a image...](/pics/522/scen1.png)

**Scenario #2**: Problem is small/linear/stationary. Solution is too big such that is completely owns the problem. h is memorizing X.

![there should be a image...](/pics/522/scen2.png)

What is the ultimate sign that the algorithm has really learned? It can generalize the inherent X-Y relationship to "unseen" data.

Validation = test for generalization. Idea: keep one part of data for testing. But this may not be reliable! The split may be lucky/unfortunate. So we have K-fold partition.

Random Sampling, K-fold cross validation:
![there should be a image...](/pics/522/randomsamp.png)

But all this would work if we had a lot of data. What if we don't? We use Leave-one-Out validation.

n-fold cross validation: vert expensive, suitable for small data.

Model complexity = <span>&#92;(&#124;P &#124; &#92;)</span> where <span>&#92;(P &#92;)</span> is the set of parameters of <span>&#92;(h\in H &#92;)</span>. Occam's Razor: Keep it simple! = Regularization
<span>&#92;[
    \min \left( \underbrace{\sum _ {x _ t\in X} (x _ t^* - x _ t^d)} _ {\text{lowest error}} + \underbrace{&#124;P &#124;} _ {\text{smallest solution}}\right)
&#92;]</span>

Augmented error function:
<span>&#92;[
    E' = E _ {total} + \underbrace{\lambda \cdot \text{model complexity}} _ {\substack {\text{penalized complex}&#92;&#92; \text{solutions with} &#92;&#92;
    \text{large variance}}}
&#92;]</span>

If <span>&#92;(\lambda &#92;)</span> too large, then simple models, then increase bias. Hence we use cross validation to optimize <span>&#92;(\lambda &#92;)</span>.

Another model selection approach: Bayesian approach is used if we have prior knowledge.

Bayes Rule:
<span>&#92;[
    P (model &#124; data) = {P(data &#124; model) \cdot P(model)\over P(data)}
&#92;]</span>

Other methods:
- Structural risk minimization
- Minimum description length

![there should be a image...](/pics/522/smallbig.png)
