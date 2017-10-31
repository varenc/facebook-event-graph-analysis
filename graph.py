import networkx as nx
#import matplotlib.pyplot as plt

G = nx.DiGraph()

# I pre-processed this event data manually with some regexes
with open('event_dump') as f:
    data = ''.join(f.readlines())

people = data.split("\n======\n")
for p in people:
    p = p.split("\n")
    name = p[0]
    if name in ["\t",""]:
        print("ERROR",p)
    G.add_node(name)
    if len(p) == 2:
        inviter = p[1].lstrip("Invited by")
    elif name != 'Chris Varenhorst':
        inviter = 'Chris Varenhorst'
    G.add_node(inviter)
    G.add_edge(inviter, name)
        

#print(G.nodes)
#print(G.edges)
#nx.draw_networkx_labels(G, pos=nx.spring_layout(G))
#plt.show()
lpath = nx.dag_longest_path(G)
print('Longest invite path:', ' --> '.join(lpath))
    
