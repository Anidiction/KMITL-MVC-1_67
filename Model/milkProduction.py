import csv

csv_path = "Model/cow_data.csv"

def calculate_milk(cowId):
    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == cowId:
                try:
                    age_years = int(row[1])
                    age_months = int(row[2])
                    
                    milk_production = age_years + age_months
                    
                    return milk_production
                
                except ValueError:
                    raise ValueError("Age is not a valid number.")

    raise ValueError("Cow not found in the CSV file")
