---
layout: article
title: Bonsai & ZeroMQ Networking
---
# Bonsai & 0MQ Networking
The Bonsai.ZeroMQ package allows us to harness the powerful [ZeroMQ](https://zeromq.org/) library to build networked applications in Bonsai. Applications could include:
- Interfacing with remote experimental rigs via network messages
- Performing distributed work across pools of machines (e.g. for computationally expensive deep-learning inference) 
- Streaming video data between clients across a network
- **Real-time interaction between clients in a multiplayer game** 

In this article, we will use Bonsai.ZeroMQ to explore this final example and build a basic client-server architecture similar to one that might be used in a multiplayer game.

## Why ZeroMQ?
The full scope of advantages offered by ZeroMQ as a networking library is beyond the scope of this article. For our purposes, it's enough to say that ZeroMQ provides a simple, efficient, socket based API that gives us the ability to implement a wide range of sophisticated network architectures. 

For a review of the primary socket types available in NetMQ (on which Bonsai.ZeroMQ is based) check the [NetMQ docs](https://netmq.readthedocs.io/en/latest/).

For those who want a deep-dive on the philosophy and structure behind ZeroMQ, read [0MQ - The Guide](https://zguide.zeromq.org/)

## Network design
The basic network architecture we want to achieve will be composed of a number of clients sending their state to a server, which then updates the other connected clients with that clients’ state. This is comparable to a multiplayer game in which client players move through the game world and must synchronise that movement via a central server so that all players see each other in their ‘true’ position in the world.

![A simple multiplayer network](~/images/zeromq/zeromq-network-diagram.svg)

An important requirement to point out here is that our server should be choosy about which clients it broadcasts information to. If client 1 updates the server with its current state, that information needs to be sent to all other connected clients, but there is no need to send it back to client 1 as it already knows its own state and this feedback message would be redundant.

ZeroMQ provides a number of socket types that could be used to achieve something approaching this architecture. The Router / Dealer socket pair acting as Server/Client has a couple of advantages for this design: 
- Routers assign a unique address for each connected client allowing clients in turn to be addressed individually
- Messages can be passed between Router / Dealer sockets without the requirement that a reply is received before the next message is sent, as is the case with the Request / Response socket pair.

## Basic Client
To begin with, we’ll create a simple client that sends basic messages on a network. In a new Bonsai project, add a **`Dealer (ZeroMQ)`** node. In the node properties, set `Host`: localhost, `Port`: 5557, `SocketConnection`: Connect, `SocketProtocol`: TCP.

![Dealer](~/images/zeromq/dealer-socket.svg)

In Bonsai.ZeroMQ, the **`Dealer`** can have two functions based on its inputs. On its own, as above, the **`Dealer`** node creates a Dealer socket that listens for messages on the specified network. With the properties specified, we are asking our **`Dealer`** to listen for messages on the local machine on port 5557 using the TCP protocol. We use the ‘Connect’ argument for the `SocketConnection` property to tell the dealer that it will connect to a static part of the network with a known IP address, in this case the server which we will implement later.

If we add inputs to the **`Dealer`**, it will act as both a sender and receiver of messages on the network. Before the **`Dealer`** node add a **`KeyDown (Windows.Input)`**, **`String (Expressions)`**, and **`Format (Osc)`** node in sequence.

![Basic client message](~/images/zeromq/dealer-basic-input.svg)

In the node properties, set the **`KeyDown`** `Filter` to the ‘1’ key and set the **`String`** `Value` to ‘Client1’. If we run the Bonsai project now, the **`Dealer`** will continue listening for incoming messages on the network, but every time the ‘1’ key is pressed a message containing the string ‘Client1’ will be sent from the socket.

> A side note on the Format node used here. The Bonsai.ZeroMQ library uses another networking package - the OSC library – to format data into a common message format. We will see the **`Parse`** node used similarly later in the article for receiving and unpacking these messages. This has a few advantages for the design of the Bonsai.ZeroMQ library iteself: 1) We don’t need different ZeroMQ socket nodes for different data types (e.g. `SendString`, `SendInt`, `ReceiveString`, `ReceiveInt`) and can dynamically set the data type being sent or received by the socket; 2) Bonsai.ZeroMQ and Bonsai.OSC can use the same messages interchangeably; 3) The functionality of Bonsai.ZeroMQ nodes can be specialised only for sending and receiving data only, rather than also having to format and parse messages.

Copy and paste this client structure a couple of times and change the **`KeyDown`** and **`String`** properties accordingly on each (2, ‘Client2’; 3, ‘Client3’) so that we have 3 total clients that send messages according to different key presses.

![Mutiple clients](~/images/zeromq/copied-clients.svg)

