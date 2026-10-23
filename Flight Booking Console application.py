
from abc import ABC, abstractmethod


# 1. Flight class
class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.__seats = seats
        self.fare = fare

    def get_seats(self):
        return self.__seats

    def book_seats(self, tickets):
        if tickets <= self.__seats:
            self.__seats -= tickets
            return True
        return False

    def display(self):
        print(
            f"{self.code} | {self.airline} | "
            f"{self.source} to {self.destination} | "
            f"Seats: {self.__seats} | Fare: Rs.{self.fare}"
        )


# 2. Abstract Passenger class
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass


# 3. Regular passenger
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0.0


# 4. Student passenger
class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10


# 5. Booking class
class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

        self.subtotal = flight.fare * tickets
        self.discount = self.subtotal * passenger.get_discount()
        self.total = self.subtotal - self.discount

    def display(self):
        print("\n--- Booking Summary ---")
        print("Booking ID:", self.booking_id)
        print("Flight:", self.flight.code)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Airline:", self.flight.airline)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger Type:", type(self.passenger).__name__)
        print("Tickets:", self.tickets)
        print("Base fare per ticket: Rs.", self.flight.fare)
        print("Subtotal: Rs.", self.subtotal)
        print("Discount: Rs.", self.discount)
        print("Final amount: Rs.", self.total)


# 6. Main flight booking system
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky Air", "Mumbai", "Bengaluru", 15, 3500),
            Flight("PN303", "Kiran Air", "Pune", "Hyderabad", 10, 2500)
        ]
        self.bookings = []
        self.next_id = 1001

    def display_flights(self):
        print("\n--- Available Flights ---")
        for flight in self.flights:
            flight.display()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight
        return None

    def book_flight(self):
        code = input("Enter flight code: ").strip()
        flight = self.find_flight(code)

        if flight is None:
            print("Error: Flight code not found.")
            return

        name = input("Enter passenger name: ").strip()
        if not name:
            print("Error: Name cannot be blank.")
            return

        try:
            age = int(input("Enter age: "))
            if age <= 0:
                print("Error: Age must be greater than 0.")
                return

            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()

            if passenger_type == "regular":
                passenger = RegularPassenger(name, age)
            elif passenger_type == "student":
                passenger = StudentPassenger(name, age)
            else:
                print("Error: Invalid passenger type.")
                return

            tickets = int(input("Enter number of tickets: "))
            if tickets <= 0:
                print("Error: Tickets must be greater than 0.")
                return

        except ValueError:
            print("Error: Please enter valid numbers.")
            return

        if tickets > flight.get_seats():
            print("Booking failed: Not enough seats available.")
            return

        # Update seats and save only after validation
        flight.book_seats(tickets)

        booking = Booking(
            f"BK{self.next_id}",
            flight,
            passenger,
            tickets
        )
        self.bookings.append(booking)
        self.next_id += 1

        print("\nBooking confirmed!")
        booking.display()

    def view_booking(self):
        if not self.bookings:
            print("No confirmed booking exists.")
        else:
            self.bookings[-1].display()

    def run(self):
        while True:
            print("\nWelcome to Kiran Air Booking")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please try again.")


# Start the application
app = FlightBookingSystem()
app.run()
