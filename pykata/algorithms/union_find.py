"""
Module demonstrates algorithm for solving dynamic connectivity problem.
Two algorithms are demonstrated:
    - quick find
    - quick union

Quick find: all objects store id of a component they all belong to.
    Find operation: check if component id of one object is equal to id of another object.
    Union operation: set id of component p to id of component q.

Quick union: all objects contain link to parent component. Root component point to itself.
    Find operation: check if roots for objects are equal.
    Union operation: set parent for root of component p to root of component q.

Improvements:
    1. Weighting. Keep track of tree size in quick union algorithm. Always connect smaller tree to larger tree.
    2. Path compression. Keep link to root from all nodes on the path.

"""
