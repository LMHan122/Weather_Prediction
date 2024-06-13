Weather Prediction Application

Introduction
Welcome to the Event Planning Weather Data Collection project! As a data analyst at our event planning company,
one of our primary tasks is to ensure the success of events by procuring suitable coverings such as tents, canopies,
and other temporary shelters.Choosing the correct size and type of covering depends heavily on the weather conditions
expected at the event location and time of year.

To facilitate this process, we've developed a Python program that leverages weather data collected from various federal
and local agencies through publicly available APIs. This program allows us to gather historical weather information for
a specific location and date, spanning the previous five years. The collected data is then stored in a local database
for testing purposes, ensuring accuracy and reliability.

Project Overview

In this project, you'll find:

1.	Weather.py: An integrated weather API to retrieve historical weather data for a given location and date.
    •	The Weather class has:
        o	Five optional parameters:
            	lat - latitude of choice location.
            	long – longitude of choice location.
            	month – month chosen.
            	day – day of the month.
            	year – year chosen.
        o	Three methods:
            	five_year_temp – will utilize the API to calculate the avg, min, and max temperature for the previous five years.
            	five_year_wind_speed - will utilize the API to calculate the avg, min, and max temperature for the previous five years.
            	five_year_precip - will utilize the API to calculate the avg, min, and max temperature for the previous five years.
            •	The User class will create an SQLite database to hold the information. It has:
            o	query_table – will print the current user table.
2.	weather.db: A local database to store the collected weather information, enabling easy access and query capabilities.
3.	main.py: A Python script that  creates a Weather and User instance, and populates the SQLite table.
4.  test.py - A Python script that executes three tests against the code.
5.	README.txt: This README file provides detailed instructions on how to set up and utilize the program effectively.
6.	Requirements.txt: This file will list all the packages and modules required to run the programs.


Citation & Acknowledgement
Zippenfenig, P. (2023). Open-Meteo.com Weather API [Computer software]. Zenodo. https://doi.org/10.5281/ZENODO.7970649
Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N. (2023). ERA5 hourly data on single levels from 1940 to present [Data set]. ECMWF. https://doi.org/10.24381/cds.adbb2d47
Muñoz Sabater, J. (2019). ERA5-Land hourly data from 2001 to present [Data set]. ECMWF. https://doi.org/10.24381/CDS.E2161BAC
Schimanke S., Ridal M., Le Moigne P., Berggren L., Undén P., Randriamampianina R., Andrea U., Bazile E., Bertelsen A., Brousseau P., Dahlgren P., Edvinsson L., El Said A., Glinton M., Hopsch S., Isaksson L., Mladek R., Olsson E., Verrelle A., Wang Z.Q. (2021). CERRA sub-daily regional reanalysis data for Europe on single levels from 1984 to present [Data set]. ECMWF. https://doi.org/10.24381/CDS.622A565A
