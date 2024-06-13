import weather as w

if __name__ == "__main__":
    #creating instance
    instance = w.Weather()
    #using method to scrap temp data
    instance_temp = instance.five_year_temp()
    # using method to scrap wind data
    instance_wind = instance.five_year_wind_speed()
    #using method to scrap precipitation data
    instance_precip = instance.five_year_precip()


    #sending the data to the SQLite db table

    session = w.Session()

    new_row = w.User(
                loc_lat = instance.lat,
                loc_long= instance.long,
                month1= instance.month,
                day_of_month= instance.day,
                yr= instance.year,
                five_yr_avg_temp = instance.avg_temp,
                five_yr_min_temp = instance.min_temp,
                five_yr_max_temp = instance.max_temp,
                five_yr_avg_wind = instance.avg_wind_speed,
                five_yr_min_wind = instance.min_wind_speed,
                five_yr_max_wind = instance.max_wind_speed,
                five_yr_sum_prec = instance.sum_precip,
                five_yr_min_prec = instance.min_precip,
                five_yr_max_prec = instance.max_precip
    )
    session.add(new_row)
    session.commit()

    table_instance = w.User()
    table_instance.query_table()

    session.close()

