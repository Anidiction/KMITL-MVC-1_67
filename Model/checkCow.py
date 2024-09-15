import csv

csv_path = "Model/cow_data.csv"


def IsCow(cowId):
    # Open the CSV file
    with open(csv_path, "r") as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Skip the first row
        next(reader)

        # Iterate over each row in the CSV file
        for row in reader:
            # Check if the cow_id matches the id in the row
            if row[0] == cowId:
                # Check if other columns are empty
                if all(cell == "" for cell in row[1:]):
                    return False
                else:
                    return True

    # If the cow or goat is not found, raise a ValueError
    raise ValueError("Cow or goat not found in the database")
