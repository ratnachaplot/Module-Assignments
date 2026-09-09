#Build a Python utility that ingests CSV or JSON, validates records, logs errors, and writes cleaned output

import csv
import logging

logging.basicConfig(
    filename="errors.log",
    filemode="w",
    level=logging.ERROR,
    format="%(levelname)s: %(message)s"
)

with open("input.csv", "r") as file:
    reader = csv.DictReader(file)

    with open("cleaned.csv", "w", newline="") as output_file:
        fieldnames = ["name", "email", "age"]

        writer = csv.DictWriter(
            output_file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for row_number, row in enumerate(reader, start=2):

            is_valid = True

            if row["name"] == "":
                logging.error(f"Row {row_number} - Name is missing")
                is_valid = False

            if "@" not in row["email"]:
                logging.error(f"Row {row_number} - Email is invalid")
                is_valid = False

            if not row["age"].isdigit():
                logging.error(f"Row {row_number} - Age is invalid")
                is_valid = False

            if is_valid:
                writer.writerow(row)
                print("This row is valid")
            else:
                print("This row is invalid")