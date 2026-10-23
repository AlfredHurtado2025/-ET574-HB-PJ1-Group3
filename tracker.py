import Data

def add_session():
    appName = input("Enter app/site name: ")
    Minutes = int(input("Enter minutes spent: "))
    category = input("Enter category (Social/School/Entertaimnet/Other): ")
    Notes = input("Enter notes (Optional): ")
    print("Session added")

    Data.could[0].append(appName)
    Data.cloud[1].append(Minutes)
    Data.cloud[2].append(category)


def view_all():
    length = len(Data.cloud[1])
    for level in range(0, length):
        print("Section" + str(Data.cloud[level]))
