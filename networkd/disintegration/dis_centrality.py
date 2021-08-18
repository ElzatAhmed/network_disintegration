from .disintegrate import disintegrate


def dis_degree(network, cost: int):

    """
    disintegrate the given network using degree centrality
    :param network: Network
    :param cost: the count of killable nodes
    :return: a list containing the ids of killed nodes
    """

    from networkd.centrality.degree import degree_centrality

    centrality, nodes = degree_centrality(network)
    return disintegrate(network, nodes, cost)


def dis_semi_local(network, cost: int):

    """
        disintegrate the given network using semi local centrality
        :param network: Network
        :param cost: the count of killable nodes
        :return: a list containing the ids of killed nodes
    """

    from networkd.centrality.semi_local import semi_local_centrality
    centrality, nodes = semi_local_centrality(network)
    return disintegrate(network, nodes, cost)


def dis_betweenness(network, cost: int):

    """
        disintegrate the given network using betweenness centrality
        :param network: Network
        :param cost: the count of killable nodes
        :return: a list containing the ids of killed nodes
    """

    from networkd.centrality.betweenness import betweenness_centrality
    centrality, nodes = betweenness_centrality(network)
    return disintegrate(network, nodes, cost)


def dis_region(network, cost: int, radius=0.05, dr=0.1, center=(0, 0)):

    """
    repeatedly recalculate the region centrality of the current network
    each time get the region with maximum degree centrality,
    kill all of its containing nodes,
    and record its center point,
    finally return a list of center points and
    a list of killed node ids
    :param network: Network
    :param cost: the count of killable nodes
    :param radius: radius of the region
    :param dr: the various of the region center position
    :param center: the initial center
    :return: a list of selected center points,
            a list of killed node ids
    """

    from networkd.centrality.region import region_centrality

    centers = []
    killed = []
    while cost:
        centrality, contains, regions = region_centrality(network, radius, dr, center)
        max_region = regions[0]
        if centrality[max_region] == 0:
            break
        centers.append(max_region.center)
        for nid in contains[max_region]:
            network.kill_node(nid)
            killed.append(nid)
        cost -= 1
    return centers, killed

