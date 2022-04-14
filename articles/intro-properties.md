---
title: "Introduction to Bonsai UI: Properties"
permalink: /docs/intro/properties/
excerpt: "A quick introduction to the properties section of the Bonsai UI."
last_modified_at:
---

- "Properties"
  - Intuition of a property grid?
  - Description
  - node properties
    - Description (bottom of the screen)
    - Different UI inputs

## Properties

Each Bonsai operator exposes a set of configuration properties that parameterize the operator's behaviour (e.g., the `Timer` operator exposes the period between generated values, whereas a `Threshold` on images exposes the brightness cutoff value applied to individual pixels).

The `Properties` panel will display all the configuration properties which are available for the currently selected operator. A summary description of the currently selected property can be found in the textbox at the bottom of the panel. Similarly, a description of the behaviour of the currently selected operator itself is shown at the top of the panel.

Most properties can be configured simply by changing the text value in the corresponding row of the property grid. Some properties have further specialized editors which can be accessed by clicking the drop-down or dialog button which will be displayed to the right of the property text.

**ProTip:** Some operators have even more specialized editor windows such as camera configuration dialogs or media player controls. If such property pages exist for the currently selected operator, the small `Property Pages` button above the property grid will become active.
{: .notice--info}
