---
layout: worksheet
title: Ephys Synchronization
---

# Ephys Synchronization

Synchronizing behaviour and other experimental events with recorded neural data is a fundamental component of neuroscience data collection and analysis. The exercises below will walk you through some common cases encountered in systems neuroscience experiments, and how to deal with them using Bonsai.

The general approach when synchronizing two independent data acquisition clocks is to record precise temporal events simultaneously in both systems. If you know that the two recorded events are the same, you know that those two time points are the same. When using multiple systems, it is common to choose the system with the fastest clock as _master_, and route all events to its analog or digital inputs.

### **Exercise 1:** Synchronizing behaviour events with ephys

- Insert a `KeyDown` source.
- Insert an `Equal` transform and set its `Value` to one of the keys. The output of this operator will toggle between `True` and `False` depending on whether the key press matches the specified key.
- Insert a `DigitalOutput` sink and connect it to Arduino pin 13.
- Connect the Arduino pin 13 to OpenEphys analog input 1.
- Insert an `Rhd2000EvalBoard` source.
- Select the `Rhd2000DataFrame` > `BoardAdcData` field from the source output using the context menu.
- Insert a `SelectChannels` transform and set the `Channels` property to 0. This will select only the first analog input channel.
- Insert a `MatrixWriter` sink and configure its `Path` property with a file name ending in `.bin`.
- Run the workflow and alternate pressing the selected key and some other key. Repeat this a couple of times to make the LED change state.
- Open the binary file in MATLAB/Python/R and plot the raw data. What can you conclude from it?

### **Exercise 2:** Synchronizing video with ephys using an LED

- Using the workflow from the previous exercise, insert a `CameraCapture` source and point the camera such that you can see clearly both the LED and the computer keyboard.
- Insert a `VideoWriter` sink and configure the `FileName` with a path ending in `.avi`.
- Insert a `Crop` transform and set the `RegionOfInterest` property to a small area around the LED.
- Insert a `Grayscale` transform.
- Insert a `Sum (Dsp)` transform. This operator will sum the brightness values of all the pixels in the input image.
- Select the `Scalar` > `Val0` field from the right-click context menu.
- Record the output in a text file using a `CsvWriter` sink.
- Open both the text file and the binary file in MATLAB/Python/R and check that you have detected an equal number of key presses in both files. What can you conclude from these two pieces of data?
- **Optional:** Repeat the exercise, replacing the `KeyDown` source with a periodic `Timer`. Can you point out some of the limitations of synchronizing a video stream with ephys using this method?

### **Exercise 3:** Synchronizing video with ephys using GPIO

Industrial grade cameras often include a GPIO connector which exposes input and output digital pins that operate similar to the pins in an Arduino or other microcontrollers. It is possible to configure these pins to report when the shutter of the camera is open or closed (i.e., when a frame is being exposed, the shutter is open and the pin goes `HIGH`, and conversely, when exposure stops, the shutter closes and the pin goes `LOW`).

By connecting this strobe signal to the ephys system and counting the number of pulses, it is possible to reconstruct with sub-millisecond precision how many exposures were acquired by the camera, and when each of them started. One problem to consider during high-speed recordings, however, is that frames may occasionally be dropped if the system cannot handle each acquired frame fast enough. One way to work around this issue is to record the hardware frame counter which can be enabled in the drivers of all industrial grade cameras.

- Connect one of the output GPIO camera pins to the OpenEphys analog input 1.
- Configure the camera output as _strobe_.
- Insert a `FlyCapture` source or other industrial grade camera capture source.
- Record the embedded hardware frame counter into a text file using `CsvWriter`.
- Record the OpenEphys analog input and verify that you can recover individual camera pulses.
- Point out some of the remaining difficulties of this approach and how you would adress them.

### **Exercise 4:** Synchronizing a visual stimulus with ephys

Displaying visual patterns on a screen or projector can be subject to significant delays that may impact synchronization with neural signals. Unfortunately, most displays do not directly provide any kind of digital output that might be used to synchronize stimulus presentation with ephys.

However, you can take advantage of the fact that all pixels in a frame are presented synchronously and reserve part of the display area to show a synchronization trigger. A passive photodiode can then be used to transduce this optical trigger into a digital signal that can be transmitted to the ephys auxiliary input channels.

In this exercise you will track the display of a very simple visual stimulus: a transition between black and white.

- Insert a `SolidColor` source and set its `Size` property to a positive value, e.g. 100,100.
- Insert a `Timer` source and set the `Period` to one second.
- Insert a `Mod` transform and set its `Value` property to 2.
- Insert a `Multiply` transform and set its `Value` property to 255.

> [!Note]
> The output of `Timer` is a growing count of the number of ticks. The `Mod` operator computes the remainder of the integer division of a number by another. Because every integer number in the sequence is alternately even or odd, the remainder of the division of the clock ticks by two will constantly oscillate between 0 and 1. Together with the `Multiply` operator, this is an easy way to make a periodic toggle between 0 and some value.

- Insert an `InputMapping` operator and connect it to the `SolidColor` source.
- Edit the `PropertyMappings` and add a mapping to the `Color` property. You will have to select four times the input to fill all the components of the `Color` scalar.
- Run the workflow and verify that the output of `SolidColor` oscillates between black and white.
- Insert an `Rhd2000EvalBoard` source.
- Select the `Rhd2000DataFrame` > `BoardAdcData` and either save or visualize its output.
- Connect a photodiode, or a photoresistor, to the ephys analog input and hold it flat against the screen, on top of the visualizer window.
- Verify that you can capture the transitions between black and white in the ephys data using the photodiode.

### **Exercise 5:** Synchronizing video acquisition to a visual stimulus using GPIO

The easiest way to synchronize the video acquisition with a visual stimulus is to make sure that your camera can see and track both your object of interest _and_ the visual stimulus. If you can extract the stimulus events from your video, then they are synchronized with all other video events by definition, since all pixels in a video frame are acquired synchronously.

However, sometimes this is not feasible: the stimulus may be covered by the subject, it may not be possible to recover the exact stimulus parameters from the camera view, or the stimulus may need to be filtered out entirely in order to allow for accurate tracking. In these situations, one solution for industrial grade cameras is to operate the camera in trigger mode, where the input GPIO channels can be used to align the beginning of each frame acquisition to the refresh rate of the display.

To do this, you can use the photodiode technique described in the previous exercise, but this time the digital signal from the photodiode will be used as a trigger for the camera by connecting it to one of the GPIO inputs.

- Assuming a DLP projector, how would you design the optical trigger for a camera system that ensures a single pulse is generated for each projected frame (hint: In a DLP projector, each colour of a BGR frame is projected sequentially: first the Blue channel, then the Green, and finally the Red channel, in quick succession)?
- **Optional:** Synchronize a camera with a projector using the GPIO trigger system outlined above.
