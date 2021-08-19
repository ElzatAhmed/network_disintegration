class Node:

    def __init__(self, nid: int, pos=None, **kwargs):

        """
        :param nid: each node must have a unique integer identifier
        :param pos: tuple of two numeric values or none
        :param kwargs: node attributes can be anything, stores as a dictionary
        """

        self.nid = nid
        self.pos = pos
        self.alive = True
        self.attr = dict(**kwargs)

    def __eq__(self, other):
        return self.nid == other.nid

    def __getattr__(self, name):
        return self.attr.get(name)

    def __str__(self):
        return f'node[identifier: {self.nid}]'
