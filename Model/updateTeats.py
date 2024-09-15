import csv
import random

csv_path = "Model/cow_data.csv"


def update_teats(cowId):

    with open(csv_path, "r") as file:
        rows = list(csv.reader(file))

    header = rows[0]
    rows = rows[1:]

    updated = False
    for row in rows:
        if row[0] == cowId:
            teats = int(row[3])
            if teats == 4:
                if random.random() < 0.05:
                    teats -= 1
                    updated = True
            elif teats == 3:
                if random.random() < 0.2:
                    teats = 4
                    updated = True

            row[3] = str(teats)

    if updated:
        with open(csv_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        return True

    return False
