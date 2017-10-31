import networkx as nx
#import matplotlib.pyplot as plt


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

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
        inviter = remove_prefix(p[1], 'Invited by ')
    else:
        inviter = 'Chris Varenhorst'
    if name not in ['Chris Varenhorst', 'Yan XZ', 'Rachel Fong','Doppel Ganger','Michael Borel']:
        G.add_node(inviter)
        G.add_edge(inviter, name)
        

#print(G.nodes)
#print(G.edges)
#nx.draw_networkx_labels(G, pos=nx.spring_layout(G))
#plt.show()
for x in range(1,500):
    lpath = nx.dag_longest_path(G)
    print(' --> '.join(lpath))
    G.remove_node(lpath[-1])
