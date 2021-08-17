import math


class Region:
    """
    circle in normalized coordinate system
    used in region_centrality algorithm
    """

    def __init__(self, radius: float, center):
        """
        everything is normalized in [0, 1]
        :param radius: a float value, the radius of the circle
        :param center: a two element tuple stands for two dimensional point
        """

        self.radius = radius
        self.center = center

    def __contains__(self, p):

        """
        check if the point given is contained in the region
        :param p: a two dimensional point
        :return: True if p is contained in the region, False otherwise
        """

        return Region.distance(p, self.center) <= self.radius

    @classmethod
    def distance(cls, p1, p2):

        """
        calculate the distance between two two dimensional points
        :param p1: the first tuple containing x and y coordinate
        :param p2: the second tuple containing x and y coordinate
        :return: the distance between two points
        """

        t1 = (p1[0] - p2[0]) * (p1[0] - p2[0])
        t2 = (p1[1] - p2[1]) * (p1[1] - p2[1])
        return math.sqrt(t1 + t2)

    @classmethod
    def next_center(cls, center, dr: float):

        """
        return next possible center point of the region
        :param center: previous center point
        :param dr: the variant of the center point
        :return: next possible center point
        """

        next_center = (center[0], center[1])
        if next_center[0] + dr <= 1:
            next_center[0] += dr
        elif next_center[1] + dr <= 1:
            next_center[1] += dr
            next_center = (0, next_center[1])
        else:
            return None
        return next_center
