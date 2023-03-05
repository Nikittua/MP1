import random
from datetime import datetime, timedelta

countries = ["Russia", "USA", "China", "Japan", "India", "Australia", "Brazil", "Canada", "France", "Germany"]

def generate_flight():

    """
    Generates a random flight detail.

    Returns:
    tuple: A tuple containing 5 elements: flight number (str), airline name (str), arrival date (str), arrival time (str), and passenger count (int).
    """
    flight_number = "AI{:03d}".format(random.randint(100, 9999))
    airline = f"Air {random.choice(countries)}"
    arrival_date = (datetime.now() + timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d")
    arrival_time = "{:02d}:00".format(random.randint(0, 23))
    # arrival_time = "{:02d}:{:02d}".format(random.randint(0, 23), random.choice([0, 15, 30, 45]))
    # arrival_time = "{:02d}:{:02d}".format(random.randint(0, 23), random.randint(0, 59))
    passenger_count = random.randint(22, 500)
    return (flight_number, airline, arrival_date, arrival_time, passenger_count)

def generate_random_flights(size):
    
    """
    Generates a list of random flight details and writes them to a text file named "flights.txt".

    Args:
    size (int): The number of flight details to generate.

    Returns:
    list: A list of flight details, where each detail is a tuple containing 5 elements: flight number (str), airline name (str), arrival date (str), arrival time (str), and passenger count (int).
    """
    flights = [generate_flight() for _ in range(size)]
    with open("C:/Users/nikittua/Desktop/MP1/Files/flights.txt", "w") as file:
        for flight in flights:
            file.write("{}, {}, {}, {}, {}\n".format(*flight))
    return flights

