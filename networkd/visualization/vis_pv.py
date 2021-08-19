from networkd.visualization.func import *


def visualize_all_pv(
        network, pos=None, labels=None, save_path='vis_pv.html', alive_node_color='blue',
        dead_node_color='red', show_buttons=False
):
    """
    generate the whole network using pyvis as key tool
    there isn`t a different color to dead edges
    every edge around a dead node is dead
    :param network: Network
    :param pos: a dictionary with node ids and position tuples as values
    :param labels: labels for each node
    :param save_path: a path for output file
    :param alive_node_color: color for alive nodes
    :param dead_node_color: color for dead nodes
    :param show_buttons:
    :return:
    """

    from pyvis.network import Network as pyNet

    nodes = network.get_node_ids()
    edges = network.get_edge_tuples()
    vis_net = pyNet(height='700px', width='1500px', notebook=True, layout=False, directed=False)
    # generate positions and xs, ys
    if pos is None:
        pos = construct_pos_dict(network.nodes)
        if pos is None:
            pos = generate_random_pos(nodes)
    # generate labels
    if labels is None:
        labels = construct_label_dict(network.nodes)
        if labels is None:
            labels = {nid: nid for nid in nodes}
    # add nodes and edges
    for node in network.nodes:
        if node.alive:
            vis_net.add_node(n_id=node.nid, label=labels[node.nid],
                             color=alive_node_color, x=pos[node.nid][0], y=pos[node.nid][1])
        else:
            vis_net.add_node(n_id=node.nid, label=labels[node.nid],
                             color=dead_node_color, x=pos[node.nid][0], y=pos[node.nid][1])
    for edge in edges:
        vis_net.add_edge(source=edge[0], to=edge[1])
    # output
    if show_buttons:
        vis_net.width = 1000
        vis_net.show_buttons()
    vis_net.show(save_path)


def visualize_cur_pv(
        network, pos=None, labels=None, save_path='vis_pv.html', node_color='blue', show_buttons=False
):
    """
    visualize the current network using pyvis as key tool
    :param labels: labels for each node
    :param network: Network
    :param pos: a dictionary with node ids and position tuples as values
    :param save_path: a path for output file
    :param node_color: color of nodes, dictionary(nid: str) or str
    :param show_buttons:
    :return:
    """

    from pyvis.network import Network as pyNet

    nodes = network.get_living_node_ids()
    edges = network.get_living_edge_tuples()

    vis_net = pyNet(height='700px', width='1500px', notebook=True, layout=False, directed=False)
    # generate positions and xs, ys
    if pos is None:
        pos = construct_pos_dict(network.nodes)
        if pos is None:
            pos = generate_random_pos(nodes)
    # generate labels
    if labels is None:
        labels = construct_label_dict(network.nodes)
        if labels is None:
            labels = {nid: nid for nid in nodes}
    # generate node colors
    if node_color is not dict:
        colors = {}
        for nid in nodes:
            colors[nid] = node_color
        node_color = colors
    # add nodes and edges
    for nid in nodes:
        vis_net.add_node(n_id=nid, label=labels[nid], color=node_color[nid], x=pos[nid][0], y=pos[nid][1])
    for edge in edges:
        vis_net.add_edge(source=edge[0], to=edge[1])
    # output
    if show_buttons:
        vis_net.width = 1000
        vis_net.show_buttons()
    vis_net.show(save_path)
