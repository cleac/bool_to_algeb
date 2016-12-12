# BOOLEAN to ARYTHMETIC function convertor

## What is it?

This is a little tool that allows to convert functions from boolean form to algebraic by these rules:
 1. A and B  =>   A * B
 2. A or B   =>  (A + B) - (A * B)
 3. not A    =>  1 - A

## How to use it?

To use it, you should have python3.3 on your machine (the least tested version).
Usage is pretty simple: you type your boolean function in doublequotes in terminal. E.g. `./main.py "x1 and x2"`.

Also, there is [systolic_processor.py](another executable file here). This is the targer of whole tool - possibility to convert boolean functions instructions of systolic processor to arythmetic. To use it, type `./systolic_processor.py` and then number of output nodes you need. (Note: if there will be to much, i may take some time, 'cause code is not very optimized)
