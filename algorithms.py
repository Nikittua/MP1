def compare_flights(flight1, flight2):
    if flight1.arrival_date != flight2.arrival_date:
        return (flight1.arrival_date < flight2.arrival_date) * 2 - 1
    elif flight1.arrival_time != flight2.arrival_time:
        return (flight1.arrival_time < flight2.arrival_time) * 2 - 1
    elif flight1.airline != flight2.airline:
        return (flight1.airline < flight2.airline) * 2 - 1
    else:
        return (flight2.passengers - flight1.passengers)
def quicksort_flights(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    right = []
    equal = []
    for flight in arr:
        comp = compare_flights(flight, pivot)
        if comp < 0:
            left.append(flight)
        elif comp > 0:
            right.append(flight)
        else:
            equal.append(flight)
    return quicksort_flights(left) + equal + quicksort_flights(right)
def bubble_sort_flights(flights):
    n = len(flights)

    for i in range(n):
        for j in range(n-i-1):
            if compare_flights(flights[j], flights[j+1]) > 0:
                flights[j], flights[j+1] = flights[j+1], flights[j]

    return flights
def shaker_sort_flights(flights):
    n = len(flights)
    left = 0
    right = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Compare by arrival date (left to right)
        for i in range(left, right):
            if compare_flights(flights[i], flights[i+1]) > 0:
                flights[i], flights[i+1] = flights[i+1], flights[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        right -= 1

        # Compare by arrival date (right to left)
        for i in range(right, left, -1):
            if compare_flights(flights[i-1], flights[i]) > 0:
                flights[i], flights[i-1] = flights[i-1], flights[i]
                swapped = True

        left += 1

    return flights



