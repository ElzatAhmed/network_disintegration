def betweenness_centrality(network):

    """
    only operate on living nodes
    operation uses networkx.betweenness_centrality method as key tool
    :param network: Network
    :return: a dictionary with node ids and corresponding betweenness centrality(normalized),
            a list of node ids in descending order on its betweenness centrality
    """

    import networkx as nx

    network.construct_nx_graph_living()
    nodes = network.get_living_node_ids()
    centrality = nx.betweenness_centrality(G=network.graph)
    nodes.sort(key=lambda o: centrality[o], reverse=True)
    return centrality, nodes
