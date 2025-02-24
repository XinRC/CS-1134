<div align = "center">
  
# Lecture 7

## Recursion

</div>
Resursion is a problem-solving technique closed related to mathematicl induction, breaking a problem into smaller instances (of the same problem) where if the smallest case is true, the broader aspects is also true. Recursion utilizes stack as a means to solve the issue. It has two elements to it:
- `Base Case`
  - Condition with the *smallest* smallest possible input 
- `Recursion Step`
  - Calls the recursion function to get the smallest instances.
 
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

Because our original start = `1` and our end = `5`, we will go to the else loop. The following is what happens to the function call / stack.
1. `(1, 5)`
2. `(1, 4)`
3. `(1, 3)`
4. `(1, 2)`
5. `(1, 1)` prints `1` because start == end, prints `2` because after the count_up function it tells us to `print(end)`
6. `
