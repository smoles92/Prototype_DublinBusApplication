import requests
import json
import pandas as pd

# Retrieve Real Time Bus Information (for bus stop 1304 (which is my stop))
# # See section 3.4.1 of the document
base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid=2762&routeid=76&maxresults&operator&format=json'
response = requests.get(base_url)
results = response.json()
print(results)
counter = 1
for i in results['results']:
    print('Result Nº' + str(counter) + ':')
    print(i)
    counter += 1


# Retrieve Timetable Bus Information by Date
# See section 3.4.2 of the document
# So far, not yet working
# base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/timetableinformation?type=day&stopid=1304&routeid=17&datetime=2017-07-14 14:45:06&format=json'
# response = requests.get(base_url)
# results = response.json()
# print(results)
# for i in results['results']:
#     print(i)

# Retrieve Full Timetable Bus Information
# See section 3.4.3 of the document
# base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/timetableinformation?operator=bac&type=week&stopid=1304&routeid=17&format=json'
# response = requests.get(base_url)
# results = response.json()
# for i in results['results']:
#     print(i)


# Retrieve Bus Stop Information
# See section 3.4.4 of the document
# Leave stopid and stopname empty to get info on all stops. Fill in to get just that stop.
"""base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/busstopinformation?operator=bac&format=json'
response = requests.get(base_url)
data = response.json()
data2 = data['results'][8]
# data3 = data2['operators']
# df = pd.DataFrame(data2)
print(data2)
df.to_csv('results.csv')"""

# Retrieve Route Information
# See section 3.4.5 of the document
# Operator bac seems to equate to Dublin Bus.
"""base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/routeinformation?routeid=46A&operator=bac&format=json'
response = requests.get(base_url)
results = response.json()
stops = results['results'][0]
print(results['results'][0]['origin'], 'to', results['results'][0]['destination'])
print(results['results'][1]['origin'], 'to', results['results'][1]['destination'])
inbound = results['results'][0]
outbound = results['results'][1]
for in_stops in inbound['stops']:
    for out_stops in outbound['stops']:
        if in_stops['stopid'] == out_stops['stopid']:
            print(in_stops)"""

# Retrieve Operator Informator
# See section 3.4.6 of the document
"""base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/operatorinformation?format=json'
response = requests.get(base_url)
results = response.json()
for i in results['results']:
    print(i)"""

# Retrieve Route List Information
# See section 3.4.7 of the document
# base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/routelistinformation?operator=bac&format=json'
# response = requests.get(base_url)
# results = response.json()
# list_stops = []
# for i in results['results']:
#     if type(i['route']) == str:
#         list_stops.append(i['route'])
#     else:
#         print(i)
# list_stops = sorted(list_stops, key=str.lower)
# print(list_stops)
