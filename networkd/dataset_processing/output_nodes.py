def output_nodes_txt(nodes: list, output_path='nodes.txt'):

    """
    output node specifics to a txt file
    :param nodes: list of nodes
    :param output_path: the output path for the data
    :return:
    """

    node_details = _construct_details(nodes)
    out_file = open(output_path, mode='w', encoding='utf-8')
    for details in node_details:
        out_file.write(details + '\n')
    out_file.close()


def _construct_details(nodes: list):

    """
    construct node details for node output
    :param nodes: list of nodes
    :return: a list containing details for each node
    """

    node_details = []
    for node in nodes:
        detail = f'{node.nid}'
        if node.pos is not None:
            detail += f' {node.pos[0]} {node.pos[1]}'
        for name in node.attr:
            detail += f' {node.attr[name]}'
        node_details.append(detail)
    return node_details
