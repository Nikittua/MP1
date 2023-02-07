from datetime import datetime
from typing import List
import time
from Flight_generator import *
from algorithms import *
import matplotlib.pyplot as plt
import numpy as np


class Flight:
    def __init__(self, flight_number, airline, arrival_date, arrival_time, passengers):
        self.flight_number = flight_number
        self.airline = airline
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.passengers = passengers

    def __lt__(self, other):
        if self.arrival_date != other.arrival_date:
            return self.arrival_date < other.arrival_date
        if self.arrival_time != other.arrival_time:
            return self.arrival_time < other.arrival_time
        if self.airline != other.airline:
            return self.airline < other.airline
        return self.passengers > other.passengers

    def __eq__(self, other):
        return (self.arrival_date == other.arrival_date and
                self.arrival_time == other.arrival_time and
                self.airline == other.airline and
                self.passengers == other.passengers)
    def __repr__(self):
        return f"{self.flight_number}, {self.airline}, {self.arrival_date}, {self.arrival_time}, {self.passengers}"

    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)




def sort_flights(flights, field, algorithm):
    # if field not in ['arrival_date', 'arrival_time', 'airline', 'passengers']:
    #     print("Invalid field. Please choose one of the following fields: 'arrival_date', 'arrival_time', 'airline', 'passengers'")
    #     return flights

    comparator = None
    if field == 'airline':
        comparator = 'airline'
    elif field == 'arrival_date':
        comparator = 'arrival_date'
    elif field == 'arrival_time':
        comparator = 'arrival_time'
    elif field == 'passengers':
        comparator = 'passengers'

    if algorithm == 'bubble':
        start_time = time.time()
        bubble_sort(flights, comparator)
        end_time = time.time()
    elif algorithm == 'shaker':
        start_time = time.time()
        shaker_sort(flights, comparator)
        end_time = time.time()
    elif algorithm == 'quick':
        start_time = time.time()
        quick_sort(flights, comparator)
        end_time = time.time()
    else:
        print("Invalid algorithm. Please choose one of the following algorithms: 'bubble', 'shaker', 'quick'")
        return flights

    print(f"Time taken by {algorithm} sort:", end_time - start_time)
    return flights
def save_flights_to_file(flights, file_name):
    with open(file_name, 'w') as f:
        for flight in flights:
            f.write(str(flight) + '\n')
def load_flights_from_file(file_name):
    flights = []
    with open(file_name, 'r') as f:
        for line in f:
            flight_number, airline, arrival_date, arrival_time, passengers = line.strip().split(', ')
            flights.append(Flight(flight_number, airline, arrival_date, arrival_time, int(passengers)))
    return flights


generate_random_flights(3000)
flights = load_flights_from_file('flights.txt')
# soeted_flights = bubble_sort(flights, 'arrival_date')
# save_flights_to_file(soeted_flights, 'sorted_flights.txt')





def measure_sort_time(sort_function, data, field):
    start = time.time()
    sort_function(data, field)
    end = time.time()
    return end - start

def plot_sort_time_vs_size(algorithm, flights, field):
    size = np.arange(1, len(flights) + 1)
    sort_time1 = np.zeros(len(flights))
    for i in range(len(flights)):
        sub_flights = flights[:i+1]
        sort_time1[i] = measure_sort_time(algorithm, sub_flights, field)



    plt.plot(size, sort_time1, label=algorithm.__name__)
    plt.legend()
    plt.xlabel('Size of array')
    plt.ylabel('Sorting time')
    plt.savefig("sort_time_vs_size.png")


plot_sort_time_vs_size(quick_sort,flights, 'passengers')
plot_sort_time_vs_size(bubble_sort,flights, 'passengers')
plot_sort_time_vs_size(shaker_sort,flights, 'passengers')

