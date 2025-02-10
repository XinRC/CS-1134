<div align="center">

#Searching Algorithms

</div>

-Linear Search: Searches one by one

```python
def linear_search(lst, val): #searching through a list ot find a target value
  val = val
  for i in range(len(lst)):
    if lst[i] == val:
      return i
  return None
```
-
