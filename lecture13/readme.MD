<div align = "center">

# Lecture 10
## Queues
  
</div>

In python, they are also known as dictionaries. It is a collection of key-value pairs. 

 ## Rules
- Each key must be unique 
- Each key maps to exactly one value
- Values do not need to be unique


Dictionaries are **dynamic** in size, meaning it grows and shrinks. They are also very *very* efficent because of their operations. For example, deletion, insertions, and "look-up" all costs θ(1). This is due to hash table implementation. 

| Operation | Definition | Example Code | 
| :---: | :--- | :--- | 
| m = Map() | Creates an empty map | m = {} | 
| m[k] = v | Adding and updating the map | m['a'] = 10 |
| m[k] | Lookup / Retrival (`k` is mapped to `v`) | 
