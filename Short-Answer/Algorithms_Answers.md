#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n^2)
This formula: a = a + n * n
If graphed on a graphing calulator would produce a parabola as n * n is n^2
and no matter what the input value of n, a + n^2 will never be < n^3.

b)O(n!)
When graphed the line gets steeper and steeper


c)O(n)
2 + n - 1 by eliminating the insugnificant values it reduces to O(n)

## Exercise II
'''
Given and n-story building and plenty of eggs, eggs are broken when thrown off floor f or higher.
Determine the value of f such that f = min(dropped + broken)
'''
let n be the coefficent of f that is n * f
the number of eggs dropped is the product of n the dropped * n and since there is at least
1 egg dropped per floor dropped is = 1

The most idea number of broken eggs is zero but zero is unattainable when dropping eggs so
the ideal number of broken eggs in this case is 1. Since the chance of an egg is broken
when dropped the number of possible broken eggs is proportional to the number of eggs
dropped. Thus broken = 1 * n.

The value of f can be computed thusly: f = (n * dropped) + (n * broken) / n

The complexity should be O(n)

def value_f(n, dropped=1, broken=1):
    f = ((n * dropped) + (n * broken)) / n
    return f