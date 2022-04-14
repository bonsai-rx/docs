---
title: "Introduction to Bonsai UI: Shortcuts"
permalink: /docs/intro/shortcuts/
excerpt: "A quick introduction to the shortcuts available in the Bonsai UI."
last_modified_at:
---

## Commands and Shortcuts

Below is a summary of the most used commands and shortcuts in the workflow editor:

### Running the workflow

{: .no_toc}

- Click the arrow `Start` button
- Press `F5`

### Stopping the workflow

{: .no_toc}

- Click the square `Stop` button
- Press `Shift`+`F5`

### Insert an operator after the selected node

{: .no_toc}

- Right-click the operator name and select the `Insert After` option
- Drag-and-drop the operator from the toolbox to the worflow
- Double-click the operator name in the toolbox
- Press the `Enter` key while the operator is selected in the toolbox
- Copy another node (`Ctrl`+`C`) and paste in the toolbox (`Ctrl`+`V`)

### Insert an operator before the selected node

{: .no_toc}

- Right-click the operator name and select the `Insert Before` option
- Hold the `Shift` key together with any of the above commands (e.g., `Shift`+`Enter`)

### Insert an operator as a new branch of the selected node

{: .no_toc}

- Right-click the operator name and select the `Create Branch` option
- Hold the `Alt` key together with any of the above commands (e.g., `Ctrl`+`Alt`+`V`)

### Create a connection between two operators

{: .no_toc}

- Right-click the source node, select the `Create Connection` option and left-click on the target node
- Drag the source node and drop it on the target node

### Remove a connection between two operators

{: .no_toc}

- Right-click the source node, select the `Remove Connection` option and left-click on the target node
- While holding the `Shift` key, drag the source node and drop it on the target node

### Selecting multiple nodes

{: .no_toc}

- Click an empty space in the workflow panel and drag a box around the nodes to be selected
- While holding the `Shift` key, press the arrow keys to select a string of nodes around the currently selected node
- Hold the `Ctrl` key and click on a node to add/remove it from the current selection

**ProTip:** Many operations can be performed on multi-node selections (e.g., delete, create connections, create a node group, etc.).
{: .notice--info}

### Open the type visualizer for an operator

{: .no_toc}

- Double-click on the target node while the workflow is running
- Right-click on the target node and select a visualizer from the `Show Visualizer` dropdown
- Press `Enter` while the target node is selected

### Grouping operators into a node group

{: .no_toc}

- Select all the nodes to group and press `Ctrl`+`G` to create a nested workflow
- Right-click on a multi-node selection and select a group type from the `Group` dropdown context menu

**ProTip:** You can change the type of an existing group simply by right-clicking on the group node and selecting a different type from the `Group` dropdown.
{: .notice--info}

### Open a node group or the default editor for an operator

{: .no_toc}

- Double-click on the target node while the workflow is not running
- If the workflow is running, hold the `Ctrl` key while double-clicking on the target node
- Press `Ctrl`+`Enter` while the target node is selected

### Ungrouping a node group

{: .no_toc}

- Right-click on the group node and select the `Ungroup` option from the context menu
- Press `Ctrl`+`Shift`+`G`

### Open context menu

{: .no_toc}

- Right-click any node, multi-node selection or empty space in the workflow panel
- Press `Shift`+`F10`

**ProTip:** Depending on what is currently selected, the context menu may show different available actions.
{: .notice--info}