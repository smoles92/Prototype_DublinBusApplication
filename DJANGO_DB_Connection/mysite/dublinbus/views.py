from django.http import HttpResponse
# from mysite.dublinbus.models import Weather2013
import MySQLdb

def index(request):
    # Connect to database using these credentials.
    db = MySQLdb.connect(user='lucas', db='summerProdb', passwd='hello_world', host='csi6220-3-vm3.ucd.ie')
    cursor = db.cursor()
    cursor.execute('SELECT summary, date, time FROM weather2013 where date="06-01-2013"')
    rows = cursor.fetchall()
    db.close()
    # Post it to html page.
    return HttpResponse(rows)
