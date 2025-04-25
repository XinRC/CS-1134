<div align = "center">

# Lecture 13
## Maps
  
</div>

In python, they are also known as dictionaries. They are a collection of key-value pairs who follow the following rules:

- Each key must be unique 
- Each key maps to exactly one value
- Values do not need to be unique


Dictionaries are **dynamic** in size, meaning it grows and shrinks. They are also very *very* efficent because of their operations. For example, deletion, insertions, and "look-up" all costs θ(1). This is due to their hash table implementation. 

</br>

<div align = "center"> 

| **Operation** | **Definition** | **Example Code** | **Runtime** |
| :---: | :--- | :--- | :---: |
| m = Map() | Creates an empty map | m = {} | θ(1) |
| m\[k] = v | Adding and updating the map | m\['a'] = 10 | θ(1) |
| m\[k] | Lookup / Retrival (`k` is mapped to `v`) | value = m\['a'] |  θ(1) |
| del m\[k] | Removes k - v pairs. Also removes key error if k does not exist | del m\['a'] | θ(1) |
| len(m) | Returns number of k-v pairs | | θ(1) |
| iter(m) | Returns an iterator of the map keys | for key in m: | Iterating costs θ(n) |

<sub>\* Note that `m` = map, `k` = key, `v` = value \*</sub>
</div>


```python
from ArrayList import ArrayList

class UnsortedArrayMap:
  class Item:
    def __iter__(self, key, value = None)
      self.key = key
      self.value = value
  def __iter__(self):
    self.table = ArrayList() # remember to import ArrayList beforehand

  # insertion
  def __set_item__(self, key, value):
    # first check if the key already exists -> if it does, replace the item value
    for item in self.table:
      if key == item.key:
        item.value = value
        return

    # if it does not already exist:
    self.table.append(UnsortedArrayMap.item(key, value))

  # lookup/retrieval
  def __getitem__(self, key):
    # first check if the key already exists -> if it does, replace the item value
    for item in self.table:
      if key == item.key:
        return item.value

    # if it does not already exist, raise an error
    raise KeyError(f"Key Error: {key}")

  # deletion (under the assumption our ArrayList has a pop with an index 
  def __delitem__(self, key):
    for idx in range(len(self.table)):
       if key == self.table[idx].key:
        self.table.pop(idx)
        return

    raise KeyError(f"Key Error: {key})

  # size
  def __len__(self):
    return len(self.table)

  def is_empty(self):
    return len(self) == 0

  # iteration...
  def __iter__(self):
    for item in self.table:
      yield item.key

#****

if __name__ == "__main__":
  bilal = UnsortedArrayMap()


  # Empty dictionary
  bilal = {} 
  
  # Assigning values
  bilal["Bilal"] = "Vocals"
  bilal["Common"] = "Vocals"
  bilal["Questlove"] = "Drums"
  bilal["Robert Glasper"] = "Piano"
  bilal["Burniss Travis"] = "Bass"

  '''
  # Lookup/Retrievl
  try:
    key = "Questlove"
    role = bilal[key]
    print(f"{key} exists!")
    #------
    key = "DiAngelo"
    role = bilal[key]
    print(f"{key} exists!")
  except KeyError:
    print(f"{key} does not exist!")
  
  # Delete values
  try:
    key = "Questlove"
    del bilal[key]
    #------
    key = "DiAngelo"
    del bilal[key]
  except KeyError:
    print(f"{key} does not exist!")
  
  # Size of the Map:
  print(len(bilal))
  
  # Iterating:
  for member in bilal:
    print(f"{member}: bilal[member]"
  '''
```
Unfortunately for the above implementation, it still runs at ϴ(n). 
