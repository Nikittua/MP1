
from datetime import datetime
from typing import List
import time
from Flight_generator import *
from algorithms import *
import matplotlib.pyplot as plt
import numpy as np
import Flight
import os




def measure_sort_time(sort_function, data):
    """
    Measures the time it takes for a sorting function to sort a given array of data.

    Args:
        sort_function (function): The sorting function to be tested.
        data (list): The data to be sorted.

    Returns:
        float: The time it took for the sorting function to sort the data in seconds.

    """
    start = time.time()
    sort_function(data)
    end = time.time()
    return end - start
def plot_sort_time_vs_size(algorithms, flights):
    """
    Plots the sorting time of different algorithms against the size of the data.

    Args:
        algorithms (list): A list of sorting algorithms to be tested.
        flights (list): A list of Flight objects to be sorted.
    """
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
    plt.savefig(os.path.join('C:/Users/nikittua/Desktop/MP1/docs/images', 'sort_time_vs_size.png'))
def save_flights_to_file(flights, file_name):
    """
    Saves a list of Flight objects to a file.

    Args:
        flights (list): A list of Flight objects.
        file_name (str): The name of the file to save the flights to.
    """
    with open(file_name, 'w') as f:
        for flight in flights:
            f.write(str(flight) + '\n')         
def load_flights_from_file(file_name):
    """
    Loads a list of Flight objects from a file.

    Args:
        file_name (str): The name of the file containing the flights.

    Returns:
        list: A list of Flight objects.
    """
    flights = []
    with open(file_name, 'r') as f:
        for line in f:
            flight_number, airline, arrival_date, arrival_time, passengers = line.strip().split(', ')
            flights.append(Flight(flight_number, airline, arrival_date, arrival_time, int(passengers)))
    return flights
def measure_multiple_sort_times(data):
    """
    Measures the time it takes for multiple sorting functions to sort a given array of data.

    Args:
        data (list): The data to be sorted.

    Returns:
        dict: A dictionary containing the time it took for each sorting function to sort the data in milliseconds.
        
    Notes:
        This function uses the `measure_sort_time` function to measure the time it takes for the following three sorting functions to sort the given data:
        - quicksort_flights
        - bubble_sort_flights
        - shaker_sort_flights
        The function returns a dictionary where the keys are the names of the sorting functions and the values are the time it took for each sorting function to sort the data in milliseconds.
    """
    times = {
        'quicksort_flights': measure_sort_time(quicksort_flights, data) * 1000
    }
    times['bubble_sort_flights'] = measure_sort_time(bubble_sort_flights, data)*1000
    times['shaker_sort_flights'] = measure_sort_time(shaker_sort_flights, data)*1000
    return times





class Flight:
    """
    Represents a flight with a flight number, airline, arrival date, arrival time, and number of passengers.

    Attributes:
        flight_number (str): The flight number.
        airline (str): The name of the airline.
        arrival_date (str): The date of arrival in 'YYYY-MM-DD' format.
        arrival_time (str): The time of arrival in 'HH:MM' format.
        passengers (int): The number of passengers on the flight.
    """
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
