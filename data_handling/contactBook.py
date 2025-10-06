import csv
import os
import time
import psutil, os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open (FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])
        
def add_contact():
    name = input('Name:').strip()
    phone = input('Phone:').strip()
    email = input('Email:').strip()

    # check for duplicates
    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists")
                return
    with open(FILENAME, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added")

def view_contacts():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows)<1:
            print("No contacts found")
            return
        
        print("\n Your contacts: \n")
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = True
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row["Name"]} | Phone: {row["Phone"]}")
                found = True
    if not found:
        print('No matching record found')

def main():
    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4)").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thanks for using our software")
            time.sleep(1)
            process = psutil.Process(os.getpid())
            print(f"Memory usage: {process.memory_info().rss / (1024 * 1024):.2f} MB")
            break
        else:
            print("Invalid choice of number")

if __name__ == "__main__":
    main()
