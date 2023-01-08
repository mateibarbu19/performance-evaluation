# Introduction

This review presents my take on a paper that challenges the organic nature of
scientific publishing, which "nourishes itself by internal communications and
intuitions, rather than repeatable experiments and investigations".

Its title quotes a interviewee's negative sentiments on the peer review system.
This is not to say that the system cannot become better in itself.

As any qualitative study does, this one first explores opinions and issues
pointed out by interviewees, relates them to the contextual problems that
started the explorations and formulates recommendations. The authors
contributions is, as they put it, "starting points for deeper discussions within
the security community".

# Recommendation addressing findings

One of the key findings of this study was that Program Chairs understood their
responsibilities better than Program Committee members (PCs). It seems that with
experience reviewers see their role in shaping the program. This correlates to
another theme, that of inexperience reviewers having a coarse approach,
forgetting to provide valuable, constructive feedback. Within the context of the
delegation process, which has as a purpose to train students to review early on,
the authors recommend conferences to recruit reviewers through the scrutiny of
the shadow/student PC processes. This is not a novel idea, but a effective one,
which mitigates bias inherit to ad-hoc training.

It seems that a overlook problem by other studies, but not a surprising one from
this @carter2017peer articles point of view, is that reviewers *postpone
everything to the end...* Reviewers shouldn't shake of the image of a mentor
yet, as Program Chairs could ensure adequate resources for them, limiting the
number of committees they activate in. Another solution may come from the
classical *divide and conquer* approach. Break up assigned papers in more
batches with a shorter turnaround time. This has it's advantages, but limits the
scheduling freedom of each reviewer. A third approach is based on interviewees'
subtle observation that a summary portraits the reviewers understating of the
paper. So asking they provide such summaries early, can establish that the
reviewer has read the paper in time to form a adequate opinion. And if we're in
a computer context, why not help automate this process?

In times where reward-based selection has become a vital organ of machine
learning, the authors saw the value in rewarding reviewers and taking credit for
a good review. This integrates into how venues relate to a reviewer, through
invitations, and a recognition process which is aided by quality indicators. The
responsibility falls onto the Program Chairs to design such a list of
indicators, and to track them. In the end, the "Good Reviewer" will be
appreciated by a letter of recommendation emphasizing the value in their  
contributions and as a member.

A key finding which I put off was the subjectiveness of evaluation metrics.
Within the security community, the number one thought on reviewers' minds is
novelty. And this novelty can be brought out by different aspects of a paper.
This seems fair enough, but taken together with the "randomness" of reviews, it
makes you beg the question: what can be done? To be more specific, reviewers
accept a clear winner and have diverse and concrete options on rejecting papers.
However, for the gray area in between there is no objectivity, being doomed to a
random outcome. In response, authors started to resubmit to other conferences,
in case they "get lucky", "gaming" the system. Whether or not it's the authors'
fault is another discussion covered in the study, but ton counteract these
effects, we should make authors accountable for their submissions. There is no
need to "send a negative connotation to reviewers" when resubmitting, but
construct based on previous reviews, which should be managed in a shared
database. Since unfair reviews are a reality, this solution takes a burden off
authors' chests, by cross-checking submissions and requiring reviewers to
unbiasedly consider a papers history as a trait.

The last two recommendation address more general problems. First there is the
inherit problems of a double-blind systems in a digital world. These were
studied before, but within a computer savvy community, embody a ghost that's
keep under silence. The papers authors haven't got a clear take on this problem.
It would be best for it to be solved through discussions within the community,
but then there comes out another lurking shadow, *social contracts*. Second, and
following the first, it seems right that after all this effort there should be a
reflection phase to see the effect on the system, and beyond the conferences'
participants, similarly to they way rolling submissions were waved in, by the
use of discussions on GitHub.

This said, there recommendations do not exhaustively address the issues found,
but more importantly represent the interviewees' opinions and hopes for change.
It seems that like evaluation metrics, these suggestions are not not highly
inter-related between participants. It just goes to show further work need to be
conducted.

# Related work

When it comes to fundamental problems in general with the peer review system,
this excellent short paper @carter2017peer underlines them even better then the
reviewed paper. Being a summary of both books and studies on this topic, in
points out the circular logic in taking peer reviewing for granted, with little
empirical evidence. We expect from it more then we put in, "reviewing is almost
always an additional burden". This is coherent with the original articles
findings that "younger faculty are ambitious and accept all invitations because
of the pressure of building their CV" and the abuse of delegation. All biases
mentioned in the short paper were treated or observed within the study.

Another short paper @lee2013bias warns us that peer reviewing has degenerated
from its historic roots. From Syrian physicians in the ninth century having
their notes checked by a senior medical council and the Royal Society of London
committee assessing the papers submitted to their journal, the peer review
system can now distort research results. It seems that at its core, reviewing
wasn't only about validating quality, but "assisting the board of editors to
accept or reject a paper and helping to improve submitted manuscripts by
eliminating major flaws and gaps". From the reviewed study's key findings,
Program Chairs understand this responsibility better the PCs. While the short
paper isn't the first to emphasize distortion of results caused by the system,
it stresses the difference between level of bias introduced by different
systems.

Changing our focus to a computer science domain, Ragone et al. proposed a
theoretical model @ragone2013peer, which helps by introducing new metrics and
techniques, whose purpose is to understand and improve the peer review system
along the following dimensions: *reliability*, *fairness*, *validity* and
*efficiency*. This is important as it checks the ability of the system to offer
a prognosis for papers impact. It represents a cornerstone reference and its
scientometric significance could not be stressed enough, as it opened my eye to
the rigor of metascience. 

Returning to short papers, CHI's peer reviewing course @wilson2022peer confirms
this study's finding on the difficulties that new reviewers face and the sudden
need of expansion of the reviewer pool. What is even more interesting is the
resonance with one of this study's participants responses on *that writing a
review is just like writing a paper*.

Strongly tied to this study's research questions, a ICSE survey
@prechelt2018community focuses on the community's perspective of the peer review
system. It seems that reviews are divided into three equally sized buckets:
good, useless or misleading and in between. Moreover, there is a need within the
community for tangible proof of improvements in the system. This study's
findings also show what the survey uncovered about reviewers abusing their power
or being unmotivated because of the little contribution reviewing brings to ones
reputation. This was specifically addressed in the endings recommendations.

A unquoted paper @petre2020mapping follows down a similar path as this ones, but
forks when it comes to setting standards for reviewing. Being also a exploration
on how peer review is used in various venues, it occupies itself with a
comprehensive analysis of the key components of the system: *criteria*, *the
review process*, *roles and responsibilities*, and *ethics and etiquette*. In
the end, it surmises both the authors and reviewers perception of reviews, being
a valuable and finite resource affected by the venues traits. It also follows a
pattern that the peer review system doesn't serve a big community. It also draws
the same conclusion as this study regarding the recruiting process, however it
goes beyond in its analysis of meta-reviews.

The related work is not limited to peer review systems investigations, so it
would be fair to mention that the authors put effort in studying what makes a
quality paper, not only a quality review, and left recommendations also in this
sense.

# References