import json
import csv

with open("data.json", "r", encoding="UTF8") as f_json:
    nombres = json.load(f_json)

with open("data.csv", "w", newline="", encoding="utf-8") as f_csv:
    ecrivain_csv = csv.writer(f_csv)
    ecrivain_csv.writerow(["reel", "imaginaire"])
    for nmb in nombres:
        ecrivain_csv.writerow(nmb)