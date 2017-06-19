import requests

# Retrieve Real Time Bus Information (for bus stop 1304 (which is my stop))
# See section 3.4.1 of the document
"""base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid=1304&routeid&maxresults&operator&format=json'
response = requests.get(base_url)
results = response.json()
counter = 1
for i in results['results']:
    print('Result Nº' + str(counter) + ':')
    print(i)
    counter += 1"""

# Retrieve Timetable Bus Information by Date
# See section 3.4.2 of the document
# So far, not yet working
"""base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/timetableinformation?type=day&stopid=1304&routeid=17&datetime=1497873600&format=json'
response = requests.get(base_url)
results = response.json()
print(results)
for i in results['results']:
    print(i)"""

# Retrieve Full Timetable Bus Information
# See section 3.4.3 of the document
"""base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/timetableinformation?type=week&stopid=1304&routeid=17&format=json'
response = requests.get(base_url)
results = response.json()
for i in results['results']:
    print(i)"""

# Retrieve Bus Stop Information
# See section 3.4.4 of the document
# Leave stopid and stopname empty to get info on all stops. Fill in to get just that stop.
"""base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/busstopinformation?stopid=1304&format=json'
response = requests.get(base_url)
results = response.json()
for i in results['results']:
    print(i)"""

# Retrieve Route Information
# See section 3.4.5 of the document
# Operator bac seems to equate to Dublin Bus.
base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/routeinformation?routeid=46A&operator=bac&format=json'
response = requests.get(base_url)
results = response.json()
stops = results['results'][0]
for i in stops['stops']:
    print(i)

# Retrieve Operator Informator
# See section 3.4.6 of the document
"""base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/operatorinformation?format=json'
response = requests.get(base_url)
results = response.json()
for i in results['results']:
    print(i)"""

# Retrieve Route List Information
# See section 3.4.7 of the document
"""base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/routelistinformation?operator=bac&format=json'
response = requests.get(base_url)
results = response.json()
for i in results['results']:
    print(i)"""

