import random


def generate_random_pos(nid_list):

    """
    generate random normalized position tuples
    :param nid_list: node id list
    :return: a dictionary with node ids and position tuples as values
    """

    pos = {}
    for nid in nid_list:
        x = random.random()
        y = random.random()
        pos[nid] = (x, y)
    return pos


def construct_pos_dict(nodes):

    """
    construct position dictionary from node attribute pos
    if only one of them is None, return None for whole
    :param nodes: node list
    :return: a dictionary with node ids and position tuples as values or None
    """

    pos = {}
    for node in nodes:
        if node.pos is None:
            return None
        pos[node.nid] = node.pos
    return pos


def construct_label_dict(nodes):

    """
    construct a label dictionary with the first attribute of each element
    :param nodes: node list
    :return: a dictionary with node ids and labels as values or None
    """

    labels = {}
    for node in nodes:
        if len(node.attr) == 0:
            return None
        for a in node.attr:
            label = node.attr[a]
            labels[node.nid] = label
            break
    return labels
