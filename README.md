===============
Newick Parser
===============

Prerequisites:

- Python 3.7 (https://www.python.org/downloads/). Not compatible with Python 1 or 2.  
- We did not test on Python releases prior to 3.7 and cannot vouch for proper functioning on those versions.

Instructions:

- The program can only read trees in Newick format from files that contain a single tree.  
- This program might not work for certain variations of the Newick format or if the tree consists of only a single leaf.  

Functionality:

- The program reads a tree in Newick format from a file and reconstructs the corresponding tree structure.
- If the file is missing or incorrectly formatted, an error message will be displayed.
