<div align = "center" >

# Lecture 8
## Sorting
  
</div>

**The sorting problem:**
- Given a list (or any sequential data), we must reorder them so they end up in **ascending** order.

```python
lst = [2,1,3]
some_sorting_function(lst)

print(lst)
# prints [1,2,3]
```
Do make note that the function is not recreating a new list but **mutating** the original list. 

</br> 

<div align = "center">
  
### Selection Sort

</div>
This sort repeatedly selects the smallest element of the list and **swaps** it with the closest **unsorted** element of the list. 

For example:
lst = \[5, 8, 12, 7, 8, 10]

- One pointer (f) will traverse the entirety of the list
- Another pointer (s) will stay at the index of the first unsorted element.

As the program traverse, it will look like the follow:

\[5, 8, 12, 7, 8, 10] The original list

\[5, 7, 12, 8, 8, 10]

\[5, 7, 8, 12, 8, 10]

\[5, 7, 8, 8, 12, 10]

\[5, 7, 8, 8, 10, 12]

```python
def swap(lst, curr, min_idx):
  temp = lst[curr]
  lst[curr] = lst[min_idx]
  lst[min_idx] = temp
  # the whole thing is θ(1)

def selection_sort(lst):
  n = len(lst)

  for curr in range(n):
    min_idx = curr

    for j in range(curr + 1):
      if lst[j] < lst[min_idx]:
        min_idx = j
    swap(lst, curr, min_idx)
```
Overall selection sort is not very efficient. 

</br>

<div align = "center">
  
### Bubble Sort

</div>

This sorting method has two methods at index `0` and `1`, if the item at index `1` is smaller than the item at `0`, then a swap would occur. Then we will move to the next index, index `1` and `2` where the cycle will continuously cycle through the list swapping when necessary. 

</br>

<div align = "center">
  <img src="https://miro.medium.com/v2/resize:fit:1000/0*nh6F_qERbgD3xmV-.gif"/>
</div>

