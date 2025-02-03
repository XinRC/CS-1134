<div align = "center">

# Lecture 4

</div>

## Asymptotic Analysis:

> Algorithms: A well defined computation procedure that describes how to transfer any given input to its desired output.

Such algorithms must have a **legal** input and provide a defined output. 
</br>

 ### For the algorithm to work, it must do two things:
- It can terminate
- It produces the correct output
</br>

## Given an example:
To create an algorithm that will determine whether a number is a prime number. There are multiple ways of checking if the number is: 

### To Check Output Correctiveness:
- Naive (Through brute force):

This will count all the way until (n), number.
  
``` python
def bf_is_prime(n):
 div_count = 0
 for curr in range(1, n+1):
  if n % curr == 0:
   div_count += 1
 return div_count
```

- First - Half Version:

Instead of counting all the numbers, the program will only count the first half of (n).

```python
def fb_is_prime(n):
 div_count = 0
 for curr in range(1, n//2+1):
  if n % curr == 0:
   div_count += 1
 return div_count
```

- Square Root Version:

This will result in: *1, 2, 3, ... √n, ... n/2 ... , n*
