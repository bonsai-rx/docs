---
uid: subjects
title: "Subjects" 
---

# Subjects

Subjects are a special type of operator that allows reusing and sharing of observable sequences. A subject acts as a bridge or proxy; it will subscribe to an observable sequence and pass all items it receives to multiple downstream operators, allowing them to share a single subscription to the source sequence.

Most subjects will be given a name. You can subscribe to a named subject from anywhere in the workflow using the `SubscribeSubject` operator, making subjects very useful to organize complex workflows into modular components that can be easily replaced. The following example demonstrates how to separate logging of a sequence of images using a [`PublishSubject`](#publishsubject).

![Example of using subjects to share observable sequences](~/images/language-subjects.svg)

> [!Warning]
> Subject names have scope. A subject with a given name can be accessed anywhere at the same level it is defined, or inside any node groups defined at that level. You cannot access a subject that was defined in a node group below the level you are in. If node groups are used to define [higher-order observable sequences](xref:higher-order), any subjects defined inside that group will be unique to each created sequence.

Finally, subjects also allow you to control the [temperature](xref:observables#temperature) of the shared sequence. You can convert a sequence from *cold* to *hot* using [`PublishSubject`](#publishsubject) or from *hot* to *cold* using [`ReplaySubject`](#replaysubject).

## Branching Subjects

Anonymous branch points in the workflow implicitly define a [`PublishSubject`](#publishsubject) with no name. All branches are first subscribed to the subject prior to subscribing to the common source sequence, so there is a guarantee that every value will be delivered to all branches, assuming immediate subscription.

![Example of using branching to share observable sequences](~/images/language-subjects-branching.svg)

> [!Warning]
> Dangling branches operate independently from each other, and from the subscription to the source sequence. If one branch terminates and resubscribes to the source (e.g. using the [`Repeat`](xref:Bonsai.Reactive.Repeat) operator) while other branches keep going, this will not reinitialize the shared subscription to the source. If such behavior is of interest, you will need to merge all branches together and implement the cancellation and resubscription logic downstream of the merge point.

## Subject Types

### AsyncSubject
[!include[Async Subject](~/articles/subject-async.md)]

### BehaviorSubject
[!include[Behavior Subject](~/articles/subject-behavior.md)]

### PublishSubject
[!include[Publish Subject](~/articles/subject-publish.md)]

### ReplaySubject
[!include[Replay Subject](~/articles/subject-replay.md)]

### ResourceSubject
[!include[Resource Subject](~/articles/subject-resource.md)]