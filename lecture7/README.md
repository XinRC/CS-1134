<div align = "center">
  
# Lecture 7

## Recursion

</div>

Recursion is utilizes stack as a means to solve the issue. Recursion has two elements to is:
- `Base Case`
  - Identify the amount of time the recursion will run
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
