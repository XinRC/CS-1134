<div align = "center">
  
# Lecture 7

## Recursion

</div>
Resursion is a problem-solving technique closed related to mathematicl induction, breaking a problem into smaller instances (of the same problem) where if the smallest case is true, the broader aspects is also true. Recursion utilizes stack as a means to solve the issue. It has two elements to it:

- `Base Case`
  - Condition with the *smallest* smallest possible input. This is what dictates how many times the recursion runs. 
- `Recursion Step`
  - An assumption where when we call the function (with a smaller input), it will do its job. After, find a way to use the assumption in order to solve the problem with the given input. 
  - Thus this means, it calls the recursion function to get the smallest instances.
 
Take for example the following code:
```python
def count_up(start, end)
  if start == end:
    print(start)
  else:
    count_up(start, end - 1)
    print(end)

count_up(1, 5)
```

Because our original start = `1` and end = `5`, we will go to the else loop. The following is what happens to the function call / stack.
1. `count_up(1, 5)`
2. `count_up(1, 4)` + prints(5)
3. `count_up(1, 3)` + print(4)
4. `count_up(1, 2)` + print(3)
5. `count_up(1, 1)` + print(2)
6. `count_up(1, 1)` = print(1) because start == end
   
8. `count_up(1, 2)` => print(1) + print(2)
9. `count_up(1, 3)` => print(1) + print(2) + print(3)
10. `count_up(1, 4)` => print(1) + print(2) + print(3) + print(4)
11. `count_up(1, 5)` => print(1) + print(2) + print(3) + print(4) + print(5)

This is because originally, we assume that `count_up(1,5)` will eventually give us `count_up(1,4) + print(5)` and assume that it will be true. Then we keep breaking down the `count_up(lower, val)`


## Asymptotic for Recursion (Recursion Tree)

1. We must represent each recursive call as a `node` (as a leaf of the tree). Denoid of each mode, write the size of the current input (e.g. n, n-1, n-2, etc).
2. If function call A makes a call to B, we must draw an "edge" aka just a line, (the branch of the tree) from A to B.
3. Finally for each node, write the "cost" of each function as if the recursion call does not exist. (This is called the local cost).

> If everything in the function is constant, then θ(n) because you are calling the function `n` amount of times. This means that that for recursion, it must be *at least* θ(n)

The link of a diagram will be later posted:

### Sample Question:
Given a list of values, we must check how many times the number `n`, in this case 2, is in the the list. 

- Base Case: if `len(lst) = 0`, we will return 0
- Hypoth: when we call a smaller instance of list, then we will count the occurance in the smaller list
```python
def count_occurance(lst, val):

  #Base Case:
  if len(lst) == 0: #θ(1)
    return 0 #θ(1)
  else:
    first_elem = lst[0] #θ(1)
    rest_elem = lst[1:] #θ(n)

    if first_elem == val: #θ(1) 
      return 1 + count_occurance(rest_elem, val)
    else:
      count_occurance(rest_elem, val)
```

Thus the total **local** cost is `n` because of `rest_elem = lst[1:]`. This means the final the total runtime is θ(n<sup>2</sup>)
 
