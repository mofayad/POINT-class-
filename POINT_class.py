import math

class Point:
    nb = 0

    def __init__(self, abs, ord):
        self.__abs = abs
        self.__ord = ord
        Point.nb += 1

    @property
    def abs(self):
        return self.__abs
    
    @abs.setter
    def abs(self, value):
        self.__abs = value

    @property
    def ord(self):
        return self.__ord
    
    @ord.setter
    def ord(self, value):
        self.__ord = value

    def __str__(self):
        return f"({self.__abs},{self.__ord})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__abs == other.abs and self.__ord == other.ord
        return False

    def calculer_distance(self, p):
        return math.sqrt(math.pow((self.__abs - p.abs), 2) + math.pow((self.__ord - p.ord), 2))

    def calculer_milieu(self, p):
        XM = (self.__abs + p.abs) / 2
        YM = (self.__ord + p.ord) / 2
        return Point(XM, YM)

class TroisPoints:
    def __init__(self, point1, point2, point3):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

    @property
    def point1(self):
        return self.__point1
    
    @point1.setter
    def point1(self, value):
        self.__point1 = value

    @property
    def point2(self):
        return self.__point2
    
    @point2.setter
    def point2(self, value):
        self.__point2 = value

    @property
    def point3(self):
        return self.__point3
    
    @point3.setter
    def point3(self, value):
        self.__point3 = value

    def sont_alignes(self):
        distance1 = self.__point1.calculer_distance(self.__point2)
        distance2 = self.__point1.calculer_distance(self.__point3)
        distance3 = self.__point2.calculer_distance(self.__point3)

        return math.isclose(distance1, distance2 + distance3) or \
               math.isclose(distance2, distance1 + distance3) or \
               math.isclose(distance3, distance1 + distance2)     

    def est_isocele(self):
        distance1 = self.__point1.calculer_distance(self.__point2)
        distance2 = self.__point1.calculer_distance(self.__point3)
        distance3 = self.__point2.calculer_distance(self.__point3)

        return math.isclose(distance1, distance2) or \
               math.isclose(distance1, distance3) or \
               math.isclose(distance2, distance3)     

    @staticmethod
    def distance_entre_points(p1, p2):
        return p1.calculer_distance(p2)

    @staticmethod
    def milieu_entre_points(p1, p2):
        return p1.calculer_milieu(p2)

# example of usage 
point_A = Point(1, 2)
point_B = Point(3, 4)
point_C = Point(5, 6)

trois_points = TroisPoints(point_A, point_B, point_C)

print(f"Distance entre point A et point B: {TroisPoints.distance_entre_points(point_A, point_B)}")
print(f"Milieu entre point A et point B: {TroisPoints.milieu_entre_points(point_A, point_B)}")

print(f"Les trois points sont alignés: {trois_points.sont_alignes()}")
print(f"Les trois points forment un triangle isocèle: {trois_points.est_isocele()}")