<div align = "center">

# Lecture 9  
## Abstract Data Types
  
</div>


> Abstraction: Seperates the interface of our program from the implementation.

There are several types of abstraction: 
1. Procedural: steps treated as units
2. Data: a way to store values without worrying about how its stored.

Imagine the interface of the program as being `public` but the implementation as `private`. 

## Stack
**LIFO** - The last item in is the first item out. To think of this, imagine a stack of plates. We must remove the top ones because if we were to remove the bottom one, the whole entire thing would topple to the ground. 

1. stack = Stack() |*creates empty stack > Θ(1)*
2. len(stack) |*number of items in the stack > Θ(1)*
3. stack.is_empty() |*true if len(stack) == 0, else false > Θ(1)*
4. stack.push(item) |*adds item onto the top of the stack > Θ(1)*
5. stack.pop() |*removes te item from top of the stack - **also returns the item** > Θ(1)*
6. stack.top() |*returns the topmost item > Θ(1)*

```python
s = Stack()
s.push(2)
s.push(4)
print(s.pop()) # prints 4 because it removes and returns the last item
print(len(s)) # prints 1 because the items in the stack
```

Because there is no Stack object in python, we must create our own object. 

</br>

### Implementation for Static Array 
In general call stacks are usually static because there is not unlimited RAM.
```python
# assuming ctypes and the previous class (ArrayList) have been imported

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

### Implementation for Dynamic Array 

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
    self.data.append(val)

  def top(self):
    if self.is_empty():
      raise Exception("The Stack is empty")

    return self.data[-1] # the ArrayList class has a function that allows us to index

  def pop(self):
    if self.is_empty():
      raise Exception("The Stack is empty")

    return self.data.pop() # the ArrayList class has a function that does popping

```

<div align = "center"> 
  
## Problem Solving with Stacks

</div>

The most "comical" problem stacks can solve is reversing a list/string. Given a string, the item at index `0` would be the the bottom-most item in the stack, followed by the item at index `1`, then `2`, then `3`, continuing until we reach the `len(s) - 1`. In the end, this means the topmost item on the stack would be the item on the last index. This means when reversing the items, the item on the last index would become the first item. The time complexity is: θ(n).

```python
string = "Plato"

def reverse(string):
  stack = ArrayStack() # dynamic array stack from previous example | this is also θ(1)

  for char in string: # adds every character, overall runtime of the loop is θ(n)
    stack.push(char) # amortized time of .push() is θ(1)

  while not stack.is_empty():
    char = stack.pop() # amoritzed time of .pop() is θ(1)
    print(char, end = "") # θ(1)

  print() # θ(1)
```
This function runs at linear time and the time complexity is also linear.


<div align = "center"> 
  
# Polish Notation

</div>  

2 + 2 -> infix notation
2 2 + -> postfix notation
\+ 2 2 -> prefix notation

Given a list: \[ 2 3 4 + 3 * - ]
We must scan the whole thing until we find out first operator, `+`. Then we must add the two numbers that prefaces it, `3` and `4`. This wll give us: \[ 2 7 3 * - ] where we scan the list until we find the first operator, `*` and muliplify the two numbers that prefaces it, `7` and `3`. This will give us \[ 2 21 - ] which will give us \[ - 19 ]

When stacking, a similiar thing happens. Whenever we reach an operand, the last two items on the stack gets popped and there would be a `push` for the result of the operand and operator. Each item are usually called "token"

```python

def eval_postfix_expr(string):
  lst = string.split() #θ(n)
  stack = ArrayStack() θ(1)

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
