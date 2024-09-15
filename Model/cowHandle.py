import csv

csv_path = "Model/cow_data.csv"


def canMilkCow(cowId):
    # Open the CSV file
    with open(csv_path, "r") as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Iterate over each row in the CSV file
        for row in reader:
            # Check if the cow_id matches the id in the row
            if row[0] == cowId:
                # Check if the number of teats is in the appropriate column
                try:
                    teats = int(
                        row[3]
                    )
                    if teats == 4:
                        return True
                    else:
                        return False
                except ValueError:
                    raise ValueError("Teats count is not a valid number.")

    # If the cow is not found, raise a ValueError
    raise ValueError("Cow not found in the CSV file")
