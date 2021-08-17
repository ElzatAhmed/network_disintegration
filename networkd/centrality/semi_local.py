def semi_local_centrality(network):

    """
    only operate on living nodes
    operation uses adjacency matrix as the key tool
    semi local centrality of each node equals to the count of the secondary neighbors of the node
    :param network:
    :return: a dictionary with node ids and corresponding semi local centrality,
            a list of node ids in descending order on its semi local centrality
    """

    nodes = network.get_living_node_ids()
    matrix_size = network.construct_adj_matrix()
    centrality = {}
    for nid in nodes:
        neighbors = secondary_neighbors(nid, network.adj_matrix, matrix_size)
        centrality[nid] = len(neighbors)
    nodes.sort(key=lambda o: centrality[o], reverse=True)
    return centrality, nodes


def secondary_neighbors(nid, adj_matrix, size):

    """
    return a list containing the ids of the secondary neighbors of the given node
    :param nid: given node if
    :param adj_matrix: adjacency matrix of the network
    :param size: the size of the adjacency matrix
    :return:
    """

    secondary = set()
    direct = direct_neighbors(nid, adj_matrix, size)
    for d in direct:
        s = direct_neighbors(d, adj_matrix, size)
        for n in s:
            secondary.add(n)
    return list(secondary)


def direct_neighbors(nid, adj_matrix, size):

    """
    return a list containing the ids of the direct neighbor nodes of the given node
    :param nid: given node id
    :param adj_matrix: adjacency matrix of the network
    :param size: the one dimensional size of the network
    :return:
    """

    neighbors = []
    for i in range(0, size):
        if i == nid:
            continue
        if adj_matrix[i][nid] == 1:
            neighbors.append(i)
    return neighbors
