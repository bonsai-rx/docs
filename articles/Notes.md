---
title: "Introduction to Bonsai UI"
permalink: /docs/editor/
excerpt: "A quick introduction to the Bonsai workflow editor."
last_modified_at:
---


# Notes
    - What do we see when we open Bonsai?
      - Open
      - Save
      - Start
      - Project Folder

    - "Toolbox"
      - How to search toolbox
      - create nodes with predefined properties by typing
      - namespaces
      - subjects are added at the end and you can right click to add the corresponding multicast or subscribe
      - description
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
    -Status bar on the bottom


    - "Properties"
      - Intuition of a property grid?
      - Description
      - node properties
        - Description (bottom of the screen)
        - Different UI inputs
        - 
    - Visualizers
    - "Shortcuts"
    - Package manager & Gallery
      - Similar UI with different purposes
      - Pages browsing
      - How to update packages / download examples
        - Right panel, describe the entries
      - Package sources 
        - How to add new ones (local vs remote)
        - 
----