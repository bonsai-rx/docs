---
uid: reactive-switch
title: Switch
---

![Marble diagram](~/images/reactive-switch.svg)

`Switch` is a higher-order operator, so it takes as input a sequence of observable sequences. At any moment `Switch` is subscribed exclusively to the latest source sequence. As soon as a new sequence is emitted by the outer observable, it cancels subscription to the previous sequence and subscribes to the new sequence.

The resulting sequence will terminate successfully when the outer sequence has terminated successfully, and the currently active sequence (if any) also terminates successfully. It will terminate exceptionally if any of the sequences produces an error.

`Switch` is useful to model interruptible states, for example when transitioning between different modes of a state-machine, or switching between different video channels on demand.