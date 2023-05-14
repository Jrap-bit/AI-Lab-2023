import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, loc, dom):
        self.loc = loc
        self.dom = dom
        self.org_dom = dom.copy()
        self.val = None
        self.adj_list = []

    def __str__(self):
        return f"{self.loc}: {self.val}"

    def add_nod(self, node):
        self.adj_list.append(node)

    def rem_dom_val(self, val):
        if val in self.dom:
            self.dom.remove(val)

    def reset_domain(self):
        self.dom = self.org_dom.copy()


def const_sat(node, val):
    for i in node.adj_list:
        if i.val == val:
            return False
    return True


def red_dom(node):
    for i in node.adj_list:
        if i.val is not None:
            node.rem_dom_val(i.val)
        i.dom = [val for val in i.dom if const_sat(i, val)]


def backtracking(node):
    global vis_nod
    vis_nod += 1
    if node is None:
        return True
    for val in node.dom:
        node.val = val
        red_dom(node)
        print("The Domain for {} is: {}".format(node, node.dom))
        if not node.dom:
            node.reset_domain()
            node.val = None
            continue
        assign_all = True
        for i in node.adj_list:
            if i.val is None:
                assign_all = False
                break
        if assign_all:
            node.reset_domain()
            return True
        if backtracking(next((n for n in node.adj_list if n.val is None), None)):
            node.reset_domain()
            return True
        node.reset_domain()
        node.val = None
    return False


def main():
    backtracking(WA)
    print("\nThe Nodes With Their Respective Colors Are: ")
    for node in [WA, NT, Q, NSW, V, SA]:
        print(node)
    print("\nNumber of nodes visited: {}".format(vis_nod))
    G = nx.Graph()
    nodes = [WA, NT, Q, NSW, V, SA]
    for node in nodes:
        G.add_node(node.loc)
    for node in nodes:
        for x in node.adj_list:
            G.add_edge(node.loc, x.loc)
    color_map = {'P': 'purple', 'G': 'green', 'Y': 'yellow'}
    colors = [color_map[node.val] if node.val is not None else 'gray' for node in nodes]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=colors, font_color='white', font_size=8, font_weight='bold')
    plt.show()


if __name__ == "__main__":
    dom = ['P', 'G', 'Y']
    vars = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA']
    for i in vars:
        globals()[i] = Node(i, dom)

    for i in vars:
        if i == 'WA':
            WA.add_nod(NT)
            WA.add_nod(SA)
        elif i == 'NT':
            NT.add_nod(WA)
            NT.add_nod(Q)
        elif i == 'Q':
            Q.add_nod(NT)
            Q.add_nod(NSW)
            Q.add_nod(SA)
        elif i == 'NSW':
            NSW.add_nod(SA)
            NSW.add_nod(Q)
            NSW.add_nod(V)
        elif i == 'SA':
            SA.add_nod(WA)
            SA.add_nod(NT)
            SA.add_nod(Q)
            SA.add_nod(NSW)
            SA.add_nod(V)
        elif i == 'V':
            V.add_nod(SA)
            V.add_nod(NSW)

    vis_nod = 0
    main()
