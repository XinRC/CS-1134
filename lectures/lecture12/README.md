<div align = "center">

# Lecture 12
## Trees
  
</div>

## Terms and Definitions
<div align = "center"> 
  
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

</div>

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
from ArrayQueue import ArrayQueue

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

    def __iter__(self):
      for node in self.breadth_first():
        yield node.data

    def __len__(self):
      return self.size

  def is_empty(self):
    return if len(self) == 0


  #PREORDER
  def preorder(self):
  ''' must require inner function | preorder is center -> left -> right '''
    def subtree_preorder(root):
    if root == None:
      pass
    else:
      #current/root/center
      yield root
  
      #left
      yield from subtree(root.left)
  
      #right
      yield from subtree(root.right)
    yield from subtree_preorder(self.root)


  # POSTORDER
  def postorder(self):
    ''' postorder is left -> right -> center(root/current) '''
    def subtree_postorder(root):
      if root == None:
        pass
      else:

        #left
        yield subtree_postorder(root.left)

        #right
        yield subtree_postorder(root.right)

        #current/root/center
        yield root
    yield from subtree_postorder(self.root)


  # INORDER
  def inorder(self):
    '''inorder is left -> center -> right'''
    def subtree_inorder(root);
      if root == None:
        pass
      else:

        #left
        yield subtree_inorder(root.left)

        #current/root/center
        yield root

        #right
        yield subtree_inorder(root.right)
  yield subtree_inorder(self.root)


  def breadth_first(self):
    if self.is_empty():
      return

    #must utilize a queue (to enqueue/dequeue) while not empty
    bfs_queue = ArrayQueue()
    bfs_queue.enqueue(self.root)

    while not bfs_queue.is_empty():
      curr_node = bsf_queue.dequeue()

      yield curr_node

      if curr_node.left is not None:
        bfs_queue.enqueue(curr_node.left)
      if curr_node.right is not None:
        bfs_queue.enqueue(curr_node.right)
      ''' this code dequeues the parent, and if the parent has children, then it will enqueue the children in their spot '''

    # height of the tree
    def height(self):
      # compares the height of the left / right
      def subtree_height(root):
        if root.left is None and root.right is None:
          return 0 # because the root is at level 0
        elif root.right is None:
          left_height = subtree_height(root.left)
          return left_height + 1
        elif root.left is None:
          right_height = subtree_height(root.right)
          return right_height + 1
        else:
          ''' for this case, we must compare left_height and right_height and use the MAX ''' 
          left_height = subtree_height(root.left)
          right_height = subtree_height(root.right)

          return max(left_height, right_height) + 1

    if self.isempty():
      raise Exception("Tree is empty")



    return subtree_height(self.root)

'''
Build and evaluate an expression that looks like (3 + 4) * 5 -> (in prefix)
Root (*): Indicate multiplication betwene two subtrees where we must build an expression that ooks like (3 + 4) * 5
Left: (Rooted at +): Indicate an addition between two subtrees
Right: (Rooted at 5): Indicate the value 5 (bc it doesn't have children and is not an operator)
'''

tree = LinkedBinaryTree()

# Create operand nodes and assigning them their value
n3 = LinkedBinaryTree.Node(3)
n4 = LinkedBinaryTree.Node(4)
n5 = LinkedBinaryTree.Node(5)

# for the operator we must have a left and right node because we are combining n3 and n4
plus = LinkedBinaryTree.Node(data = "+", left = n3, right = n4) 
times = LinkedBinaryTree.Node(data = "*", left = plus, right = n5)

# assign the root
tree = LinkedBinaryTree(root = times)

def eval_exp_tree(expression_tree: LinkedBinaryTree): #should return a float
  def subtree_eval(root: LinkedBinaryTree.Node):
    # Base Case -> if this node is a leaf, return its data
    if root.left == None and root.right == None:
      return root.data

    # Recursive Case -> evaluate the children first
    left_value = subtree_eval(root = root.left)
    right_value = subtree_eval(root = root.right)

    # Apply operator at current node

    if root.data == "+":
      return left_value + rightvalue
    elif root.data == "-":
      return left_value - right_value
    elif root.data == "*":
      return left_value * right_value
    elif root.data == "/":
      if right_value == 0:
        raise ZeroDivisionError
      else:
        return left_value / right_value
    else:
      raise ValueError(f"Unknown operator {root.data}") #When it is not an operator

  if tree.root is None:
    raise Exception("Cannot evaluate an empty tree")

  return subtree_eval(tree.root)

#Evaluating
result = eval_exp_tree(tree
print(tree)
    
```

## \[EXTRA] Generating from other generators
This technique was used in the previous code. This is an explaination on how it works

```python
def gen_yield():
  yield 1
  yield 2
  yield 3

def gen_2():
  yield 0

  # how would we yield the numbers from the function gen_yield()? The following would technically work but it looks bulky
  '''
  for value in gen_vield():
    yield value
  '''

  # a one-line solution for the above situation
  yield from gen_one()

  yield 4
  yield 5

# 1 2 3 4 5 (space represents a new line)
```
