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
