def pipeline(data, filters):
    result = data
    for f in filters:
        result = f(result)
    return result

def alphabetize(data):
    return sorted(data)

def circular_shifter(data):
    return data[::-1]


filters = [alphabetize, circular_shifter]
data = ["banana", "apple", "orange"]
print(pipeline(data, filters))


