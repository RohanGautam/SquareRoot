# SquareRoot

This project explores how triangles can be used to find the square root of a number.

## New readme
I made this project 5 years ago (from the date of writing)! My previous code (the python script) was quite bad and ineffecient. Also, the math was clumsy. I've been learning Julia recently and wanted to try it out on a small project so I thought a rewrite of this idea with updated math and better code would be cool. The new perspective on the same idea involves viewing this "square root decomposition" as just rotations and scaling of vectors with one end at the origin. Look at the old readme below to see more details on the project and how I viewed it at the time. The table below has the two types of plots you can make, depending on how you decompose the squares the number!


|       Optimal      | Non-optimal splits for pretty plot 😛|
| :----------------: | ------------------ |
| ![](imgs/new2.png) | ![](imgs/new1.png) |
## Old readme

### Prerequisites

- Python 3
- matplotlib

```
pip install matplotlib
```

## The Idea

The basic idea of this is to find the square root of a number using the pythagoras theorem. In the result, the square root of the given number will be the hypotenuse of the last triangle.If the number is not a pythagorean triplet, one side can be expressed as a natural number and the other is the hypotenuse of ANOTHER triangle, and so on.Look at the examples below.

|        (a)         | (b)                |        (c)         |
| :----------------: | ------------------ | :----------------: |
| ![](imgs/old1.png) | ![](imgs/old2.png) | ![](imgs/old3.png) |

As seen in (a), the value of root(3) is the length of the hypotenuse of a right angled triangle with one side "1", and the other side root(2). Root(2) is itself calculated by measuring the hypotenuse of another triangle with with sides "1" each.

This gives a brief idea of how it works. (b) and (c) provide more examples.
In all cases, the length of the hypotenuse of the last triangle is the value of the square root of the desired number.

## Acknowledgments

- A part of the algorithm was based from [here](https://math.stackexchange.com/questions/2125690/find-coordinates-of-3rd-right-triangle-point-having-2-sets-of-coordinates-and-a)
- Shout out to my buddy pythagoras
