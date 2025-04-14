# Chloe Smith
# Implementation of Pipes and Filters Design Pattern

def pipeline(data, filters):
    result = data
    for f in filters:
        result = f(result)
    return result

def alphabetize(data):
    return sorted(data)

def circular_shifter(data):
    return data[::-1]

def KWIC_input(data):
    if type(data) == list:
        return data
    elif type(data) == str:
        return data.split()


