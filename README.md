# HW to Chapter 13: Convolutional Layer

This assignment focuses on understanding the fundamental concepts of convolutional layers in neural networks. It includes both theoretical explanations and a practical programming task to implement a basic convolution operation.

## Contents
### Non-programming Assignment
1.What is convolution operation and how does it work?
2. Why do we need convolutional layers in neural networks?
3. How are the sizes of the original image, the filter, and the resultant convoluted image related?
4. What is padding and why is it needed?
5. What is strided convolution and why is it needed?

### Programming Assignment
Implement a convolution algorithm without padding and without striding for an original image of size 6x6 and a filter of size 3x3.


## Programming Assignment Solution

Implementation of Convolution Algorithm (without padding and without striding)
This code performs a convolution operation on a 6x6 input image using a 3x3 filter. The convolution is done without padding and with a stride of 1.

### Expected Output
Convoluted Output:
[[ 5.  0. -5.  0.]
 [ 7. 12.  5. -1.]
 [ 5. 12.  8. -3.]
 [-1.  4.  7.  7.]]

## Requirements
1. Python 3.10+
2. numpy

## How to Run
1. Clone the repository:

git clone https://github.com/mtrishal123/HW_to_Chapter_13.git

cd HW_to_Chapter_13

2. Run the python script
   
   python cnnExample.py


## Notes
1. The programming assignment was implemented without padding and with a stride of 1.
2. The assignment is structured to help understand how convolution layers work in neural networks.


