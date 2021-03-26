# write a programme to read specific columns of a given csv file and print the content of the column

import csv

header = ["place", "name", "age"]
with open("city.csv", "w") as file:
    write = csv.DictWriter(file, fieldnames=header)
    write.writeheader()
    write.writerow({"place": "vatakara", "name": "chithra", "age": 21})
    write.writerow({"place": "malaparamb", "name": "Arya", "age": 21})
    write.writerow({"place": "iringal", "name": "swathi", "age": 23})
    write.writerow({"place": "Palakkaadu", "name": "Alen", "age": 13})
with open("city.csv", "r") as file:
    read = csv.DictReader(file);
    n = input("Enter the column name you want(place,name,age):")
    for i in read:
        print(i[n])