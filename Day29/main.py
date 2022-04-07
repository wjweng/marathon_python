import csv
with open("C0AH10-2022-02.csv", encoding="utf-8") as weather_file:
    weather_data = csv.reader(weather_file)

    for row in weather_data:
        if row[7] != "氣溫(℃)":
            print(row[0], row[7])

import pandas
weather_data = pandas.read_csv("C0AH10-2022-02.csv", header=1, usecols=["ObsTime", "Temperature"], nrows=10)
print(weather_data)
print(weather_data["Temperature"])

weather_data = pandas.read_csv("C0AH10-2022-02.csv", header=1, usecols=["ObsTime", "Temperature"], nrows=10)
print(type(weather_data))
print(type(weather_data["Temperature"]))

print(weather_data.columns)
print(weather_data.index)

print(weather_data["Temperature"].index)

index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ObsTime_series = pandas.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index)
Temperature_series = pandas.Series([16.8, 17.0, 15.8, 14.3, 13.6, 14.4, 17.6, 15.6, 16.5, 17.2], index)
print(ObsTime_series)
print(Temperature_series)

weather_dict = {"ObsTime": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "Temperature": [16.8, 17.0, 15.8, 14.3, 13.6, 14.4, 17.6, 15.6, 16.5, 17.2]}
weather_dataframe = pandas.DataFrame(weather_dict, index)
print(weather_dataframe)

# ObsTime_series.name = "ObsTime"
# Temperature_series.name = "Temperature"
weather_dataframe_2 = pandas.concat([ObsTime_series, Temperature_series], axis=1)
weather_dataframe_2.columns = ["ObsTime", "Temperature"]
print(weather_dataframe_2)
