<div align="center">

#Searching Algorithms

</div>

- Linear Search: Searches one by one

```python
def linear_search(lst, val): # search through a list ot find a target value
  val = val #θ(1)
  for i in range(len(lst)): #θ(n)
    if lst[i] == val: #θ(1)
      return i #θ(1)
  return None #θ(1)

# overall has θ of n
```
- 
