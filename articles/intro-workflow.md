---
title: "Introduction to Bonsai UI: Workflow"
permalink: /docs/intro/workflow/
excerpt: "A quick introduction to the workflow section of the Bonsai UI."
last_modified_at:
---

- "Workflow"
  - left-right flow of information
  - dot on the left accepts an input
  - you can reorder nodes by alt dragging
  - errors on compiling are red
  - Nodes have properties (can be access through the "Properties") that can be dynamically changed by externalizing properties (ref).
    - These "settable" properties are shown as gray starburst circle with a dashed line to the corresponding node.
  - Nodes can be grouped
    - Some groups have no functional consequence (GroupedWorkflow), others do.
    - Regardless, one can access the inside of the group by double clicking the node
    - Groups usually have inputs (WorkflowInput) and outputs (workflowoutput)
  - Two ways to interact with nodes with the mouse:
    - Some nodes have a behavior when interacted with by double left clicking (e.g. GroupedWorkflow, FileCapture, CreateWindow)
    - Right clicking exposes stuff
      - Generally speaking: Go over all the menu items in the tab
  - Disabled nodes appear grayed out. 


## Workflow

The `Workflow` panel is where you place reactive operators to create data processing pipelines or other asynchronous computations. Each operator in Bonsai is represented by a circular node. Nodes can be connected together, forming a directed feedforward graph from left to right. Connections indicate which operators receive data from which other operators (see the [Introduction](/introduction/) and the [Language Guide](/docs/observables/) for an extended discussion).

The most useful action to learn your way around the `Workflow` panel is right-clicking. This will bring up the context menu for the specific node you selected, or a list of possible actions you can do with the current selection:

![The workflow context menu](~/images/contextmenu.png)

If only one node is selected, the `Output` menu item will display the type of the elements emitted in the observable sequence of that operator.

**ProTip:** If the output of an operator is a complex type, you can also inspect its public data members from the context menu. Clicking on any one of these members will automatically place a new `MemberSelector` transform which selects that member from the output.
{: .notice--info}

The context menu also allows you to externalize public properties of the operator into explicit nodes in the workflow, so you can change their values dynamically based on the output of other nodes (see the [Property Mapping](/docs/property-mapping/) section for more information).

Finally, it is possible to group nodes, both for organizing large workflows, and to define [higher-order operators](/docs/higher-order/). The most basic grouping is the nested workflow which allows you to encapsulate a workflow fragment inside a single node. This `NestedWorkflow` can be assigned a `Name` and `Description` for ease of reference. Any named properties which are externalized by nodes in the group will be shown as properties of the `NestedWorkflow` so you can literally treat the group as a single node.

**ProTip:** You can use `NestedWorkflow` nodes to document your workflow by adding names and descriptions to individual processing branches. No additional processing cost is incurred by the use of `NestedWorkflow` nodes.
{: .notice--info}

### Snippets

You can create and save workflow snippets by selecting one or more nodes and clicking the `Save Snippet As...` button in the context menu.

Snippets are a powerful way to reuse common workflow patterns across projects. When you save a new snippet file it will immediately show up in the `Toolbox` panel for placement. Placing a snippet is equivalent to copying the workflow fragment stored in the snippet file into your current workflow.

It is possible to organize snippets into folders so you can search them by keyword, similar to the role of namespaces found in compiled Bonsai packages.