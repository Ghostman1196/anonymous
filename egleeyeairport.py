class Passenger:
    def __init__(self, flight_number, name, passport_number, nationality):
        self.flight_number = flight_number
        self.name = name
        self.passport_number = passport_number
        self.nationality = nationality

    def __str__(self):
        return f"{self.flight_number:<15} {self.name:<20} {self.passport_number:<20} {self.nationality:<5}"

class Flight:
    def __init__(self, flight_number, destination, arrival_time, departure_time):
        self.flight_number = flight_number
        self.destination = destination
        self.arrival_time = arrival_time
        self.departure_time = departure_time

    def __str__(self):
        return f"{self.flight_number:<15} {self.destination:<15} {self.arrival_time:<10} {self.departure_time:<10}"

class Hanger:
    def __init__(self, flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination

    def __str__(self):
        return f"{self.flight_number:<15} {self.destination:<15}"

def print_passenger_info(passengers):
    print("Flight Number : FD9463")
    print("Name          Passport Number          Nationality")
    print("-" * 50)
    for passenger in passengers:
        print(passenger)
    print()

def print_flight_info(flights):
    print("Flight Number Distination              Arrival Time          Departure Time")
    print("-" * 50)
    for flight in flights:
        print(flight)
    print()

def print_hanger_info(hangers):
    print("Airport : International Airport ()")
    print("Hanger Information :")
    print("Flight Number Distination")
    print("-" * 50)
    for hanger in hangers:
        print(hanger)
    print()

def main():
    
    passengers = [
        Passenger("FD9463", "John Doe", "PD156987", "TH"),
        Passenger("FD9463", "Jane Smith", "PD159876", "TH")
    ]

    flights = [
        Flight("FL6451", "Udon", "08:00", "09:00"),
        Flight("FL7358", "Bangkok", "08:00", "09:00")
    ]

    hangers = [
        Hanger("FL6451", "New York"),
        Hanger("FL7358", "London")
    ]

    print_passenger_info(passengers)
    print_flight_info(flights)
    print_hanger_info(hangers)

if __name__ == "__main__":
    main()
