---
layout: article
title: Bonsai & Arduino
---
# Bonsai & Arduino

Bonsai excels at processing parallel and asynchronous streams of data (e.g. cameras, audio, etc...). However, for some applications, you might be looking for a solution to "*close the loop*". In other words, not only *see* (*read*) the world but also *act* (*write*) on it.

While there are multiple hardware options integrated in Bonsai to achieve such a goal, the [**Arduino Package**](xref:Bonsai.Arduino) is perhaps the the easiest and most affordable option.

In this tutorial, we will cover the basics on how to set up the communication protocol between Bonsai and Arduino, as well some examples and best practices when writing these workflows.

## The Firmata protocol

In order to leverage the hardware capabilities of the [**Arduino board**](https://www.arduino.cc/en/Guide/Introduction) we must be able to communicate from, and to Bonsai. A bidirectional communication protocol must therefor be in place between the computer and the Arduino board. Thankfully, the Arduino community has long solved this problem through the implementation of the [`Firmata protocol`](https://www.arduino.cc/reference/en/libraries/firmata/).

The `Firmata protocol` is a generic serial communication protocol between a software application running on a host PC (in our case Bonsai), and a family of microcontrollers  (in our case an Arduino, or Arduino-compatible board).

As in most forms of communication, both parties must be able to speak the same *language*. In our case, the `Firmata protocol` is implemented at the firmware level in our microcontroller, and is, at this point, implemented in a wide swath of computer software packages, including Bonsai.
Using this protocol, the PC can abstract from the precise hardware implementation of the microcontroller, and instead send simple serial messages ([MIDI format](http://firmata.org/wiki/Protocol)) with instructions to be read and executed by the microcontroller (E.g. "What is the state of Pin1?" or "Turn on Pin13").

Finally, while an extensive review of the protocol is far beyond the scope of this article, if you are curious about some of the implementation details, check the references at the end of the article.

The next sections will be dedicated to showing you how to command an Arduino with Bonsai. I will cover the basics and leave some examples and best practices when building these workflows. At the end, I will try to cover a couple of more advanced topics that might be of interest.

## Getting started

### Configuring Arduino

As I mentioned before, Arduino must be loaded with a specific firmware that implements the Firmata protocol. There are several options as to which exact implementation you can use (including coding your own implementation). For the sake of simplicity, in this tutorial I will always be referring to the `StandardFirmata` implementation.

To configure the Arduino board with Firmata:

1. Open the Arduino IDE and [setup your board](https://docs.arduino.cc/software/ide-v1/tutorials/getting-started/cores/arduino-avr);
2. Open the `StandardFirmata.ino` sketch (`File -> Examples -> Firmata -> StandardFirmata`);
3. Upload the sketch to your board.

At this point your Arduino is running Firmata and, as long as you do not upload any other sketch over it, you should not have to repeat these steps.

## Creating an Arduino object

Once the Arduino side of things is taken care of, we move to Bonsai.

The first thing to setup a communication between Arduino and Bonsai is to instantiate an Arduino connection using the [**`CreateArduino`**](xref:Bonsai.Arduino.CreateArduino) operator.

This node sets:
 - The communication protocol [`Baudrate`](xref:Bonsai.Arduino.CreateArduino.BaudRate). This value must match the value previously defined in the `StandardFirmata.ino` file (by default 57600 bits/second);

 - The [`Name`](xref:Bonsai.Arduino.CreateArduino.Name) to be given to the Arduino object. While the field can be left empty, it is strongly advised to enter a non-null value. This will be the name of the object we will target later, to send/receive data to/from the Arduino;

 - The [`PortName`](xref:Bonsai.Arduino.CreateArduino.PortName), which defines the COM port the Arduino is currently connected to. If the previous [`Name`](xref:Bonsai.Arduino.CreateArduino.Name) property is left empty, [`PortName`](xref:Bonsai.Arduino.CreateArduino.PortName) will be used to name the object;

 - The [`SamplingInterval`](xref:Bonsai.Arduino.CreateArduino.SamplingInterval) that determines the frequency at which analog data is sampled from the Arduino. While in theory this value can be lowered to obtain higher sampling rates (by default 19 milliseconds or ~52Hz), given hardware resource contraints, the minimum value might differ across boards. For an Arduino UNO, for instance, this value seems to cap at 10 milliseconds.

>> ADD WORKFLOW WITH ARDUINO OBJECT HERE

Now that we have created an object we can establish a connection with, it is finally time to get some data from Arduino.

## Digital Input and Output

Reading and Writing digital values from an Arduino is acomplished by instantiating a [**`DigitalOutput`**](xref:Bonsai.Arduino.DigitalOutput) and [**`DigitalInput`**](xref:Bonsai.Arduino.DigitalInput), respectively. Both nodes require two properties to be defined:

- The [`Pin`](xref:Bonsai.Arduino.DigitalOutput.Pin) number that the user wishes to Read/Write to;

- The [`PortName`](xref:Bonsai.Arduino.CreateArduino.PortName) of the Arduino object . As previously stated, if [`Name`](xref:Bonsai.Arduino.CreateArduino.Name) was left empty, the Arduino board can be selected by the COM port name. However, to increase the code flexibility across setups, the user is encouraged to enter a value. Under this scenario, the previously defined [`Name`](xref:Bonsai.Arduino.CreateArduino.Name) will be selectable under [`PortName`](xref:Bonsai.Arduino.CreateArduino.PortName). This way, when running the workflow in a distinct host PC, the user will simply have to change  [**`CreateArduino's`**](xref:Bonsai.Arduino.CreateArduino) [`PortName`](xref:Bonsai.Arduino.CreateArduino.PortName).


### Digital Input

[**`DigitalInput`**](xref:Bonsai.Arduino.DigitalInput) source outputs a ```Boolean``` value (True/False) each time the state of the defined [`Pin`](xref:Bonsai.Arduino.DigitalOutput.Pin) number changes (i.e. "Toggles"). Additionally, at start-up, the node will output the current value of the pin.

In addition to [**`DigitalInput`**](xref:Bonsai.Arduino.DigitalInput), [**`InputPullUp`**](xref:Bonsai.Arduino.InputPullUp) is also able to report the state of a digital input pin. Using this node enables the internal pull-up resistor, affording an identical behavior to setting [```pinMode(pin, INPUT_PULLUP)```](https://www.arduino.cc/reference/en/language/functions/digital-io/pinmode/) in Arduino code.

It should be noted that while any of the read events do not carry any temporal information from the Arduino, they can be timestamped in Bonsai with the [**`Timestamp`**](xref:Bonsai.Reactive.Timestamp) operator. Critically, the logged time will correspond to the time the event was registered in Bonsai and not when it was detected in hardware.

>> ADD WORKFLOW WITH ARDUINO OBJECT HERE

### Digital Output

[**`DigitalOutput`**](xref:Bonsai.Arduino.DigitalOutput), in contrast to the previous node, instructs the Arduino to change the state of a given [`Pin`](xref:Bonsai.Arduino.DigitalOutput.Pin). This node accepts a single input in the form of a ```Boolean``` that is used to set the state of the output pin (```True=HIGH```, ```False=LOW```). The new value will remain set until a distinct value is received.

>> ADD WORKFLOW WITH ARDUINO OBJECT HERE

### Combining DigitalOutput and DigitalInput to measure communication latencies

When using Arduino to control experimental rigs, especially those implementing closed-loop interactions, it is important to benchmark how long it takes for an instruction sent from Bonsai to produce an output in the world.

One way to achieve this is to measure the time it takes to detect a change in a pin state connected to a second pin we write to. Let's first connect pin 5 to pin 6 in Arduino. We will then read from pin 5 (e.g. False) and use this value to update the state of pin 6 (i.e. NOT(False) = True). This operation will change the state of pin 5 (e.g. True) and restart a new loop. The time between each toggle read (e.g. False -> True) will give us a benchmark the round-trip time (TODO ADD WORKSHEET EXAMPLE HERE).

>> ADD WORKFLOW WITH ARDUINO OBJECT HERE


## Analog Input and Output

### Analog Input

[**`AnalogInput`**](xref:Bonsai.Arduino.AnalogInput) can be used to read analog values from the Arduino pin. It should be noted that only [analog-read enabled pins](https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/) are compatible with this functionality. For instance, in Arduino UNO, 6 analog pins are available and can be address by ```AX``` (e.g. ```A1```).

The output of [**`AnalogInput`**](xref:Bonsai.Arduino.AnalogInput) is an ```Int``` ranging from `0-1023` (`10 bits`) that linearly maps to the digitized voltage range of the analog input pin (e.g. for Arduino UNO, `0-1023` -> `0-5 Volts`).

Finally, the sampling rate of this node is defined by [`SamplingInterval`](xref:Bonsai.Arduino.CreateArduino.SamplingInterval). While the sampling frequency is relatively stable, a small delay (and jitter) is to be expected from the time of acquisition to receiving data in Bonsai.

>> ADD WORKFLOW WITH ARDUINO OBJECT HERE

### Analog Write

The [**`AnalogOutput`**](xref:Bonsai.Arduino.AnalogOutput) operator implements the [`analogWrite(pin, value)`](https://www.arduino.cc/reference/en/language/functions/analog-io/analogwrite/) function found in Arduino sketches.

In most boards, this function does not implement a "true" analog output, instead it tries to "approximate" an analog signal using [Pulse-Width Modulation (`PWM`)](https://en.wikipedia.org/wiki/Pulse-width_modulation). When using `PWM` in Arduino, a single input must be provided that determines the duty-cycle of the output square-wave.

Thus, [**`AnalogOutput`**](xref:Bonsai.Arduino.AnalogOutput) receives as an input an ```Int``` in the range `0-255` `(8 bits)`. This value will linearly map to the output `PWM` duty cycle (i.e. `0%-100%`). Once a value is received, the Arduino board will continuously generate a PWM wave (by default, [in Arduino UNO, 500Hz or 1kHz](https://www.arduino.cc/reference/en/language/functions/analog-io/analogwrite/)) with the specified duty-cycle. The wave can be stoped by simply sending a `0` value.

| ![PWM_figure](https://upload.wikimedia.org/wikipedia/commons/b/b8/Duty_Cycle_Examples.png) |
|:--:|
| **Pulse-width modulation of a square wave. A 50%, 75%, and 25% duty-cycle would correspond to an [**`AnalogOutput`**](xref:Bonsai.Arduino.AnalogOutput) input value of 128, 191 and 64, respectively.** (Reproduced from: https://en.wikipedia.org/wiki/Pulse-width_modulation under a CC BY-SA 4.0 license)|

>> ADD WORKFLOW WITH ARDUINO OBJECT HERE


[![Example Workflow](../images/acquisition-example.svg)](../workflows/acquisition-example.bonsai)
[![Example Workflow](../images/acquisition-example.svg)](../workflows/acquisition-example.bonsai)


## Servo Output

In addition to writing analog and digital values, the communication between Bonsai and Arduino is also able to control servo motors using, under the hood, the ['Servo.h'](https://www.arduino.cc/reference/en/libraries/servo/) library.
Similarly to the previously showcased outputs, the [**`ServoOutput`**](xref:Bonsai.Arduino.ServoOutput) operator expects a [`Pin`](xref:Bonsai.Arduino.ServoOutput.Pin) connected to the servo-motor, and a [`PortName`](xref:Bonsai.Arduino.ServoOutput.PorName). You can instruct the servo to move to a specific angle (`0-180 degrees`) by simply sending an ```Int``` input to the operator.

[![Example Workflow](../images/CreateArduino.svg)](../workflows/CreateArduino.bonsai)

## Coding best practices

We have now covered the main operators that afford communication between Bonsai and Arduino. In this next section we will review coding pratices that will make your workflow more readable, scalable, and sometimes performant.
### Subjects

Covering the topic of `Subjects` is far from the scope of this tutorial. For now, let's just take the intuition that `Subjects` are operators that allow the sharing of observables across your workflow, without the need for explicit branches to be made between operators.
For instance:

The output of timer is shared using a [**`PublishSubject`**](xref:Bonsai.Expressions.PublishSubject), and subscribed to using [**`SubscribeSubject`**](xref:Bonsai.Expressions.SubscribeSubject) from anywhere in your workflow. Keep in mind that, in order to pair connections between `Subjects`, these must have names. This can also be leveraged to keep your code cleaner as we will see.

As a side node, due to the priority `Subjects` are initialized with in Bonsai, it is highly recomended to use them to define all your hardware objects and connections at the highest level of your workflow.


#### Subjects afford "one-to-many" logic
Consider the example wherein you might be interested in reading from a single digital pin and perform two independent computations in Bonsai. This would look something like:

--input(1) -go1
--input(1) -go2

While valid, this creates a problem if you need to change the pin you want to read from. Since the number of changes you will need to refactor in your workflow will scale with the number of branches that use that operator.

A good pratice to avoid these pitfals is to assign your observable to a subject with a more abstract name (e.g. `ButtonSignal`).

--workflow

As you can probably tell, as long as the downstream branches are subscribed to `ButtonSignal`, you would simply need to change the pin number in a single place (i.e. when creating the `Subject`)

#### Subjects afford One-to-many logic "many-to-one" logic



## Alternatives to Firmata

### An example of a simple Serial communication protocol

## General references:

- https://github.com/firmata/arduino

- https://github.com/martin-eden/firmata_protocol/blob/main/protocol.md

- http://firmata.org/wiki/Protocol
