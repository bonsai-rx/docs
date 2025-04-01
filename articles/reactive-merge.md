---
uid: reactive-merge
title: Merge
---

![Marble diagram](~/images/reactive-merge.svg)

The `Merge` operator allows you to combine the output of multiple sequences of the same type into a single sequence. `Merge` subscribes to all source sequences in parallel and emits all the elements from each sequence downstream.

The resulting sequence will terminate successfully only when all source sequences have terminated successfully, or exceptionally as soon as any sequence produces an error.

### Higher-order operator

`Merge` also works as a higher-order operator, so it can take as input a sequence of observable sequences. In this case, it will subscribe to all source sequences as soon as they are emitted by the outer sequence, and emit all elements from each sequence downstream.

![Higher order](~/images/reactive-mergewindow.svg)

The higher-order variant is useful to combine notifications from multiple event sources running in parallel, for example when waiting for the first event from multiple input conditionals, or when logging data from multiple sources to the same file.

### Example
Use `Merge` to merge two or more sequences together.

:::workflow
![Merge Sequences](../workflows/reactive-merge-example.bonsai)
:::

### Alternative
Use [`Sum`](xref:Bonsai.Reactive.Sum) instead to yield a single value at the end of a sequence.