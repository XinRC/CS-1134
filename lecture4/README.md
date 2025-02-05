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
1. Drop the lowest order terms
2. Ignore leading constants of highest order

For example, for ever `x = 5` or similar code, you can add `+1`. However, for `loops`, you must represent the loop as `n` and multiply it by those inside the loop. For example:

```python
def count(n):
 x = 0 # +1 runtime
 for i in range(1, n+1): # * n 
  if i % 2 == 0: # +1 runtime
   x += 1 # +1 runtime
 return x # +1 runtime
```
So the previous code will run at 2n + 2 because there are two items in the for loop, then we must multiply the items by `n`, then combine the +1s from outside the for loop. However, because we do not care about coefficients or digits outside of `n`, we will ignore those. Thus, T(θ) = n

</br>

Thus, `T(n) ≅ n`. When using very big numbers, the smaller T(n) is, the better optimized the algorithm is. Another way to determine how optimized the algorithm is by look at its function. For example, T(1) is more optimized than T(n^2) since n^2 is a quadriatic. 

---

## Asymptotic Analysis OFFICAL:

> θ -> how the runtime grows as `n` approaches infinity **at an exact rate**

> O -> also represents the upperbound *(worse-case scenario)* as `n` approaches infinity.

Usually, we only care about the *worse-case scenario*, aka the UPPERBOUND. 


### Big-O Analysis:

f(n) = runtime of the algorithm (how many steps as `n` grows)
g(n) = some function to compare how fast `f(n)` grows. For example: log(n), n^2

Thus: `f(n)` = O(g(n))

This is because `f(n)` <= c * g(n), where c is a constant, n_o = the point where n is "really really big"


**EXAMPLE**

if `f(n) = 3n^2 + 6n - 15,` if we want to prove that the upperbound of the function is `g(n) = n^2`, we have to find the `constant`.
- The constant should be greater than (or equal to) the ccoefficient of the greatest degree. In this case, `c = 4`. Thus we get:

`g(n) = 4n^2`

3n^2 + 6n -15 <= 4n^2
