---
uid: subject-publish
title: "PublishSubject"
---

![Marble diagram](~/images/language-subject-publish.svg)

`PublishSubject` passes to each subscribed observer only the values from the source sequence which were emitted after the time of subscription.

This fire-and-forget behavior means that any observers which subscribe late might lose one or more items emitted between the time that `PublishSubject` was created and the time that the observer subscribed to it. If you require guaranteed delivery of all values from the source sequence, you need to ensure that all observers subscribe immediately upon workflow initialization. If this is not possible, you should consider switching to an [`AsyncSubject`](xref:Bonsai.Reactive.AsyncSubject) if the sequence contains a single value, or a [`ReplaySubject`](xref:Bonsai.Reactive.ReplaySubject) if the sequence contains multiple values.

If the source sequence terminates with an error, `PublishSubject` will not emit any items to subsequent observers, but will pass along the terminating error.