import random

import matplotlib
from networkd.visualization.func import *


def visualize_all_nx(
        network, pos=None, alive_node_color=(0, 1, 0), dead_node_color=(1, 0, 0),
        alive_edge_color=(0, 0, 1), dead_edge_color=(0, 0, 0), save_path=None
):
    """
    visualize the whole network using networkx as tool
    including the alive and dead nodes and edges
    :param network: Network
    :param pos: a dictionary of node ids with position tuples as values
    :param alive_node_color: color for painting the alive nodes, default=green
    :param dead_node_color: color for painting the dead nodes, default=red
    :param alive_edge_color: color for painting the alive edges, default=blue
    :param dead_edge_color: color for painting the dead edges, default=black
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
            node_color.append(alive_node_color)
        else:
            node_color.append(dead_node_color)
    for edge in network.edges:
        if edge.alive:
            edge_color.append(alive_edge_color)
        else:
            edge_color.append(dead_edge_color)
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
