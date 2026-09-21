import csv
from datetime import datetime
import calendar

def get_current_month_year():
    current_month = datetime.now().month
    current_year = datetime.now().year
    return current_month, current_year

def get_greek_month_names():
    greek_month_names = ['ΙΑΝ', 'ΦΕΒ', 'ΜΑΡ', 'ΑΠΡ', 'ΜΑΙ', 'ΙΟΥΝ', 'ΙΟΥΛ', 'ΑΥΓ', 'ΣΕΠ', 'ΟΚΤ', 'ΝΟΕ', 'ΔΕΚ']
    return greek_month_names

def get_calendar(year, month):
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    return cal.monthdatescalendar(year, month)

def get_max_chars(calendar_month):
    max_chars = len(str(max(day.day for week in calendar_month for day in week)))
    return max_chars

def print_calendar_header(month_name, year):
    print("_" * 62)
    print()
    print(f"{month_name} {year}")
    print()
    print("_" * 62)
    print()
def print_days_of_week(days_of_week_gr, max_chars):
    """
    Εμφανίζει τις ημέρες της εβδομάδας    
    """
    print("  |  ".join(day.rjust(max_chars + 2) for day in days_of_week_gr))
    print()

def print_calendar(calendar_month, month, list_of_event_dates, max_chars):
    """
    Εμφανίζει το ημερολόγιο
    """
    for week in calendar_month:
        dates = []
        for day in week:
            if day.month == month:
                if list_of_event_dates != []:
                    flag=False
                    day_=str(day)
                    for i in range(len(list_of_event_dates)):
                        if flag == False:
                            if day_ == list_of_event_dates[i]:
                                dates.append(f"[{'*'}{day.day:2d}]".rjust(max_chars + 4))
                                flag=True
                    if flag==False:
                        dates.append(f"[ {day.day:2d}]".rjust(max_chars + 4))
                else:
                    dates.append(f"[ {day.day:2d}]".rjust(max_chars + 4))
            else:
                dates.append(f" {day.day:2d} ".rjust(max_chars + 4))
        print(" | ".join(dates).rjust(21))

def print_instructions():
    """
    Εμφανίζει τις οδηγίες χρήσης του ημερολογίου
    """
    print("_" * 62)
    print()
    print("Πατήστε ENTER για προβολή του επόμενου μήνα, \"q\" για έξοδο ή κάποια από τιςπαρακάτω επιλογές:\n\" - \"  για πλοήγηση στον προηγούμενο μήνα\n\" + \"  για διαχείριση των γεγονότων του ημερολογίου\n\" * \"  για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα")

def display_submenu():
    print("Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:")
    print("1 Καταγραφή νέου γεγονότος")
    print("2 Διαγραφή γεγονότος")
    print("3 Ενημέρωση γεγονότος")
    print("0 Επιστροφή στο κυρίως μενού")

def add_event(list_of_event_dates):
    # Ελέγχει αν υπάρχει το αρχείο events.csv
    try:
        with open('events.csv', 'r') as csvfile:
            pass
    except FileNotFoundError:
        # Αν δεν υπάρχει το αρχείο, δημιουργεί νέο αρχείο CSV
        with open('events.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['date', 'time', 'duration', 'title'])
    while True:
        # Λαμβάνει την ημερομηνία του γεγονότος από τον χρήστη
        date = input("Ημερομηνία γεγονότος (YYYY-MM-DD): ")
        # Γίνεται έλεγχος εγκυρότητας για την ημερομηνία
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Μη έγκυρη μορφή ημερομηνίας. Πληκτρολογήστε την ημερομηνία με τη μορφή: YYYY-MM-DD.")
    list_of_event_dates += [date]
    
    while True:
        # Λαμβάνει την ώρα του γεγονότος από τον χρήστη
        hour = input("Ώρα γεγονότος (HH:MM): ")
        # Γίνεται έλεγχος εγκυρότητας για την ώρα
        try:
            datetime.strptime(hour, "%H:%M")
            break
        except ValueError:
            print("Μη έγκυρη μορφή ώρας. Πληκτρολογήστε την ώρα με τη μορφή: HH:MM.")
    while True:
        # Λαμβάνει την διάρκεια του γεγονότος από τον χρήστη
        duration = input("Διάρκεια γεγονότος (σε λεπτά): ")
        try:
            # Ελέγχει αν η ώρα που έλαβε είναι θετική
            duration = int(duration)
            if duration < 0:
                raise ValueError
            break
        except ValueError:
            print("Μη έγκυρη μορφή διάρκειας. Πληκτρολογήστε ένα θετικό αριθμό.")
    title = input("Τίτλος γεγονότος: ")
    # Εισάγει τις λεπτομέρειες του γεγονότος στο csv αρχείο
    with open('events.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([date, hour, duration, title])
    print("Το γεγονός προστέθηκε στο ημερολόγιο.")
    return list_of_event_dates
def edit_event(list_of_event_dates):
    # Ζητά από τον χρήστη να εισάγει το έτος και τον μήνα του γεγονότος προς ενημέρωση
    year = input("Εισάγετε το έτος του γεγονότος προς ενημέρωση: ")
    month = input("Εισάγετε τον μήνα του γεγονότος προς ενημέρωση (01-12): ")

    # Αναζητά τα γεγονότα του επιλεγμένου μήνα
    events = search_events(year, month)
    if not events:
        print("Δεν υπάρχουν γεγονότα κατά τη διάρκεια του μήνα που επιλέξατε.")
        return list_of_event_dates

    # Εμφανίζει τα γεγονότα που βρέθηκαν
    for index, event in enumerate(events):
        print(f"{index}. {event['title']} -> Ημερομηνία: {event['date']}, Ώρα: {event['time']}, Διάρκεια: {event['duration']}")

    # Ζητά από τον χρήστη να επιλέξει γεγονός προς ενημέρωση
    event_index = input("Επιλέξτε γεγονός προς ενημέρωση: ")
    try:
        event_index = int(event_index)
        if event_index < 0 or event_index >= len(events):
            raise ValueError
    except ValueError:
        print("Μη έγκυρος αριθμός γεγονότος. Προσπαθήστε ξανά.")
        return list_of_event_dates
        
    event = events[event_index]
    
    # ΑΠΟΘΗΚΕΥΣΗ ΑΡΧΙΚΩΝ ΤΙΜΩΝ: Τις κρατάμε για να βρούμε τη σωστή γραμμή στο CSV
    orig_date = event['date']
    orig_time = event['time']
    orig_duration = str(event['duration'])
    orig_title = event['title']
    
    event_date = datetime.strptime(event['date'], '%Y-%m-%d')
    event_time = datetime.strptime(event['time'], '%H:%M')
    
    date = input(f"Ημερομηνία γεγονότος ({event_date.strftime('%Y-%m-%d')}): ")
    if date:
        if orig_date in list_of_event_dates:
            list_of_event_dates.remove(orig_date)
        list_of_event_dates.append(date)
        event['date'] = date
    else:
        event['date'] = event_date.strftime('%Y-%m-%d')
        
    time = input(f"Ώρα γεγονότος ({event_time.strftime('%H:%M')}): ")
    if time:
        event['time'] = time
    else:
        event['time'] = event_time.strftime('%H:%M')
        
    duration = input(f"Διάρκεια γεγονότος ({event['duration']}): ")
    if duration:
        event['duration'] = duration
        
    title = input(f"Τίτλος γεγονότος ({event['title']}): ")
    if title:
        event['title'] = title

    with open("events.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        events_list = list(reader)
        
    # Ενημερώνει το γεγονός στο αρχείο CSV ψάχνοντας τις αρχικές τιμές
    with open("events.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        updated = False
        for row in events_list:
            if len(row) < 4:
                continue
            # Αν βρούμε την ακριβή αρχική εγγραφή (και δεν την έχουμε ήδη ενημερώσει)
            if not updated and row[0] == orig_date and row[1] == orig_time and row[2] == orig_duration and row[3] == orig_title:
                writer.writerow([event['date'], event['time'], event['duration'], event['title']])
                updated = True
            else:
                writer.writerow(row)
                
    print(f"Το γεγονός {event['title']} ενημερώθηκε.")
    return list_of_event_dates


def delete_event(list_of_event_dates):
    # Ζητά από τον χρήστη να εισάγει το έτος και τον μήνα του γεγονότος προς διαγραφή
    year = input("Εισάγετε το έτος του γεγονότος προς διαγραφή: ")
    month = input("Εισάγετε τον μήνα του γεγονότος προς διαγραφή (01-12): ")

    # Αναζητά τα γεγονότα του επιλεγμένου μήνα
    events = search_events(year, month)
    if not events:
        print("Δεν υπάρχουν γεγονότα κατά τη διάρκεια του μήνα που επιλέξατε.")
        return

    # Εμφανίζει τα γεγονότα που βρέθηκαν
    for index, event in enumerate(events):
        print(f"{index}. {event['title']} -> Ημερομηνία: {event['date']}, Ώρα: {event['time']}, Διάρκεια: {event['duration']}")

    # Ζητά από τον χρήστη να εισάγει γεγονός προς διαγραφή
    event_index = input("Επιλέξτε γεγονός προς διαγραφή: ")
    try:
        event_index = int(event_index)
        if event_index < 0 or event_index >= len(events):
            raise ValueError
    except ValueError:
        print("Μη έγκυρος αριθμός γεγονότος. Προσπαθήστε ξανά.")
        return

    event = events[event_index]
    with open("events.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        events_list = list(reader)
    # Διαφράφει το επιλεγμένο γεγονός από το αρχείο CSV    
    with open("events.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in events_list:
            if row[3] != event['title']:
                writer.writerow(row)
            else:
                list_of_event_dates.remove(event['date'])
    print(f"Το γεγονός {event['title']} διαγράφηκε.")

    # Ενημερώνει τη λίστα γεγονότων
    events = search_events(year, month)
    for index, event in enumerate(events):
        print(f"{index}. {event['title']} -> Ημερομηνία: {event['date']}, Ώρα: {event['time']}, Διάρκεια: {event['duration']}")
    input("Πατήστε ENTER για επιστροφή στο κυρίως μενού: ")

def search_events(year, month):
    events = []
    try:
        with open('events.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 4:
                    continue
                event = {'date': row[0], 'time': row[1], 'duration': row[2], 'title': row[3]}
                if event['date'].startswith(f"{year}-{month}"):
                    events.append(event)
    except FileNotFoundError:
        # Αν το αρχείο δεν έχει δημιουργηθεί ακόμα, δεν υπάρχει πρόβλημα
        pass
    return events

def show_events_by_month():
    year = input("Εισάγετε έτος: ")
    month = input("Εισάγετε μήνα (01-12): ")
    events = search_events(year, month)
    if not events:
        print("Δεν υπάρχουν γεγονότα κατά τη διάρκεια του επιλεγμένου μήνα.")
        return
    for index, event in enumerate(events):
        print(f"{index}. {event['title']} -> Date: {event['date']}, Time: {event['time']}, Duration: {event['duration']}")
    input("Πατήστε ENTER για επιστροφή στο κυρίως μενού: ")

def main():
    list_of_event_dates=[]
    # Ελέγχει αν υπάρχει το αρχείο events.csv
    try:
        with open('events.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                list_of_event_dates+=row
    except FileNotFoundError:
        pass
        
    current_month, current_year = get_current_month_year()
    greek_month_names = get_greek_month_names()
    while True:
        month_name = greek_month_names[current_month - 1][:3]
        print_calendar_header(month_name, current_year)
        days_of_week_gr = [' ΔΕΥ ', 'ΤΡΙ', 'ΤΕΤ', 'ΠΕΜ', 'ΠΑΡ', 'ΣΑΒ', 'ΚΥΡ']
        calendar_month = get_calendar(current_year, current_month)
        max_chars = get_max_chars(calendar_month)
        print_days_of_week(days_of_week_gr, max_chars)
        print_calendar(calendar_month, current_month, list_of_event_dates, max_chars)
        print_instructions()
        user_input = input()
        if user_input == "+":
            display_submenu()
            # Ζητα από τον χρήστη να επιλέξει ενέργεια
            user_input = input()
            
            if user_input == '1':
            # Εισάγει νέο γεγονός στο ημερολόγιο καλώντας τη συνάρτηση add_event με όρισμα τη λίστα των ημερομηνιών με γεγονότα   
                list_of_event_dates = add_event(list_of_event_dates)
                                
            elif user_input == '2':
            # Διαγράφει γεγονός από το ημερολόγιο καλώντας τη συνάρτηση delete_event με όρισμα τη λίστα των ημερομηνιών με γεγονότα
                delete_event(list_of_event_dates)
                                
            elif user_input == '3':
                # Ενημερώνει γεγονός του ημερολογίου καλώντας τη συνάρτηση edit_event με όρισμα τη λίστα των ημερομηνιών με γεγονότα
                edit_event(list_of_event_dates)
                                
            elif user_input == '0':
            # Επιστρέφει στο κυρίως μενού    
                pass
        elif user_input == "":
            current_month += 1
            if current_month > 12:
                current_month = 1
                current_year += 1
        elif user_input == "-":
            current_month -= 1
            if current_month < 1:
                current_month = 12
                current_year -= 1
        elif user_input == "*":
            
            show_events_by_month()
        elif user_input == "q":
            return

if __name__ == "__main__":
    main()
