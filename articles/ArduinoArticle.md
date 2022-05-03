# Bonsai & Arduino

Bonsai excels at processing parallel and asynchronous streams of data (e.g. cameras, audio, etc...). However, for some applications, you might be looking for a solution to "*close the loop*". In other words, not only *see* (*read*) the world but also *act* (*write*) on it.

While there are multiple hardware options integrated in Bonsai to achieve such a goal, the [**Arduino Package**](xref:Bonsai.Arduino) is perhaps the the easiest and most affordable option.

In this tutorial, I will cover the basics on how to set up the communication between Bonsai and Arduino, as well some examples and best practices when writing these workflows.


## What is the Firmata protocol

In order to leverage the hardware capabilities of the [**Arduino board**](https://www.arduino.cc/en/Guide/Introduction) we must be able to communicate from, and to Bonsai. A bidirectional communication protocol must therefor be in place between the computer and the Arduino board. Thankfully, the Arduino community has long solved this problem through the implementation of the [`Firmata protocol`](https://www.arduino.cc/en/reference/firmata).

The `Firmata protocol` is a generic serial communication protocol between a software application running on a host PC (in our case Bonsai), and a family of microcontrollers  (in our case an Arduino, or Arduino-compatible board).

As in most forms of communication, both parties must be able to speak the same *language*. In our case, the `Firmata protocol` is implemented at the firmware level in our microcontroller, and is, at this point, implemented in a wide swath of computer software packages, including Bonsai.
Using this protocol, the PC can abstract from the precise hardware implementation of the microcontroller, and instead send simple serial messages ([MIDI format](http://firmata.org/wiki/Protocol)) with instructions to be read and executed by the microcontroller (E.g. "What is the state of Pin1?" or "Turn on Pin13").

Finally, while an extensive review of the protocol is far beyond the scope of this article, if you are curious about some of the implementation details, check the references at the end of the article.

The next sections will be dedicated to showing you how to command an Arduino with Bonsai. I will cover the basics and leave some examples and best practices when building these workflows. At the end, I will try to cover a couple of more advanced topics that might be of interest.

## Getting started

### Configuring Arduino

As I mentioned before, Arduino must be loaded with a specific firmware that implements the Firmata protocol. There are several options as to which exact implementation you can use (including coding your own implementation). For the sake of simplicity, in this tutorial I will always be referring to the `StandardFirmata` implementation.

To configure the Arduino board with Firmata:

1. Open the Arduino IDE and [setup your board](https://www.arduino.cc/en/Guide/ArduinoUno);
2. Open the `StandardFirmata.ino` sketch (`File -> Examples -> Firmata -> StandardFirmata`);
3. Upload the sketch to your board.

At this point your Arduino is running Firmata and, as long as you do not upload any other sketch over it, you should not have to repeat these steps.

## Creating an Arduino object

Once the Arduino side of things is taken care of, we move to Bonsai.

