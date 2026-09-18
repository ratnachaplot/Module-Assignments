#Create a multi-command CLI app with ingest, run, evaluate, and report commands
import argparse
import csv

def ingest(filename):
    print(f"Ingesting file: {filename}")

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        rows = list(reader)

        print(f"Records loaded: {len(rows)}")

def validate_record(row):
    if row["name"] == "":
        return False

    if "@" not in row["email"]:
        return False

    if not row["age"].isdigit():
        return False

    return True

def calculate_statistics(filename):
    total_records = 0
    valid_records = 0
    invalid_records = 0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_records += 1

            if validate_record(row):
                valid_records += 1
            else:
                invalid_records += 1

    return total_records, valid_records, invalid_records

def run(filename):
    print(f"Processing file: {filename}")

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        valid_records = []
        invalid_records = []

        for row in reader:
            if validate_record(row):
                valid_records.append(row)
            else:
                invalid_records.append(row)

    with open("cleaned.csv", "w", newline="") as file:
        fieldnames = ["name", "email", "age"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for row in valid_records:
            writer.writerow(row)

    with open("errors.log", "w") as file:
        for row in invalid_records:
            file.write(f"Invalid record: {row}\n")

    print(f"Valid records: {len(valid_records)}")
    print(f"Invalid records: {len(invalid_records)}")
    print("Cleaned data written to cleaned.csv")
    print("Errors written to errors.log")

    return valid_records,invalid_records

def evaluate(filename):
    print(f"Evaluating file: {filename}")

    total_records, valid_records, invalid_records = calculate_statistics(filename)

    success_rate = (valid_records / total_records) * 100

    print(f"Total records: {total_records}")
    print(f"Valid records: {valid_records}")
    print(f"Invalid records: {invalid_records}")
    print(f"Success rate: {success_rate:.2f}%")

def report(filename):
    print("================================")
    print("        DATA CLEANING REPORT")
    print("================================")

    total_records, valid_records, invalid_records = calculate_statistics(filename)

    success_rate = (valid_records / total_records) * 100

    print(f"Input file       : {filename}")
    print(f"Total records    : {total_records}")
    print(f"Valid records    : {valid_records}")
    print(f"Invalid records  : {invalid_records}")
    print(f"Success rate     : {success_rate:.2f}%")
    print()
    print("Cleaned file     : cleaned.csv")
    print("Error log        : errors.log")
    print("================================")
    
parser = argparse.ArgumentParser()

parser.add_argument(
    "command",
    choices=["ingest", "run", "evaluate", "report"]
)

parser.add_argument(
    "filename",
    nargs="?"
)

args = parser.parse_args()

if not args.filename:
    print("Please provide a CSV filename")
    raise SystemExit(1)

if args.command == "ingest":
    ingest(args.filename)

elif args.command == "run":
    run(args.filename)

elif args.command == "evaluate":
    evaluate(args.filename)

elif args.command == "report":
    report(args.filename)