---
layout: article
title: Bonsai & 0MQ Networking
---
# Bonsai & 0MQ Networking

The Bonsai.ZeroMQ package allows us to harness the powerful 0MQ library to build networked applications in Bonsai. Applications could include:
- Interfacing with remote experimental rigs via network messages
- Performing distributed work across pools of machines (e.g. for computationally expensive deep-learning inference) 
- Streaming video data between clients across a network
- *Real-time interaction between clients in a multiplayer game* 

In this article, we will use Bonsai.ZeroMQ to explore this final example and build a basic client-server architecture similar to one that might be used in a multiplayer game.

## Network design