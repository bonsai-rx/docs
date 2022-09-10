---
uid: subject-async
title: "AsyncSubject"
---

![Marble diagram](~/images/language-subject-async.svg)

`AsyncSubject` stores and passes the last value (and only the last value) emitted by the source sequence to each subscribed observer. The value is also only sent out after the source sequence completes. If the source sequence does not emit any values, `AsyncSubject` will also complete without emitting any values.

Any observers which subscribe after the source sequence completes will also immediately receive the stored value. If the source sequence terminates with an error, `AsyncSubject` will not emit any values but will pass along the error notification to all observers.
