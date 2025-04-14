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
    shifted_list = []
    
    for i in range(len(data)):
        shifted = data[i:] + data[:i]
        shifted_list.append(" ".join(shifted))
    
    return shifted_list

def KWIC_input(data):
    if type(data) == list:
        return data
    elif type(data) == str:
        return data.split()
    

data = 'my name is chloe'
filters = [KWIC_input, alphabetize, circular_shifter]

print(pipeline(data, filters))


