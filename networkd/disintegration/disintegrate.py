def disintegrate(network, nid_list, cost):

    """
    disintegrate network by the given rule
    :param network: Network
    :param nid_list: sorted node id list
    :param cost: the count of killable nodes
    :return: a list containing the ids of killed nodes
    """

    killed = []
    i = 0
    for nid in nid_list:
        if i == cost:
            break
        network.kill_node(nid)
        killed.append(nid)
        i += 1
    return killed
