def region_centrality(network, radius=0.05, dr=0.1, center=(0, 0)):

    """
    region centrality: sum of the degree centrality of the nodes contained in the region
    traverse all the possible regions and calculate its centrality
    :param network: Network
    :param radius: the radius of the region
    :param dr: the various of the region center point
    :param center: the initial center point
    :return: a dictionary of all the regions with its centrality as its value,
            a dictionary of all the regions with a list of containing node ids as its values,
            a list of regions in descending order on region centrality
    """

    from networkd.classes.region import Region
    from networkd.centrality.degree import degree_centrality

    nodes = network.get_living_node_ids()
    degree_centrality = degree_centrality(network)[0]
    centrality = {}
    contains = {}
    regions = []
    region = Region(radius, center)
    while True:
        containing = []
        for nid in nodes:
            if region.__contains__(network.get_node(nid).pos):
                containing.append(nid)
        dc = 0
        for nid in containing:
            dc += degree_centrality[nid]
        centrality[region] = dc
        contains[region] = containing
        regions.append(region)
        next_center = Region.next_center(region.center, dr)
        if next_center is None:
            break
        region = Region(radius, next_center)
    regions.sort(key=lambda o: centrality[o], reverse=True)
    return centrality, contains, regions
