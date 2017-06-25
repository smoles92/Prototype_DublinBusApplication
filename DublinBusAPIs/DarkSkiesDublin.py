import requests
import datetime

#base_url_forecast = 'https://api.darksky.net/forecast/5ccf6f7c005b5f1fd272b987e93349bc/53.3498,-6.2603?units=auto'
base_url_time_machine = 'https://api.darksky.net/forecast/5ccf6f7c005b5f1fd272b987e93349bc/53.3498, -6.2603,1352419200'
response = requests.get(base_url_time_machine)
results = response.json()
print(results)
counter = 0
for i in results['hourly']['data']:
    print(i)
    counter += 1
    print(counter)
print('Location:', results['timezone'])
print('Overall:', results['hourly']['summary'])
print('\n<<------------------------------>\n')
for i in results['hourly']['data']:
    date = datetime.datetime.fromtimestamp(i['time'])
    print('Time:', date)
    print('Summary:', i['summary'])
    print('Temperature:', str(i['temperature']) + 'º')
    print('Precipitation Probability:', i['precipProbability'])
    print('Precipitation Intensity:', i['precipIntensity'])
    print('Wind Speed:', str(i['windSpeed']) + 'km/h')
    print('\n<<------------------------------>\n')
