import json

from django.http import HttpResponse
from django.shortcuts import render

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except:
    pass
from .models import PilotRoutes
from django.db.models import Q
from .Algorithms import project_central
import MySQLdb
import time
from datetime import datetime, timedelta

route_id, source_id, destination_id, direction = '56A', 1, 1, 1
new_info_buses = ['1']
old_info_buses = []
list_routes = ['1', '4', '7', '9', '11', '13', '14', '15', '16', '17', '18', '25', '27', '31', '32',
                   '33', '37', '38', '39', '40', '41', '42', '43', '44', '47', '49', '53', '59', '61', '63',
                   '65', '66', '67', '68', '69', '70', '75', '76', '79', '83', '84', '102', '104', '111',
                   '114', '116', '118', '122', '123', '130', '140', '142', '145', '150', '151', '161', '184',
                   '185', '220', '236', '238', '239', '270', '747', '757', '14C', '15A', '15B', '16C', '17A',
                   '25A', '25B', '25D', '25X', '26A', '27A', '27B', '27X', '29A', '31A', '31B', '31D', '32A', '32X',
                   '33A', '33B', '33X', '38A', '38B', '38D', '39A', '40B', '40D', '41A', '41B', '41C', '41X', '42D',
                   '44B', '45A', '46A', '46E', '51D', '51X', '54A', '56A', '65B', '66A', '66B', '66X', '67X', '68A',
                   '68X', '69X', '70D', '76A', '77A', '77X', '79A', '7A', '7B', '7D', '83A', '84A', '84X']



def index(request):
    global list_routes
    return render(request, 'dublinbuspredict/index.html', {'list_routes': list_routes})


def pilot_routes(request):
    route_id = request.GET.get('route')
    print(route_id)
    route_stops = PilotRoutes.objects.filter(route_id=route_id)
    stops = []
    for i in route_stops:
        stops.append(i.stop_id)
    print(stops)
    return HttpResponse(json.dumps({"stops":stops}), content_type='application/json')


def pilot_dest(request):
    source_id = request.GET.get('source')
    route_id = request.GET.get('route')
    print(source_id, route_id)
    global direction
    direction = PilotRoutes.objects.filter(Q(route_id=route_id) & Q(stop_id=str(source_id))).values_list('direction')[0][0]
    print(direction)
    bus_stops = PilotRoutes.objects.filter(Q(route_id=route_id) & Q(direction=direction))

    stops = []
    found = False
    for i in bus_stops:
        print(i.stop_id, source_id)
        if str(i.stop_id) == str(source_id):
            found = True
            continue
        if found:
            stops.append(i.stop_id)
    print(stops)
    return HttpResponse(json.dumps({"stops":stops}), content_type='application/json')


def run_model(request):
    global route_id
    global source_id
    global destination_id
    global new_info_buses
    route_id = request.GET.get('route')
    source_id = request.GET.get('source')
    destination_id = request.GET.get('destination')
    print(route_id, source_id, destination_id)
    new_info_buses = project_central.main(route_id, source_id, destination_id)
    print('In da views!')
    return render(request, 'dublinbuspredict/map.html', {'info_buses':new_info_buses})

def divs(request):
    global new_info_buses
    global old_info_buses
    while old_info_buses == new_info_buses:
        time.sleep(5)
        print('Same')
    old_info_buses = new_info_buses
    bus3, bus2, bus1 = [], [], []
    for i in range(0, len(new_info_buses)):
        if i % 2 == 1:
            if len(bus1) != 2:
                bus1.append((new_info_buses[i - 1], new_info_buses[i]))
            elif len(bus2) != 2:
                bus2.append((new_info_buses[i - 1], new_info_buses[i]))
            elif len(bus3) != 2:
                bus3.append((new_info_buses[i - 1], new_info_buses[i]))
    print('Bus 1:', bus1)
    print('Bus 2:', bus2)
    print('Bus 3:', bus3)
    total_buses = [bus1, bus2, bus3]
    clean = [x for x in total_buses if x != []]
    # Get journey times
    if len(bus1) != 0:
        for i in clean:
            # Arrival at source
            print('WOOOOOOOW!', i[0][0])
            x = [i][0][0]['predicted_arrival_time']
            x = datetime.strptime(x, '%H:%M:%S')
            # Arrival at destination
            y = [i][0][1]['predicted_arrival_time']
            y = datetime.strptime(y, '%H:%M:%S')
            # Minus and get it in seconds and then convert to minues
            journey_time =(y - x) * 60
            print('Journey time is', journey_time, 'minutes.')
    return HttpResponse(json.dumps({'list_routes': list_routes, 'info_buses': new_info_buses}), content_type='application/json')

def load_routes_for_map(request):
    global list_routes
    global source_id
    global route_id
    global destination_id
    global new_info_buses
    return HttpResponse(json.dumps({'list_routes': list_routes, 'info_buses': new_info_buses}), content_type='application/json')

def map(request):
    return render(request, 'dublinbuspredict/map.html')

def connections(request):
    return render(request, 'dublinbuspredict/connections.html')

def contact(request):
    return render(request, 'dublinbuspredict/contact.html')

def tickets_fares(request):
    return render(request, 'dublinbuspredict/tickets_fares.html')

def sampleQuery(rows):
    # Connect to database using these credentials.
    global route_id
    global source_id
    global destination_id
    global direction
    print('From map:', route_id, source_id, destination_id)
    # direction = PilotRoutes.objects.filter(Q(route_id=route_id) & Q(stop_id=str(source_id))).values_list('direction')[0][0]
    print('Direction:', direction)
    # bus_stops = PilotRoutes.objects.filter(Q(route_id=route_id) & Q(direction=direction))
    # stop_names = PilotRoutes.objects.select_related(depth=1)
    # for i in stop_names:
    #     print(i.name)
    db = MySQLdb.connect(user='lucas', db='summerProdb', passwd='hello_world', host='csi6220-3-vm3.ucd.ie')
    cursor = db.cursor()
    cursor.execute('SELECT pilot_routes.sequence, bus_stops.name, bus_stops.long_name, bus_stops.lat, bus_stops.lon '
                   'FROM pilot_routes, bus_stops '
                   'WHERE direction = ' + str(direction) + ' AND pilot_routes.route_id = "' + str(route_id) + '" AND pilot_routes.stop_id = bus_stops.stop_id '
                   'ORDER BY pilot_routes.sequence;')
    rows = cursor.fetchall()
    print('Here:', rows)
    # cursor.execute("""
    #                     SELECT 46_a_route.stop_sequence, bus_stops.name, bus_stops.long_name, bus_stops.lat, bus_stops.lon
    #                     FROM 46_a_route, bus_stops
    #                     WHERE direction = 1
    #                         AND 46_a_route.stop_id = bus_stops.stop_id
    #                     ORDER BY 46_a_route.stop_sequence;""")
    # rows = cursor.fetchall()
    db.close()

    return HttpResponse(json.dumps({'data': rows}), content_type="application/json")
    
