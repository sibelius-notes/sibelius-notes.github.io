# My Lecture Notes
In the future, I will keep it consistent, i.e., LaTeX for math courses and markdown for arts courses. Maybe just for quick scatter cs notes, I will also use markdown.

# Note of usage
You will need to
- generate a list of posts/courses from `courses.csv` by calling `python3 gen_posts`. They will not overwrting the existing posts unless you set one flag.

- convert markdown files to html:
    * `cd markdown`
    * call `./gen` to convert.

Note that you `shouldn't` use markdown to do math often since the conversion is weird. You will need to `\\(x+y\\)` or `\\[\sum_x^y\\]` in original markdown files. Also for equations, you will need to do

```latex
$$
\begin{aligned}
x &= y \\\\ % escaping
y &= x
\end{aligned}
$$
```

Also, if you really want to do math inside the markdown, you can "steal" the style sheet and use pandoc with extra options. I believe, at the end, you can achieve almost the same result with pandoc. But why doing so many LaTeX with markdown? Using LaTeX!


# Starter kit for [Alembic](https://alembic.darn.es/)

This is a very simple starting point if you wish to use Alembic [as a Jekyll theme gem](https://alembic.darn.es/#as-a-jekyll-theme) or as a [GitHub Pages remote theme](https://github.com/daviddarnes/alembic-kit/tree/remote-theme) (see `remote-theme` branch).

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/daviddarnes/alembic-kit)

or

**[Download the GitHub Pages kit](https://github.com/daviddarnes/alembic-kit/archive/remote-theme.zip)**


# References

[original github](https://github.com/daviddarnes/alembic)

[what I am learning from](https://github.com/bawejakunal/bawejakunal.github.io)
