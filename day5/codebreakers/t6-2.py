from t6 import Watch


def better_watch(watch1: Watch, watch2: Watch) -> Watch:
    if watch1.brand == "BitWatch" and watch2.brand != "BitWatch":
        return watch1
    elif watch1.brand != "BitWatch" and watch2.brand == "BitWatch":
        return watch1

    if len(watch1.superpower) > len(watch2.superpower):
        return watch1
    elif len(watch1.superpower) < len(watch2.superpower):
        return watch2

    if watch1.price > watch2.price:
        return watch1
    elif watch1.price < watch2.price:
        return watch2

    return watch1


if __name__ == "__main__":
    w1 = Watch("BitWatch", 100, "rewinds time")
    w2 = Watch("Codelex", 200, "shoots lasers")
    w3 = Watch("Techno", 100, "violently explodes")
    w4 = Watch("Techno", 150, "violently explodes")

    print(better_watch(w1, w2))
    print(better_watch(w2, w3))
    print(better_watch(w3, w4))
