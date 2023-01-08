# Terms and domain

## **IS MOST RESEARCH WRONG?**

![Thumbnail of Veritasium [video](http://www.youtube.com/watch?v=42QuXLucH3Q).
In its description we find a reference to metascience paper with 10k+
citations.](res/vertasium.jpg)

## What is Metascience?

:::::::::::::: {.columns}
::: {.column width="35%"}

![First page of John Ioannidis's paper that led to a broad investigation of
scientific research methodology.
@ioannidis2005most](res/Ioannidis_(2005).jpg)

:::
::: {.column width="65%"}

### Definition

**Metascience, the science of science**, uses rigorous methods to examine how
scientific practices influence the validity of scientific conclusions. It has
its roots in the *philosophy of science* and the *study of scientific methods*,
but is distinguished from the former by a reliance on *quantitative analysis*,
and from the latter by a broad focus on the general *factors* that contribute to
the **limitations and successes of research**. @schooler2014metascience

### At the end of the day {.example}

Meta-research involves taking a bird’s eye view of science. @ioannidis2015meta

:::
::::::::::::::


## Scientometrics - can you believe it?

### Definition

Scientometrics can be defined as the "quantitative study of science,
communication in science, and science policy" @scientometrics

### What does it all mean? {.example}

The intended effect [of rankings] is to create competition among institutions of
higher learning and research and thereby to increase their efficiency. The
rankings are supposed to identify excellence in these institutions and among
researchers. **Unintended effects** may be 'oversteering', either by forcing
less competitive **institutions to be closed down** or by **creating
oligopolies** whose once achieved position of supremacy cannot be challenged
anymore by competitors. @weingart2005impact

###  Where do we stand? {.alert}

The future of the higher education and research system rests on two pillars:
traditional **peer review** and **ranking**. @weingart2005impact

## Peer review - all shapes and sizes

### Definition

Peer review is designed to assess the validity, quality and often the
originality of articles for publication. Its ultimate purpose is to maintain the
integrity of science by filtering out invalid or poor quality articles. @whatis

### Types @ali2016peer

- *single blind*
    - the author is not aware of the reviewers' identities
    - reviewers may be unnecessarily critical while giving feedback
- **double blind**
    - the authors and reviewers are not aware of each other's identities
    - eliminates chances of bias
    - reviewers may still be able recognize authors through other markers such
      as writing style, subject matter and self-citation
- *open*
    - authors and reviewer are known to each other throughout the process

---

![Depiction of the paper-reviewer matching process (left) and decision-making
process (right) for submitted papers from the presented paper
@soneji2022flawed](res/reviewing-process.png){
height=85% }

# Presented paper

## The security community needs

> "*Flawed, but like democracy we don’t have a better system*": The Experts’
> Insights on the Peer Review Process of Evaluating Security Papers
> @soneji2022flawed

Accepted in the 43rd IEEE Symposium on Security and Privacy, this paper presents
a exploratory qualitative study based on interviews with Program Committee
members (PCs) and Chairs ($n = 21$), being first of its kind.

The need for such a study is justified within these contextual problems:

- exponential increase in paper submissions to all venues
- delegation system of reviews and quantity and quality of them
- new submission model: rolling deadline 

Research questions:

1. How is the Science of Security currently served by the
    peer review process?
2. What are experts' opinions on current peer review mechanisms?


## Type of research - Qualitative

### Definition

Qualitative research seeks to understand - through person-to-person interviews -
how and why people think and behave the way that they do. ... Take a **small
sample size**, spend time with the individuals, and learn about their
impressions and motivations. @qualitativeresearch

### Science of Security {.example}

However, we find that there is little clarity on what "scientific" means in the
context of computer security research, or consensus on what a "Science of
Security" should look like. @herley2017sok

### Human factors and data saturation {.alert}

Because security researchers study and **develop systems and solutions mainly
for human use**, qualitative human factors research in security is crucial.
... To obtain rigorous and exhaustive qualitative results, we conducted
interviews until new themes stopped emerging. @soneji2022flawed

# Accept, Reject ... Revise?

## Novelty - the priority

The only common metric, which was mentioned by $\textcolor{orange}{90.47}%$ of
participants, being followed by correctness with only $\textcolor{orange}{42.85}%$
acknowledgment.

### Sounds simple enough {.example}

P20: Traditionally speaking, something that has not been published in a
peer-reviewed setting such as a journal or a conference.

::: {.block}
### Too subjective of a metric {.alert}

P19: Novelty is definitely subjective. This is something where different
reviewers will see different values out of a paper.

:::

It was evaluated differently, whether or not it emerged from the following:

- insight
- solution
- method or attack
- *being interesting or exciting*
- comparison with previous work or state-of-the-art.

## Red flags waving you out

Reviewers have much more concrete and diverse opinions when rejecting a paper,
mentioning $52$ red flags, which can be grouped in these categories:

::: columns

:::: {.column width=40%}

Content-related:

- Not novel or insignificant
- Mistakes in:
    - Title
    - Introduction
    - Methodology
    - Experiments
    - Evaluation
    - Results
    - Ethical aspects
- Wrong fit.

::::

:::: {.column width=30%}

Argument-related:

- Poorly argued:
    - Inaccurate
    - Unsupported
    - Unexplained
    - Obfuscation
- Relevance:
    - Motivation
    - Related work
    - Application.

::::

:::: {.column width=28%}

Writing-related:

- Poor writing
- Poor English
- Jargon
- Graphs, tables, figures.

::::

:::

::: {.block}
### Self-fulfilling prophecy {.alert}

P09: the acceptance rate is so low that ... look for reasons to reject instead
of reasons for accepting a paper.

:::

## Consistency - is everything the same?

Papers and reviewers don't always mix. Each reviewer has a core area of
research, and when there's a mismatch we are left wondering weather or not that
paper was fit for the venue. This may end up in a high-level review that someone
had to do, or a rejection.

### Hopes and wishes {.example}

... change their evaluation metrics based on the type of paper. P15 wished to
be consistent with their evaluation metrics, but they review papers from a broad
spectrum, making it challenging to apply the same rubric for every paper. P11
added that every paper has its own story to tell, and factors, such as stress
and emotion, take effect when reviewing a paper. @soneji2022flawed


### High price to pay {.alert}

Five participants reported that they lower their expectations, sometimes for
novelty, when reviewing security papers from non-top-tier venues, but the
correctness and other evaluation metrics they use stay consistent.
@soneji2022flawed

## Randomness

### A key finding

Perceived "randomness" of reviews was **the most frequent issue** of all of the
issues that were discussed by our participants in the reviewing system of
top-tier security conferences. Strong accepts and rejects seem to be consistent,
but **reviewers' decisions are subjective and random for papers in the middle
range**. Our participants stated that authors could "game" the system, taking
advantage of the randomness and lack of precision in the current reviewing
process by resubmitting at other venues with next to no changes until they "*get
lucky*", increasing the reviewing load and potential reviewer burnout.
@soneji2022flawed

### Who's right? {.alert}

P07: If we can be more accurate in our reviews, then yeah, it (gaming the
system) is a horrible thing to do. But, we are not; it works. And so, somebody
whose job depends on getting these papers in, why would you blame them for doing
something that works.

# Make it a better place

## Responsibilities of a PC @soneji2022flawed

### The dream PC {.example}

- Accept papers of quality.
- Provide constructive feedback.
- Review and advocate papers **fairly.**
- Help shape **the best program.**

### Chairs - how can I help?

From our analysis, we observe that Program Chairs have a very fine-grained
approach to evaluate papers for high quality ... providing constructive
feedback to authors as one of their primary responsibilities.

Only our chair participants ... firmly believed that **the responsibility of
reviewers does not end at inserting their reviews** in the system, but they
should also support ... the program ...

### Chairs - turn a blind eye {.alert}

No chair participant reported fair assessment as their responsibility.

## Characteristics of high-quality reviews @soneji2022flawed

### The dream review {.example}

- Providing constructive and actionable feedback.
- Being detailed and informative.
- Being comprehensive and well-structured.
- Being clear and carefully written.
- Being objective.
- **Including a paper summary.**
- Being anonymous.

### The small things {.alert}

P15: ... and some people do not really do that well (write a summary statement
about the paper), and I think it affects the quality of the review

### Accountability

According to P11, regardless of the review being good or negative, the reviewer
must be responsible for it, and an ideal solution is open reviews.

## Cards on the table

### Objectivity

P20: ... it's very hard to divorce a reviewing system if the community is
not huge and everyone knows each other, even if it's double-blind. ... it's
difficult to fix social problems with cabals that are accepting each other's
papers.

### Something on your mind?

Although our questionnaire did not cover the topic of PC discussions, eight
participants shared their concerns and opinions. ... P05 shared that if junior
PC members are intimidated by seniors, they might not speak freely or fight
against them. Such an issue defeats the purpose of PC discussions - to decide
the outcome collectively. @soneji2022flawed

### Hiding in plain sight

... there is still much redundancy with rolling submissions because many papers
that get rejected from one conference get reviewed verbatim by other PC members
at other venues. @soneji2022flawed

# Does it relate?

## Rolling submissions @soneji2022flawed

### The Good {.example}

... a benefit of having rolling submissions is the possibility of dialogue with the
authors and conveying reviewer expectations to revise the paper instead of
having the vicious cycle of rejection and resubmission.

### The Bad {.alert}

Participants ... reported that workload distribution has increased with rolling
submissions. They felt an increase in workload even though the number of papers
to review per day remained the same because with rolling deadlines review
turnaround times have been reduced ...

### The Ugly

P09 complained that the rolling deadlines model forgets how significant the
paper is and only focuses on how ready the paper is for publication. P09 is
worried that later submission rounds might receive a positive boost because they
might have accepted fewer papers in earlier rounds.

## Review delegation @soneji2022flawed

### The Good {.example}

P15: This revised model is pushing more people to write reviews where you
(reviewers) are by construction more constructive and positive towards papers
be- cause they’re fighting perhaps the common instinct to find reasons to
reject.

### The Bad {.alert}

P16 and P18 reported that the community is tired of PC members who delegate
everything to students and postdocs and still get rewarded for being on the PC.
P18 believed that it is terrible when reviewers outsource the reviews and add PC
memberships to their CV.

### The Ugly

P20 stated that delegation is abused a lot within the security community and is
considered a tradition. Senior members may not agree to be on the PC if they
could not delegate.

# Doctor, am I cured?

## Recommendations @soneji2022flawed {.allowframebreaks}

### Focus on review quality when mentoring novice reviewers.

To address the problem of reviewing overload with a scarcity of qualified
reviewers (P08), we recommend that conferences recruit reviewers through a
vetting process inspired by the shadow/student PC processes.

### Assist reviewers in performing timely reviews.

1. to ensure adequate resources of individual reviewers, chairs can request
   that reviewers limit the number of PCs that they serve on concurrently
2. to avoid overwhelming the reviewer, conferences can assign papers in
   more batches with a shorter turnaround time
3. to help individual PC members start their reviews, Program Chairs can
   ask reviewers to submit paper *summaries* early
4. leveraging more automation in managing the reviewing process

### Reward and recognize good reviewer behavior.

1. Leverage characteristics of high-quality reviews to design a list of quality
   indicators
2. Monitor reviewers’ performance by tracking
    certain variables such as:
    - the number of papers reviewed
    - time since the last paper was assigned
    - average review turnaround time
    - review length
    - inter-reviewer agreement
    - participation in rebuttals and discussions

### Make authors accountable for their submissions.

As some authors might be hesitant to submit their previous reviews, we believe
that organizations of top-tier security conferences could come together and
build a shared database to keep track of each paper in the reviewing pipeline.

## Take away

### The bigger picture {.alert}

P07: My main concern is you would not be able to use papers that are accepted in
selective conferences the same way you have been using them in the past to
signal quality and academic excellence.

::: {.block}
### Writing a review {.example}

P01: I feel that writing a review is just like writing a paper. In that, you
establish a position, you make some claims regarding that position, and then you
provide evidence to support that position. If any of these things are missing,
it is not a good review or a good paper.

:::

The authors have summarized their findings of PC members
[recommendations](https://github.com/sonejiananta/Security-Review-Process/blob/main/RecommendationsToWriteBetterSecurityPapers.pdf)
for authors looking to improve their paper writing.

```{=latex}
\center{\LARGE{\emph{The End.}}}
\center Made with \emoji{heart}, \LaTeX{} and \href{pandoc.org}{Pandoc}.
```

# Bibliography

## References {.allowframebreaks}
