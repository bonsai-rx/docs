---
uid: higher-order
title: "Higher-Order Operators"
---

# Higher-Order Operators

When building simple reactive programs, it is usually enough to place a source for every device or every file you are accessing, and explicitly replicate the chain of transforms, sinks and combinators representing all the operations you need to perform on the data.

However, sometimes you may need to build systems that deal with an unknown number of sources. For example, imagine you wanted to create a workflow to merge together several video files. If you knew beforehand how many files you will need to combine and where they are exactly located, you might use the [`Concat`](xref:Bonsai.Reactive.Concat) operator to design a workflow like the following:

:::workflow
![Concatenate video files using first order operators](~/workflows/concatfile-firstorder.bonsai)
:::

But what if you did not know beforehand how many video files you will need to combine, and you wanted to merge all these videos without having to manually place a source node for every file?

Suppose all you had to get started was the [`EnumerateFiles`](xref:Bonsai.IO.EnumerateFiles) source. This operator creates an observable sequence that will emit all the file names in a folder, one after the other.

<img alt="Enumerate all file names in a folder"
     src="~/images/concatfile-enumeratefiles.svg"
     style="max-height:100px" />

In order to merge all the frames from these files in a single sequence you would need to create a different [`FileCapture`](xref:Bonsai.Vision.FileCapture) source for every file name emitted by this sequence, and pass all these sources to the [`Concat`](xref:Bonsai.Reactive.Concat) operator to generate a single sequence of frames. In other words, you want to create a sequence of frames for every file name in the folder, and then combine all these sequences into a single video file.

Whenever an operator receives or emits a sequence of sequences, we call it a higher-order operator. These operators play a particularly powerful role in the Bonsai programming language so it is useful to describe them in some detail.

## Higher-Order Workflows

Higher-order operators are represented in the workflow as nodes, just like any other operator. However, some higher-order operators allow you to specify their behaviour by using node groups. This allows you to program how the created sequences behave by reusing existing sources, transforms and other nodes.

For example, the video concatenation workflow can be implemented in Bonsai as follows:

![Concatenate video files using higher order operators](~/images/concatfile-higherorder.png)

The behaviour of the [`CreateObservable`](xref:Bonsai.Reactive.CreateObservable) operator is specified by the floating node group. Each time a new file name is emitted by the [`EnumerateFiles`](xref:Bonsai.IO.EnumerateFiles) source, the `CreateObservable` operator creates a new observable sequence controlled by the operators inside the group.

The input to the node group -- represented by the `Source1` operator -- is a sequence containing the individual items received by `CreateObservable`. In this case, it is a sequence with a single item that returns the file name emitted by the `EnumerateFiles` source. We use an externalized property to assign this value to the [`FileName`](xref:Bonsai.Vision.FileCapture.FileName) property of the `FileCapture` node, so that the correct video is accessed. Finally, the output of the node group determines the type and timing of the items emitted by the created sequence.

> [!Note]
> The `CreateObservable` operator creates new sequences for every input notification. However, it does not automatically subscribe to them -- they are latent. No data actually flows through the operators in the node group until some other higher-order operator -- in this case `Concat` -- actually takes these sequences and subscribes to them.

## Marble diagrams for higher-order operators

Marble diagrams can also be extended to describe the behaviour of higher-order operators. Emitted sequences are represented by diagonal timelines branching off the main operator timeline. The start of the branching sequence represents the time at which that sequence was emitted.

For example, the [`CreateObservable`](xref:Bonsai.Reactive.CreateObservable) operator used to convert file names into sequences of video frames is described below: 

<img alt="Create sequences of frames from file names"
     src="~/images/concatfile-createobservable.svg"
     style="max-height:250px;padding:1em 0" />

This marble diagram makes clear that the operator reacts to each file name notification by creating a new observable sequence. In this case, each created sequence will emit all the frames in the specified video. In general, however, this operator can produce all kinds of sequences, determined by the particular combination of operators inside the node group.

Finally, operators can combine sequences of sequences into a single sequence by collecting all the items from each sequence. There are multiple ways to perform this combination. For example, the [`Concat`](xref:Bonsai.Reactive.CreateObservable) operator subscribes to each emitted sequence one at a time, advancing to the next sequence only when the previous one terminated successfully.

This behaviour is described by the following marble diagram:

<img alt="Combine all sequences of frames into a single sequence"
     src="~/images/concatfile-combine.svg"
     style="max-height:250px;padding:1em 0" />