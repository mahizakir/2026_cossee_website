+++
title = "Meta-analysis terminology can be confusing"
date = 2025-05-17
authors = ["Coralie Williams"]
banner = "/web_files/tangle.jpg"
summary = "A COSSEE blog post about the language of meta-analysis and why precise terms matter."
+++

Image credit: patpitchaya (iStock)

I doubt I am the only one who has felt lost at times with meta-analysis terminology. Early on, I even struggled to understand what effect size referred to. I thought it meant the strength of a relationship in a model. It does, but in meta-analysis effect sizes are also the outcome data we analyse. So, the same term can refer both to the estimated effect (the regression coefficient) and the data we are modelling, depending on the context. I started writing the following points down out of frustration and to keep track for myself when reading the meta-analytic literature.

Subgroup analysis, moderator analysis, meta-regression

Sometimes we come across terms that sound different but actually mean similar things. Moderator analysis is a broad term for any method that looks at whether moderators (also called predictors, or independent variables) help explain differences in the effect sizes being analysed. One type of such methods is subgroup analysis , where studies are grouped based on a categorical variable and effect sizes are compared across these groups (e.g. treated vs control). This method is useful to answer many questions, but it is limited to categorical variables. Meta-regression takes things a step further by using a regression model to look at how one or more moderators are linked to variation in effect sizes. These moderators can be categorical, continuous, or both. So, subgroup analysis is really just a simpler case of meta-regression, and they are both types of moderator analysis used in meta-analysis.

Fixed-effect vs fixed-effects models

Fixed-effect (singular noun) vs fixed-effects (plural noun) are sometimes used interchangeably in the literature to describe meta-analysis models, despite referring to different statistical assumptions (Borenstein et al., 2010; Viechtbauer, 2010). The fixed-effect (singular) model assumes that all studies in the meta-analysis estimate a common true effect size . Whereas, the fixed-effects (plural) model assumes that each study has its own true effect , but these are treated as fixed quantities and not drawn from a distribution. This makes it suitable for cases where we believe heterogeneity exists but want to restrict inference to the studies at hand (which is actually quite rare). In statistical modelling, "fixed effect" usually refers to a non-random coefficient in a regression model, for example species traits. But in meta-analysis, the label “ fixed effect” can refer to a model. Confusing? Yep. And that's why some recommend renaming the fixed-effect model to the common-effect or equal-effects model for clarity.

Multivariate in meta-analysis

Another tricky term is multivariate . In a statistical sense multivariate refers to multiple response (outcome) variables. However, in meta-analytical modelling, this term can have several meanings. I recommended reading a great post by James Pustejovsky here who elaborates on this (with some humour) and explains its various meanings which has help me a lot to understand this term in the context of meta-analysis methodology.

These kinds of nuances in terminology can make it hard to get a clear conceptual footing, especially when new to the field, but hopefully it doesn’t scare you away from the wonderful (really it is) world of meta-analysis!

References - Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2010). A basic introduction to fixed-effect and random-effects models for meta-analysis. Research Synthesis Methods, 1(2), 97–111. https://doi.org/10.1002/jrsm.12

- Viechtbauer, W. (2010). Conducting Meta-Analyses in R with the metafor Package. Journal of Statistical Software, 36(3). https://doi.org/10.18637/jss.v036.i03
