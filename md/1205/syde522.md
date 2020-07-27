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
