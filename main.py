import requests  # import Requests (is a simple HTTP library).


# Create a function to get the weather information, using API KEY and url.
def get_weather_data(city):
    API_KEY = 'enter your API KEY here'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    try:
        data = requests.get(url).json()  # send the request, get the info in json format.
        # print(data)
        description = data['weather'][0][
            'description']  # get the weather description from the dictionary ex.clear sky etc.
        temperature = int(data['main']['temp']) - 273.15  # get temp, transform kelvin to celsius (-273.15) to get temp.
        real_feel = int(data['main']['feels_like']) - 273.15  # get real feel temp, in celsius degrees formula.
        # get an f string to get rid of to many print statements, and get all the info you want.
        print(f'City: {city}; description : {description}; temp: {round(temperature, 2)};'
              f' feels_like : {round(real_feel, 2)}')
    except KeyError as e:
        print(f'An error occurred.The following key does not exists: {e}\n'
              f'Please check the API url ')


if __name__ == '__main__':
    city = input('city: ')  # Name the city you want to get the weather predictions.
    get_weather_data(city)
