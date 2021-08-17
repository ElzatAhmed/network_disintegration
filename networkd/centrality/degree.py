def degree_centrality(network):

    """
    only operate on living nodes
    operation uses adjacency matrix as the key tool
    :param network: Network
    :return: a dictionary with node ids and corresponding degree centrality(normalized),
            a list of node ids in descending order on its degree centrality
    """

    nodes = network.get_living_node_ids()
    matrix_size = network.construct_adj_matrix()
    n = len(nodes)
    centrality = {}
    if n - 1 <= 0:
        centrality = {nid: 0 for nid in nodes}
    else:
        for nid in nodes:
            centrality[nid] = _degree_(nid, network.adj_matrix, matrix_size) / (n - 1.0)
    nodes.sort(key=lambda o: centrality[o], reverse=True)
    return centrality, nodes


def _degree_(nid, adj_matrix, size):
    degree = 0
    for i in range(0, size):
        if i == nid:
            continue
        if adj_matrix[i][nid] == 1:
            degree += 1
    return degree
