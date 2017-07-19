# from dublinbusjourney.dublinbuspredict.Algorithms.bus_location_finder import main_bus_finder
from .bus_location_finder import main_bus_finder
from datetime import datetime, timedelta
from dateutil import parser
import requests
from .model_prototype_0 import model
# from dublinbusjourney.dublinbuspredict.Algorithms.model_prototype_0 import model
import time

def holidays(date):
    publicholidays_2017 = ['2017-08-07', '2017-10-30', '2017-12-25', '2017-12-26',
                        '2017-12-27']
    schoolholidays_2017 = ['2017-07-07', '2017-08-07', '2017-09-07', '2017-10-07',
                        '2017-11-07', '2017-12-07', '2017-07-13', '2017-07-14',
                        '2017-07-15', '2017-07-16', '2017-07-17', '2017-07-18',
                        '2017-07-19', '2017-07-20', '2017-07-21', '2017-07-22',
                        '2017-07-23', '2017-07-24', '2017-07-25', '2017-07-26',
                        '2017-07-27', '2017-07-28', '2017-07-29', '2017-07-30',
                        '2017-07-31', '2017-01-08', '2017-02-08', '2017-03-08',
                        '2017-04-08', '2017-05-08', '2017-06-08', '2017-07-08',
                        '2017-08-08', '2017-09-08', '2017-10-08', '2017-11-08',
                        '2017-12-08', '2017-08-13', '2017-08-14', '2017-08-15',
                        '2017-08-16', '2017-08-17', '2017-08-18', '2017-08-19',
                        '2017-08-20', '2017-08-21', '2017-08-22', '2017-08-23',
                        '2017-08-24', '2017-08-25', '2017-08-26', '2017-08-27',
                        '2017-08-28', '2017-08-29', '2017-08-30', '2017-08-31',
                        '2017-10-28', '2017-10-29', '2017-10-30', '2017-10-31',
                        '2017-01-11', '2017-02-11', '2017-03-11', '2017-04-11',
                        '2017-05-11', '2017-12-23', '2017-12-24', '2017-12-25',
                        '2017-12-26', '2017-12-27', '2017-12-28', '2017-12-29',
                        '2017-12-30', '2017-12-31']
    date = date[6:10] + '-' + date[3:5] + '-' + date[:2]
    p_holiday = False
    s_holiday = False
    if date in publicholidays_2017:
        p_holiday = True
    if date in schoolholidays_2017:
        s_holiday = True
    return p_holiday, s_holiday


def weather():
    base_url_time_machine = 'http://api.wunderground.com/api/c59c002ced7bb1cb/conditions/q/IE/Dublin.json'
    response = requests.get(base_url_time_machine)
    results = response.json()
    return results['current_observation']['precip_1hr_metric'][1:]
    # for i in results['current_observation']:
    #     print(i)


def time_to_arrive(datetime, sec):
    #year = (int(datetime[6:10]) * 31556926) + (int(datetime[3:5]) * 2629743.83) + (int(datetime[:2]) * 86400) + (int(datetime[11:13]) * 3600) + (int(datetime[14:16]) * 60) + (int(datetime[17:]))
    new_time = datetime + timedelta(seconds=sec)
    new_time = new_time.strftime('%d/%m/%Y %H:%M:%S')
    return new_time


def treat_data(data, source_stop):
    cleaned = []
    for i in data:
        # x = i[0]['predicted_arrival_time']
        # x = parser.parse(x)
        # print('First time:', x)
        found = False
        for j in i:
            # print(j, source_stop)
            if str(j['stopid']) == str(source_stop):
                x = j['predicted_arrival_time']
                x = parser.parse(x)
                found = True
            if found:
                y = j['predicted_arrival_time']
                y = parser.parse(y)
                print(x)
                print('Matching against:', y)
                # print('Printing data here:', j)
                if x < y:
                    # Minus and get it in seconds and then convert to minues
                    journey_time = (y - x)
                    print('Journey time:', journey_time)
                    j['journey_time'] = str(journey_time)
                elif y < x:
                    # Minus and get it in seconds and then convert to minues
                    journey_time = (x - y)
                    print('Journey time:', journey_time)
                    j['journey_time'] = str(journey_time)
                else:
                    journey_time = (x - y)
                    j['journey_time'] = str(journey_time)
                j.pop('previous_stop', None)
                j.pop('datetime', None)
                j.pop('delay', None)
                j.pop('duration', None)
                j.pop('arrival_hour', None)
                print('Printing data here:', j)
                cleaned.append(j)
    bus3, bus2, bus1 = [], [], []
    # for i in range(0, len(data)):
    #     if i % 2 == 1:
    #         if len(bus1) != 2 and i <= 1:
    #             bus1.append((data[i - 1], data[i]))
    #         elif len(bus2) != 2 and i <= 3:
    #             bus2.append((data[i - 1], data[i]))
    #         elif len(bus1) != 2:
    #             bus3.append((data[i - 1], data[i]))
    # print('Bus 1:', bus1)
    # print('Bus 2:', bus2)
    # print('Bus 3:', bus3)
    # total_buses = [bus1, bus2, bus3]
    # clean = [x for x in total_buses if x != []]
    # ready_data = []
    # x = (data[0][0])['predicted_arrival_time']
    # x = parser.parse(x)
    # # Get journey times
    # if len(bus1) != 0:
    #     for i in data:
    #         # Arrival at source
    #         print('WOOOOOOOW!', i[0][0])
    #         print('x:', x)
    #         # Arrival at destination
    #         y = (i[0])['predicted_arrival_time']
    #         y = parser.parse(y)
    #         print('y', y)
    #         if x < y:
    #         # Minus and get it in seconds and then convert to minues
    #             print(x, 'minus', y)
    #             journey_time = (y - x)
    #         elif y < x:
    #             # Minus and get it in seconds and then convert to minues
    #             print(y, 'minus', x)
    #             journey_time = (x - y)
    #         i[0]
    #         print('Journey time is', journey_time, 'minutes.')
    return cleaned


def main(bus_route, source_stop, destination_stop):
    print(time.time())
    source_stop = source_stop
    destination_stop = destination_stop
    bus_route = bus_route
    print("Inside central:", bus_route, source_stop, destination_stop)
    information_from_bus_finder = main_bus_finder(destination_stop, bus_route)
    if type(information_from_bus_finder) == str:
        print(information_from_bus_finder)
        return information_from_bus_finder
    rain = weather()
    # buses_for_website = []
    # bus = []
    for i in information_from_bus_finder:
        for j in i:
            delay = j['delay']
            hour = j['arrival_hour']
            weekday = datetime.weekday(parser.parse(j['datetime']))
            holiday = holidays(j['datetime'])
            p_holiday = holiday[0]
            s_holiday = holiday[1]
            # print(delay, hour, weekday, p_holiday, s_holiday, rain)
            j['duration'] = (model(delay, hour, weekday, p_holiday, s_holiday, rain))[0]
            j['predicted_arrival_time'] = (time_to_arrive(parser.parse(j['datetime']), j['duration']))
            if str(j['stopid']) == source_stop:
                j['status'] = 'src'
            elif str(j['stopid']) == destination_stop:
                j['status'] = 'dest'
            else:
                j['status'] = 'normal'

    #     # buses_for_website.append(bus)
    # print(time.time())
    # print(bus)
    clean = treat_data(information_from_bus_finder, source_stop)
    print(clean)
    return clean

if __name__ == '__main__':
    bus_route = '76'
    source_stop = '2118'
    destination_stop = '2120'
    main(bus_route, source_stop, destination_stop)
