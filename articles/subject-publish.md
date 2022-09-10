---
uid: subject-publish
title: "PublishSubject"
---

![Marble diagram](~/images/language-subject-publish.svg)

`PublishSubject` passes to each subscribed observer only the values from the source sequence which were emitted subsequent to the time of observer subscription.

This means that any observers which subscribe late might lose one or more items between the time that `PublishSubject` is created and the time that the observer subscribes to it. If you require guaranteed delivery of all values from the source sequence, you need to ensure that all observers subscribe immediately upon workflow initialization. If this is not possible, you should consider switching to an [`AsyncSubject`](xref:Bonsai.Expressions.AsyncSubjectBuilder) if the sequence contains a single value, or a [`ReplaySubject`](xref:Bonsai.Expressions.ReplaySubjectBuilder) if the sequence contains multiple values.

If the source sequence terminates with an error, the `PublishSubject` will not emit any items to subsequent observers, but will pass along the terminating error.