Greek Calendar CLI Application

This Greek Calendar CLI is a Python-based command-line application that displays a calendar in Greek, allows navigation between months, and provides basic event management.

Features

Greek Language Support: The calendar displays months and days in Greek.

Monthly Navigation: Move between months with intuitive keyboard shortcuts.

Event Management: Add and view events for each selected month.

Usage Instructions

Run the Application:
python calendar_app.py

Navigate the Calendar:

Enter: Go to the next month.
"-": Return to the previous month.
"+": Add a new event.
"*": Display events for the current month.
"q": Quit the application.
Display Example: The calendar displays each day in [dd] format for the current month, while days outside the month are shown without brackets for easy distinction.

Code Breakdown
display_calendar(): Renders a Greek-labeled calendar for the specified month and year.
display_menu(): Shows user instructions, including available commands.
main_loop(): Manages input handling, navigates months, and creates events.

Dependencies
Python 3 (standard libraries datetime and calendar are used)
