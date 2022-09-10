---
uid: subject-multicast
title: "MulticastSubject"
---

The `MulticastSubject` operator works like a sink which accesses the subject with the specified name, at the same scope level or above, and passes any values emitted by the source sequence to the shared subject. Depending on the behavior of the subject, these values will then be passed to any operators subscribed to the subject, including any termination and error notifications.

![Example workflow](~/images/language-subject-multicast.svg)
