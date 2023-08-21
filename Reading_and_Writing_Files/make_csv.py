import csv 
from faker import Faker


def make_csv():
    with open("mycsv.csv", "w") as file:
        mywriter = csv.writer(file)
        header = ["name", "street_address", "city"]
        mywriter.writerow(header)
        fake = Faker()
        for i in range(1000):
            row = [fake.name(),fake.street_address(), fake.city()]
            mywriter.writerow(row)

            
if __name__ == "__main__":
    make_csv()


