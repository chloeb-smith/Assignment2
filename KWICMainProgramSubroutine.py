# Mika Collins
# Implementation of Main Program and Subroutine Design - KWIC

def user_input():
    text_list = []

    text = input("Enter text here: ")
    print()
    
    if text != "":
        text_list.append(text)

    return text_list

def circular_shifter(text_list):
    shifted_list = []
    
    for text in text_list:
        words = text.split()
        
        for i in range(len(words)):
            shifted = words[i:] + words[:i]
            shifted_list.append(" ".join(shifted))
    
    return shifted_list

def alphabetizer(shifts):
    return sorted(shifts)

def output(alphabetical_shifts):
    
    for shift in alphabetical_shifts:
        print(shift)

def main():
    text_list = user_input()
    shifts = circular_shifter(text_list)
    alphabetical_shifts = alphabetizer(shifts)
    output(alphabetical_shifts)

main()