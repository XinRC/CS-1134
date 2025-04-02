<div align = "center">

# Lecture 12
## Trees
  
</div>

Terms to note:
- **Parent**: the node above another node, can also be called the "root-node"
- **Child**: the node below another node
- **Siblings**: if the nodes have the same parent
- **Internal Nodes**: any nodes that is *not* the last node.
- **Leaf Nodes**: any end nodes.
- **Subtrees**: A smaller tree that is part of a bigger tree. It would have a different "root" than the ultimate "root-node". Technically, you can also consider leaf nodes as subtrees rooted at their specific numbers.
- **Edge** are the "lines" that connect each node, where `(u,v)` is an edge if `u` is the parent of `v`
- **Path** where it is simply just the path of a tree. where p = (v<sub>1</sub>, v<sub>2</sub>, ... v<sub>k</sub>) is a path where each 2 consecutive nodes form an edge
- **Length of Path** is the amount of edges in a path, where |p| = number of edges in p.
- **Ancestor** where in `(u,v)`, `u` is an ancestor of `v` if there is a path to `u` from `v`
- **Descendent** where in `(u,v)`, `v` has the ancestor of `u` if there is a path from `u` to `v`


Do note that at each "break" or "edge", there will be a new **level**. By increasing the level as we go down, the depth of the node will be the level of the node. The **height of the tree** is the length of the *longest* path in the tree. 

  
</br>

<div align = "center">

<img src = "https://www.w3schools.com/dsa/img_exercises_trees.png" width = 350 height = 300>
  
</div>

A full binary tree is only possible if the parents has *only* 0 or 2 children. A *complete* binary tree is when each parent has 2 children, aka when all levels have all possible node, meaning each parent *must* have 2 children. 

<div align = "center">

<img src = "https://ik.imagekit.io/upgrad1/abroad-images/imageCompo/images/unnamed_11_IWS24B.png?pr-true" width = 200 height = 150>

</div>
