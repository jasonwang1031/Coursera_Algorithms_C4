from math import sqrt


def importfile(filename):
    file = open(filename)
    city_list = file.readlines()[1:]

    City_Dict = {}

    for city in city_list:
        index, x, y = city.split()
        City_Dict[int(index)]=[]
        City_Dict[int(index)].append(float(x))
        City_Dict[int(index)].append(float(y))
    return City_Dict


def tsp(cities):
    city = 1 #start the tour at the first city
    distance = 0
    
    first_city_x = cities[city][0]
    first_city_y = cities[city][1]

    while len(cities)>0:
        x = cities[city][0]
        y = cities[city][1]
        del cities[city] #delete the first city 
        min_dist_square = float("inf")
        min_index = 0
        for c in cities:
            dist_square = (cities[c][0]-x) ** 2 + (cities[c][1]-y) ** 2
            if dist_square < min_dist_square:
                min_index = c
                min_dist_square = dist_square
            
        if (min_index != 0):
            # travel to the next city
            distance += sqrt(min_dist_square)
            city = min_index
            print (str(city)+' : ' +str(sqrt(min_dist_square)))
    
    min_dist_square = (x-first_city_x) ** 2 + (y-first_city_y) ** 2
    distance += sqrt(min_dist_square)
    print ('1 : ' +str(sqrt(min_dist_square)))
    print (distance)

if __name__ == "__main__":
    CityDict = importfile("nn.txt")
    tsp(CityDict)
