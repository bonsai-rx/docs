---
uid: subject-subscribe
title: "SubscribeSubject"
---

The `SubscribeSubject` operator is essentially a source which accesses a subject with the specified name, at the same scope level or above, and subscribes to it. Depending on the behavior of the subject, values from the shared underlying sequence will then be passed to any operators downstream from `SubscribeSubject`, as if these operators were connected to the subject directly.

![Example workflow](~/images/language-subject-subscribe.svg)
