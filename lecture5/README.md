<div align="center">

#Searching Algorithms

</div>

- Linear Search: Searches one by one

```python
def linear_search(lst, val): # search through a list to find a target value
  val = val #θ(1)
  for i in range(len(lst)): #θ(n)
    if lst[i] == val: #θ(1)
      return i #θ(1)
  return None #θ(1)

# overall = θ(n) + θ(1)
# ignoring θ(1) -> T(n) = θ(n)
```
- Sorted Search (Binary Search): Sortings them in a chronological order. Through this, the algorithm can first go to the middle of the list and check if the value is greater than or less than the value the user wants. This would ultimately lead to T(n) -> `θ(log(n))` if the list was previously sorted, if the list was not yet sorted, then the algorithm will look like: `θ(nlog(n))`.

```python
def binary_search(lst, val):
  val = val
  start, stop = 0, len(lst) - 1
  
  while start <= stop:
    midpoint = (start + stop) // 2

    if lst[midpoint] == val:
      return midpoint
    elif lst[midpoint] > val:
      stop = midpoint - 1
    else:
      start = midpoint + 1
  
  return None #If the value is not in the list

```
