<div align = "center">

# Lecture 12
## Trees
  
</div>

## Terms and Definitions

| Terms | Definition |
| :---: | :--- |
| **Parent** | The node above another node. Also called "root-node" |
| **Child** | The node below another node | 
| **Siblings** | This is when two nodes have the same parent |
| **Internal Nodes** | Any node that is *not* the last node |
| **Leaf Nodes** | And end nodes |
| **Subtrees** | A smaller tree that is part of a bigger tree. For every subtree, it would have a different "root-node" spanning from its root-node to the leaf-node of its subtree | 
| **Edge** | The "lines" that connect each node. `(u,v)` is an edge if `u` is the parent of `v` | 
| **Path** | The path of a tree. Where p = (v<sub>1</sub>, v<sub>2</sub>, ... v<sub>k</sub>) is a path where each 2 consecutive nodes form an edge
| **Length of Path** | The amount of "edges" in a path ( |p| = number of edges in p )
| **Ancestor** | Where in `(u,v)`, `u` is the ancestor of `v` if there is a path to `u` from `v` |
| **Descendent** | Where in `(u,v)`, `v` has the ancestor of `u` if there is a path from `u` to `v` |
| **Level** | Whenever there is a "break" or "edge", a "level" will be formed. Levels increase as we get deeper into the tree. | 
| **Height of the Tree** | The length of the longest path in the tree | 

## Types of Binary Trees
> **Full Binary Tree**: Each tree node can only have 0 or 2 children.

> **Complete Binary Tree**: Each parent *must* have 2 children for each level. This means every level must have the max possible amount of nodes. 


<div align = "center">

<img src = "https://ik.imagekit.io/upgrad1/abroad-images/imageCompo/images/unnamed_11_IWS24B.png?pr-true" width = 400 height = 250>

(For each level of the tree, each parent must have 2 children until we arrive at the level of the leaf nodes)

</div>

</br>
</br>

<div align = "center">
  
## To Traverse a List
To traverse a list, it will cost a minimum of θ(n) due to us going through the list `n` amount of times. 

</div>

## Preorder
This method looks at the center, left, then right recursively. This means we will get the value of the "center" value first then continuously get the value of the left value (because if it splits up, the left value would be considered a "center") until we reach the leftmost value. Then we will take the right value, and if it is the "center", then it will take the left value until it reaches the leftmost value, then taking the right value. 

<div align = "center">

<img src = "https://upload.wikimedia.org/wikipedia/commons/a/ac/Preorder-traversal.gif" width = 300 height = 200>

</div>

## Postorder
This method looks at the left, right, then center recursively. If the node is a "center" (aka a parent), then we will skip it and go to the next left/right before finally stating the center. Pretty much it goes down the furtherest left path, if there is no more left path, then it will go to the right path, and if there is no more right path, then it will recount the center path. This means ultimately the last value would be the root-root value.

<div align = "center">

<img src = "https://upload.wikimedia.org/wikipedia/commons/2/28/Postorder-traversal.gif" width = 300 height = 200>

</div>

## Inorder
This method is how we would read in english, from left, center, then right. If the node is a "center (aka a parent), we must skip it and go to the leftmost value. Ultimately we will go down to the furthest left value, go up a level to the center value, then go to the right value. 

<div align = "center">

<img src = "https://upload.wikimedia.org/wikipedia/commons/4/48/Inorder-traversal.gif" width = 300 height = 200>

</div>

## Breadth-First Order
This is the most common method - it is also not the only one in the list that is not recursive. For this method, we must recognize the levels each nodes reside on. We will traverse from level 0 to level `n`. We will then get the values of each level from left to right (usually it goes from left to right, it is not required though). 


<div align = "center">

<img src = "https://miro.medium.com/v2/resize:fit:1400/0*HN6Tr71sgf1qR70n.gif" width = 300 height = 200>

</div>

## Tree Implementation

```python
class Node:
  def __init__(self, data, left = None, right = None): # left/right represents the children
    self.data = data

    self.left = left
    if left is not None:
      self.left.parent = self

    self.right = right
    if right is not None:
      self.right.parent = self

    self.parent = None
```

***

```python
class LinkedBinaryTree:
  class Node:
    def __init__(self, data, left = None, right = None): # left/right represents the children
      self.data = data
  
      self.left = left
      if left is not None:
        self.left.parent = self
  
      self.right = right
      if right is not None:
        self.right.parent = self
  
      self.parent = None

  def __init__(self, root = None):
    self.root = root
    self.size = self.count_nodes()

  def count_nodes(self):
    '''
    total nodes rooted at root = 1 + total left nodes + total right nodes (where recursion comes in)
    base case = root is None
    recursive element = split the left and right nodes and trust it will work
    '''

    def subtree_count(root):
      if root is None:
        return 0
      else:
        left_count = subtree_count(root.left) # gathers the count from the left
        right_count = subtree_count(root.right) # gathers the count from the right

        return 1 + left_count + right_count # adds 1 (because we must count the root too) with the left/right count

    return subtree_count(self.root)


  def sum(self):
    '''
    sum at root = root's value + sum at left + sum at right
    base case = root is None
    recursive element = split the left and right into nodes and trust it will work
    '''
    def subtree_sum(root):
      if root is None:
        return 0
      else:
        left_sum = subtree_sum(root.left) # gathers the left sums
        right_sum = subtree_sum(root.right) # gathers the right sums 

      return root.data + left_sum + right_sum # adds the root data with the data from the left/right sums

    return subtree_sum(self.root)
```
