#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)  This algorithm's run time will increase linearly with the value of n because the operations need to be performed nth number of times


b) O(n^2) This algorithm's run time increase proportionally with the square of n because of the number of times the nested function has to run


c) O(2^n) This algorithm's run time doubles as the number of n increases because it is calling itself recursively

## Exercise II

function:

1. If number of floors of the building left to check is 1, check if egg broke. If egg is not broken, then f = current floor

2. If number of floors of the building is more than 1, find the midpoint floor of the building.
If egg is not broken at this floor, take the floors above the current floor and repeat steps 1 and 2
If egg is broken at this floor, take the floor bellow the current floor
and repeat steps 1 and 2



This function has a runtime complexity of O(log(n))