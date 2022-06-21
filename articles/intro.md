## What is Bonsai?

Bonsai is a programming language with the following major features:

1. **It operates on sequences of elements that are ordered in time.** Elements within these sequences can be any kind of data (images, numbers, strings, etc), and these sequences can be either finite or infinite. Elements within sequences can occur regularly or irregularly and do not need to conform to any underlying clock -- sequences are asynchronous. Most hardware that interacts with the world is asynchronous: a human using a keyboard can produce a sequence of keystrokes, and a webcam can produce a sequence of images, but the time of each keypress and image capture is unrelated. Bonsai addresses this fact at the core of its design and is therefore particularly good at interacting with the physical world.

![A simple sequence](../images/simple-sequence.svg)

_Footnote: If you look at the source code of Bonsai, the technical name for the datatype of all sequences in Bonsai is "IObservable"._

2. **It is (strictly) composable.** Operations on sequences (generation, filtering, combining, etc.) are composed in order to define new sequences. In this way, Bonsai operators are much closer to normal mathematical functions than those in many of the programming languages with which you might already be familiar. In fact, one can think of Bonsai as an algebra that operates on temporal sequences in a similar way to how linear algebra operates on matrices.

3. **It is a visual language.** Operator composition is defined using a graphical tool. To define a composition, operators are linked together in order to form a visual graph (in the mathematical sense), which is called a "workflow" in Bonsai. Each node defines a sequence and each connection gives a node the option to get data from the connected preceding node(s).

The visual language of Bonsai can be read using the following colour code:

### How to read Bonsai code

The visual language of Bonsai contains the following 4 major colors:

- **Green == Sources.** Sources generate sequences of data and do not require an input connection. Some sources generate infinite sequences (i.e. webcams), while others generate finite sequences (i.e. movie files).
- **Blue == Transforms.** Transforms always have a single input connection. Transforms apply some operation on the elements of the incoming sequence, and every element of the input sequence is transformed into an element in the output sequence, with no changes to order or rate.
- **Orange == Combinators.** Combinators take one or more input sequences and apply some sort of control flow. With a combinator node, you can combine data, monitor various sequences, generate new events, drop events, etc. Most of the reactive operators fall into this category, and most of the complexity of a Bonsai workflow lies in the orange nodes.
- **Purple == Sinks.** Sinks take one sequence as input and output the exact same sequence, but they cause some kind of side effect outside of Bonsai (i.e. save data to a file, turn on or off some hardware, etc). Sinks do not change the elements in a sequence, and therefore can be placed anywhere in a workflow without changing its operation.
