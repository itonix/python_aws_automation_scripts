# import json

# with open('temperature_anomaly.json', 'r') as file:
#     temperature_data = json.load(file)
# # print(temperature_data)
# for year,data in temperature_data["data"].items():
#    print("{} ... {}".format(year,data))

# #print(temperature_data["data"])


import json

import urllib.request
with urllib.request.urlopen('https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/europe/tavg/ocean/12/1/2000-2025/data.json') as url:
    temperature_data = json.loads(url.read().decode())
print(temperature_data)

file_to_save = "temprature.txt"
with open(file_to_save, 'w') as temp_file:
    for year,data in temperature_data["data"].items():
        val = data['anomaly'] 
        temp_file.write("{} ... {}\n".format(year,val))

# file_to_save = "temprature.txt"
# with open(file_to_save, 'w') as temp_file:
#     for 

