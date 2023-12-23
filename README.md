# Newick_format_check
Tool for checking the validity of a given Newick format file

Dendrograms are a common way to visualize relationships among samples. They can be used whenever
trying to visualize many pairwise comparisons and are commonly used in combination with heatmaps.
Today we will be working with a dendrogram that is used to show the evolutionary history
(phylogenetic relationships) of organisms.
When a dendrogram is used to visualize the phylogenetic relationship between organisms, it is referred
to as a phylogenetic tree. However, note that not all dendrograms are phylogenetic trees. Only those
that represent a hypothesis of phylogenetic relationships among organisms.
A common format in which dendrograms are encoded is Newick format. Newick format is simpler than
another dendrogram format, Nexus, which offers the ability to enocde more information about the
dendrogram. However, Newick format is able to enocde all the core information you need to draw the
encodeded dendrogram.
Newick format is described by one of its formulators here. I also describe it below.
Newick has the following core format to describe a dendrogram.

If you were to write a script to validate Newick format, you would need to check the correct pairings of
parentheses as well as the other format rules. This task is to write a script that checks whether parentheses are
paired.
Write a script that uses one or more functions to assess whether or not all parentheses in an input string are
paired.
As with question 1, the body of your script should only have a single line (except import sys) that is not
within a function. That line should be calling a function and passing command line input as arguments.

Synopsis: 

    <script name>.py <test string>
