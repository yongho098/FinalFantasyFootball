import json
import os
import csv

def asdf():
    out = []
    with open('output.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            out.append(row)
        print(out)

#
# with open('eligible.txt', 'w') as outfile:
#     json.dump(data, outfile)

# with open('eligible2.txt') as json_file:
#     data = json.load(json_file)
#     for i in data:
#         print(i)
#         print(len(data))

# def tests():
#     outss = open('output.csv', 'w', newline='')
#     outputDictWriter = csv.DictWriter(outss, ['Team', 'Name', 'Role', 'Class', 'World', 'FFlogs', 'Note'])
#     outputDictWriter.writeheader()
#     outputDictWriter.writerow({'Name': 'asdf', 'Role': 'ddd', 'Class': 'x', 'World': 12, 'FFlogs': 2})
#     outputFile.close()

asdf()
