def destCity(paths):
    # Create a set of starting cities
    start_cities = set(cityA for cityA, cityB in paths)
    
    # Find the city in paths that is not a start city
    for cityA, cityB in paths:
        if cityB not in start_cities:
            return cityB

# paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
# print(destCity(paths))  # Output: "Sao Paulo"