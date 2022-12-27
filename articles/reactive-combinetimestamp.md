---
uid: reactive-combinetimestamp
title: CombineTimestamp
---

![Marble diagram](~/images/reactive-combinetimestamp.svg)

`CombineTimestamp` is used primarily to create a sequence of <xref href="System.Reactive.Timestamped`1"/> values for downstream operators, when timestamps have been extracted from other sources.

Alternatively, it can be used to preserve the value of a timestamp during post-processing operations. In this case, even though the timestamped value may be transformed multiple times, we can keep the original acquisition timestamp in a branch and use the <xref href="Bonsai.Reactive.Zip"/> operator followed by `CombineTimestamp` to carry the timestamp value forward.
