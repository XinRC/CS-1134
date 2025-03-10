<div align = "center">
  
# Abstract Data Types
  
</div>


> Abstraction: Seperates the interface of our program from the implementation.

There are several types of abstraction: 
1. Procedural: steps treated as units
2. Data: a way to store values without worrying about how its stored.

Imagine the interface of the program as being `public` but the implementation as `private`. 

## Stack
**LIFO** - The last item in is the first item out. To think of this, imagine a stack of plates. We must remove the top ones because if we were to remove the bottom one, the whole entire thing would topple to the ground. 

1. stack = Stack() # creates empty stack
2. len(stack) # number of items in the stack
3. stack.is_empty() # true if len(stack) == 0, else false
4. stack.push(item) # adds item onto the top of the stack
5. stack.pop() # removes te item from top of the stack - **also returns the item**
6. stack.top() # returns the topmost item


```python
s = Stack()
s.push(2)
s.push(4)
print(s.pop()) # prints 4 because it removes and returns the last item
print(len(s)) # prints 1 because the items in the stack
```

Because there is no Stack object in python, we must create our own object. 
