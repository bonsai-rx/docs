---
uid: subjects
---

# Subjects

Subjects are a special type of operator that allows reusing and sharing of observable sequences. A subject acts as a bridge or proxy; it will subscribe to an observable sequence and pass all items it receives to multiple downstream operators, allowing them to share a single subscription to the source sequence.

Most subjects will be given a name. You can subscribe to a named subject from anywhere in the workflow using the [`SubscribeSubject`](#subscribesubject) operator, making subjects very useful to organize complex workflows into modular components that can be easily replaced. The following example demonstrates how to separate logging of a sequence of images using a [`PublishSubject`](#publishsubject).

:::workflow
![Example of using subjects to share observable sequences](~/workflows/language-subjects.bonsai)
:::

Finally, subjects also allow you to control the [temperature](xref:observables#temperature) of the shared sequence. You can convert a sequence from *cold* to *hot* using [`PublishSubject`](#publishsubject) or from *hot* to *cold* using [`ReplaySubject`](#replaysubject).

## Scope of Subjects

Subjects have a visibility scope. Any subject can be accessed in the same workflow where it is declared, or inside any workflows nested inside operators defined at the same scope level. However, if a nested operator defines their own local scope and a subject is declared inside this new scope, that subject will not be visible outside that nested workflow. The border of node groups provides a visual indication of whether a nested operator defines a new local scope.

![Visual indication of node group name scoping](~/images/language-subjects-scope.svg)

Similarly, if node groups are used to define [higher-order observable sequences](xref:higher-order), any subjects defined inside the local scope will be unique to each created sequence.

## Branching Subjects

Anonymous branch points in the workflow implicitly define a [`PublishSubject`](#publishsubject) with no name. All branches are first subscribed to the subject prior to subscribing to the common source sequence, so there is a guarantee that every value will be delivered to all branches, assuming immediate subscription.

:::workflow
![Example of using branching to share observable sequences](~/workflows/language-subjects-branching.bonsai)
:::

> [!Warning]
> Dangling branches operate independently from each other, and from the subscription to the source sequence. If one branch terminates and resubscribes to the source (e.g. using the [`Repeat`](xref:Bonsai.Reactive.Repeat) operator) while other branches keep going, this will not reinitialize the shared subscription to the source. If such behavior is of interest, you will need to merge all branches together and implement the cancellation and resubscription logic downstream of the merge point.

## Source Subjects

Subjects can be declared either as a sink from an existing observable sequence, or as a source. Source subjects do not have a pre-existing input sequence from which values are generated, but rather they are setup to redirect inputs from multiple writers into one reader, for example for logging or control purposes.

:::workflow
![Example of declaring a subject as a sink or a source](~/workflows/language-subject-declaration.bonsai)
:::

If subjects are created as a source, the type of the subject needs to be declared explicitly on creation. This is done by selecting the source sequence in the workflow whose type we would like to share, and using the right-click context menu.

<img alt="How to declare a subject as a source"
     src="~/images/language-subject-source.png"
     style="max-height:160px;object-fit:contain" />

## Subject Types

Below are listed all different subject types, each represented visually by a unique icon.

:::workflow
![Visual indication of subject types](~/workflows/language-subject-types.bonsai)
:::

The last two operators, [`SubscribeSubject`](#subscribesubject) and [`MulticastSubject`](#multicastsubject), are used to access existing declared subjects for reading and writing, respectively. This is visually indicated by the `*` in the operator icon. Their behavior will be determined by the type of subject they are accessing.

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

### SubscribeSubject
[!include[Subscribe Subject](~/articles/subject-subscribe.md)]

### MulticastSubject
[!include[Multicast Subject](~/articles/subject-multicast.md)]