---
uid: reactive-repeat
title: Repeat
---

![Marble diagram](~/images/reactive-repeat.svg)

`Repeat` reacts to successful termination by disposing the previous subscription and resubscribing to the source sequence. Elements received from all of the subscriptions are forwarded to the result sequence.

> [!Warning]
> If any of the subscriptions terminates exceptionally, the result sequence will also terminate exceptionally, and no further resubscriptions will be made.

[!include[Resubscription](~/articles/reactive-resubscription.md)]
