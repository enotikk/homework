from urllib.request import urlopen
import re

link = "https://weather.com/ru-RU/weather/today/l/063735862ffb0af39053e702550b27da07a302df1f117eca3029084c941f79d9"
#link = "https://weather.com/ru-RU/weather/today/l/92a09811e9aebee960adac3a308dd0c083f6308ae9d7d5d02538ea529413c739"

def get_weather():
    text = urlopen(link).read().decode("utf-8")
    temp = re.findall('<div class="today_nowcard-temp"><span class="">(&minus;|\-)*([0-9]+)<sup>', text)[0]
    temp = temp[0] + temp[1]
    v = re.findall('<th>Влажность</th><td><span class=""><span>([0-9]+)<span', text)[0]
    return {"температура": temp, "влажность": v}
