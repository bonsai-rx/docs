---
uid: observables
---

# Observables

Observable sequences were first introduced in the [ReactiveX](http://reactivex.io/) library and are a central concept in the Bonsai programming language. This section discusses what is an observable sequence and how they are manipulated using Bonsai reactive operators.

## Introduction

An observable is a sequence of elements ordered in time, and can be represented visually using a marble diagram.

![Marble diagram](~/images/language-marblediagram.svg)

Each marble is called an `OnNext` notification, and represents a unique element emitted by the sequence. The color of each notification is typically used to represent the *order* of elements in the sequence, and shape indicates the *type or value* of each element. Marble diagrams allow you to describe when elements are emitted by a sequence. Notifications can occur regularly or irregularly and do not need to conform to any underlying clock -- observable sequences are asynchronous.

![Marble diagram with error](~/images/language-marblediagram-error.svg)

Sequences can be finite or infinite, depending on whether they emit a termination message. There are two types of termination message: `OnCompleted` (represented by a vertical bar) indicates successful termination of the sequence, and `OnError` (represented by an X) indicates an abnormal termination of the sequence due to a failure.

## Reactive Programming

In reactive programming, we compose operations on sequences (generation, filtering, combining, etc.) in order to define new sequences. The behaviour of each operator can also be analysed using a marble diagram. Below is an example for an operator manipulating a single sequence.

![Marble diagram for operator](~/images/language-marblediagram-operator.svg)

Arrows entering the box indicate that the operator is receiving notifications from the observable sequence that it is subscribed to. Arrows leaving the box show items that are emitted by the operator itself. If no `subscribe` arrow is explicitly indicated in the diagram, it is assumed to be placed at the start of the source sequence.

In this case we can see from the diagram that the [`Condition`](xref:Bonsai.Reactive.Condition) operator is filtering the input notifications from the source sequence: only notifications with a specific shape are sent out in the result sequence.

## Bonsai Workflows

The Bonsai language uses a graphical representation called a *workflow* to describe complex combinations of operations on observable sequences.

:::workflow
![Example workflow](~/workflows/language-sampleframe.bonsai)
:::

In a workflow, each node represents an operator defining an observable sequence. Nodes can be connected to other nodes, from left to right. Each connection indicates that the downstream operator on the right subscribes, or "listens", to the notifications of the upstream operator on the left.

By chaining networks of observable sequences in this way, it becomes possible to express complex interactive systems using a very compact visual representation. For example, the workflow diagram above describes a system that saves a grayscale snapshot from a camera into a file whenever there is a key press.

> [!Warning]
> Do not confuse a *workflow* with the marble diagrams described above. A marble diagram describes the dynamic behaviour over time of an observable sequence or reactive operator, whereas a Bonsai workflow describes only which different operators subscribe to each other.

We often combine marble diagrams with the workflow representation to better understand the behaviour of a Bonsai program. In the example above, we can see from the workflow that the [`Sample`](xref:Bonsai.Reactive.Sample) operator subscribes to the sequences generated by two other operators: [`Grayscale`](xref:Bonsai.Vision.Grayscale) and [`KeyDown`](xref:Bonsai.Windows.Input.KeyDown). `Grayscale` sends out images periodically, following the camera. However, `KeyDown` sends out a notification only when there is a key press, which can happen at any moment, even in between camera images.

What exactly will be the result sequence coming out of `Sample` in this case? Below is the marble diagram for the `Sample` operator, where the first sequence is the "source" sequence (`Grayscale`), and the second sequence is the "sampler" (`KeyDown`).

<img alt="Sample operator" src="~/images/language-samplegrayscale.svg" style="max-height:250px;padding:1em 0" />

From the marble diagram the behaviour of `Sample` is clear: it sends out the latest image that was received from `Grayscale` whenever there was a new key press. Marble diagrams can be an extremely useful tool to convey graphically the intuition of what a reactive operator is doing and are used extensively throughout the documentation.

## Hot versus cold observable sequences {#temperature}

One of the most important aspects for understanding the behaviour of observable sequences is to clarify the side-effects of subscription. For example, when an image processing operator like `Grayscale` subscribes to a sequence of images from a camera for the first time, the camera is turned on and an acquisition loop starts streaming live frames. If instead we have the `Grayscale` operator subscribe to a sequence of images from a pre-recorded video, the movie file is opened and frames begin to be decoded from disk into memory.

<img alt="Observable side effects" src="~/images/language-temperature-effects.svg" style="max-height:250px" />

Starting the camera or opening a movie file are examples of subscription side effects which are necessary in order to generate the data emitted from a sequence. The effects of subscription can have critical implications in the behaviour of our reactive programs, and to understand them we often need to determine what we call the *temperature* of the underlying observable sequence.

Consider again the difference between starting a camera and opening a video file when we have multiple observers. A video camera streams a live feed of images. When an operator subscribes to the feed at time *t<sub>0</sub>* it will receive frames from time *t > t<sub>0</sub>*. If another operator subscribes to the camera at a later time *t<sub>1</sub>*, it will receive all frames from time *t > t<sub>1</sub>* but not earlier: the camera shares the same subscription with all observers and never re-emits frames from the past! When observable sequences share the same subscription across all downstream observers, they are said to be *hot*.

<img alt="Observable side effects" src="~/images/language-temperature.svg" style="max-height:180px" />

A video file also generates a sequence of images, but in contrast to the camera, these images are generated on-demand. They are permanently stored on disk, and whenever an operator subscribes to the file, all the images can be played back from the beginning. Every operator will receive all the frames from the file, no matter when they subscribe to the sequence. When observable sequences have this on-demand behaviour, they are said to be *cold*.

Understanding the *temperature* of an observable sequence is particularly important when that sequence is shared between multiple operators. It can help to understand whether those operators will see the same data items, and what the effect of subscribing to the shared sequence at different times is going to be.

It is also possible to change the temperature of observable sequences using reactive operators. The [Replay](xref:Bonsai.Reactive.Replay) operator can be used to subscribe to the camera and start recording all incoming images. Every time a downstream observer subscribes to the result sequence, it will then replay all images on-demand, even if they subscribe late. The originally *hot* sequence has been turned into a *cold* observable by the replay behaviour.

<img alt="Replay operator" src="~/images/reactive-replay.svg" style="max-height:250px;padding:1em 0" />

Conversely, the [Publish](xref:Bonsai.Reactive.Publish) operator can be used to share a single subscription to a video file when sending images to downstream observers. In this case, instead of requesting a new subscription to the video for each new observer, the publish behaviour will always share only the images coming from the original subscription, no matter at what point the video is in. The original sequence has been turned from *cold* to *hot*.

<img alt="Publish operator" src="~/images/reactive-publish.svg" style="max-height:250px;padding:1em 0" />

In the Bonsai visual language, whenever two operators receive data from the same source, i.e. whenever there are branches in the workflow, subscriptions use the `Publish` behaviour. This means that the default sharing behaviour of Bonsai sequences is *hot*. It is possible to change this by using specialized sharing operators, called [Subjects](xref:subjects).