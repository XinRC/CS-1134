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

This will result in: *1, 2, 3, ... √n, ... n/2 ... , n* This cuts the dataset (numbers) in half from √n. 

```python
def square_root_prime(n):
 div_count = 0
 for curr in range(1, sqrt(n) + 1):
  if num % curr == 0:
   div_count += 1
 return div_count
```

Overall, all the functions above are ways to **optimze** the program. 

## Runtime:
Runtime is very important in Computer Science. To figure out the runtime for the program, a function is used to determine its runtime. 

```python
For T(n), where T(n) stands for runtime. T represents speed while (n) 
```
Thus in asymptotic analysis, usually it will:
1. Drop the lower order terms
2. Ignore leading constants of highest order
