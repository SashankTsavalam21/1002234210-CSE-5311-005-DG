MAX_CITIES = 15

class Road:
    def __init__(self, city1, city2, cost):
        self.city1 = city1  
        self.city2 = city2  
        self.cost = cost 

class RoadList:
    def __init__(self):
        self.data = [] 
        self.n = 0      

city_matrix = [
    [0, 10, 0, 0, 0, 0, 0, 15, 0],
    [10, 0, 12, 0, 0, 0, 0, 18, 0],
    [0, 12, 0, 5, 0, 3, 0, 0, 8],
    [0, 0, 5, 0, 6, 9, 0, 0, 0],
    [0, 0, 0, 6, 0, 7, 0, 0, 0],
    [0, 0, 3, 9, 7, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 2, 9],
    [15, 0, 0, 0, 0, 0, 2, 0, 11],
    [0, 0, 8, 0, 0, 0, 9, 11, 0]
]

num_cities = 9

city_parent = [i for i in range(MAX_CITIES)]

city_names = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas']

road_list = RoadList()

def kruskal():
    global road_list
    road_list.n = 0

    for i in range(num_cities):
        for j in range(num_cities):
            if city_matrix[i][j] != 0:
                road_list.data.append(Road(i, j, city_matrix[i][j]))
                road_list.n += 1

    road_list.data.sort(key=lambda x: x.cost)
    print("\nRoads in the Minimum Cost Spanning Network:")
    for i in range(road_list.n):
        city1 = find(road_list.data[i].city1)
        city2 = find(road_list.data[i].city2)

        if city1 != city2:
            union(city1, city2)
            print(f"{city_names[road_list.data[i].city1]} <-> {city_names[road_list.data[i].city2]} = ${road_list.data[i].cost}")

def find(i):
    while city_parent[i] != i:
        i = city_parent[i]
    return i

def union(i, j):
    city_parent[i] = j

if __name__ == "__main__":
    kruskal()
