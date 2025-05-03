import csv
import json

def csv_to_json():
    csv_file_path = "amazon_sales_data_2025.csv"
    json_file_path = "amazon_sales_data_2025.json"
    data = []

    try:
        with open(csv_file_path, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print(f"✅ Successfully converted {len(data)} rows from CSV to JSON.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    csv_to_json()
