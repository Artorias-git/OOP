
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def xy(self):
        return (int(self.__x), int(self.__y))

    def __eq__(self, b):
        return self.__x == b.__x and self.__y == b.__y

    def __str__(self):
        return f"[{self.__x}; {self.__y}]"

class Figure:
    def __init__(self, points):
        self._pts = points
        self.__area = self._update_area()

    def _update_area(self):
        #print("Figure::__update_area")
        pass

    @property
    def area(self):
        return self.__area

    @property
    def points(self):
        return self._pts

    def __lt__(self, b):
        return self.__area < b.area

    def __le__(self, b):
        return self.__area <= b.area

    def __eq__(self, b):
        return self.__area == b.area

    def __ne__(self, b):
        return self.__area != b.area

    def __ge__(self, b):
        return self.__area >= b.area

    def __gt__(self, b):
        return self.__area > b.area

class Triangle(Figure):
    def _update_area(self):
        first = self._pts[0]
        second = self._pts[1]
        third = self._pts[2]
        S = abs((first[0] - third[0]) * (second[1] - third[1]) - (second[0] - third[0]) * (first[1] - third[1])) * 0.5
        return S

    def __str__(self):
        return f"[{self._pts[0]}; {self._pts[1]}; {self._pts[2]}]"

class Fourangle(Figure):
    def _update_area(self):
        if check_convex(self._pts):
            a = get_length(self._pts[0], self._pts[1])
            b = get_length(self._pts[1], self._pts[2])
            c = get_length(self._pts[2], self._pts[3])
            d = get_length(self._pts[3], self._pts[0])
            p = (a + b + c + d) / 2
            return ((p - a)*(p - b)*(p - c)*(p - d)) ** 0.5
        else:
            return 0

    def __str__(self):
        return f"[{self._pts[0]}; {self._pts[1]}; {self._pts[2]}; {self._pts[3]}]"

def get_length(point1, point2):
    x = [0, point1[0], point2[0]]
    y = [0, point1[1], point2[1]]
    return ((x[2] - x[1]) ** 2 + (y[2] - y[1]) ** 2) ** 0.5

def check_convex(points):
    def make_vector(A):
        X1 = (A[1][0] - A[0][0])
        Y1 = (A[1][1] - A[0][1])
        X2 = (A[2][0] - A[0][0])
        Y2 = (A[2][1] - A[0][1])
        return (X1 * Y2 - Y1 * X2)
    N = len(points)
    previous = 0
    for i in range(N):
        cord_for_vector = [points[i], points[(i + 1) % N], points[(i + 2) % N]]
        currant = make_vector(cord_for_vector)
        if (currant != 0):
            if (currant * previous < 0):
                return False
            else:
                previous = currant
    return True

def create_points_obj():
    f = open("trin", "r").read().replace("[", "").replace(",", "").split("]")
    points = []
    for i in range(len(f)-1):
        f[i] = f[i].split()
        points.append([int(f[i][0]), int(f[i][1])])
    N = len(points)
    for i in range(N - 1):
        for j in range(i + 1, N - 1):
            if points[i] == points[j]:
                del points[j]
                N -= 1
    object_list = []
    for i in points:
        object_list.append(Point(i[0], i[1]))
    return object_list

def create_triangle_obj():
    triangles_list = []
    for a in range(len(points) - 2):
        for b in range(a + 1, len(points) - 1):
            for c in range(b + 1, len(points)):
                first = points[a].xy
                second = points[b].xy
                third = points[c].xy
                triangl = (Triangle([first, second, third]))
                if triangl.area != 0:
                    triangles_list.append(triangl)
    return triangles_list

def create_fourangle_obj():
    fourangles_list = []
    for a in range(len(points) - 3):
        for b in range(a + 1, len(points) - 2):
            for c in range(b + 1, len(points) - 1):
                for d in range(c + 1, len(points)):
                    cord = [points[a].xy, points[b].xy, points[c].xy, points[d].xy]
                    fourangle = (Fourangle(cord))
                    if fourangle.area != 0:
                        fourangles_list.append(fourangle)
    return fourangles_list

points = create_points_obj()
triangles_list = create_triangle_obj()
#fourangles_list = create_fourangle_obj()


error_list = []

def get_min_max_area(list):
    min = list[0]
    max = list[0]
    for i in range(len(list)-1):
        try:
            if min.area > list[i+1].area:
                min = list[i+1]
            if max.area < list[i+1].area:
                max = list[i+1]
        except:
            error_list.append(i)
            continue
    return min, max

def print_min_max():
    lists = [triangles_list, fourangles_list]
    for i in lists:
            mins, maxs = get_min_max_area(i)
            print(mins.area, "\n", mins.points, "\n")
            print(maxs.area, "\n", maxs.points, "\n")

f = Fourangle([[1, 1], [1, 50], [37, 36], [100, 2]])
print(f.area)
#print_min_max()
#print("broken ones: ", error_list) #не знаю почему, но эти (у меня их было 3) обекта в площади имеют значение complex, вместо float

