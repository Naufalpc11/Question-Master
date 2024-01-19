import json

from utility import Utility

def calculate_total_scores(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    total_score = 0

    for key in data:
        scores = data[key]
        for score_entry in scores:
            total_score += score_entry['score']

    return total_score

# Path ke file JSON Anda
file_path = Utility.getFile("skor.json")

total_scores = calculate_total_scores(file_path)
print(f"Total skor dari semua kelas: {total_scores}")
