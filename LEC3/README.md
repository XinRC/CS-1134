<div align = "center">
  
# Lecture 3

</div>

## Iterators:
When working with Iterators/Generators, a few things need to be kept in mind:
>Iterable: An item that is able to be become an iterator. This includes lists and strings.

>Iterator: The object that will be iterated through. 

By using the following code, the programmer will be able to assign the list as an iterator:
```python
lst = [1, 2]
lst_iterator = iter(lst)
```

To iterate through to the next integer, the command `next()` should be used.
```python
lst = [1, 2]
lst_iterator = iter(lst)

print(next(lst_iterator)) # will print 1
print(next(lst_iterator)) # will print 2
```
