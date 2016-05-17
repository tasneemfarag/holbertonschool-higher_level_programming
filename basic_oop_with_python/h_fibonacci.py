#!/usr/bin/env python
'''function fibonacci(x) that computes the fibonacci number of the parameter'''
def fibonacci(x):
 	a,b = 1,1
 	for i in range(x-1):
  		a,b = b,a+b
 	return a
'''
for testing
for i in range(1, 20):
    print "Fibonacci of %d is %d" % (i, fibonacci(i))
'''    