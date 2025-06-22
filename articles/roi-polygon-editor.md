## Editor

To open the Region of Interest (ROI) editor, start the workflow and click on the ellipsis button inside the `Regions` property in the property grid, or double-click the operator node while holding <kbd>Ctrl</kbd>.

### Create ROI

To create a new ROI, press and hold the left mouse button anywhere in the editor window and drag the mouse to define a rectangular region of interest. Release the button to complete the selection. Additional ROIs can be created by pressing and holding the left mouse button in any location *outside* the boundaries of existing ROIs.

> [!NOTE]
> You can create an elliptical region of interest by holding <kbd>Shift</kbd> while dragging. You can further constrain an elliptical or rectangular region to be circular or square, respectively, by holding <kbd>Ctrl</kbd>.

### Move ROI

To move an ROI, press and hold the left mouse button anywhere *inside* the boundaries of an existing region and drag the mouse to reposition it. Releasing the button will complete the move.

### Scale ROI

To scale the shape of an ROI, press and hold the left mouse button anywhere *inside* the boundaries of an existing region and drag the mouse while holding <kbd>Shift</kbd>. Dragging the mouse away from the click will scale the region horizontally or vertically proportionally to the X and Y displacement, respectively. Releasing the button will complete the scale action.

> [!NOTE]
> You can constrain the scale to preserve the proportions of the original shape by holding <kbd>Ctrl</kbd>.

### Select ROI

You can select any existing ROI by clicking anywhere *inside* the boundaries of an existing region, or by pressing the <kbd>Tab</kbd> key to cycle between existing ROIs.

> [!TIP]
> Cycling selected ROIs using the <kbd>Tab</kbd> key can be very useful for locating extremely small regions which may have been created by mistake, in case they are hard to pick up by clicking.

### Delete ROI

To delete an ROI, first [select the ROI](#select-roi), and then press the <kbd>Del</kbd> key.

### Move control point

To move a control point in the polygonal ROI, press and hold the right mouse button *inside* the ROI, near the point you want to move, and drag the mouse to reposition the selected point.

### Add control point

To add a new control point to the polygonal ROI, double-click with the left mouse button *inside* the ROI. The new control point will be placed in the middle of the line segment which is closest to the double-click location.

### Remove control point

To remove a control point from the polygonal ROI, double-click with the right mouse button *inside* the ROI. The control point closest to the double-click location will be removed.

> [!NOTE]
> A minimum of three points are required to form a polygon; therefore, it is not possible to remove control points from triangular shapes.

> [!TIP]
> Undo and redo operations are supported on any of the above actions. To undo an action press <kbd>Ctrl</kbd>+<kbd>Z</kbd> on your keyboard. To redo something you've undone, press <kbd>Ctrl</kbd>+<kbd>Y</kbd>. You can press these shortcuts multiple times if you want to undo or redo multiple steps.