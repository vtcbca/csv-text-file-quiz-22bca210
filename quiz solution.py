import csv

f=open('contact.csv','w',newline='')

w=csv.writer(f)

header=('name','contact')

w.writerow(header)
row=[['om',1122334455],['sai',1234567890],['ram',1231231230],['radha',9987654321],['kishan',9909876678]]
w.writerows(row)
f.close()

search_name = input("Enter the name to search for: ")

found = False

with open('Contact.csv', 'r',newline='') as file:
    for row in i:
        name, contact = row.strip().split(',')
        if search_name == name:
            print(f"Contact found: {name} - {contact}")
            found = True
            break

if not found:
    print("Contact not found.")
