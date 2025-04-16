<div align = "center">

# Lecture 14
## Binary Search Tree

</div>

## Formal Definition:
If you want `T` to be a binary search tree (BST), `T` would only be a BST if for each node (`n`):

- All keys stored on the left subtree is **less** than the value in the root `n`
- All keys stored on the right subtree is **greater** than the value in the root `n`

<div align = "center">

<img src = "https://blog.boot.dev/img/800/binary-search-tree.png.webp" width = 300 height = 200>

<sub>(The left side is always smaller than the node itself, and the right side is always greater than the node itself. )</sub>

</br>

</div>


```python
# given that we already have the BinarySearchTree class implemented
bst = BinarySearchTree()
lst = \[14, 18, 22, 24]

  for num in lst:
    bst.insert(num)

'''
(14)
  \
  (18)
    \
    (22)
      \
      (24)

Traversing would cost θ(h) where `h` represents the height of the tree. Can also be denoted as θ(n) but preferably denoted as θ(h).
In this case, the height would be 3, because there are 3 levels: [0 -> 1 -> 2 -> 3]
'''

```

<div align = "center">
  
## Operations
</div>

| Operation Name | Definition | Runtime | 
| :--- | :--- | :--- |
| Lookup | Must have a `current` that traverse the BST and starts at the root-root. Depending on if the target value is less than or greater than the current node, we will either recurse to the left or right. This will eventually give us the target value, or it means the target value does not exist. This is pretty much "binary search" | **Best case:** Ω(1) if `root.data == target_value` </br></br> **Average Case:** θ(h) for skewed cases or θ(log(n)) for balanced trees. </br></br> **Worse Case:** O(h) for skewed trees. 
| Insertion | There are 3 types: [Rebalancing, Skewed, and "Simply inserting" (being the easiest to implement, also the one we will discuss). </br></br>  Given our current node (`n`), and the new node (`v`), if the tree is empty, `v` would become the root. Otherwise, if `v` < `n`, we will recurse into the left child (until there is no left child to which `v` becomes the left child. If `v` > `n`, we will recurse into the right child (until there is no right child to which `v` becomes the right child). | **Best case:** Ω(1) when BST is empty or Ω(log(n)) </br></br> **Average Case:** θ(log(n)) for balanced trees, but generally θ(h) </br></br> **Worse Case:** O(h) for skewed trees. |
| Duplications | If `v == node.data`, then we must ignore. BSTs dont allow duplicates. | θ(1) |
| Deletion | There are 3 types: [] | | 



**Deletion**
- balancing
- skewed
- still rebalancing but less heavy. (may keep the left side complete but modify the right side) (root be switched to the smallest value on the right side)

  1. search for the node we want to delete
  2. no child: disconnect target, 1 child promoted to the target node, 2 child where we will look for the inorder successor (smallest in the left subtree) 
  3. replace target's value with successors then recursively delete
 
  generally Ω/θ = logn, O(h)
