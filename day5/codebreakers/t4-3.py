def road_calculator(roads: list[str]):
    road_dict = {}
    for road in roads:
        name, length, speed = road.split(" ")
        road_dict[(name, int(length))] = int(speed)

    total = 0
    for (_, length), speed in road_dict.items():
        total += length // speed
    print(total)


if __name__ == "__main__":
    roads = ["ThisIsARoad 100 20",
             "YetAnotherRoad 40 20",
             "ThisIsAnotherRoad 5 5",
             "ThisIsARoad 60 15",
             "YetAnotherRoad 40 8"]
    road_calculator(roads)
