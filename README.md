# python-programming-problems
python-programming-problems

Problem 1:
=======

Lets assume we have two sorted arrays of integers, as following:

array `a` has m elements
array `b` has n elements

size of array `a` is m+n, hence `a` can accomodate all the elements that are there in array `b` as well as its own.

now you need to write a code so that the elements from array `b` are copied into array `a`, keeping its orignal property maintained which is; it has been sorted.

eaxmple:

a = [1,20,31,45,50,........]
b = [10,12,17,70]

after operation

a = [1,10,12,17,20,31,45,50,70]

kindly try to optimize the code so that it can run faster, list/mention any bottlenecks if you find which might be hindering the performance.


Problem 2:
=======

Let assume we have a 2D-array/Matrix of unique integers with the following property.

1. Elements in columns are sorted from top to bottom.
2. Elements in rows are sorted from left to right.

We need to perform a simple operation `delete` by keep the property of the Matrix maintained so that algoritm can run consistently after consecutive operations on the matrix.

`delete` operation: should take a key `k`(integer) which is has to be lookedup into the Matrix and if found should be deleted (so that on next run, it can be lookedup again) else report the user with a error message telling "This key doesn't exists.".

example:

a = [ [1, 13, 21, 56, 70],
        [3, 15, 25, 60, 73],
	[5, 18, 30, 63, 75],
	[9, 20, 35, 69, 88] ]

operation 1: delete 27
result: "This key doesn't exists."

operation 2: delete 63
result: "Key deleted."

operation 3: delete 63
result: "This key doesn't exists."

Try to develop an optimized code, with minium time complexity possible.

Problem 3:
=======

Develop a simple program which can simualte a simple `tree` with add, delete and update operation, also you need to store the tree on disk so that next time when the program loads it restores to the tree to the previous state.


Problem 4:
=======

In java and many ther High level languages by default strings are immutable(non-changeable) give a critical reasoning that why desginers of java and other such languages choose to handle string in this manner over the way its predecessors use to handle strings.

If you think its rather a wrong methodology then please support your agrument.
Problem Author: Anand Kumar Mishra (akm.coder@gmail.com)
