# Python DFA

A simple DFA simulator in Python

For usage, see **[machine.py](./machine.py)** that shows how to build a 
DFA machine. There is also a test file to see how you can check what the 
machine accepts and what it doesn't. Basically, you need to write your 
own test but this is a simple example.

**This implementation is a toy project.**

If you're looking for something more robust, consider works:
maybe something like [this](https://github.com/mvcisback/dfa) 


For example usage of the extremely crude draw functionality:

```
python test-draw.py > machine1.dot
dot -Tsvg machine1.dot > machine1.svg
```

This basically generates what looks like dot file which `graphviz` 
tool can use to draw the graph. Obviously, you need to have
`graphviz` installed in your system. `dot` program comes with `graphviz`.

You're intended to manipulate `dot` file as your needs. What this 
module provides is merely an absolute toy.

To see what kind of `dot` file is generated, see [machine1.dot](./machine1.dot).
