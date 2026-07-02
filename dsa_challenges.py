def filter_and_sort_evens(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return sorted(evens)


def count_character_frequency(text):
    text = text.lower()
    freq = {}

    for char in text:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1

    return freq


# Tests
print(filter_and_sort_evens([5, 2, 8, 1, 4]))
print(count_character_frequency("Hello World"))