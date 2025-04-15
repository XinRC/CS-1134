<div align = "center">

# Lecture 9  
## Abstract Data Types
  
</div>


> **Abstraction**: Seperates the interface of our program from the implementation.

There are several types of abstraction: 
1. Procedural: steps treated as units
2. Data: a way to store values without worrying about how its stored.

Imagine the interface of the program as being `public` but the implementation as `private`. 

<div align = "center">

## Stack

<div align = "left">

> **LIFO**: The last item in is the first item out. To think of this, imagine a stack of plates. We must remove the top ones because if we were to remove the bottom one, the whole entire thing would topple to the ground. 
  
</div>

 </br>

| **Operation** | **Definition** | **Runtime** | 
| --- | :--- | :---: | 
| stack = Stack() | creates an empty stack | Θ(1) | 
| len(stack) | number of items in the stack | Θ(1) | 
| stack.is_empty() | **true** if len(stack) is 0 | Θ(1) | 
| stack.push(*item*) | pushes *item* on to the top of the stack | Θ(1) |
| stack.pop | removes and returns the topmost item on the stack | Θ(1) |
| stack.top() | returns the topmost item on the stack | Θ(1) | 

</div>

The program should function to what it looks like below. Assume that `Stack()` was defined and has a general general stack implemtnation. 

```python
s = Stack()
s.push(2)
s.push(4)
print(s.pop()) # prints 4 because it removes and returns the last item
print(len(s)) # prints 1 because the items in the stack
```
</br>

<div align = "center">
  
<img src = "https://miro.medium.com/v2/resize:fit:1400/0*jQp8Ec60Kpfb15JI.gif" width = 200 height = 200>

(How the `push` and `pop` methods work using a stack)

</div>

</br>

## Implementation for Static Array 
In general call stacks are usually static because there is no unlimited RAM.
```python
# assuming ctypes and the ArrayList class have been imported

# for static-size stack:
class StaticArrayStack:
  def __init__(self, max_capacity):
    self.data = make_array(max_capacity)
    self.capacity = max_capacity
    self.n = 0 # this is the current size 

  def is_empty(self):
    return len(self) == 0

  def is_full(self):
    return len(self) == self.max_capacity

  def __len__(self):
    return self.n

  def push(self,item):
    if self.isfull():
      raise Exception("Stack is full")
    
    self.data[self.n] = item
    self.n += 1

  def pop(self):
    if self.is_empty():
      raise Exception("Stack is empty")

    item = self.data[self.n - 1] # assigns the "topmost" item as at the variable "item"  
    self.data[self.n - 1] = None # "topmost" item disappears because it becomes "None"
    self.n -= 1

    return item

  def top(self):
    if self.is_empty():
      raise Exception("Stack is empty")

    item = self.data[self.n - 1]
    return item
```

</br>

## Implementation for Dynamic Array 

```python
# assuming ctypes and the previous class (ArrayList) have been imported.
# many of the following functions like `append` have been previously defined in the class ArrayList().
# this is why we are not redefining them.

# for dynamic-size stack:
class ArrayStack:

  def __init__(self):
    self.data = ArrayList()

  def __len__(self);
    return len(self.data)

  def is_empty(self):
    return len(self) == 0

  def push(self, val):
    self.data.append(val) # using an ArrayList() class method because the ArrayList is where we store our data

  def top(self):
    if self.is_empty():
      raise Exception("The Stack is empty")

    return self.data[-1] # the ArrayList() class has a method that allows us to index (since it works similar to a list)

  def pop(self):
    if self.is_empty():
      raise Exception("The Stack is empty")

    return self.data.pop() # the ArrayList() class has a method that does popping

```

<div align = "center"> 
  
## Problem Solving with Stacks

</div>

The most "comical" problem stacks can solve is reversing a list/string. Given a string, the item at index `0` would be the the bottom-most item in the stack, followed by the item at index `1`, then `2`, then `3`, continuing until we reach the `len(s) - 1`. In the end, this means the topmost item on the stack would be the item on the last index. This means when reversing the items, the item on the last index would become the first item. The time complexity is: θ(n).

```python
string = "Plato"

def reverse(string):
  stack = ArrayStack() # the dynamic array stack implemented from the previous example

  for char in string: # adds every character, into the stack
    stack.push(char) 

  while not stack.is_empty():
    char = stack.pop() 
    print(char, end = "") 


"""
Result:

otalP
"""
```
This function runs at linear time and the time complexity is also linear.

</br>

<div align = "center"> 
  
# Polish Notation

</br>

| **Notation** | **Example*** | **Telling Them Apart** | 
| :---: | :---: | :--- |
| Infix | 2 + 2 | Normal math notation |
| Postfix | 2 2 + | Operand usually in the end |
| Prefix | + 2 2 | At least one operand in the beginning usually |

</div>

> **Only** postfix works very well with stacks. 

</br>

### Explaination for Postfix:

Given a list: `[ 2 3 4 + 3 * - ]`, We must scan the whole list until we find our first operator, `+`. Then we must add the two numbers that prefaces it, `3` and `4`. This will give us: `[ 2 7 3 * - ]` then we traverse the list until we find the next operator, `*` and muliplify the two numbers that prefaces it, `7` and `3`. This will give us `[ 2 21 - ]`. Again we find the next operator `-` and subtract the two numbers that preface it, `2` and `21` which will give us `[ - 19 ]`.

We can utilize stacks because it follows the same strategy as the postfix method. 

```python

def eval_postfix_expr(string):
  lst = string.split() # seperating string into a list so we can evaluate each value by itself. Costs θ(n)
  stack = ArrayStack() 

  for token in lst:
    if token not in "+-*/":
      stack.push(int(token))
    else:
      op_one = stack.pop()
      op_two = stack.pop()

      if token == "+":
        res = op_one + op_two
      elif token == "-":
        res = op_one - op_two
      elif token == "*":
        res = op_one * op_two
      else:
          if op_one == 0:
            raise ZeroDivisionError
          else:
            res = op_one / op_two

      stack.push(int(res))

  return stack.pop()
```

</br>
<div align = "center">
  
[More Resources](https://github.com/sebastianromerocruz/CS1134-data-structures-and-algorithms/tree/main/lectures/08-stacks)

</div>
