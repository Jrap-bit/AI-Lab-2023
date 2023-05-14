import networkx as nx
import matplotlib.pyplot as plt

# Define the entities as nodes
entities = {"Midas", "Daughter", "Greek King", "Rich", "Lesson", "Home", "Wish", "Angel", "Help", "Gold", "Rocks",
            "Plants", "Touch Turns To Gold", "Angel", "Excited", "Devastated"}

# Define the edges with relation labels as tuples
edges = [('Midas', 'Greek King', 'was-0'),

         ('Midas', 'Gold', 'had-1'),
         ('Midas', 'Rich', 'was-1'),
         ('Midas', 'Daughter', 'loved-1'),
         ('Midas', 'Daughter', 'had-1'),

         ('Midas', 'Angel', 'found-2'),
         ('Angel', 'Help', 'needed-3'),
         ('Midas', 'Angel', 'helped-4'),
         ('Angel', 'Wish', 'granted-5'),

         ('Midas', 'Touch Turns To Gold', 'wished-6'),

         ('Midas', 'Rocks', 'touched-7'),
         ('Midas', 'Plants', 'touched-7'),
         ('Rocks', 'Gold', 'turned-8'),
         ('Plants', 'Gold', 'turned-8'),

         ('Midas', 'Home', 'reached-9'),
         ('Midas', 'Excited', 'was-10'),
         ('Midas', 'Daughter', 'hugged-11'),
         ('Daughter', 'Gold', 'turned into-12'),

         ('Midas', 'Devastated', 'was-13'),
         ('Midas', 'Lesson', 'learned-14'),

         ('Angel', 'Wish', 'Takes Away-15')]

# Create the graph and add nodes and edges
G = nx.DiGraph()
labels = {}
G.add_nodes_from(entities)
for start_node, end_node, label in edges:
    if (start_node, end_node) not in labels:
        labels[(start_node, end_node)] = label
    else:
        labels[(start_node, end_node)] += ", " + label

    G.add_edge(start_node, end_node, label=labels[(start_node, end_node)])

# Visualize the graph
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=11)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['label'] for u, v, d in G.edges(data=True)}, font_size=8)
# plt.show()

Entity1 = "Midas"
Entity2 = "Daughter"
Action = "hugged"

for i in labels:
    if (Entity1, Entity2) in labels:
        act_list = []
        time = []
        new_arr = labels[(Entity1, Entity2)].split(",")
        for i in new_arr:
            act_list.append(i.strip().split("-")[0])
            time.append(i.strip().split("-")[1])
        if Action in act_list:
            print("{} {} {} at time {}".format(Entity1, Action, Entity2, time[act_list.index(Action)]))
    else:
        print("No relation between {} and {}".format(Entity1, Entity2))
