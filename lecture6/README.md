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

