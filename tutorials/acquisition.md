---
layout: worksheet
title: Acquisition and Tracking
---

# Acquisition and Tracking

## Video Acquisition

Bonsai can be used to acquire and record data from many different devices. The exercises below will make you comfortable with the most common Bonsai data types. The first data type we will discuss is an image, which is represented as a 2D matrix of pixels. Each pixel represents either a brightness value in a grayscale image, or a BGR colour value in a colour image.

### **Exercise 1:** Saving a video

:::workflow
![Saving a video](~/workflows/acquisition-video.bonsai)
:::

- Insert a [`CameraCapture`](xref:Bonsai.Vision.CameraCapture) source.
- Insert a [`VideoWriter`](xref:Bonsai.Vision.VideoWriter) sink.
- Configure the `FileName` property of the `VideoWriter` operator with a file name ending in `.avi`.
- Run the workflow and check that it generates a valid video file.

### **Exercise 2:** Saving a grayscale video

:::workflow
![Saving a grayscale video](~/workflows/acquisition-grayvideo.bonsai)
:::

- Insert a [`Grayscale`](xref:Bonsai.Vision.Grayscale) transform between `CameraCapture` and `VideoWriter`.
- Run the workflow. The output should now be a grayscale movie.
- How would you modify the workflow to record **both** a colour and a grayscale movie?

## Audio Acquisition

Audio data is captured at much higher temporal sampling frequencies than video. However, the data is typically buffered into chunks of multiple samples before being sent to the computer. Also, multi-channel data can be acquired simultaneously in the case of a stereo microphone, or high-density ephys probes. Such multi-sample, multi-channel data is typically represented as a 2D matrix, where rows represent channels, and columns represent time.

### **Exercise 3:** Saving a WAV file

:::workflow
![Saving a WAV file](~/workflows/acquisition-audio.bonsai)
:::

- Insert an [`AudioCapture`](xref:Bonsai.Audio.AudioCapture) source.
- Insert an [`AudioWriter`](xref:Bonsai.Audio.AudioWriter) sink.
- Configure the `FileName` property of the `AudioWriter` operator with a file name ending in `.wav`.
- Make sure that the [`SampleRate`](xref:Bonsai.Audio.AudioWriter.SampleRate) property of the `AudioWriter` matches the frequency of audio capture.
- Run the workflow for some seconds. Playback the file in your favorite media player to check that it is a valid audio file.

### **Exercise 4:** Saving raw binary waveform data

:::workflow
![Saving raw binary waveform data](~/workflows/acquisition-audiobinary.bonsai)
:::

- Replace the `AudioWriter` operator with a [`MatrixWriter`](xref:Bonsai.Dsp.MatrixWriter) sink.
- Configure the `Path` property of the `MatrixWriter` operator with a file name ending in `.bin`.
- Run the workflow for some seconds.
- Open the resulting binary file in MATLAB/Python/R and make a time series plot of the raw waveform samples.
  - **MATLAB:** Use the [`fread`](https://www.mathworks.com/help/matlab/ref/fread.html) function to read the binary file. The source data must be set to `int16`.
  - **Python:** Use the [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html) in the [`numpy`](https://numpy.org/install/) package to read the binary file. The `dtype` option must be set to `np.int16`.

### **Exercise 5:** Trigger an auditory stimulus

:::workflow
![Playback an audio file](~/workflows/acquisition-audioplayback.bonsai)
:::

- Insert an [`AudioReader`](xref:Bonsai.Audio.AudioReader) source.
- Configure the [`FileName`](xref:Bonsai.Audio.AudioReader.FileName) property to point to the audio file you recorded in _Exercise 3_.
- Insert an [`AudioPlayback`](xref:Bonsai.Audio.AudioPlayback) sink.
- Run the workflow and check the sound is played correctly.

:::workflow
![Trigger an auditory stimulus](~/workflows/acquisition-audiotrigger.bonsai)
:::

- Insert a [`KeyDown`](xref:Bonsai.Windows.Input.KeyDown) source.
- Set the [`BufferLength`](xref:Bonsai.Audio.AudioReader.BufferLength) property of the `AudioReader` to zero, so that all audio data is read into a single buffer.
- Combine the key press with the audio data using the [`WithLatestFrom`](xref:Bonsai.Reactive.WithLatestFrom) combinator.
- Right-click the `WithLatestFrom` operator. Select the `Tuple` > `Item2` member from the context menu.
- Move the `AudioPlayback` sink so that it follows the selected `Item2` member.
- Run the workflow and press a key. What happens if you press the key several times?

## Arduino Acquisition

In order to communicate and interact with an Arduino using Bonsai, you must program the microcontroller to send and receive binary data from the computer via the USB cable. Fortunately, the Arduino environment already comes with a standard implementation of an efficient binary protocol called **[Firmata](https://github.com/firmata/arduino)** which can be used for serial communication with external applications such as Bonsai.

### Configure Arduino for real-time communication

- Open the [Arduino IDE](https://www.arduino.cc/en/Main/Software).
- Upload `StandardFirmata` to your Arduino. The code can be found in `File` > `Examples` > `Firmata`.

### **Exercise 6:** Saving analog data

:::workflow
![Saving analog data](~/workflows/acquisition-analog.bonsai)
:::

- Insert an [`AnalogInput`](xref:Bonsai.Arduino.AnalogInput) source.
- Configure the [`PortName`](xref:Bonsai.Arduino.AnalogInput.PortName) property to point to the correct serial port where the Arduino is connected.
- Run the workflow and visualize the output of the analog source. What do you see?
- **Optional:** Connect a sensor to the analog input pin, e.g. a potentiometer or a button.
- Insert a [`CsvWriter`](xref:Bonsai.IO.CsvWriter) sink. This operator records input data into a text file.
- Configure the [`FileName`](xref:Bonsai.IO.CsvWriter.FileName) property of the `CsvWriter` operator with a file name ending in `.csv`.
- Run the workflow, record some interesting signal, and then open the result text data file.

### **Exercise 7:** Control an LED

:::workflow
![Control an LED](~/workflows/acquisition-led.bonsai)
:::

- Insert a [`Boolean`](xref:Bonsai.Expressions.BooleanProperty) source.
- Insert a [`DigitalOutput`](xref:Bonsai.Arduino.DigitalOutput) sink.
- Set the [`Pin`](xref:Bonsai.Arduino.DigitalOutput.Pin) property of the `DigitalOutput` operator to 13.
- Configure the [`PortName`](xref:Bonsai.Arduino.DigitalOutput.PortName) property.
- Run the workflow and change the `Value` property of the `Boolean` operator.
- **Optional:** Use your mouse to control the LED! Replace the `Boolean` operator by a [`MouseMove`](xref:Bonsai.Windows.Input.MouseMove) source (hint: use [`GreaterThan`](xref:Bonsai.Expressions.GreaterThanBuilder), [`LessThan`](xref:Bonsai.Expressions.LessThanBuilder), or equivalent operators to connect one of the mouse axis to `DigitalOutput`).

### **Exercise 8:** Control a servo motor

:::workflow
![Control a servo motor](~/workflows/acquisition-servo.bonsai)
:::

- Insert a [`Timer`](xref:Bonsai.Reactive.Timer) source. Set its [`Period`](xref:Bonsai.Reactive.Timer.Period) property to 500 ms.
- Insert a [`Take`](xref:Bonsai.Reactive.Take) operator. Set its [`Count`](xref:Bonsai.Reactive.Take.Count) property to 10.
- Insert a [`Rescale`](xref:Bonsai.Dsp.Rescale) operator. Set its [`Max`](xref:Bonsai.Dsp.Rescale.Max) property to 10, and its [`RangeMax`](xref:Bonsai.Dsp.Rescale.RangeMax) property to 180.
- Insert a [`Repeat`](xref:Bonsai.Reactive.Repeat) operator.
- Insert a [`ServoOutput`](xref:Bonsai.Arduino.ServoOutput) sink.
- Set the [`Pin`](xref:Bonsai.Arduino.ServoOutput.Pin) property of the `ServoOutput` operator to 9.
- Configure the [`PortName`](xref:Bonsai.Arduino.ServoOutput.PortName) property.
- Connect a servo motor to the Arduino pin 9 and run the workflow. Can you explain the behaviour of the servo?
- **Optional:** Make the servo sweep back and forth.

## Video Tracking

Bonsai allows processing captured raw video data to extract real-time measures of behaviour or other derived quantities. The exercises below will introduce you to some of its online video processing capabilities.

### **Exercise 9:** Segmentation of a coloured object

:::workflow
![Segmentation of a coloured object](~/workflows/acquisition-segmentation1.bonsai)
:::

- Insert a [`CameraCapture`](xref:Bonsai.Vision.CameraCapture) source.
- Insert a [`RangeThreshold`](xref:Bonsai.Vision.RangeThreshold) transform.
- Open the visualizer for the `RangeThreshold` operator.
- Configure the [`Lower`](xref:Bonsai.Vision.RangeThreshold.Lower) and [`Upper`](xref:Bonsai.Vision.RangeThreshold.Upper) properties of the `RangeThreshold` to isolate your coloured object (hint: click the small arrow to the left of each property to expand their individual values).

This method segments coloured objects by setting boundaries directly on the BGR colour space. This colour space is considered a poor choice for colour segmentation. Can you see why?

:::workflow
![Segmentation of a coloured object](~/workflows/acquisition-segmentation2.bonsai)
:::

- Replace the `RangeThreshold` operator by a [`ConvertColor`](xref:Bonsai.Vision.ConvertColor) transform. This node converts the image from the BGR colour space to the [Hue-Saturation-Value (HSV) colour space](https://en.wikipedia.org/wiki/HSL_and_HSV).
- Insert an [`HsvThreshold`](xref:Bonsai.Vision.HsvThreshold) transform.
- Configure the [`Lower`](xref:Bonsai.Vision.HsvThreshold.Lower) and [`Upper`](xref:Bonsai.Vision.HsvThreshold.Upper) properties of the `HsvThreshold` to isolate the object.
- Test the resulting tracking under different illumination conditions.

### **Exercise 10:** Real-time position tracking

:::workflow
![Real-time position tracking](~/workflows/acquisition-tracking.bonsai)
:::

- Starting with the workflow from the previous exercise, insert a [`FindContours`](xref:Bonsai.Vision.FindContours) transform. This operator traces the contours of all the objects in a black-and-white image. An _object_ is defined as a region of connected white pixels.
- Insert a [`BinaryRegionAnalysis`](xref:Bonsai.Vision.BinaryRegionAnalysis) transform. This node calculates the area, center of mass, and orientation for all the detected contours.
- Insert a [`LargestBinaryRegion`](xref:Bonsai.Vision.LargestBinaryRegion) transform to extract the largest detected object in the image.
- Select the `ConnectedComponent` > `Centroid` field of the largest binary region using the context menu.
- Record the position of the centroid using a [`CsvWriter`](xref:Bonsai.IO.CsvWriter) sink.
- **Optional:** Open the CSV file in Excel/Python/MATLAB/R and plot the trajectory of the object.

### **Exercise 11:** Background subtraction and motion segmentation

:::workflow
![Background subtraction](~/workflows/acquisition-backsubtraction.bonsai)
:::

- Create a grayscale video workflow similar to _Exercise 2_.
- Insert a [`Skip`](xref:Bonsai.Reactive.Skip) operator. Set its `Count` property to 1.
- In a new branch, insert a [`Take`](xref:Bonsai.Reactive.Take) operator. Set its `Count` property to 1.
- Combine the images from both branches using the [`CombineLatest`](xref:Bonsai.Reactive.CombineLatest) combinator.
- Insert the [`AbsoluteDifference`](xref:Bonsai.Dsp.AbsoluteDifference) transform after `CombineLatest`.
- Insert a [`Threshold`](xref:Bonsai.Vision.Threshold) transform. Visualize the node output and adjust the [`ThresholdValue`](xref:Bonsai.Vision.Threshold.ThresholdValue) property.

_Describe in your own words what the above workflow is doing._

:::workflow
![Motion segmentation](~/workflows/acquisition-motionsegmentation.bonsai)
:::

- Replace the `CombineLatest` operator with the [`Zip`](xref:Bonsai.Reactive.Zip) combinator.
- Delete the `Take` operator.

_Describe in your own words what the above modified workflow is doing._

### **Exercise 12:** Measuring motion

:::workflow
![Measuring motion](~/workflows/acquisition-motion.bonsai)
:::

- Create a grayscale video stream similar to _Exercise 2_.
- Insert a [`BackgroundSubtraction`](xref:Bonsai.Vision.BackgroundSubtraction) transform. Set its `AdaptationRate` property to 1.
- Insert a [`Sum`](xref:Bonsai.Dsp.Sum) operator. This operator will sum the values of all the pixels in the image.
- Run the workflow, point the camera at a moving object and visualize the output of the `Sum` operator. Compare small movements to big movements. What happens to the signal when the object holds perfectly still?
- Right-click the `Sum` operator. Select the `Scalar` > `Val0` member from the context menu.

> [!Note]
> The `Sum` operator sums the pixel values across all image colour channels. However, in the case of grayscale binary images, there is only one active channel and its sum is stored in the [`Val0`](xref:OpenCV.Net.Scalar.Val0) field.

- Record the motion of an object using a [`CsvWriter`](xref:Bonsai.IO.CsvWriter) sink.
