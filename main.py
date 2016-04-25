#!/usr/bin/python3

from helpers import *
import time

linebreaker = str('-'*50 + '\n')

# First while loop for the quit option
while True :
    while True : # Second while loop to deal with bad input for main menu
        user_choice = input(linebreaker + (
    '''Main Menu:
1 - Data Summary Statistics
2 - Enter a PID
3 - Help
4 - Quit
''') + linebreaker + ('Choose an option: '))
        if user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
            break
    if user_choice == '1' :
        while True :
            user_choice2 = input(linebreaker + ( # If user chooses 1, show second menu
    '''Data Summary Statistics:
1 - Object types (Folder, File, Aggregate)
2 - MIME types
3 - Maximum file size
4 - Minimum file size
5 - Average file size
''') + linebreaker + ('Choose an option: '))
            if user_choice2 == '1' or user_choice2 == '2' or user_choice2 == '3' or user_choice2 == '4' or user_choice2 == '5' :
                break
        if user_choice2 == '1' : # Show object type vizualization
            object_type_viz()
        elif user_choice2 == '2' : # Show MIME type vizualization
            mime_type_viz()
        elif user_choice2 == '3' : # Calculate and show max file size
            print(str('-'*50))
            print('Maximum file size: ' + str(max(file_size_lst)) + ' bytes')
        elif user_choice2 == '4' : # Calculate and show min file size
            print(str('-'*50))
            print('Minimum file size: ' + str(min(file_size_lst)) + ' bytes')
        elif user_choice2 == '5' : # Calculate and show average file size
            print(str('-'*50))
            print('Average file size: approx ' + str(total_file_size//file_size_count) + ' bytes')
    elif user_choice == '2' : # If user chooses 2, let them enter a PID
        while True:
            user_choice2 = input('Enter a PID: ')
            if user_choice2 in csvdict : # Has to be in the PID dictionary in order to continue
                break
        print(str('-'*50))
        print(str(csvdictviz(user_choice2))) # Show 'visualization' of PID data
    elif user_choice == '3' :
        print(helptext) # Show help text
    elif user_choice == '4' :
        break # Quit
    time.sleep(2) # Wait a little bit, then show return options
    while True:
        user_choice3 = input(linebreaker + ( # Menu that lets you start over or quit
'''1 - Return to Main Menu
2 - Quit
''') + linebreaker + ('Choose an option: '))
        if user_choice3 == '1' or user_choice3 == '2' :
            break
    if user_choice3 == '1' :
        continue
    elif user_choice3 == '2' :
        break