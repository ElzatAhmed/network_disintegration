import networkd as nd


network = nd.Network()
network.add_node(nd.Node(0, pos=None, color='red'))
network.add_node(nd.Node(1, pos=None, color='green'))
network.add_node(nd.Node(2, pos=None, color='blue'))
network.add_edge(nd.Edge(0, 1))
network.add_edge(nd.Edge(0, 2))
killed = nd.dis_degree(network, 2)
for nid in killed:
    print(network.get_node(nid).__getattr__('color'))
