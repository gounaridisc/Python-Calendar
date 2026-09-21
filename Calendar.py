from datetime import datetime
import datetime
# Get the current month and year
now = datetime.datetime.now()
current_month = now.month
current_year = now.year


import calendar

# Define a list with the Greek names of the months
greek_month_names = ['ΙΑΝ', 'ΦΕΒ', 'ΜΑΡ', 'ΑΠΡ', 'ΜΑΙ', 'ΙΟΥΝ', 'ΙΟΥΛ', 'ΑΥΓ', 'ΣΕΠ', 'ΟΚΤ', 'ΝΟΕ', 'ΔΕΚ']

# Define a list with the Greek names of the days of the week
days_of_week_gr = ['ΔΕΥ', 'ΤΡΙ', 'ΤΕΤ', 'ΠΕΜ', 'ΠΑΡ', 'ΣΑΒ', 'ΚΥΡ']

# Create a calendar object with the first day of the week set to Monday
cal = calendar.Calendar(firstweekday=calendar.MONDAY)

# Initialize an empty list to store the events
events = []

def display_calendar(current_month, current_year):
    """
    Display the calendar for the specified month and year.
    """
    # Calculate the maximum number of characters that the dates will occupy
    max_chars = len(str(max(day.day for week in cal.monthdatescalendar(current_year, current_month) for day in week)))

    # Clear the screen to display only the calendar and the menu
    print('\033[H\033[J')

    # Print the month and year
    print("_" * 100)
    print()
    print(f"{greek_month_names[current_month - 1][:3]} {current_year}")
    print()
    print("_" * 100)
    print()

    # Print the Greek names of the days of the week, right-aligning them using the calculated width
    print(" | ".join(day.rjust(max_chars + 2) for day in days_of_week_gr))
    # Add a newline to separate the rows
    print()

        # Print the calendar
    for week in cal.monthdatescalendar(current_year, current_month):
        # Initialize an empty list to store the dates for the current week
        dates = []
        for day in week:
            if day.month == current_month:
                # If the day is part of the current month, add it to the dates list in brackets and right-align it using the calculated width
                dates.append(f"[{day.day:2d}]".rjust(max_chars + 2))
            else:
                # If the day is not part of the current month, print the day of the month and right-align it using the calculated width
                dates.append(f" {day.day:2d} ".rjust(max_chars + 2))
        # Print the dates for the current week, right-aligning the whole string using the calculated width
        print(" | ".join(dates).rjust(21))

def display_menu(current_month, current_year):
    """
    Display the instructions for the user.
    """
    # Print the instructions for the user
    print("_" * 100)
    print()
    print("Press ENTER to go to the next month, \"q\" to exit or one of the following:\n\" - \"   to return to the past month\n\" + \"  to create a new event\n\" * \"   to show the events of the selected month\n→")


def main_loop(current_month, current_year):
    while True:
        # Display the calendar and the menu
        display_calendar(current_month, current_year)
        display_menu(current_month, current_year)

        # Get the user input
        user_input = input()

        if user_input == "":
            # If the user presses the enter key, go to the next month
            current_month += 1
            if current_month > 12:
                current_month = 1
                current_year += 1
        elif user_input == "-":
            # If the user enters "-", go to the previous month
            current_month -= 1
            if current_month < 1:
                current_month = 12
                current_year -= 1
        elif user_input == "q":
            # If the user enters "q", exit the loop and end the program
            break
        elif user_input == "+":
            # If the user enters "+", create a new event
            create_event(current_month, current_year)


if __name__ == "__main__":
    # Call the main loop function
    main_loop(current_month, current_year)
