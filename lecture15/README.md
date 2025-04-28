<div align = "center">

# Lecture 15
## Hash Tables
  
</div>

> [!WARNING]
> Needs to be revised

- `Bucket Array`:
  - Giant list of spots/"bucket" locations
  - Each key is mapped to a single bucket using a deterministic rule, deterministic means "predictable"
  - Is Θ(1)

- `Hashing`:
  - A `hash function` lets us take any key and deterministically converts it to a number (index).
  - A simple hashing function could be just the length of the `key`. Do note that means multiple 3-lettered keys would have the same index - being not very efficient.
 
- `Hash Table`:
  - Uses a function
  - Handles collisions
  - Overall uses Θ(1)
 

<div align = "center">

| Word | Definition |
| :--- | :--- | 
| Universe: `u` | A set from which the keys will be taken from. A `set` is assumed to be an array where the values are not the same | 
| Hash Table: </br> <sub>T\[0, ..., N-1]</sub> | An array with `N` slots |
| Hash Function: </br> <sub>h(`u`)</sub> | A function that maps keys from the universe into slots in the table. | 
| Collision | When 2 keys links to the same Hash Table index, two strategies to prevent this: </br> 1. Chaining: </br> 2. Finds next avaliable spot (will not be used in CS-1134)


</div>

## Chaining:
If too many keys map to the same hash table - it would detriment the runtime. 

We want a hash function that would uniformly distribute keys. Having it never collide is impossible - so the hash function should "uniformly" distribute the keys. "Uniformly" as in when a function is given a random chosen key it will be equally likely to be mapped at any slot of `T`.

There is a 2 step process:
- **A coding fnction (h<sub>1</sub>)**: This costs Θ(1) that transforms the key to an integral (could be a huge (and negative) number
- **A compression function(h<sub>2</sub>**: Converst down the output of h<sub>1</sub> into a usable index where 0 <= index <= capacity

<div align = "center">
  
| Looks like|
| --- |
|h(key) = h<sub>2</sub>(h<sub>1</sub>(key)|

<img src = "https://github.com/user-attachments/assets/7a020874-81f5-48aa-b1e6-58e6e3ff50d2" width = 500 height = 300>

</div>

## Coding Functions
### Will utilize python's built in coding functions

- Integer Casting (not a good function is the first 8 bytes of prefix is the same - most of the time a good process)
  - Look at the binary representation of the key
  - Take the 8 least significant bytes
  - Interpret them as a 64 bit number

- Component Sum (words with the same letters would point at the same key)
  - Take each byte in key
  - Cast to an integer
  - Add them together

- Polynomial Accumulation
  - Let `z` be any interger >= 2, for any key h<sub>1</sub>(key) = (k<sub>0</sub>  * z <sup> 0 </sup>) + (k<sub>1</sub> * z<sup>1</sup>) + ... + (k<sub>m-1</sub> * z<sup>m-1</sup>)
 
## Compression Functions
### We want to convert these huge numbers into a usable index

- Moding / Division Method
  - h<sub>2</sub>(k) = k mod `N` where `N` is the max capacity and `k` is the current 64-bit number
  - best used when no patterns

- The MAD Method:
  - Stands for (Multiply, Add, Divide)
    - Let `p` be a prime number such that p > |`u`| with u representing the universe
    - Let `a` be any number from 1 to p-1
    - Let `b` be another integer from 0 to p-1


<div align = "center">
  
h<sub>2</sub>(k) = ((a * k + b) % p) % N

</div>

## Runtime Analysis

- Find 
  - Compute hash function
  - Search through chain in slot
  - Worse Case scenario: O(n)
  - **Load Factor**
    - Load Factor α = n / N where `n` represents the number of keys and `N` is the capacity
- 


## Callable Objects:
```python
class Counter:
  def __init__(self):
    self.count = 0
  def increment(self:
    self.count += 1
  def __call__(self):
    self.increment += 1

'''
#Using the increment would be:
counter = Counter()
counter.increment()
counter.increment()

#Using the call dunder method:
counter = Counter()
counter()
counter()
'''
```

Method:
```python
HASH_PRIME = 40206835204840513073

from random import randrange
from ctypes import py_object
from UnsortedArrayMap import UnsortedArrayMap

def make_array(n):
  return (n * pyobject)()

class ChainingHashTableMap:
  class MADHashFunction:
    def __init(self, N, p=Hash_PRIME): # N is the size and p is the prime number
      self.N = N
      self.p = p
      self.a = randrange(1, self.p - 1)
      self.b = randrange(0, self.p - 1)

    def __call__(self, key):
      # [(a * hashed_key + b) mod p] mod N 
      return ((self.a * hash(key) + self.b) % self.p) % self.N

  def __init__(self, N=64):
    self.table = make_array(N)

    for i in range(N): #for every "part" of the table, we will be adding another data structure to handle collisions
      self.table[i] = UnsortedArrayMap()

    self.n = 0
    self.h = ChainingHashTableMap.MADHashFunction(N)


  def is_empty(self):
    return len(self) == 0

  # RETRIEVAL / LOOKUP
  def __getitem__(self, key): # "double indexing" process
    i = self.h(key) #which bucket are we in
    curr_bucket = self.table[i]

    val = curr_bucket[key]
    return val

  # CREATE NEW KEY-VALUE PAIR
  def __setitem__(self, key, value):
    i = self.h(key) # first find the bucket -> must also find the size
    curr_bucket = self.table[i]

    old_size = len(curr_bucket)

    curr_bucket[key] = value

    new_size = len(curr_bucket)

    if new_size > old_size:
      self.n += 1

    if self.n > len(self.table): # resizing
      self.rehash(2 * len(self.table))

  # DELETION:
  def __delitem__(self, key)
    i = self.h(key)
    curr_bucket = self.table[i]

    del curr_bucket[key]

    self.n -= 1

    if self.n > len(self.table) // 4:
      self.rehash(len(self.table) // 2)

    def __contains__ (self, key):
      try:
        self[key]
        return True
      except KeyError:
        return False

    def __iter__(self): # useless -> gets rid of the point of hash tables
      for curr_bucket in self.table:
        for key in curr_bucket:
          yield key 

    def rehash(self, n):
      old = [(key, self[key]) for key in self]

      self.__init__(new_size)

      for key, val in old:
        self.[key] = val
```
