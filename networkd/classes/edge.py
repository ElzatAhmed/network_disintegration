class Edge:

    def __init__(self, nid0, nid1, **kwargs):

        """
        :param nid0: the node on one side of the edge
        :param nid1: the node on the another side of the edge
        :param kwargs: edge attributes can be anything
        """

        self.nid0 = nid0
        self.nid1 = nid1
        self.alive = True
        self.attr = dict(kwargs)

    def __contains__(self, nid):
        return nid == self.nid0 or \
               nid == self.nid1

    def __eq__(self, other):
        return self.__contains__(other.nid0) and \
               self.__contains__(other.nid1)

    def __str__(self):
        return f'edge[n0: {self.nid0}, n1: {self.nid1}]'
