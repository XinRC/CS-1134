<div align = "center">

# Lecture 3

</div> 

## Iterators / Iterable

>Iterable: An item that is able to be an iterator. This includes lists and strings.

>Iterators: The item will be iterated through. 

The `iter()` function will convert the data type into an iterator, allowing for the call of the `next()` function. The `next()` function will iterate through the items of the iterator.

```python
lst = [1, 2, 3]
lst_iterator = iter(lst)

for item in lst:
  print(next(lst_iterator))

#1
#2
#3
```

However, if the itervaled item has already been cycled through, it will not repeat the process if the `next()` function was called again. Instead, it will raise a `StopIteration Erorr` as seen below.

```python
word = "abc"
word_iterator = iter(word)

print(next(word_iterator)) # prints "a"
print(next(word_iterator)) # prints "b"
print(next(word_iterator)) # prints "c"
print(next(word_iterator)) # raises StopIteration Error
```

## Generators

Generators is a more efficient way of iterating. While the previous programs will create the iterator to its full extent, a generator will do it **lazily** and only provide the next iterator data when and *if* it was asked for. If it was not asked for at all, the generator will not provide the data.

To write a generator, it is very similar to that of defining a function. However, instead of using `return` the keyword `yield` is used to return the data at that one specific yield point. If the function is called again, the function will continue from that yield point and continue forward.

```python
def generator():
```
