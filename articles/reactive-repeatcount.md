---
uid: reactive-repeatcount
title: RepeatCount
---

![Marble diagram](~/images/reactive-repeatcount.svg)

`RepeatCount` reacts to successful termination by disposing the previous subscription and resubscribing to the source sequence, up to the maximum number of times specified in the <xref href="Bonsai.Reactive.RepeatCount.Count"/> property. Value notifications received from all of the subscriptions are forwarded to the result sequence.

> [!Warning]
> After the source sequence completes successfully the specified number of times, the result sequence will also terminate successfully. If any of the subscriptions terminates exceptionally, the result sequence will also terminate exceptionally, and no further resubscriptions will be made.

[!include[Resubscription](~/articles/reactive-resubscription.md)]
