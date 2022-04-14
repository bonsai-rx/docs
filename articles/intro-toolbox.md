---
title: "Introduction to Bonsai UI: Toolbox"
permalink: /docs/intro/toolbox/
excerpt: "A quick introduction to the toolbox section of the Bonsai UI."
last_modified_at:
---

- "Toolbox"
  - How to search toolbox
  - create nodes with predefined properties by typing
  - namespaces
  - subjects are added at the end and you can right click to add the corresponding multicast or subscribe
  - description


## Toolbox

The `Toolbox` allows you to search for available Bonsai operators to place in the workflow. The listing is organized into five main categories:

|                Category                | Description                                           |
| :------------------------------------: | ----------------------------------------------------- |
|     ![Source](~/images/source.svg)     | generate event streams from devices or files          |
|  ![Transform](~/images/transform.svg)  | convert or process individual data items              |
|       ![Sink](~/images/sink.svg)       | save data or trigger external outputs                 |
| ![Combinator](~/images/combinator.svg) | manage control flow or synchronize parallel inputs    |
|   ![Workflow](~/images/workflow.svg)   | reusable workflow fragments stored in `.bonsai` files |

Operators inside each major category are further organized by package namespaces. These namespaces come from the packages you have installed at any given moment. The name of each namespace can give you a hint about what kind of operations or devices can be accessed inside (e.g., the `Audio` namespace provides access to audio capture devices or WAV file readers).

Once you have found which operator you want to insert, you can place it by double-clicking, dragging it to the workflow or alternatively right-clicking and selecting a specific placement option. See the [Commands and Shortcuts](#commands-and-shortcuts) section for more information.

### Search Operators

Another way to quickly find operators is to use the `Search` textbox. Any text inserted here is matched against available operator or namespace names for a match in any order. This means you can search not only for a specific operator name but also by category names to locate all the operators in a namespace (e.g., try typing `Arduino`).

**ProTip:** You can also directly type and search for operator names when the `Workflow` panel has the input focus. This allows you to simply start typing an operator name and directly select which operator you want with the up/down arrow keys. Once you have the right operator, press the `Enter` key to place it. You can repeat the process multiple times to very quickly chain a sequence of operators.
{: .notice--info}