<div align = "center">
  
# Lecture 3

</div>

## Iterators:
When working with iterators/generators, a few things need to be kept in mind:
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
print(next(lst_iterator)) # will result in a StopIteration Error
```
However, do note that if the iterator has already been cycled through, the next attempt at `next()` will result in a StopIteration Error (as shown above)


## Generators:
While iterators utilize a lot more resources and all the iterations are calculated prior to their utilization, generators use up less resources since it provides the data as it is being requested. Meaning if a certain data was never requested, it will never compute for it. An important keyword for generators is `yield` as it is used similarly to that of "return" in a function, except it will go back to the yield call if the program was to be called again. 

```python
def generator():
num = 1
yield num # will return 1

num += 1
yield num #will return 2 if next() was called again

num += 1
yield num #will return 3 if next() was called again
```
