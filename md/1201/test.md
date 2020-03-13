---
title: Testing
layout: mdtoc
---
# inline math
&#92;(x=2 &#92;)

# display
&#92;[
    hey
&#92;]

# maxp

&#92;[
    &#92;begin{array}{ll}
    &#92;max & &#92;begin{array}{l}c^T x&#92;end{array}&#92;&#92;
    &#92;text{s.t.} & &#92;begin{array}{lll}
    Ax \le b &#92;&#92;
    x\ge 0
    &#92;end{array}
    &#92;end{array}
&#92;]

# minp

&#92;[
    &#92;begin{array}{ll}
    &#92;min & &#92;begin{array}{l}b^T y&#92;end{array}&#92;&#92;
    &#92;text{s.t.} & &#92;begin{array}{lll}
    A^T y\ge c &#92;&#92;
    y\ge 0
    &#92;end{array}
    &#92;end{array}
&#92;]

# cases
&#92;[
    x= &#92;begin{cases}
     0& &#92;text{if } x=0 &#92;&#92;
      x & &#92;text{otherwise}
    &#92;end{cases}
&#92;]

# brace
&#92;(&#92;left&#92;{ {1\over x}, {1\over x^2} &#92;right&#92;} &#92;)

# array
&#92;[
    &#92;begin{array}{llll}
    x &#92;&#92; y &#92;&#92; z &#92;&#92; w &#92;&#92;
    &#92;end{aligned}
&#92;]

# pmatrix
&#92;[
    &#92;begin{pmatrix}
    1 & 1 & 2 &#92;&#92;
    2 & 2 & 3 &#92;&#92;
    3 & 3 & 4
    &#92;end{pmatrix}
&#92;]
