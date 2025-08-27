---
uid: reactive-concat
title: Concat
---

![Marble diagram](~/images/reactive-concat.svg)

The `Concat` operator allows you to combine the output of multiple sequences of the same type into a single sequence. `Concat` subscribes to each sequence in turn, emits all the values from that sequence until successful termination, and then subscribes to the next sequence. Each sequence is guaranteed to only start after the previous one terminates.

The resulting sequence will terminate successfully when the last source sequence has terminated successfully, or exceptionally as soon as any sequence produces an error.

### Examples

Use `Concat` to sequentially combine the outputs of multiple sequences.

:::workflow
![Concat Example](../workflows/reactive-concat-example.bonsai)
:::

#### Stimulus Composition

Use `Concat` to create a stimulus sequence by combining multiple preloaded or defined sequences.

:::workflow
![Concat Application Stimuli](../workflows/reactive-concat-application-stimuli.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.Vision` and `Bonsai.Vision.Design` packages to be installed. Load separate images into each [`LoadImage`](xref:Bonsai.Vision.LoadImage) operator.

### Alternative

Use [`Merge`](xref:Bonsai.Reactive.Merge) instead if you want to combine sequences in parallel online.

Use [`OnErrorResumeNext`](xref:Bonsai.Reactive.OnErrorResumeNext) instead to concatenate multiple observable sequences, even if one or more terminate with an error.

### Higher-order operator

`Concat` also works as a higher-order operator, so it can take as input a sequence of observable sequences. In this case, it will subscribe to the first source sequence and start passing along all emitted values. As soon as that sequence terminates, it will subscribe to the next received sequence, either immediately if it arrived before termination of the first sequence, or as soon as a new observable sequence is emitted.

![Higher order](~/images/reactive-concatwindow.svg)

The higher-order variant is useful to queue execution of long-running operations, for example to sequence logic states in a task, or merging video files in a folder sequentially into a single frame sequence.