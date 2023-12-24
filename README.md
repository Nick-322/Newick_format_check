# Newick_format_check
Tool for checking the validity of a given Newick format

## Background info about dendrograms and Newick format
Dendrograms are a common way to visualize relationships among samples. They can be used whenever trying to visualize many pairwise comparisons. One major example of the use of dendrograms is phylogenetic tree, which is defined as a dendrogram that visualizes the phylogenetic relationship between organisms. 

A common format in which dendrograms are encoded is Newick format. Newick format is able to enocde all the core information you need to draw the encodeded dendrogram.

Newick has the following basic format to describe a dendrogram:
(A,B),C;


In a Newick tree representation, parentheses are used to enclose groups of taxa that share a common ancestor. For the sample basic format, it would look like the following in a dendrogram:

    A----\
         |----\
    B----/     |
               |
    C---------/

Branch lengths for each node could be encoded in our basic format as follows:

(A:8,B:5),C:4;


In this example, each node has a branch length which follows a ":" character.

## newick_check.py
In Newick format, parentheses pairing match is very important to accurately represent the hierarchical relationships of nodes within a phylogenetic tree. Missing the match leads to the misinterpretation of the relationships between nodes in a dendrogram.  
When writing a script to validate Newick format, therefore, you would need to check the correct pairings of parentheses as well as the other format rules. 

newick_check.py does a task of checking whether all the parentheses in a given Newick format are correctly paired.

Synopsis: 

    newick_check.py <test string>

The script should print "PAIRED" or "NOT PAIRED" to the terminal
