---
uid: expressions-visualizermapping
title: "VisualizerMapping"
---

The `VisualizerMapping` operator specifies that the visualizer of the current node should be combined with the target node. The behaviour of the target operator will otherwise remain unaffected, since the subscription to the mapping is not considered as a proper upstream source. This is indicated in the editor by the dashed line linking the property mapping operator to its target.

> [!Note]
> If multiple visualizer mappings are specified for the target node, the order of visualizer combination follows the connection order, from top to bottom.

> [!Warning]
> The visualizer of the target node must be a type derived from <xref href="Bonsai.Design.MashupVisualizer"/>. Furthermore, the target mashup must also support the specified visualizer type as a mashup source. Otherwise, the visualizer mapping will have no effect.
