<div align = "center">

# Lecture 16
## Priority Queues / Heaps

</div>

Formally defined as **PQ** or **Heaps** is a form of ADT in which each element has a value *and* a priority. The item with the highest priority is returned first. PQs and Heaps are most often used for task scheduling algorithms. 

Insertions are done freely
Removals occur at the min values or at values with the max priority. 

</br>

## Binary Heap
Although not technically a binary tree - we will be thinking about the binary heap as a binary tree, but it will be implemented NOT as one. Some properties include:

- Each node is less than or equal to its children. (Means their children is larger than or equal to them)
- Must be a complete binary tree
  - All levels are fully filled except for the last (guarantees log(n) lookup time.
- It will have an "array" implementation
  - For any node at index `i` ...
    - Left child's index is at: 2i + 1
    - Right child's index is at: 2i + 2
    - Parent's index is: (i - 1) // 2

<div align = "center">
  
| **Defintition** | **Showcase** | 
| :--- | :--- |  
| Insertion | **1.** Place new element in next avaliable spot (in the end). </br> **2.** "Bubble up" (upheap) until the heap order property is restored. This is by finding the parent using `(i - 1) // 2`. If the parent's value is greater than the new element's value, then we will swap their indexes. | 
| Removal | **1.** Swap the root with the last element. </br> **2.** Remove the last element (which was a former head/root). </br> **3.** "Bubble down" (downheap) if necessary. 

</div>
