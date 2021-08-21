def input_edges_txt(edge_src: str, attr_names: list, attr_delimiter=None):
    """
    read edge infos from given edge_src file as a txt file
    :param edge_src: path to the dataset file
    :param attr_names: a list of str of attribute names of edges included in the file
    :param attr_delimiter: a character for functions to split the lines
    :return: a list of edges
    """

    correct = _check_attr(attr_names)
    if not correct:
        print('please check you attr_names list!')
    src_file = open(edge_src, 'r', encoding='utf-8')
    lines = src_file.readlines()
    edge_details = []
    for line in lines:
        if line[0] == '#':
            continue
        line = line.strip()
        if attr_delimiter is None:
            infos = line.split()
        else:
            infos = line.split(attr_delimiter)
        edge_details.append(infos)
    return _construct_edges(edge_details, attr_names)


def _construct_edges(edge_details: list, attr_names: list):

    """

    :param edge_details: a list of node details as str
    :param attr_names: a list of str of attribute names of edges included in the file
    :return:
    """

    from networkd.classes.edge import Edge

    edges = []
    for detail in edge_details:
        attr = {}
        s = None
        t = None
        i = 0
        for name in attr_names:
            if s is None and _is_source(name):
                s = int(detail[i])
            elif t is None and _is_to(name):
                t = int(detail[i])
            else:
                attr[name] = detail[i]
            i += 1
        assert not(s is None or t is None)
        edge = Edge(s, t)
        edge.attr = attr
        edges.append(edge)
    return edges


source = ['source', 'nid0', 'id0', 'node_id0', 'n_id0']
to = ['to', 'nid1', 'id1', 'node_id1', 'n_id1']


def _check_attr(attr_names: list):

    """
    there must be a source id and a to id in the dataset
    :param attr_names:
    :return: boolean
    """

    source_check = False
    to_check = False
    for attr in attr_names:
        if _is_source(attr):
            source_check = True
        if _is_to(attr):
            to_check = True
    return source_check and to_check


def _is_source(attr: str):
    for s in source:
        if attr == s:
            return True
    return False


def _is_to(attr: str):
    for t in to:
        if attr == t:
            return True
    return False
