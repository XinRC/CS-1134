<div align = "center">

# Lecture 4

</div>

## Asymptotic Analysis Prologue:

> Algorithms: A well defined computation procedure that describes how to transfer any given input to its desired output.

Such algorithms must have a **legal** input and provide a defined output. 
</br>

 ### For the algorithm to work, it must do two things:
- It must terminate
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
Runtime is very important in Computer Science. To figure out the runtime for the program, a function is used to determine its runtime. The jist of Big Theta is that it is usually refered to as the average runtime. Focusing more on it will showcase two other types of notations that will be discussed later, `Big O` and `Big Ω`. Do note that string multiplication is θ(n)

```python
For T(n), where T(n) stands for runtime. T represents speed while (n) 
```
Thus in asymptotic analysis, usually it will:
1. Drop the lowest order terms
2. Ignore leading constants of highest order

For example, for every `x = 5` or similar code, you can add `+1`. However, for `loops`, you must represent the loop as `n` and multiply it by those inside the loop. For example:

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

Thus, `T(n) ≅ n`. When using very big numbers, the smaller T(n) is, the better optimized the algorithm is. Another way to determine how optimized the algorithm is by look at its function. For example, T(1) is more optimized than T(n<sup>2</sup>) since n<sup>2</sup> is a quadriatic. 

---
<div align = "center">
 
## Asymptotic Analysis:

</div>

> θ -> how the runtime grows as `n` approaches infinity **at an exact rate**

Usually we only care about the upper-bound since it is the worse case scenario.

---
<div align = "center">
 
### BIG - O Analysis:

</div>

> O -> This is how fast the algorithm **might** grow. ("worse-case scenario").

f(n) = runtime of the algorithm (how many steps as `n` grows)
g(n) = some function to compare how fast `f(n)` grows. For example: log(n), n<sup>2</sup>

Thus: `f(n)` = O(g(n))

This is because `f(n)` <= c * g(n), where c is a constant, n = the point where n is "really really big"


**EXAMPLE**

if `f(n) = 3n^2 + 6n - 15,` if we want to prove that the upperbound of the function is `g(n) = n^2`, we have to find the `constant`.
- The constant should be greater than (or equal to) the ccoefficient of the greatest degree. In this case, `c = 4`. Thus we get:

`3n^2 + 6n -15 <= 4n^2`

Given that `n = 5` (randomly seleted), plug 5 into all of `n`, which will give us: `90 <= 100`

Because the above relation is true, when graphing the relation on a graph, we are able to prove that c*g(n) is the upperbound of f(n).

</br>

<div align = "center">
 
### BIG - Ω Anaylsis:

</div>

> Ω -> This is how fast the algorithm is **guaranteed** to grow. ("best-case scenario").

Similar proof, except instead of finding the upperbound, we are finding the lowerbound.

f(n) -> runtime as `n` approaches infinity
g(n) -> some function used as the **lowerbound** of f(n)

Thus `f(n) = Ωg(n)`

- There will also be a constant `c` where `f(n) >= c*g(n)`

**EXAMPLE**
f(n) = 3n<sup>2</sup> + 6n - 15
g(n) = c * n<sup>2</sup>

- The constant should be less than (or equal to) the coefficient of the greatest degree. In this case, `c = 2`. Thus we get:

  `3n^2 + 6n -15 >= 2n^2` plugging in `n = 5` (given that n = 5) will give us `90 >= 50`.
  
</br>
<div align = "center">

### Big Theta Notation:

</div>
 
f(n) = θ*g(n) if there exist values for c<sub>1</sub>, c<sub>2</sub>, and n<sub>o</sub> such that c<sub>1</sub> * g(n) <= f(n) <= c<sub>2</sub> * g(n:

> Remember that c1 must be an integer smaller than or equal to the coefficient of the greatest degree, vice verse for c2

**EXAMPLE**

f(n) = 3n<sup>2</sup> + 6n - 15
c<sub>1</sub> = 3 
c<sub>2</sub> = 9
n = 3

</br>

3n<sup>2</sup> = dominant term
6b = linear growth
(-)15 = insignificant

*Lower Bound*
Must prove that `3n^2 + 6n - 15 >= 3n^2` which when we plug in `n = 3` -> 30 >= 27 #TRUE

*Upper Bound*
Must prove that `3n^2 + 6n - 15 <= 9n^2` which when we plug in `n = 3` -> 30 >= 81 #TRUE

Thus we have the lower bound and upper bound of `3n^2 <= f(n) <= 9n^2`
