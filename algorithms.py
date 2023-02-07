def bubble_sort(flights, field):
    if field not in ['arrival_date', 'arrival_time', 'airline', 'passengers']:
        print("Invalid field. Please choose one of the following fields: 'arrival_date', 'arrival_time', 'airline', 'passengers'")
        return flights

    n = len(flights)
    for i in range(n):
        for j in range(n-i-1):
            if (field == 'arrival_date' and flights[j].arrival_date > flights[j+1].arrival_date) or \
               (field == 'arrival_time' and flights[j].arrival_time > flights[j+1].arrival_time) or \
               (field == 'airline' and flights[j].airline > flights[j+1].airline) or \
               (field == 'passengers' and flights[j].passengers > flights[j+1].passengers):
                flights[j], flights[j+1] = flights[j+1], flights[j]

    return flights
def shaker_sort(flights, field):
    if field not in ['arrival_date', 'arrival_time', 'airline', 'passengers']:
        print("Invalid field. Please choose one of the following fields: 'arrival_date', 'arrival_time', 'airline', 'passengers'")
        return flights
    
    n = len(flights)
    start = 0
    end = n - 1
    swapped = True
    comparator = None
    if field == 'arrival_date':
        comparator = lambda x, y: x.arrival_date > y.arrival_date
    elif field == 'arrival_time':
        comparator = lambda x, y: x.arrival_time > y.arrival_time
    elif field == 'airline':
        comparator = lambda x, y: x.airline > y.airline
    elif field == 'passengers':
        comparator = lambda x, y: x.passengers > y.passengers
    
    while swapped:
        swapped = False
        for i in range(start, end):
            if comparator(flights[i], flights[i+1]):
                flights[i], flights[i+1] = flights[i+1], flights[i]
                swapped = True
                
        if not swapped:
            break
        
        swapped = False
        end -= 1
        
        for i in range(end-1, start-1, -1):
            if comparator(flights[i], flights[i+1]):
                flights[i], flights[i+1] = flights[i+1], flights[i]
                swapped = True
                
        start += 1
                
    return flights
def quick_sort(flights, field):
    fields = ['arrival_date', 'arrival_time', 'airline', 'passengers']
    if field not in fields:
        print(f"Invalid field. Please choose one of the following fields: {fields}")
        return flights

    comparator = {
        'arrival_date': lambda x: x.arrival_date,
        'arrival_time': lambda x: x.arrival_time,
        'airline': lambda x: x.airline,
        'passengers': lambda x: x.passengers,
    }.get(field)

    if comparator is None:
        return flights

    def quick_sort(array, low, high):
        if low < high:
            pivot = partition(array, low, high)
            quick_sort(array, low, pivot-1)
            quick_sort(array, pivot+1, high)

    def partition(array, low, high):
        pivot = comparator(array[high])
        i = low - 1
        for j in range(low, high):
            if comparator(array[j]) <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        return i + 1

    quick_sort(flights, 0, len(flights) - 1)
    return flights