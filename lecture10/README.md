<div align = "center">

# Lecture 10
## Queues
  
</div>

Queues is another type of abstract data types. It is similar to its real world application where the first person in is the first person out (FIFO - *first in first out*). The "in" represents "enqueue" and the "out" represents "dequeue". 

### Operations we want for queues:
- q = Queue() # creation of a queue - θ(1)
- len(q) # determines the length of queue - θ(1)
- q.isempty() # checks if the queue is empty - θ(1)
- q.enqueue(item) # adds item at the end of the queue - θ(1) amortized 
- q.dequeue(item) # removes and returns item at the front of a queue - θ(1) amortized
- q.first() # returns the first item of the queue - θ(1)


### Two Models of Queues:
> Traditional Model where "everybody moves forward when dequeuing" - θ(n) because of the shifting

> Ciruclar Model where if the front item/s are dequeued, then the following enqueued item's data will be placed in the front indexes.
> Thus index <sub> front + 1 </sub> = (index<sub> front </sub> + 1) % capacity. This is where the index of the "first" changes. 

</br>

<div align = "center">
<img src = "https://i.makeagif.com/media/4-25-2020/tW3iGC.gif" width = 400 height = 250 />
  
(Copy of Circular Model)
</div>

```python
# static queue implementation
from ctypes import py_object

def make_array(n):
  return (n * py_object)()

class StaticArrayQueue():
  def __init__(self, max_cap):
    self.data_arr = make_array(max_cap)
    self.capacity = max_cap
    self.n = 0 #current size
    self.front_ind = None

  def __len__(self):
    return self.n

  def is_empty(self):
    return len(self.n) == 0

  def is_full(self):
    return len(self.n) == self.capacity

  def enqueue(self, item):
    if self.is_full():
      raise Exception("The Queue is full")

    elif self.isempty():
      self.data_arr[0] = item #enqueues the item into the first index
      self.front_ind = 0 
      self.n += 1

    else:
      back_ind = (self.front_ind + self.n) % self.capacity
      self.data_arr[back_ind] = item
      self.n += 1

  def dequeue(self):
    if self.is_empty():
      raise Exception("Cannot dequeue an empty queue")

    value = self.data_arr[self.front_ind] #saves the value at the front (so we can return it)
    self.data_arr[self.front_ind] = None #empties the spot (front)
    self.front_ind = (self.front_ind + 1) % self.capacity  #forces the new front index to be moved to the right
    self.n -= 1 #updates the size of the queue

    if self.is_empty():
      self.front_ind = None

    return value

  def first(self):
    return self.data_arr[front_ind]

```
