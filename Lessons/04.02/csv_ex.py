import csv

# with open("test.csv", 'r+') as f:
#     for line in f:
#         print(line.split(','))
#     f.write('test, new test, etc')

with open("test.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for cell in row:
            print(cell)

with open("test.csv", 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["new val 1", "new val 2", "new val 3", "new, val 4", 14576896452345678])
    writer.writerows([[1,2,3],[4,5,6],[7,8,9]])

headline = ["color", "size", "season"]

with open("sneakers.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, headline)
    writer.writeheader()
    writer.writerow({"color":"black", "size":38, "season":"summer"})
    writer.writerow({"color":"red", "season":"summer", "size":37})

with open("sneakers.csv", 'r', newline='') as f:
    reader = csv.DictReader(f, headline)
    isFirst = True
    for row in reader:
        if isFirst:
            isFirst = False
            continue
        for key in headline:
            print(row[key])
