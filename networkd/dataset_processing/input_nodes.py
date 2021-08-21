def input_nodes_txt(node_src: str, attr_names: list, attr_delimiter=None):
    """
    read node infos from given node_src file as a txt file
    :param node_src: path to the data_set file
    :param attr_delimiter: a character for functions to split the lines
    :param attr_names: a list of str of attribute names of nodes included in the file
    :return: a list of nodes
    """

    correct = _check_attr(attr_names)
    if not correct:
        print('please check you attr_names list')
    src_file = open(node_src, 'r', encoding='utf-8')
    lines = src_file.readlines()
    node_details = []
    for line in lines:
        if line[0] == '#':
            continue
        line = line.strip()
        if attr_delimiter is None:
            infos = line.split()
        else:
            infos = line.split(attr_delimiter)
        node_details.append(infos)
    return _construct_nodes(node_details, attr_names)


def _construct_nodes(node_details: list, attr_names: list):
    """
    construct nodes from the node details
    :param node_details: a list of node details as str
    :param attr_names: a list of str of attribute names of nodes included in the file
    :return: a list of nodes
    """

    from networkd.classes.node import Node

    nodes = []
    for details in node_details:
        attr = {}
        x = None
        y = None
        nid = None
        i = 0
        for name in attr_names:
            if nid is None and _is_identifier(name):
                nid = int(details[i])
            elif x is None and name == 'x':
                x = float(details[i])
            elif y is None and name == 'y':
                y = float(details[i])
            else:
                attr[name] = details[i]
            i += 1
        assert nid is not None
        node = Node(nid)
        node.attr = attr
        if not(x is None or y is None):
            node.pos = (x, y)
        nodes.append(node)
    return nodes


def _check_attr(attr_names: list):
    """
    there must an id value
    :param attr_names:
    :return: boolean
    """

    has_id = False
    for attr in attr_names:
        if _is_identifier(attr):
            has_id = True
    return has_id


_identifier = ['id', 'nid', 'identifier', 'node_id', 'n_id']


def _is_identifier(attr: str):
    for _id in _identifier:
        if attr == _id:
            return True
    return False
