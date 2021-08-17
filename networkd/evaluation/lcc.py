def lcc(network):

    """
    lcc stands for largest connected component
    means the node with the biggest degree centrality
    so we can just use the degree centrality algorithm
    :param network: Network
    :return: the node with lcc value, the lcc value
    """

    from networkd.centrality.degree import degree_centrality

    centrality, nodes = degree_centrality(network)
    lcc_node = network.get_node(nodes[0])
    lcc_value = centrality[nodes[0]]
    return lcc_node, lcc_value
