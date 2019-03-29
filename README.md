# Map2Positive
# Language: Python
# Input: CSV (negative and positive values)
# Output: EDA (with [-1, 1] range mapped to [0, 2]
# Tested with: PluMA 1.0, Python 3.6 

PluMA plugin to take a signed and weighted network (edges assumed to be in the range [-1, 1])
and convert it to an unsigned network with edges assumed to be in the range [0, 2].

The plugin accepts input as a CSV file with network nodes represented as both
rows and columns.  Entry (i, j) contains the weight of the edge from node i to node j.

It generates output in EDge Attribute (EDA) format, which can be imported into Cytoscape (tested with version 3.2.1).
The modified edge weights then become attributes of each edge, and can be used for further
downstream analysis or visualization.  With EDA format, the original edge weights are 
preserved and not overwritten, and thus can be used if desired.
