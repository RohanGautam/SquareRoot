# SquareRoot

This project explores how triangles can be used to find the square root of a number.


### Prerequisites

* Python 2
* matplotlib

```
pip install matplotlib
```
## The Idea

The basic idea of this is to find the square root of a number using the pythagoras theorem. In the result, the square root of the given number will be the hypotenuse of the last triangle.If the number is not a pythagorean triplet, one side can be expressed as a natural number and the other is the hypotenuse of ANOTHER triangle, and so on.Look at the examples below.

<img width="182" alt="1" src="https://user-images.githubusercontent.com/17317792/38777123-46a9c6ae-40c0-11e8-89cb-8fd7387acaf5.PNG">

As seen above, the value of  root(3) is the length of the hypotenuse of a right angled triangle with one side "1", and the other side root(2). Root(2) is itself calculated by measuring the hypotenuse of another triangle with with sides "1" each.

This should give you a brief idea of how this works.Here are a few more complex examples with big numbers:

<img width="185" alt="2" src="https://user-images.githubusercontent.com/17317792/38777159-f9d5b3aa-40c0-11e8-8b4e-97f50be77eee.PNG">

<img width="229" alt="3" src="https://user-images.githubusercontent.com/17317792/38777162-0690fadc-40c1-11e8-8a5b-d4863db9623b.PNG">

In all cases, the length of the hypotenuse of the last triangle is the value of the square root of the desired number.

## Acknowledgments

* A part of the algorithm was based from [here](https://math.stackexchange.com/questions/2125690/find-coordinates-of-3rd-right-triangle-point-having-2-sets-of-coordinates-and-a)
* Shout out to my buddy pythagoras


