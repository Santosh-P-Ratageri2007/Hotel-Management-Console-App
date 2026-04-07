# ==========================================
# FINAL MICRO-PROJECT - HOTEL MANAGEMENT SYSTEM
# ==========================================

# ------------------------------------------
# Week 3 – Basic Logic, Functions, Conditions
# Contributors:
# Abhishek (Strings), Shreya (Conditionals),
# Santosh & Jaysree (Menu + Flow),
# Dhanush & Anuradha (Core Logic)
# ------------------------------------------

hotel_name = "Grand Hotel"

# ------------------------------------------
# Week 4 – Data Structures (List, Tuple, Dictionary)
# Abhishek & Shreya – Tuple
# ------------------------------------------
room_types = ("Single", "Double", "Deluxe")

# Rooms list
rooms = [101, 102, 103, 104, 105]

# Dictionary for room details
room_details = {
    101: {"Type": "Single", "Price": 2000, "Status": "Available"},
    102: {"Type": "Double", "Price": 3000, "Status": "Available"},
    103: {"Type": "Deluxe", "Price": 5000, "Status": "Available"},
    104: {"Type": "Single", "Price": 2000, "Status": "Available"},
    105: {"Type": "Deluxe", "Price": 5000, "Status": "Available"}
}

# Track booking, payment, check-in
booked_rooms = []
payments_done = []
checked_in_rooms = []

# ------------------------------------------
# Week 5 – File Handling + Exception Handling
# Anuradha – File Handling
# Abhishek – Exception Handling
# ------------------------------------------
file_name = "hotel_data.txt"


# ------------------------------------------
# View Rooms (Santosh)
# ------------------------------------------
def view_rooms():
    print("\nWelcome to", hotel_name.upper())
    print("Available Rooms:")
    for r in rooms:
        if room_details[r]["Status"] == "Available":
            print("Room:", r, "| Type:", room_details[r]["Type"])


# ------------------------------------------
# Book Room (Dhanush + Shreya)
# ------------------------------------------
def book_room():
    try:
        r = int(input("Enter room number to book: "))
        
        if r in room_details:
            if room_details[r]["Status"] == "Available":
                name = input("Enter guest name: ")
                
                room_details[r]["Status"] = "Booked"
                room_details[r]["Guest"] = name
                booked_rooms.append(r)

                # String usage (Abhishek)
                print(name + " booked Room " + str(r))

                file = open(file_name, "a")
                file.write(f"Booked: Room {r}, Guest: {name}\n")
                file.close()

            else:
                print("Room already booked!")
        else:
            print("Invalid room!")

    except ValueError:
        print("Invalid input!")


# ------------------------------------------
# Payment (Anuradha + Abhishek)
# ------------------------------------------
def payment():
    try:
        r = int(input("Enter room number: "))

        if r in booked_rooms:

            days = int(input("Enter number of days: "))
            price = room_details[r]["Price"]
            total = days * price

            print("Total Payment:", total)

            payments_done.append(r)

            file = open(file_name, "a")
            file.write(f"Payment: Room {r}, Amount: {total}\n")
            file.close()

        else:
            print("Room not booked!")

    except ValueError:
        print("Invalid input!")


# ------------------------------------------
# Check In (Santosh & Jaysree)
# ------------------------------------------
def check_in():
    try:
        r = int(input("Enter room number to check-in: "))

        if r in booked_rooms:
            if r in payments_done:
                if r not in checked_in_rooms:
                    checked_in_rooms.append(r)
                    room_details[r]["Status"] = "Occupied"
                    print("Checked into room", r)
                else:
                    print("Already checked in!")
            else:
                print("Please complete payment first!")
        else:
            print("Room not booked!")

    except ValueError:
        print("Invalid input!")


# ------------------------------------------
# Check Out (Dhanush)
# ------------------------------------------
def check_out():
    try:
        r = int(input("Enter room number to check-out: "))

        if r in checked_in_rooms:

            print("Checked out:", room_details[r].get("Guest", "Guest"))

            checked_in_rooms.remove(r)
            booked_rooms.remove(r)
            if r in payments_done:
                payments_done.remove(r)

            room_details[r]["Status"] = "Available"
            room_details[r].pop("Guest", None)

            file = open(file_name, "a")
            file.write(f"Checked Out: Room {r}\n")
            file.close()

        else:
            print("Room not checked in!")

    except ValueError:
        print("Invalid input!")


# ------------------------------------------
# Menu System (Santosh & Jaysree)
# ------------------------------------------
while True:

    print("\n----- HOTEL MANAGEMENT MENU -----")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. Payment")
    print("4. Check In")
    print("5. Check Out")
    print("0. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            view_rooms()

        elif choice == 2:
            book_room()

        elif choice == 3:
            payment()

        elif choice == 4:
            check_in()

        elif choice == 5:
            check_out()

        elif choice == 0:
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")
