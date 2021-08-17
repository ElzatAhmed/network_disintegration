def slcc(network):

    """
    slcc stands for the scale of the largest connected component
    a loop that contracts the lcc node each time
    till lcc value equals to 0
    a new temp network is created because slcc method could destroy the original network
    :param network: Network
    :return: existing node count, contraction library
    """

    from .lcc import lcc

    temp_network = clone_network(network)
    contraction = {}
    while True:
        lcc_node, lcc_value = lcc(temp_network)
        if lcc_value == 0:
            break
        con_nodes = node_contraction(temp_network, lcc_node.nid)
        contraction[lcc_node.nid] = con_nodes
    return len(network.get_living_node_ids()), contraction


def node_contraction(network, nid):

    """
    node_contraction: kill all the connected nodes and absorb their information
    :param network: Network
    :param nid: given node id
    :return: list of connected nodes
    """

    con_nodes = network.get_connected_nodes(nid)
    for n in con_nodes:
        network.kill_node(n)
    return con_nodes


def clone_network(network):

    """
    create a new identical network as the given network but with different objects
    :param network: sample network
    :return: cloned network
    """

    from networkd.classes.network import Network
    from networkd.classes.node import Node
    from networkd.classes.edge import Edge

    temp_nodes = []
    temp_edges = []
    for node in network.nodes:
        temp_node = Node(node.nid, node.pos)
        temp_node.__attr__ = node.__attr__
        temp_node.alive = node.alive
        temp_nodes.append(temp_node)
    for edge in network.edges:
        temp_edge = Edge(edge.nid0, edge.nid1)
        temp_edge.__attr__ = edge.__attr__
        temp_edge.alive = edge.alive
        temp_edges.append(temp_edge)
    clone = Network()
    clone.add_nodes_from(temp_nodes)
    clone.add_edges_from(temp_edges)
    return clone
