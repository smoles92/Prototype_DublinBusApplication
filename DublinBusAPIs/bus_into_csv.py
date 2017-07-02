import requests
import csv

# Retrieve Real Time Bus Information (for bus stop 1304 (which is my stop))
# See section 3.4.1 of the document
base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid=763&routeid=46a&maxresults&operator&format=json'
response = requests.get(base_url)
results = response.json()
csv_file = open('C:\/Users\lucas\Desktop\Codex\/UnivDublin\SummerProject\BusData46A.csv', 'w', newline='')
csvwriter = csv.writer(csv_file)
counter = 0

for i in results['results']:
    if counter == 5:
        break
    if counter == 0:
        header = i.keys()
        csvwriter.writerow(header)
    counter += 1
    csvwriter.writerow(i.values())
    print('Result Nº' + str(counter) + ':')
    print(i)

csv_file.close()
