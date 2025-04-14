# Chloe Smith
# Tests for Pipes and Filters

import KWICPipesFilters as pipes

def main():
    filters = [pipes.KWIC_input, pipes.alphabetize, pipes.circular_shifter]
    string_data = 'apples bananas oranges'
    list_data = ['apples', 'bananas', 'oranges']

    assert pipes.pipeline(string_data, filters) == ['apples bananas oranges', 'bananas oranges apples', 'oranges apples bananas']
    assert pipes.pipeline(list_data, filters) == ['apples bananas oranges', 'bananas oranges apples', 'oranges apples bananas']

    print('All tests passed.')

main()
