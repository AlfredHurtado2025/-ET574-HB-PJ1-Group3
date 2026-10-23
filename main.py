import tracker
import Data

while True:

    print('Welcome to Screen Time Tracker!')
    print()

    print(' 1. Add Screen Time Tracker!\n 2. view Summary\n 3. View All Session\n 4. Exit')

    choice = int(input("Enter Choice: "))

    if choice == 1:
        tracker.add_session()
    elif choice == 2:
        tracker.view_summary()
    elif choice == 3:
        tracker.view_all()
    elif choice == 4:
        break
    else:
        print('Invalid Input! Try Again.')
