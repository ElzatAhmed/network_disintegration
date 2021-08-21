def output_edges_txt(edges: list, output_path='edges.txt'):

    """
    output edge specifics to a txt file
    :param edges: list of edges
    :param output_path: the output path for the data
    :return:
    """

    edge_details = _construct_details(edges)
    out_file = open(output_path, mode='w', encoding='utf-8')
    for details in  edge_details:
        out_file.write(details + '\n')
    out_file.close()


def _construct_details(edges: list):

    """
    construct edge details for edge output
    :param edges: list of edges
    :return:
    """

    edge_details = []
    for edge in edges:
        details = f'{edge.nid0} {edge.nid1}'
        for name in edge.attr:
            details += f' {edge.attr[name]}'
        edge_details.append(details)
    return edge_details
