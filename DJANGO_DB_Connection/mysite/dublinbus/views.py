from django.http import HttpResponse
# from mysite.dublinbus.models import Weather2013
import MySQLdb

def index(request):
    # Connect to database using these credentials.
    db = MySQLdb.connect(user='lucas', db='summerProdb', passwd='hello_world', host='csi6220-3-vm3.ucd.ie')
    cursor = db.cursor()
    cursor.execute('SELECT 46_a_route.stop_sequence, bus_stops.name, bus_stops.long_name, bus_stops.lat, bus_stops.lon '
                   'FROM 46_a_route, bus_stops '
                   'WHERE direction = 1 AND 46_a_route.stop_id = bus_stops.stop_id '
                   'ORDER BY 46_a_route.stop_sequence;"')
    rows = cursor.fetchall()
    db.close()
    # Post it to html page.
    return HttpResponse(rows)
