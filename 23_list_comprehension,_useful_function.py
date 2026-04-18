#23 LIST COMPREHENSIONS = [expression for item in iterable if condition == True]
            

numbers = [1, 2, 3, 4, 5]

result = [(num, "even") if num % 2 == 0 else (num, "odd") for num in numbers]
print(result)  # Output: [(1, 'odd'), (2, 'even'), (3, 'odd'), (4, 'even'), (5, 'odd')]

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


#*  filter() function: filter(function, iterable) -> filter object
words = ["apple", "banana", "cherry", "date", "elderberry"]

def is_long_word(word):
    return len(word) > 6

long_words = list(filter(is_long_word, words))
print(long_words)  # Output: ['banana', 'cherry', 'elderberry']


#*  map() function: map(function, iterable) -> map object
celsius = [0, 10, 20, 30, 40]

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
fahrenheit = list(map(celsius_to_fahrenheit, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]


#*  sum() function: sum(iterable, start=0) -> number
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # Output: 15

numbers = [1, 2, 3, 4, 5]
total_with_start = sum(numbers, 10)
print(total_with_start)  # Output: 25


#*   lambda functions: lambda arguments: expression
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

