import pyowm
owm = pyowm.OWM('96ac4f46bd0af96f9cc487419c806b05')

def pullglobaltemperature():
	observation = owm.weather_at_place('Portland,usa')
	w = observation.get_weather()
	weatherstring = str(w.get_temperature("fahrenheit"))
	return float(weatherstring[44:48])
	
def pullglobalhumidity():
	observation = owm.weather_at_place('Portland,usa')
	w = observation.get_weather()
	humstring = w.get_humidity()
	return humstring

