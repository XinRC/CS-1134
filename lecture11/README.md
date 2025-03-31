<div align = "center"> 

# Lecture 11
## Linked Lists

</div>

**Pros of an array list:**
- Access any element in constant time through indexing
- Good amortized performance overall

**Cons of an array list:**
- With a very large dataset, storing data would be problematic
- Insertions (and deletions) are expensive, usually being ϴ(n)

However, linked lists combat the expensive nature of insertions and deletions. 

## Linked Lists
> Values that are *linked* together sequentially to form a list. For a regular array list, the values would have **zero** idea they are placed near each other. Do note that linked lists are **one way**


## Anatomy of a Node:
A node knows it is the trailer of a node and that is it a head of another node. 

<div align = "center">

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220712172013/Singlelinkedlist.png" width = "600"/>
  
</div>

```python
class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None


def main():
  #creating the linked list
  head = Node() #first instance of a Node
  head.data = 1
  print(head.data) #prints 1


  #adding elements to the linked list (one directional list)
  new = Node(2)
  head.next = new_node
  print(head.next.data) #prints 2

  new_node = Node(3)
  head.next.next = new_node
  print(head.next.next.data) #prints 3
  # [ 1 -> 2 -> 3]


  #changing the head of a linked list
  new_head = Node(0)
  new_head.next = head #points new node's next pointer to the current header
  head = new_head #points header's pointer to the new head
  # [ 0 -> 1 -> 2 -> 3]

  #traverse our linked list
  current = head
  print("[", end = "")

  while current != None:
    print(f"{current.data} ->", end = "")
    current = current.next

  print("]")

if __name__ = "__main__":
  main()
    
```
