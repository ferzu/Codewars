# Quiz: Lambda with Map() and Filter()
# map() takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. filter () constructs an iterator from those elements of "iterable" for which "function" returns true. Rewrite it with a lambda expression defined within the call to map() and filter().
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]
def mean(num_list):
    return sum(num_list) / len(num_list)
averages = list(map(mean, numbers))
print(averages)

# Solution:
def mean(num_list):
    return sum(num_list) / len(num_list)
averages = list(map(lambda x : sum(x)/len(x), numbers))
print(averages)


# Lambda with Filter
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]
def is_short(name):
    return len(name) < 10
short_cities = list(filter(is_short, cities))
print(short_cities)

# Solution:
def is_short(name):
    return len(name) < 10
short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)
