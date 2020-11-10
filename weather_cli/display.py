from weather_cli.parser import get_headings, get_curr_weather, get_curr_temp, get_forecasts

def print_headings(headings):
    print("\n")
    for heading in headings.values():
        print(f'{heading}')

def print_curr_weather(weather):
    '''
    Takes in tuple of temp, precip, humidity, wind
    '''
    temp, precip, humidity, wind = weather

    print(f'\nTemp: {temp}\n\nPrecipitation: {precip}\nHumidity: {humidity}\nWind: {wind}\n')

def print_forecasts(forecasts):
    print("\n")
    for day in forecasts:
        forecast = forecasts[day]
        high = forecast.get('high')
        low = forecast.get('low')
        descr = forecast.get('descr')
        print(f'{day} --> High: {high} Low: {low}   {descr}')
    print("\n")


def display_current_weather(soup):
    print("\nCurrent Weather:")
    print_headings(get_headings(soup))
    print_curr_weather(get_curr_weather(soup))

def display_forecasts(soup):
    print("\nWeek's Forecast:")
    print_headings(get_headings(soup))
    print_forecasts(get_forecasts(soup))
