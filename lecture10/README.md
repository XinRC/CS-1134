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
> Thus index <sub> front + 1 </sub> = (index<sub> front </sub> + 1) % capacity 

```python
index
```
