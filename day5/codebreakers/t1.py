def beacon_locator(beacon_coords: str):
    coords = [int(n) for n in beacon_coords.split(" ")]
    x_total, y_total = 0, 0

    count = len(coords) // 2
    for i in range(count):
        x_total += coords[2*i]
        y_total += coords[2*i+1]

    print(f"{round(x_total / count)} {round(y_total / count)}")


if __name__ == "__main__":
    coords = "1001 3 54 192 598 43 -4 16 -205 9"
    beacon_locator(coords)
