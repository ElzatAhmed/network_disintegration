import numpy as np
import networkx as nx
import networkd as nd


class Network:

    def __init__(self):

        """
        nodes: list of type Node, nodes in the network
        edges: list of type Edge, edges in the network
        graph: a networkx graph
        adj_matrix: adjacency matrix
        con_matrix: connection matrix
        """

        self.nodes = list()
        self.edges = list()
        self.graph = nx.Graph()
        self.adj_matrix = None
        self.con_matrix = None

    def _contains_node_(self, node):
        for n in self.nodes:
            if n.__eq__(node):
                return True
        return False

    def _contains_edge_(self, edge):
        for e in self.edges:
            if e.__eq__(edge):
                return True
        return False

    def add_node(self, node: nd.Node):  # add a single node to the network
        if self._contains_node_(node):
            # network cannot have two identical nodes
            print(f'network contains a same node with node identifier: {node.nid}')
            return
        self.nodes.append(node)

    def add_nodes_from(self, nodes: list):  # add a list of nodes to the network
        for node in nodes:
            self.add_node(node)

    def add_edge(self, edge: nd.Edge):  # add a single edge to the network
        if self._contains_edge_(edge):
            # network cannot have two identical edges
            print('network contains a same edge')
            return
        self.edges.append(edge)

    def add_edges_from(self, edges: list):  # add a list of edges to the network
        for edge in edges:
            self.add_edge(edge)

    def get_node(self, nid: int):  # get a specified node from the network
        for node in self.nodes:
            if node.nid == nid:
                return node
        return None

    def get_edge(self, nid0: int, nid1: int):  # get a specified edge from the network
        given = nd.Edge(nid0, nid1)
        for edge in self.edges:
            if given.__eq__(edge):
                return edge
        return None

    def get_node_ids(self):  # get a list containing ascending identifiers of all the nodes
        nids = []
        for node in self.nodes:
            nids.append(node.nid)
        nids.sort()
        return nids

    def get_living_node_ids(self):  # get a list containing ascending identifiers of all the living nodes
        nids = []
        for node in self.nodes:
            if not node.alive:
                continue
            nids.append(node.nid)
        nids.sort()
        return nids

    def get_edge_tuples(self):  # get a list containing (id0, id1) like info tuples of all the edges
        edge_tuples = []
        for edge in self.edges:
            edge_tuples.append((edge.nid0, edge.nid1))
        return edge_tuples

    def get_living_edge_tuples(self):   # get a list containing (id0, id1) like info tuples of all the living edges
        edge_tuples = []
        for edge in self.edges:
            if not edge.alive:
                continue
            edge_tuples.append((edge.nid0, edge.nid1))
        return edge_tuples

    def kill_node(self, identifier: int):

        """
        kill a node in the network
        find the node, if not existed return
        else find all the edges that contain this node
        kill those edges
        kill the node
        :param identifier: node identifier
        :return:
        """

        node = self.get_node(identifier)
        if node is None or not node.alive:
            return
        for edge in self.edges:
            if edge.__contains__(identifier):
                edge.alive = False
        node.alive = False

    def construct_nx_graph_whole(self):

        """
        construct networkx graph
        add all of the node identifiers and edge tuples
        despite it`s alive or not
        :return:
        """

        self.graph = nx.Graph()
        self.graph.add_nodes_from(self.get_node_ids())
        self.graph.add_edges_from(self.get_edge_tuples())

    def construct_nx_graph_living(self):

        """
        construct networkx graph
        add only the living node identifiers and edge tuples
        :return:
        """

        self.graph = nx.Graph()
        self.graph.add_nodes_from(self.get_living_node_ids())
        self.graph.add_edges_from(self.get_living_edge_tuples())

    def construct_adj_matrix(self):

        """
        construct the adjacency matrix of the network
        get the max value of the identifiers of the network nodes as max_id
        matrix size would be max_id + 1
        traverse all the living edges
        and set the corresponding matrix element to 1
        :return:
        """

        max_id = self.get_node_ids()[-1]
        size = max_id + 1
        self.adj_matrix = np.zeros((size, size), dtype=int)
        for edge in self.edges:
            if not edge.alive:
                continue
            self.adj_matrix[edge.nid0][edge.nid1] = 1
            self.adj_matrix[edge.nid1][edge.nid0] = 1

    def construct_con_matrix(self):

        """
        construct the connection matrix of the network
        connection matrix: c[i][j] = 1 iff there is at least one path from i to j, otherwise c[i][j] = 0
        construct the current networkx graph
        implement the all_pairs_shortest_path algorithm of networkx
        :return:
        """

        max_id = self.get_node_ids()[-1]
        size = max_id + 1
        self.con_matrix = np.zeros((size, size), dtype=1)
        self.construct_nx_graph_living()
        paths = nx.all_pairs_shortest_path(self.graph)
        for i in paths:
            for j in paths[i]:
                self.con_matrix[i][j] = 1

    def get_adjacency_nodes(self, nid: int):

        """
        get a list containing the ids of the adjacency nodes of the given node
        construct adjacency matrix and check the ith row
        :param nid: given node id
        :return adj_nodes: adjacency node ids
        """

        adj_nodes = []
        self.construct_adj_matrix()
        for i in range(0, len(self.adj_matrix)):
            if i == nid:
                continue
            if self.adj_matrix[i][nid] == 1:
                adj_nodes.append(i)
        return adj_nodes

    def get_connected_nodes(self, nid: int):

        """
        get a list containing the ids of the connected nodes of the given node
        construct connection matrix and check the ith row
        :param nid: given node id
        :return con_nodes: connected node ids
        """

        con_nodes = []
        self.construct_con_matrix()
        for i in range(0, len(self.con_matrix)):
            if i == nid:
                continue
            if self.con_matrix[i][nid] == 1:
                con_nodes.append(i)
        return con_nodes
