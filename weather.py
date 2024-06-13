'''
Establishing the Weather class and methods
'''
import openmeteo_requests
import requests_cache
from retry_requests import retry
from sqlalchemy import create_engine, Column, Integer, Float, String, select
from sqlalchemy.orm import sessionmaker, declarative_base


class Weather:
    def __init__(self, lat=32.7, long=-97.3, month=7, day=7, year=2024):
        '''
        :param lat: latitude of choice location in float - has default value
        :param long: longitude of choice location in float - has default value
        :param month: for month of choice, two character string - has default value
        :param day: for day of choice, two character string - has default value
        :param year: start year of choice - has default value

        The rest of the variables start with a value of zero until a method is used to cal the value:

        avg_temp: Average temperature for the previous five years for the day, month, and year selected in Fahrenheit
        min_temp: Lowest temperature for the previous five years for the day, month, and year selected in Fahrenheit
        max_temp: Highest temperature for the previous five years for the day, month, and year selected in Fahrenheit
        avg_wind_speed: Average wind speed for the previous five years for the day, month, and year selected in mph
        min_wind_speed: Lowest wind speed for the previous five years for the day, month, and year selected in mph
        max_wind_speed: Highest wind speed for the previous five years for the day, month, and year selected in mph
        sum_precip: Average precipitation for the previous five years for the day, month, and year selected in inches
        min_precip: Lowest precipitation for the previous five years for the day, month, and year selected in inches
        max_precip: Highest precipitation for the previous five years for the day, month, and year selected in inches
        '''
        self.lat = lat
        self.long = long
        self.month = month
        self.day = day
        self.year = year
        self.avg_temp = 0.0
        self.min_temp = 0.0
        self.max_temp = 0.0
        self.avg_wind_speed = 0.0
        self.min_wind_speed = 0.0
        self.max_wind_speed = 0.0
        self.sum_precip = 0.0
        self.min_precip = 0.0
        self.max_precip = 0.0

    def five_year_temp(self):
        '''
        Calculates the average, lowest, and highest temp for the previous five years
        '''
        #creating list to hold the temp for the previous five years
        self.temp_data = []

        #converting the day and month to 2 character string to be used in date
        day = str(self.day).zfill(2)
        month = str(self.month).zfill(2)

        #creating a years variable to be used in loop without changing the initial data
        years = self.year - 1

        #creating loop to access the api for all 5 dates
        for i in range(5):
            self.date = str(years) + '-' + month + '-' + day
            '''
            A portion of this scrip comes from the Weather API website
            '''
            #set up the Open-Meteo API client with cache and retry on error
            self.cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
            self.retry_session = retry(self.cache_session, retries=5, backoff_factor=0.2)
            self.openmeteo = openmeteo_requests.Client(session=self.retry_session)

            self.url = "https://archive-api.open-meteo.com/v1/archive"

            #listing all required weather variables
            params = {
                "latitude": self.lat,
                "longitude": self.long,
                "start_date": self.date,
                "end_date": self.date,
                "daily": "temperature_2m_mean",
                "temperature_unit": "fahrenheit",
            }
            responses = self.openmeteo.weather_api(self.url, params=params)

            # Process first location.
            response = responses[0]

            # Process daily data and appending to the list created
            daily = response.Daily()
            self.temp_data.append(round(daily.Variables(0).ValuesAsNumpy()[0], 1))

            years = int(years) - 1

        #assigning the values to the correct class variables
        self.avg_temp = round(sum(self.temp_data)/len(self.temp_data), 1)
        self.min_temp = min(self.temp_data)
        self.max_temp = max(self.temp_data)


    def five_year_wind_speed(self):
        '''
        Calculates the average, lowest, and highest wind speed in mph for the previous five years
        '''
        #creating list to hold the wind speed for the previous five years
        self.wind_data = []

        #converting the day and month to 2 character string to be used in date
        day = str(self.day).zfill(2)
        month = str(self.month).zfill(2)

        #creating a years variable to be used in loop without changing the initial data
        years = self.year - 1

        #creating loop to access the api for all 5 dates
        for i in range(5):
            self.date = str(years) + '-' + month + '-' + day
            '''
            A portion of this scrip comes from the Weather API website
            '''
            #set up the Open-Meteo API client with cache and retry on error
            self.cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
            self.retry_session = retry(self.cache_session, retries=5, backoff_factor=0.2)
            self.openmeteo = openmeteo_requests.Client(session=self.retry_session)

            self.url = "https://archive-api.open-meteo.com/v1/archive"

            #listing all required weather variables
            params = {
                "latitude": self.lat,
                "longitude": self.long,
                "start_date": self.date,
                "end_date": self.date,
                "daily": "wind_speed_10m_max",
                "wind_speed_unit": "mph",
            }
            responses = self.openmeteo.weather_api(self.url, params=params)

            # Process first location.
            response = responses[0]

            # Process daily data and appending to the list created
            daily = response.Daily()
            self.wind_data.append(round(daily.Variables(0).ValuesAsNumpy()[0], 1))

            years = int(years) - 1

        #assigning the values to the correct class variables
        self.avg_wind_speed = round(sum(self.wind_data)/len(self.wind_data), 1)
        self.min_wind_speed = min(self.wind_data)
        self.max_wind_speed = max(self.wind_data)


    def five_year_precip(self):
        '''
        Calculates the sum, lowest, and highest precipitation in inches for the previous five years
        '''
        #creating list to hold the wind speed for the previous five years
        self.precip_data = []

        #converting the day and month to 2 character string to be used in date
        day = str(self.day).zfill(2)
        month = str(self.month).zfill(2)

        #creating a years variable to be used in loop without changing the initial data
        years = self.year - 1

        #creating loop to access the api for all 5 dates
        for i in range(5):
            self.date = str(years) + '-' + month + '-' + day
            '''
            A portion of this scrip comes from the Weather API website
            '''
            #set up the Open-Meteo API client with cache and retry on error
            self.cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
            self.retry_session = retry(self.cache_session, retries=5, backoff_factor=0.2)
            self.openmeteo = openmeteo_requests.Client(session=self.retry_session)

            self.url = "https://archive-api.open-meteo.com/v1/archive"

            #listing all required weather variables
            params = {
                "latitude": self.lat,
                "longitude": self.long,
                "start_date": self.date,
                "end_date": self.date,
                "daily": "precipitation_sum",
                "precipitation_unit": "inch",
            }
            responses = self.openmeteo.weather_api(self.url, params=params)

            # Process first location.
            response = responses[0]

            # Process daily data and appending to the list created
            daily = response.Daily()
            self.precip_data.append(round(daily.Variables(0).ValuesAsNumpy()[0], 3))

            years = int(years) - 1

        #assigning the values to the correct class variables
        self.sum_precip = round(sum(self.precip_data), 3)
        self.min_precip = min(self.precip_data)
        self.max_precip = max(self.precip_data)

'''
creating a second class that will create a table in SQLite
'''

#create engine
engine = create_engine("sqlite:///weather.db", echo=True)

#create the session
Session = sessionmaker(engine)
session = Session()

#make the base class
Base = declarative_base()

#creating a new class to make a table
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    loc_lat = Column(Float)
    loc_long = Column(Float)
    month1 = Column(Integer)
    day_of_month = Column(Integer)
    yr = Column(Integer)
    five_yr_avg_temp = Column(Float)
    five_yr_min_temp = Column(Float)
    five_yr_max_temp = Column(Float)
    five_yr_avg_wind = Column(Float)
    five_yr_min_wind = Column(Float)
    five_yr_max_wind = Column(Float)
    five_yr_sum_prec = Column(Float)
    five_yr_min_prec = Column(Float)
    five_yr_max_prec = Column(Float)


    #creating method to show the data added to the table
    #changed the format of the method per a stackoverflow page so the data will show instead of just the object
    #https://stackoverflow.com/questions/3618690/how-to-query-a-table-in-sqlalchemy
    def query_table(self):
        all_rows = session.query(Base.metadata.tables['user']).all()
        print(User.__table__.columns.keys())
        for row in all_rows:
            print(row)

#creating the table
Base.metadata.create_all(engine)





























