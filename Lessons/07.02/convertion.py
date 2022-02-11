import csv, json, pickle

data_v1 = [
    {"model":"1.6", "year":1989, "horsepower":102},
    {"model":"1.8", "year":1986, "horsepower":75}
]

data_v2 = {
    "model": ["1.6", "1.8"],
    "year": [1989, 1986],
    "horsepower": [102, 75]
}

with open("test_v1.json", 'w') as f:
    json.dump(data_v1, f)

with open("test_v2.json", 'w') as f:
    json.dump(data_v2, f)

fieldnames = ["model", "year", "horsepower"]

with open("test_v1.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    writer.writerows(data_v1)

with open("test_v2.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldnames)
    for i in range(len(data_v2[fieldnames[0]])):
        current_line = []
        for headfield in fieldnames:
            current_line.append(data_v2[headfield][i])
        print(current_line)
        writer.writerow(current_line)

new_data_v1 = []
with open("test_v1.csv", 'r', newline='') as f:
    reader = csv.DictReader(f, fieldnames)
    for line in reader:
        new_data_v1.append(line)
print(new_data_v1)

with open('test_v1.pickle', 'wb') as f:
    pickle.dump(data_v1, f)

with open('test_v2.pickle', 'wb') as f:
    pickle.dump(data_v2, f)