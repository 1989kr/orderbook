# OrderBook
OrderBook Simulator with Limit and Iceberg functionality

## Design
Proof of concept of a Limit Order Book (LOB) where the bid and ask order books are implemented as separate trees.
Inspired by the [Limit Book] implementation by Panagiotis Garefalakis where limit levels
are stored as nodes inside the trees and each node is a doubly-linked list of orders, sorted chronologically.



## Structure
* OrderBook and demoOrderBook store in `orderbook`
* Source code stored under `orderbook/src/`

## Run
* python -m demoOrderBook


## References
* https://github.com/pgaref/orderbook

