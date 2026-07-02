def calculate_average(numbers):
    try:
        total = 0
        for number in numbers:
            total += number

        return total / len(numbers)

    except ZeroDivisionError:
        print("Cannot calculate average of an empty list.")
        return None


def get_list_element(my_list, index):
    try:
        return my_list[index]

    except IndexError:
        print("Error: Index is out of bounds.")
        return None

    except TypeError:
        print("Error: First argument must be a list.")
        return None


# Test data for calculate_average
data1 = [10, 20, 30]
data2 = [5]
data3 = []

print(calculate_average(data1))
print(calculate_average(data2))
print(calculate_average(data3))

# Test data for get_list_element
print(get_list_element([1, 2, 3], 1))
print(get_list_element([1, 2, 3], 5))
print(get_list_element(100, 0))