def flight_searcher(flights: list[str]):
    for flight in flights:
        flight_num, _ = flight.split(" ")
        if flight_num == flight_num[::-1]:
            print(flight)


if __name__ == "__main__":
    flights = ["123321 11:44",
               "569362 01:57",
               "444444 03:34",
               "007007 12:04",
               "889832 05:58"]
    flight_searcher(flights)
