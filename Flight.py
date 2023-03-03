from datetime import datetime
from typing import List
import time
from Flight_generator import *
from algorithms import *
import matplotlib.pyplot as plt
import numpy as np


def measure_sort_time(sort_function, data):
    start = time.time()
    sort_function(data)
    end = time.time()
    return end - start
def plot_sort_time_vs_size(algorithms, flights):
    size = np.arange(1, len(flights) + 1)
    sort_times = []
    labels = []
    for algorithm in algorithms:
        sort_time = np.zeros(len(flights))
        for i in range(len(flights)):
            sub_flights = flights[:i+1]
            sort_time[i] = measure_sort_time(algorithm, sub_flights)
        sort_times.append(sort_time)
        labels.append(algorithm.__name__)

    plt.figure(figsize=(8, 6))
    for i in range(len(algorithms)):
        plt.plot(size, sort_times[i], label=labels[i])
    plt.legend()
    plt.xlabel('Size of array')
    plt.ylabel('Sorting time')
    plt.savefig('sort_time_vs_size.png')

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
def measure_sort_times(data):
    times = {}
    times['quicksort_flights'] = measure_sort_time(quicksort_flights, data)*1000
    times['bubble_sort_flights'] = measure_sort_time(bubble_sort_flights, data)*1000
    times['shaker_sort_flights'] = measure_sort_time(shaker_sort_flights, data)*1000
    return times



num_flights = 2000
generate_random_flights(num_flights)
flights = load_flights_from_file('flights.txt')
times = measure_sort_times(flights)
for sort_algorithm, sort_time in times.items():
    print(f"{sort_algorithm}: {sort_time} ms")




algorithms = [quicksort_flights,bubble_sort_flights,shaker_sort_flights]
plot_sort_time_vs_size(algorithms, flights)
