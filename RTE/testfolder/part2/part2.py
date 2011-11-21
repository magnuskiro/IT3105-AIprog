#!/usr/bin/env python
# -*- coding: utf-8 -*-

#*************************************************************************
#
#     This sample implementation is incomplete!
#     You need to implement the remaining parts yourself.
#
#*************************************************************************

"""
Sample implementation of tree edit distance algorithm from
Kaizhong Zhang & Dennis ShaSha,
"Simple fast algorithms for the editing distance beteen trees and related problems",
SIAM Journal on Computing, Vol. 18, No. 6, pp. 1245-1262, 1989.

This is a fairly literal translation of the algorithm described in the paper.
It can probably be improved in several ways, e.g., by avoiding recursion in
the preprocessing.
"""

# EM - 11/2011


class Node(list):
    """
    Simple recursive representation of a tree as a labeled node with zero or
    more child nodes
    """

    def __init__(self, label, *children):
        self.label = label
        list.__init__(self, children)

    def is_leaf(self):
        return not self

    def left_child(self):
        return self[0]

    def __str__(self):
        """
        string representation of tree as a labeled bracket structure
        """
        if self.is_leaf():
            return self.label
        else:
            return ( self.label +
                     "( " +
                     " ".join([str(child) for child in self]) +
                     ")" )

    def __repr__(self):
        return self.label


class ForestDist(dict):
    """
    ForestDist is a dictionary storing the distance between two forest.

    Keys are tuples of the form (forest1, forest2)

    forest1 is either a tuple (i1,j2) where
    i1 = start index of source forest1 and
    j1 = end index of source forest1,
    or None (i.e. empty forest)

    Likewise forest2 is eitehr a tuple (i2,j2) where
    i2 = start index of target forest2 and
    j2 = end index of target forest2,
    or None (i.e. empty forest).

    Values are distances >= 0.

    By definition,
    ForestDist(None,None) = 0 and
    forest (i,j) = None when i>j.
    """

    def __init__(self,*args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        # forestdist(Ã˜,Ã˜) = 0
        # (cf. Zhang & Shasha:p.1253)
        self[None,None] = 0

    def __getitem__(self, (forest1, forest2)):
        # If i>j, then T[i..j] = 0
        # (cf. Zhang & Shasha:p.1249)
        if forest1 is not None:
            i1, j1 = forest1
            if i1 > j1:
                forest1 = None

        if forest2 is not None:
            i2, j2 = forest2
            if i2 > j2:
                forest2 = None

        return dict.__getitem__(self, (forest1, forest2))



def unit_costs(node1, node2):
    """
    Defines unit cost for edit operation on pair of nodes,
    i.e. cost of insertion, deletion, substitution are all 1
    """
    # insertion cost
    if node1 is None:
        return 1

    # deletion cost
    if node2 is None:
        return 1

    # substitution cost
    if node1.label != node2.label:
        return 1
    else:
        return 0


def postorder(root_node):
    """
    Return a list of nodes resulting from a left-to-right postorder traversal
    of the tree rooted in root_node
    """
    # Cf.  Zhang & Shasha:p.1249:
    # "Let T[I] be the ith node in the tree according to the left-to-right
    # postordering"

    raise NotImplementedError()
    # TODO: 
    #*************************************************************************
    #
    #     Your implementation goes here
    #
    #*************************************************************************

    #Observations: The postorder number of a node is larger than
        #the postorder numbers of all its descendants
        #the postorder numbers of all its left siblings

def leftmost_leaf_descendant_indices(node_list):
    """
    Return a list of the *indices* of the leftmost leaf descendants according
    to a list of post-ordered nodes
    """
    # Cf.  Zhang & Shasha:p.1249:
    # "l(i) is the number of the leftmost leaf descendant of the subtree
    # rooted at T[i]. When T[i] is a leaft, l(i)=i."

    raise NotImplementedError()
    # TODO:
    #*************************************************************************
    #
    #    Your implementation goes here
    #
    #*************************************************************************
""" lmld(v, l), v = root node of a tree t. l= ampty array.
foreach child c of v (left to right) do l ← lmld(c, l );
if v is a leaf then
    l [id(v)] ← id(v)
else
    c1 ← first child of v;
    l [id(v)] ← l [id(c1)];
return l;
""" #outputs the array l, l[i] is the left-most leaf descendant of node t[i]


def key_root_indices(lld_indices):
    """
    Return a list of the *indices* of the key roots from a list of the indices
    of the leftmost leaf descendants
    """
    # Cf. Zhang & Shasha:p.1251: "LR_keyroots(T) = {k| there exists no k'>k
    # such that l(k)=l(k')}

    raise NotImplementedError()
    # TODO: 
    #*************************************************************************
    #
    #    Your implementation goes here
    #
    #*************************************************************************
""" kr(l , lc)

input:
l[1..|T|]: l [i ] is the left-most leaf descendent of node T[i ]
lc = |leaves(T)| is the number of leaves in T

code:
kr [1..lc]: empty array;
visited[ ]: boolean array of size |l |, init with false;
k ← |kr |; i ← |l |;
while k ≥ 1 do
    if not visited[l [i ]] then
        kr [k- -] ← i ;
        visited[l [i ]] ← true;
    i - -;
return sort(kr );
""" # output: array kr [1..|leaves(T)|] with key roots sorted by node ID


def distance(t1, t2, costs=unit_costs):
    """
    Compute edit distance between tree t1 and tree t2
    Unit costs are used if no explicit costs are provided.
    """
    # Cf. Zhang & Shasha:p.1252-1253

    # Use an embedded function, so T1,T2, l1,l2, and TD are available from the
    # name space of the outer function and don't need to be dragged around in
    # each function call
    def edit_dist(i, j):
        """
        compute edit distance between two subtrees rooted in nodes i and j
        respectively
        """
        # temporary array for forest distances
        FD = ForestDist()

        for n in range(l1[i], i+1):
            FD[ (l1[i],n), None ] = ( FD[ (l1[i],n-1), None ] +
                                      costs(T1[n], None) )

        for m in range(l2[j], j+1):
            FD[ None, (l2[j],m) ] = ( FD[ None, (l2[j],m-1) ] +
                                      costs(None, T2[m].label) )

        raise NotImplementedError()
        # TODO:
        #*************************************************************************
        #
        #    Your implementation of the final part of edit_dist goes here
        #
        #*************************************************************************
""" tree-edit-distance(t1,t2)
        td[1..|T1|, 1..|T2|] : empty array for tree distances;
        l1 = lmld(root(T1)); kr1 = kr(l1, |leaves(T1)|);
        l2 = lmld(root(T2)); kr2 = kr(l2, |leaves(T2)|);
        for x = 1 to |kr1| do
        for y = 1 to |kr2| do
        forest-dist(kr1[x], kr2[y], l1, l2, td);
"""

""" forest-dist(i , j , l1, l2, td)
fd[l1[i ] − 1..i , l2[j ] − 1..j ] : empty array;
fd[l1[i ] − 1, l2[j ] − 1] = 0;
for di = l1[i ] to i do fd[di , l2[j ] − 1] = fd[di − 1, l2[j ] − 1] + !del ;
for dj = l2[j ] to j do fd[l1[i ] − 1, dj ] = fd[l1[i ] − 1, dj − 1] + !ins ;
for di = l1[i ] to i do
    for dj = l2[j ] to j do
        if l [di ] = l [i ] and l [dj ] = l [j ] then
            fd[di , dj ] = min(fd[di − 1, dj ] + !del, fd[di , dj − 1] + !ins, fd[di − 1, dj − 1] + !ren);
            td[di , dj ] = f [di , dj ];
        else fd[di , dj ] = min(fd[di − 1, dj ] + !del ,
            fd[di , dj − 1] + !ins, fd[l [di ] − 1, l [dj ] − 1] + td[di , dj ]);
Nikolaus
"""
        return TD[i,j]


    # Compute T1[] and T2[]
    T1 = postorder(t1)
    T2 = postorder(t2)

    # Compute l()
    l1 = leftmost_leaf_descendant_indices(T1)
    l2 = leftmost_leaf_descendant_indices(T2)

    # LR_keyroots1 and LR_keyroots2
    kr1 = key_root_indices(l1)
    kr2 = key_root_indices(l2)

    # permanent treedist array
    TD = dict()

    for i in kr1:
        for j in kr2:
            edit_dist(i, j)

    print_matrix(T1, T2, TD)

    return TD[i,j]



def print_matrix(T1, T2, TD):
    print "   " + "".join([("%-3s" % n.label) for n in T2])
    for i in range(len(T1)):
        print "%-2s" % T1[i].label,
        for j in range(len(T2)):
            print "%-2s" % TD[i,j],
        print
    print



if __name__ is "__main__":
    # Cf. Zhang & Shasha: Fig. 4 and Fig. 8

    t1 = Node("f",
             Node("d",
                  Node("a"),
                  Node("c",
                       Node("b"))),
             Node("e"))



    t2 = Node("f",
              Node("c",
                   Node("d",
                        Node("a"),
                        Node("b"))),
              Node("e"))

    print "t1 =", t1
    print "t2 =", t2
    print

    d = distance(t1, t2)
    print "distance =", d

