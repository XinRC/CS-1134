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
```
