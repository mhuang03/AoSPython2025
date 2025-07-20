def road_calculator(roads: list[str]):
    total = 0
    for road in roads:
        name, length, speed = road.split(" ")
        total += int(length) // int(speed)
    print(total)


if __name__ == "__main__":
    roads = ["ThisIsARoad 100 20",
             "YetAnotherRoad 40 20",
             "ThisIsAnotherRoad 5 5",
             "ThisIsARoad 60 15",
             "YetAnotherRoad 40 8"]
    road_calculator(roads)
