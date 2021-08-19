import random

import matplotlib


def visualize_all_nx(
        network, pos=None, color_alive_nodes=(0, 1, 0), color_dead_nodes=(1, 0, 0),
        color_alive_edges=(0, 0, 1), color_dead_edges=(0, 0, 0), save_path=None
):
    """
    visualize the whole network using networkx as tool
    including the alive and dead nodes and edges
    :param network: Network
    :param pos: a dictionary of node ids with position tuples as values
    :param color_alive_nodes: color for painting the alive nodes, default=green
    :param color_dead_nodes: color for painting the dead nodes, default=red
    :param color_alive_edges: color for painting the alive edges, default=blue
    :param color_dead_edges: color for painting the dead edges, default=black
    :param save_path: a file path for output file, default=None
    :return:
    """

    import networkx as nx
    import matplotlib.pyplot as plt

    network.construct_nx_graph_whole()
    node_color = []
    edge_color = []
    for node in network.nodes:
        if node.alive:
            node_color.append(color_alive_nodes)
        else:
            node_color.append(color_dead_nodes)
    for edge in network.edges:
        if edge.alive:
            edge_color.append(color_alive_edges)
        else:
            edge_color.append(color_dead_edges)
    if pos is None:
        pos = construct_pos_dict(network.nodes)
        if pos is None:
            pos = generate_random_pos(network.get_node_ids())
    f = plt.figure()
    nx.draw_networkx_nodes(G=network.graph, pos=pos, nodelist=None, node_size=5, node_color=node_color)
    nx.draw_networkx_edges(G=network.graph, pos=pos, edgelist=None, width=0.5, edge_color=edge_color)

    if save_path is None:
        plt.show()
    else:
        matplotlib.use("Agg")
        f.savefig(save_path)


def visualize_cur_nx(
        network, pos=None, node_color=(0, 1, 0), edge_color=(0, 0, 1), save_path=None
):
    """
    visualize the current network using networkx as tool
    only the alive nodes and edges
    :param network: Network
    :param pos: a dictionary of node ids with position tuples as values
    :param node_color: color for nodes, default=green
    :param edge_color: color for edges, default=blue
    :param save_path: a file path for output file, default=None
    :return:
    """

    import networkx as nx
    import matplotlib.pyplot as plt

    network.construct_nx_graph_living()
    nodes = network.get_living_node_ids()
    edges = network.get_living_edge_tuples()
    if pos is None:
        pos = construct_pos_dict(network.nodes)
        if pos is None:
            pos = generate_random_pos(network.get_node_ids())
    f = plt.figure()
    nx.draw_networkx_nodes(G=network.graph, pos=pos, nodelist=nodes, node_size=5, node_color=node_color)
    nx.draw_networkx_edges(G=network.graph, pos=pos, edgelist=edges, width=0.5, edge_color=edge_color)
    if save_path is None:
        plt.show()
    else:
        matplotlib.use("Agg")
        f.savefig(save_path)


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
