# Chloe Smith
# Tests for Pipes and Filters

import KWICPipesFilters as pipes

def main():
    filters = [pipes.KWIC_input, pipes.alphabetize, pipes.circular_shifter]
    string_data = 'apples bananas oranges'
    list_data = ['apple', 'banana', 'orange']

    assert pipes.pipeline(string_data, filters) == ['oranges', 'bananas', 'apples']
    assert pipes.pipeline(list_data, filters) == ['orange', 'banana', 'apple']

    print('All tests passed.')

main()
