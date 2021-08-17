def nc(network):

    """
    nc stands for natural connectivity
    this method uses math and numpy as key tools
    :param network: Network
    :return: natural connectivity of the network
    """

    import numpy as np
    import math

    network.construct_adj_matrix()
    w, v = np.linalg.eig(network.adj_matrix)
    s = 0
    for i in w:
        s += math.pow(math.e, i)
    result = math.log(s / len(w))
    return result
