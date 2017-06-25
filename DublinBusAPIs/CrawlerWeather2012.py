# >> This program is used to crawl data from the UndergroundWeather API and put into a table in our shared server database.
# Be careful when running the programming as there is a limit on how many calls per minute can be made. I got a warning already
# for calling more than 10 times a minute, and only have two more warnings. If querying lot of separate call, put a time/counter
# on the for loop. Cheers. <<

# The first import gets all the data types we need for the table. There other data types, like TIMESTAMP, for example, that can be imported.
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
# This code here is used because, apparently, Python3 doesnt' have native MySQLdb?
# Should check if this really is the case. In the meantime, you will have to import
# the module pymysql.
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

def base(engine):
    # This code is used to set up a table. Careful: __tablename__ is NOT a variable name, so
    # do not change it!!
    Base = declarative_base()
    class User(Base):
        __tablename__ = 'weather2013'

        # SQLAlchemy always requires a primary key!!
        weather_id = Column(Integer, primary_key=True)
        date = Column(String(100))
        time = Column(String(100))
        summary = Column(String(100))
        temp = Column(Float)
        rain = Column(Float)
        wind = Column(Float)

    # This code sends the command to create the table. Don't worry, it won't create the same table twice.
    Base.metadata.create_all(engine)
    return User

def connect_api(day):
    """Established the connection. Takes day as input and uses it to get weather information on the relevant day."""
    # This code opens the connection to the weather API. There's a condition because 0 needs to be added to single digit day.
    if day < 10:
        base_url = 'http://api.wunderground.com/api/c59c002ced7bb1cb/history_2013010' + str(day) + '/q/IE/Dublin.json'
    else:
        base_url = 'http://api.wunderground.com/api/c59c002ced7bb1cb/history_201301' + str(day) + '/q/IE/Dublin.json'

    # This code sets up our static data table for all the stations.
    # This code gets the data from Dublin Bikes.
    response = requests.get(base_url)
    # print(response) #This is just to show that the response connected without error (should show <Response [200]. It can be commented out.
    return response

def call_api(day):
    """Receives day and sends the call to connect to the API. Returns info from the call."""
    response = connect_api(day)
    results = response.json()
    return results

def main():
    # For loop to call the API for each day on the month.
    for day in range(1, 32):
        # This code creates/opens the connection to the database
        engine = create_engine('mysql+pymysql://lucas:hello_world@csi6220-3-vm3.ucd.ie/summerProdb')
        User = base(engine)
        # This code sets up a session. The session is like a notepad, where we take notes of all the changes
        # we want to do the database.
        Session = sessionmaker(bind=engine)
        session = Session()
        # Get the weather info for day (int for loop).
        results = call_api(day)
        # Create empty list and then filter in only the data fields we want using a for loop.
        weather = []
        date = (results['history']['date']['mday'] + '-' + results['history']['date']['mon'] + '-' + results['history']['date']['year'])
        for i in results['history']['observations']:
            # Used METAR because that is the one weather station common to all the hours.
            if 'METAR' in i['metar']:
                # print(i['date']['hour'] + ':' + i['date']['min'] + ':00')
                time = (i['date']['hour'] + ':' + i['date']['min'] + ':00')
                # print('Summary:', i['conds'])
                summary = i['conds']
                # print('Temp:', i['tempm'])
                temp = i['tempm']
                # print('Rain:', i['rain'])
                rain = i['rain']
                # print('Wind Speed:', i['wspdm'])
                wind = i['wspdm']
                # print('\n<<--------------------------->>\n')
                weather.append({'date':date, 'time':time, 'summary':summary, 'temp':temp, 'rain':rain, 'wind':wind})
        # print(weather)
        # Push information into the database.
        for i in weather:
            # This code creates a row.
            ed_user = User(date=i['date'], time=i['time'], summary=i['summary'], temp=i['temp'], rain=i['rain'], wind=i['wind'])
            # Save row in notepad. Attention: the row is only stored in the notepad at this point.
            # Its not yet in the database.
            session.add(ed_user)
            # This code makes the actual changes to the database.
            session.commit()

if __name__ == '__main__':
    # Flow control begins here.
    main()
