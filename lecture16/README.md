<div align = "center">

# Lecture 16
## Priority Queues / Heaps

</div>

Formally defined as **PQ** or **Heaps** is a form of ADT in which each element has a value *and* a priority. The item with the highest priority is returned first. PQs and Heaps are most often used for task scheduling algorithms. 

- Insertions are done freely
- Removals occur at the min values or at values with the max priority. 

</br>

## Binary Heap
Although not technically a binary tree - we will be thinking about the binary heap as a binary tree, but it will be implemented NOT as one. Some properties include:

- Each node is less than or equal to its children. (Means their children is larger than or equal to them).
- Parents have a higher priority than their child
- Must be a complete binary tree
  - All levels are fully filled except for the last (guarantees log(n) lookup time.
- It will have an "array" implementation
  - For any node at index `i` ...
    - Left child's index is at: 2i + 1
    - Right child's index is at: 2i + 2
    - Parent's index is: (i - 1) // 2:
        - This is assuming if the index starts at 1, otherwise we must do i // 2 since array's index starts at 0.

<div align = "center">
  
| **Defintition** | **Showcase** | 
| :---: | :--- |  
| Insertion | **1.** Place new element in next avaliable spot (in the end). </br> **2.** "Bubble up" (upheap) until the heap order property is restored. This is by finding the parent using `(i - 1) // 2`. If the parent's value is greater than the new element's value, then we will swap their indexes. | 
| Removal | **1.** Swap the root (first element) with the last element. </br> **2.** Remove the last element (which was a former head/root). </br> **3.** "Bubble down" (downheap) if necessary. Thos means if the child's value is greater than the head, we must swap their indexes. If it "index" is outside of the array, then it works and we are good. 

</div>

## Implementation:
This implementations before represent the methods used to determine the index of the right and left child, along with current index's parent. The `has_left` and `has_right` methods will check if the current index has a left/right child. NOTE the class of the Priority Queue will be called `class ArrayMinHeap`

```python
def right(self, i):
  return (2 * i) # 2 * i because the first item (at index )) is NONE

def left(self, i):
  return (2 * i + 1) # 2 * i + 1 because the first item (at index 0) is NONE

def parent(self, i):
  return (i // 2)

def has_left(self, i):
  return self.left(i) <= len(self.data) - 1

def has_right(self, i):
  return self.right(i) <= len(self.data) - 1
```

For each item in the priority queue, they must have a priority and a value. Because we are creating a min heap, we must also make a dunder method that allows us to compare the priority of the value and the other. 

```python
class ArrayMinHeap:

  class Item:
    def __init__(self, priority, value = None):
      self.priority = priority
      self.value = value
    def __le__(self, other):
      return self.priority <= other.priority


  def __init__(self, priority_lst = None, values_lst = None)
    self.data = [None]
  
    if priorities_lst is not None:
      for i in range(len(priority_lst)):
        new_item = ArrayMinHeap.Item(priorities_lst[i], values_lst[i])
        self.data.append(new_item)

    first_non_leaf_index = self.parent(len(self.data) - 1)

    for i in range(first_non_leaf_index, 0, -1):
      self.fix_down(i)
    
```

Upheaping:
We must compare the current index (of the newly inserted item) with its parent's index. If the current index value is smaller than the parent's index value, then we must swap. This keeps cycling until the parent's index value is smaller than the current index value. This would look like in code, calling it "fix_up". NOTE the beginning of the heap will be NONE.:

```python
def fix_up(self, i):
  curr_index = i
  continue = True

  while continue is True and curr_index > 1:
    parent_index = self.parent(curr_index)
    if self.data[parent_index] <= self.data[current_index]:
      continue = False
    else:
      self.swap(current_index, parent_index
      current_index = parent_index

def insert(self, priority, value = None):
  new_item = ArrayMinHeap.Item()
  self.data.append(new_item)

  self.fix_up(len(data) - 1) #calling it on the last element (aka newly inserted element)

def delete_min(self): # always be deleting at the root (because it is a QUEUE
  if self.is_empty():
    raise Exception("The Heap is empty.")
  self.swap(1, len(self.data) - 1) #swap our root with the last element so we can "pop" at ammortized time
  item = self.data.pop()

  '''
  Because of the swap, we must downheap to make sure our parent is always smaller than its children.
  We would get the values of the left and right child value and we will compare the current index value
  to the child with the smallest value. If the smallest child's value is smaller than the current index
  value, then we must swap
  '''
  if not self.is_empty():
    self.fix_down(1)
  return item


def fix_down(self, i):
  current_index = i
  continue = True

  while continue is True and self.has_left(current_index): # makes sure the current index has a left child 
    left_index = self.left(current_index)
    right_index = self.right(current_index)
    smallest_child_index = right_index if self.data[right_index] <= self.data[left_index] else left_index

    if self.data[current_index] <= self.data[smallest_child_index]:
      continue = False
    else:
      self.swap(current_index, smallest_child_index)
      current_index = smallest_child_index

def is_empty(self):
  return len(self.data) == 0

def swap(self, current_index, parent_index):;
  self.data[current_index], self.data[parent_index] = self.data[parent_index], self.data[current_index]
```
