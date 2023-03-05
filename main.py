from Flight import *
from Flight_generator import *




if __name__ == '__main__':
    num_flights = 1000
    generate_random_flights(num_flights)
    flights = load_flights_from_file('C:/Users/nikittua/Desktop/Methodi Progi/MP1/flights.txt')
    times = measure_multiple_sort_times(flights)
    for sort_algorithm, sort_time in times.items():
        print(f"{sort_algorithm}: {sort_time} ms")
    algorithms = [quicksort_flights,bubble_sort_flights,shaker_sort_flights]
    # plot_sort_time_vs_size(algorithms, flights)