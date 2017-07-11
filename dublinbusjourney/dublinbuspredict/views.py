from django.http import HttpResponse
from django.shortcuts import render
import MySQLdb

def index(request):
    return render(request, 'dublinbuspredict/index.html')

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
    db = MySQLdb.connect(user='lucas', db='summerProdb', passwd='hello_world', host='csi6220-3-vm3.ucd.ie')
    cursor = db.cursor()
    cursor.execute("""
                        SELECT 46_a_route.stop_sequence, bus_stops.name, bus_stops.long_name,bus_stops.lat, bus_stops.lon 
                        FROM 46_a_route, bus_stops
                        WHERE direction = 1
                            AND 46_a_route.stop_id = bus_stops.stop_id
                        ORDER BY 46_a_route.stop_sequence;""") # select 46_a_route.stop_sequence, bus_stops.name, bus_stops.long_name,
    rows = cursor.fetchall()
    db.close()

    
    return render(rows, 'dublinbuspredict/sampleQuery.html')
   # return HttpResponse(rows)
