---
uid: subject-async
title: "AsyncSubject"
---

![Marble diagram](~/images/language-subject-async.svg)

[`AsyncSubject`] stores and passes the last value (and only the last value) emitted by the source sequence to each subscribed observer. The value is also only sent out after the source sequence terminates. If the source sequence does not emit any value, [`AsyncSubject`] will also terminate without emitting any values.

> [!Tip]
> You can use the [`Take`](xref:Bonsai.Reactive.Take) operator before [`AsyncSubject`] to store the first value from an infinite sequence.

Any observers which subscribe after the source sequence terminates will immediately receive the stored value. If the source sequence terminates with an error, [`AsyncSubject`] will not emit any values but will pass along the error notification to all observers.

<!-- Reference-style links -->
[`AsyncSubject`]: xref:Bonsai.Reactive.AsyncSubject