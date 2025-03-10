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
  
## Selection Sort

</div>
This sort repeatedly selects the smallest element of the list and **swaps** it with the closest **unsorted** element of the list. 

- One pointer (f) will traverse the entirety of the list
- Another pointer (s) will stay at the index of the first unsorted element.

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
</br>

<div align = "center">

<img src="https://miro.medium.com/v2/resize:fit:1400/1*5WXRN62ddiM_Gcf4GDdCZg.gif" width = "500" height = "300"/>
  
</div>

</br>
Overall selection sort is not very efficient, running at θ(n<sup>2</sup>). 

<div align = "center">
  
## Bubble Sort

</div>

This sorting method has two methods at index `0` and `1`, if the item at index `1` is smaller than the item at `0`, then a swap would occur. Then we will move to the next index, index `1` and `2` where the cycle will continuously cycle through the list swapping when necessary. 

</br>

<div align = "center">
  <img src="https://miro.medium.com/v2/resize:fit:1000/0*nh6F_qERbgD3xmV-.gif" width = "500" height = "300"/>
</div>

```python
def bubble_sort(lst):
  n = len(lst)

  for i in range(n - 1): #  n - 1 is to avoid going out of the bounds
    for j in range(n - i - 1): #  n - i is to avoid the sorted portion and the -1 is to go out of the bounds
      if lst[j] > lst[j + 1]:
        lst[j], lst[j + 1] = lst[j + 1], lst[j] #  swaps the elements

```
<div align = "center">

## Insertion Sort

</div>

We first assume that the item in index `0` has already been sorted (it does not have to be true). We then compare the next index, at index `1` which if the item at index `1` is greater than the item at index `0`, we do not do anything. However, if the item at index `0` is greater than the item at index `1`, then we swap. Then we move our pointers to the next item at index `1` and `2`, if the item at index `2` is smaller than the item at index `1`, we will swap them. Then we will compare the item formerly at index `2` and compare it to the item on the current index `0`. If the item formerly at index `2` is smaller than the item currently at index `0`, then we will swap. This will continue until the whole list has been sorted. 

</br>
<div align = "center">
<img src= "https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" width = "500" height = "300"/>
</div>
</br>

```python
def insertion_sort(lst):
  for idx in range(1, len(lst)):
    curr = lst[idx]
    j = idx

    while j >= 1 and lst[j - 1] > curr:
      lst[j] = lst[j-1]
      j -= 1

    lst[j] = curr
      
```

<div align = "center">

 ## Merge Sort
 
</div>

This sorting algorithm utilizes recursion. Given a list, we will keep dividing the list into 2 until it reaches its base case (of 1 item). Then once it is in its base case, we will "merge" it to make it follow sequential order. Then it will do the same for the other base cases, eventually merging them with the previous merged list. 

<div align = "center">
<img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif" width = "500" height = "300">
</div>
