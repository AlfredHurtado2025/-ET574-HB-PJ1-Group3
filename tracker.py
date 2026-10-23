import Data


def add_session():
    appName = input("Enter app/site name: ")
    Minutes = int(input("Enter minutes spent: "))
    category = input("Enter category (Social/School/Entertaimnet/Other): ")
    Notes = input("Enter notes (Optional): ")
    print("Session added")

    Data.cloud[0].append(appName)
    Data.cloud[1].append(Minutes)
    Data.cloud[2].append(category)


def view_all():
    length = len(Data.cloud[1])
    for level in range(0, length):
        print("Section" + str(Data.cloud[level]))


def view_summary():
    total_minutes = sum(Data.cloud[1])
    total_session = len(Data.cloud[0])
    max_minutes = max(Data.cloud[1])
    min_minutes = max(Data.cloud[1])
    average_minutes = total_minutes / total_session
    print(f"Total Minutes: {total_minutes}")
    print(f"Total Sessions: {total_session}")
    print(f"Max Minutes: {max_minutes}")
    print(f"Min Minutes: {min_minutes}")
    print(f"Average Minutes: {average_minutes}")
