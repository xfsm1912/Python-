import objgraph
from graphviz import Source
# render('d')

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

objgraph.show_refs([a], filename='sample-graph.png')
# objgraph.show_backrefs([a])
