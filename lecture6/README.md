<div align = "center">

# The Reality of Appending

</div>

While previously it was infered that the python list function, `.append()` has the time complexity of θ(1), everytime the list appends something, it is actually running on θ(n). However, we can still assume it runs on θ(1) time. 

### ***Dynamic Arrays***
- Arrays are fixed-size data structures.
  - Stores a sequence of values
  - Stores contiguously (together in memory)
  - Requires all elements to be the same size

```python
lst = [10, 20, 30, 40, 50]

print(len(lst)) # will output 5
print(lst[4]] # will output 50
```
For the list data structure itself, it has attributes (like that of `len()` which holds the length of the list), and the data limit itself (so for example if the limit was 1000). 
The address of `lst[k]` = Base address + (k * size of an element). Thus given that the Base address is: 0x4a003 and the size of the element is 8 (byte), to find the information from lst\[4] will make us do: 
- lst\[4] = 0x4a003 + (4 * 8) => 0x4a023


### ***Dynamic Arrays / Array Lists***
This does not directly allocate appended material to the next avaliable memory slot, they instead pre-allocate extra memory. This means that they allocate more memory than it was initially needed. 
- **If the pre-allocated memory is not yet full:** the appended material will be θ(1) since the pre-allocated space is avaliable.
- **When the pre-allocated memory IS full:** then it will create completely different array with a much larger size. copys the elements, and index the new elements. ]

### ***Optimized Resizing Approach***
Instead of resizing the size by 1 everytime, python lists will **double** in size whenever they run out of space, thus being far more efficient. This causes the runtime to behave differently:
- **Best Case**: Ω(1) when there is still is avaliable space
- **Worse Case** O(`k`) when the list must be resized.

### ***Amortised Analysis***
The average (or amortised) time per append operation is θ(1) because it runs on constant time much more than the time is runs on `n` time (when doubling). 
Thus to figure out amortised time: 
> T<sub>amortised</sub>(n) = total cost of the entire series / `n`

> T<sub>naive</sub>(n) => Θ(n<sup>2</sup>) / n => θ(`n`)
> T<sub>optimized</sub>(n) => n / n => θ(`1`)
