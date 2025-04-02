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
<div align = "center">
  
## Doubly Linked List
### Bi-Directional Linked List
  
<img src="https://techvidvan.com/tutorials/wp-content/uploads/2021/06/Doubly-linked-list-in-DS-1.jpg" width = 400 height = 250>

</div>

</br>

```python
#starts with a head list and en end list, always "insert" after the head list but before the end list.. 
class DoublyLinkedList:
  class Node:
    def __init__(self, data = None):
      self.data = None
      self.next = None
      self.prev = None

  def __init__(self):
    self.header = DoublyLinkedList.Node()
    self.trailer = DoublyLinkedList.Node()
    self.n = 0 #size

    #connecting header and trailer together
    self.header.next = self.trailer
    self.trailer.prev = self.header

  def __len__(self):
    return self.n

  def is_empty(self):
    if len(self) == 0:
      return True
    else:
      return False

  #ADDING
  def add_after(self, node, val): #"new_node" is after node.
    new_node = DoublyLinkedList.Node(val)

    #keep track of connections
    prev_node = node
    next_node = node.next

    prev_node.next = new_node
    new_node.prev = prev_nod

    new_node.next = next_node
    next_node.prev = new_node
    self.n += 1

    return new_node #returns a  pointer to the new node

  def add_first(self,val):
    return self.add_after(self.header, val)

  def add_last(self, node, val):
    return self.add_after(self.trailer.prev, val)

  def add_before(self,node, val):
    return self.add_after(node.prev, val)

  #DELETION
  def disconnect(self):
    self.data = None
    self.next = None
    self.prev = None

  def delete_node(self, node):
    data = node.data

    #save references to the surronding nodes 
    previous = node.prev
    after_node = node.next

    #connect surronding nodes to each other
    previous.next = after_node
    after_node.prev = previous

    #update the size
    size.n -= 1

    #disconnect node we are deleting
    node.disconnect()

  def delete_first(self):
    if self.is_empty():
      raise Exception("List is empty")
    return self.delete_node(self.header.next)

  def delete_last(self):
    if self.is_empty():
      raise Exception("List is empty")
    return self.delete_node(self.trailer.prev)

  def remove_all(self,elem):
    cursor = self.header.next

    while cursor is not self.trailer: #while the item after the header node is not yet the trailing node
      if cursor.data == elem:
        next_node = cursor.next
        self.delete_node(cursor)
        cursor = next_node
      else:
        cursor = cursor.next

  def __iter__(self): #the iterator to allow usage on a "for loop"
    cursor = self.header.next

    while cursor is not self.trailer:
      yield cursor.data
      cursor = cursor.next

  def __repr__(self): #defeats the purpose of the linked list because it turns it into an array
    return '[' + ' <--> '.join([str(elem) for elem in self]) + ']'

  def __str__(self):
    return repr(self)
  
  
def main():
  dll = DoublyLinkedList
  dll.add_last(1)
  dll.add_last(2)
  dll.add_last(3)
  dll.add_after(dll.header.next, 10)
  print(dll)
  # [1 <--> 10 <--> 2 <--> 3]

```
