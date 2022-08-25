---
layout: article
title: Bonsai & ZeroMQ Networking
---
# Bonsai & ZeroMQ Networking
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

## Basic client
To begin with, we’ll create a simple client that sends basic messages on a network. In a new Bonsai project, add a **`Dealer (ZeroMQ)`** node. In the node properties, set `Host`: localhost, `Port`: 5557, `SocketConnection`: Connect, `SocketProtocol`: TCP.

![Dealer](~/images/zeromq/dealer-socket.svg)

In Bonsai.ZeroMQ, the **`Dealer`** can have two functions based on its inputs. On its own, as above, the **`Dealer`** node creates a Dealer socket that listens for messages on the specified network. With the properties specified, we are asking our **`Dealer`** to listen for messages on the local machine on port 5557 using the TCP protocol. We use the ‘Connect’ argument for the `SocketConnection` property to tell the dealer that it will connect to a static part of the network with a known IP address, in this case the server which we will implement later.

If we add inputs to the **`Dealer`**, it will act as both a sender and receiver of messages on the network. Before the **`Dealer`** node add a **`KeyDown (Windows.Input)`**, **`String (Expressions)`**, and **`Format (Osc)`** node in sequence.

![Basic client message](~/images/zeromq/dealer-basic-input.svg)

In the node properties, set the **`KeyDown`** `Filter` to the ‘1’ key and set the **`String`** `Value` to ‘Client1’. If we run the Bonsai project now, the **`Dealer`** will continue listening for incoming messages on the network, but every time the ‘1’ key is pressed a message containing the string ‘Client1’ will be sent from the socket.

> A side note on the Format node used here. The Bonsai.ZeroMQ library uses another networking package - the OSC library – to format data into a common message format. We will see the **`Parse`** node used similarly later in the article for receiving and unpacking these messages. This has a few advantages for the design of the Bonsai.ZeroMQ library iteself: 1) We don’t need different ZeroMQ socket nodes for different data types (e.g. `SendString`, `SendInt`, `ReceiveString`, `ReceiveInt`) and can dynamically set the data type being sent or received by the socket; 2) Bonsai.ZeroMQ and Bonsai.OSC can use the same messages interchangeably; 3) The functionality of Bonsai.ZeroMQ nodes can be specialised only for sending and receiving data only, rather than also having to format and parse messages.

Copy and paste this client structure a couple of times and change the **`KeyDown`** and **`String`** properties accordingly on each (2, ‘Client2’; 3, ‘Client3’) so that we have 3 total clients that send messages according to different key presses.

![Mutiple clients](~/images/zeromq/copied-clients.svg)

> For the purposes of this article we are creating all of our clients and our server on the same Bonsai project and same machine for ease of demonstration. In a working example, each client and server could be running in separate Bonsai instances on different machines on a network. In this case, localhost would be replaced with the server machine’s IP address.

## Basic server
Now that we have our client pool set up and sending messages, let’s implement a server to listen for those messages. Add a **`Router (ZeroMQ)`** node to the project and set its properties to match the **`Dealer`** sockets we already added so that it is running on the same network. As the **`Router`** is acting as server and will be the ‘static’ part of the network, set its `SocketConnection` property to ‘Bind’.

![Router](~/images/zeromq/server-listener-added.svg)

As with the **`Dealer`** node, a **`Router`** node without any input will simply listen for messages on the network and not send anything in return. If we run the project now and monitor the output of the **`Router`** node, we’ll see that each time the client sends a message triggered by its associated key press we get a `ZeroMQMessage` arriving at the **`Router`**. Expanding the output of the **`Router`** node, we can see that the `ZeroMQMessage` contains a `byte` array address (in this case the address of the client that sent the message), a `byte` array containing the message itself, and the message type (the socket from which this message originated). To make sense of the message, let’s externalize the `Address` and `Message` outputs (right-click **`Router`** node and select each). Add an **`Index (Expressions)`** node to the `Address` output and set its `Value` property to 1 to access the unique address ID. Add a **`Parse (OSC)`** node to the `Message` output and set its `TypeTag` property to ‘s’ to indicate we expect the message to be a `string`.

![Router message parsing](~/images/zeromq/router-parsing.svg)

Running the project and then triggering client messages with key presses, we should see a unique `byte` value for each client in the **`Index`** node output and a corresponding `string` in the **`Parse`** node output.

## Client address tracking
So far our network is rather one-sided. We can send client messages to the server which can in turn receive and parse them, but so far nothing is relayed back to the clients. The first goal for server feedback is that any time a client message is received, the server sends this message back to all connected clients. To do this, we first need a way of keeping track of all connected clients. Add a **`Zip (Reactive)`** node to the **`Index`** node and connect the `Address` output as the second input to the **`Zip`**. 

![Address key-value pair](~/images/zeromq/address-kvp.svg)

Every time the **`Router`** receives a message, the **`Zip`** will create a `Tuple` that can be thought of as a key-value pair, with the unique `byte` address of the client as the key, and the full `byte` array address used by ZeroMQ for routing as the value. Next, add a **`DistinctBy (Reactive)`** node after the **`Zip`** and set the `KeySelector` property to the `byte` value (`Item1`).

![Unique key-value pair](~/images/zeromq/address-kvp-distinctby.svg)

The **`DistinctBy`** node filters the output of **`Zip`** according to the unique `byte` value and produces a sequence containing only the distinct – or ‘new’ – values produced by **`Zip`**. The output of **`DistinctBy`** will therefore effectively be a sequence of unique client addresses corresponding to each connected client. We also need to store these unique values and make them available to other parts of the Bonsai workflow. Add a **`ReplaySubject (Expressions)`** node after **`DistinctBy`** and name it ‘ClientAddresses’. 

![Address replay subject](~/images/zeromq/address-replaysubject.svg)

A **`ReplaySubject`** has the useful feature that it stores its input sequence and replays those values to any current or future subscribers. The effect in this case is that anything that subscribes to **`ClientAddresses`** will receive all the unique client addresses encountered by the server so far.

## Server --> client communication
Eventually, we will use these unique client addresses to route server messages back to specific clients. For now, we’ll implement a more basic approach where the server just sends messages back to the client that originally sent them. To do this, we first need to format the messages received by the server in a way that they can be sent back to the client. The **`Router`** node expects inputs that are a `Tuple` of a `byte` array corresponding to the client address (where to send the message) and an OSC `Message` (the contents of the message). We can implement this structure by adding a **`Format (OSC)`** node after the **`Parse`** node and using a **`Zip (Reactive)`** node to combine it with the `Address` output from the **`Router`**.

![Server message format](~/images/zeromq/server-message-format.svg)

Note here that order matters for the **`Zip`** node, the `Address` must be the first input, and the **`Format`** must be the second). With this new **`Zip`** node, every time the **`Router`** receives a message it parses the contents and reformats the contents back into an OSC `Message`. That formatted message is then combined with the corresponding client address. To send this data from the server we’ll first create a **`BehaviorSubject`** `Source` for the **`Zip`** output (`right-click on Zip >> Create Source >> BehaviorSubject`) and connect it to the **`Router`**. Name it ‘ServerMessages’. Add a **`MulticastSubject (Expressions)`** node after the **`Zip`** and set the subject `Name` also to ‘ServerMessages’.

![Server message multicast](~/images/zeromq/server-message-multicast.svg)

By creating the **`BehaviorSubject`** `Source` for the **`Zip`** node, we created a `Source` with an address/message `Tuple` output expected by the **`Router`** node input. Using a **`BehaviorSubject`** ensures that only the most recent message is used. Connecting it as an input to the **`Router`** node sets up the **`Router`** to send messages from **`BehaviorSubject`** while continuing to listen for incoming client messages. Finally, we used a **`MulticastSubject`** to feed the output of **`Zip`** into the **`BehaviorSubject`** to complete the loop: 
1. Client **`Dealer`** sends a message
2. Client message received by **`Router`**
3. Message reformatted into an addressed message
4. Addressed message passed back to **`Router`** to send back to client **`Dealer`**. 

If we run the workflow now and monitor the output of the three **`Dealer`** clients we’ll see that a message is received back at the **`Dealer`** only when that specific client sends a message to the server. 

## SelectMany detour
Now our network has a complete loop of client --> server --> client communication, but only the client that sends a message receives anything back from the server. Instead we’d like all clients to know when any of the clients sends a message. We already have access to the connected clients from **`ClientAddresses`**, and we know how to package data and send it back to clients via the **`Router`**. In an imperative language we would do something like:

```
foreach (var client in ClientAddresses) {
    Router.SendMessage(client.Address, Message);
}
```

using a loop to send the message back to each client in turn. In a reactive / observable sequence based framework we have to think about this a bit differently. The solution is to use a **`SelectMany`** operator and it is worth taking a detour here to understand its use in some detail before we apply it to our network.

The **`SelectMany`** operator can be a tricky one to understand. Lee Campbell’s excellent [Introduction to Rx](http://introtorx.com/Content/v1.0.10621.0/08_Transformation.html#SelectMany) book does a good job of summarising its utility, suggesting we think of it as “from one, select many” or “from one, select zero or more”. In our case, we can think of **`SelectMany`** as a way to repeat some processing logic several times and feed the output of each repeat into a single sequence. More concretely, taking a single message and repeating the act of sending it several times for each client address. It is easier to show by example, so let’s set up a toy example in our project. 

Create a **`KeyDown (Windows.Input)`** node followed by a **`SelectMany (Expressions)`**. Set the `Filter` for the **`KeyDown`** to a key that hasn’t been assigned to a client yet – here I will use ‘A’. 

![SelectMany setup](~/images/zeromq/keydown-selectmany.svg)

Inside the **`SelectMany`** node add a **`SubscribeSubject (Expressions)`** and set its subscription to the `ClientAddresses` subject we created earlier to replay unique client addresses. Add a **`TakeUntil (Reactive)`** node after the **`SubscribeSubject`** and connect the output of **`TakeUntil`** to the **`WorkflowOutput`** (disconnecting the `Source` node). Finally, create a **`KeyUp (Windows.Input)`** node and connect it to **`TakeUntil`**. Set the key `Filter` for **`KeyUp`** to the same as previously created **`KeyDown`** node outside the **`SelectMany`**.

![Inside SelectMany](~/images/zeromq/keydown-selectmany-internal.svg)

Run the project and inspect the output of the **`SelectMany`** node. If no client messages are triggered and we press ‘A’ to trigger the **`SelectMany`** nothing will be returned. If we trigger a single client and press ‘A’ again **`SelectMany`** gives us the address of that client. If we trigger a second client and press ‘A’ we get the addresses of these first two clients in sequence, and so on if we add the third client. Whenever we press ‘A’ we get a sequence of all the connected client addresses. Every time we trigger **`SelectMany`** with a **`KeyDown`** we generate a new sequence that immediately subscribes to **`ClientAddresses`**, a **`ReplaySubject`** which replays all our unique client addresses into the sequence. We could keep initiating these new sequences by continually pressing ‘A’ and if a new client address were to be added then all these sequences would report the new address (you can test this by connecting the **`SusbcribeSubject`** directly to the workflow output and deleting **`KeyUp`** and **`TakeUntil`**). Instead, we want to complete each new sequence once it has given us all the client addresses so we use an arbitrary event (releasing the key that initiated the sequence) to trigger **`TakeUntil`** and close the sequence. The overall effect is something similar to a loop that iterates over all client addresses every time we request it with a key press. This is the general structure of what we want to achieve next in our server logic to broadcast messages back to all connected clients.

## All client broadcast
To apply the logic of our previous **`SelectMany`** example to server messages, we need something to trigger the **`SelectMany`** sequence creation (**`KeyDown`** in previous example) and something to trigger the sequence termination (**`KeyUp`** in previous example). We already have a trigger for sequence creation in the output of the **`Zip`** that formats the message to be sent back to clients from the server, since we want to implement our **`SelectMany`** sequence every time a client message is received. For our sequence termination trigger, we want something that is guaranteed to fire after the server receives a client message but before the next message is received, such that our **`SelectMany`** sequence for each message responds only to that one message. A simple solution is therefore to use the arrival of the next message as our sequence terminator trigger. To implement this, add a **`Skip (Reactive)`** node after the **`Zip`** that deals with creating key-value pairs of client addresses and connect this to a **`PublishSubject (Expressions)`**. Ensure that the **`Skip`** node’s `Count` property is set to 1, and name the **`PublishSubject`** ‘NextMessage’.

![Server next message](~/images/zeromq/server-nextmessage.svg)

The logic here is that we use **`Skip`** to create a sequence that lags exactly 1 message behind the **`Router`** sequence of received messages, i.e. when the first message is received, **`NextMessage`** will not produce a result until the second message is received. We can then use this inside our **`SelectMany`** logic for generating server messages. Add a **`SelectMany (Expressions)`** node after the server message preparation **`Zip`** and name it ‘SelectAllClients’.

![Add select many](~/images/zeromq/add-select-many.svg)

Inside the **`SelectMany`** node, create 2 **`SubscribeSubject (Expressions)`** nodes and link them to the **`ClientAddresses`** and **`NextMessage`** subjects. Connect the `byte` array output of the **`ClientAddresses`** **`SubscribeSubject`** to the **`WorkflowOutput`** via a **`TakeUntil (Reactive)`** node, and use the **`NextMessage`** **`SubscribeSubject`** as the second sequence for **`TakeUntil`**.

![Select all clients](~/images/zeromq/selectallclients-internal.svg)

Now our `SelectAllClients` **`SelectMany`** will produce a sequence of all unique client addresses every time the server receives a message. Remember however that our **`Router`** requires inputs in the form of a `Tuple` of a `byte` array address and an OSC `Message`. To get the **`SelectMany`** output in the correct format, add a **`WithLatestFrom (Reactive)`** node after the **`SelectMany`** and use the OSC `Message` of the preceding **`Zip`** as its second input.

![Reformat SelectMant](~/images/zeromq/selectmany-format.svg)

In this context, **`WithLatestFrom`** combines each client address from **`SelectMany`** with the most recent received message. The result is that when a message is received from a client, several copies of the message are repackaged addressed to each of the connected clients. To see this, run the workflow and inspect the output of the 3 **`Dealer`** nodes. When a client sends a message, all connected clients (those that have already sent at least 1 message to the server) will receive a copy of that message. Let’s also check the content of those messages by adding a **`Parse (OSC)`** node to each of the `Message` outputs of the **`Dealer`** nodes. Ensure that the `TypeTag` property of the Parse node is set to ‘s’ to decode the string contents of the message.

![Client message parsing](~/images/zeromq/client-message-parsing.svg)

Running the workflow again and inspecting the output of the **`Parse`** nodes, we should see that all connected clients are updated with any client messages sent to the server.
