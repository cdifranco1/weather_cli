import sys, bs4, requests

base_url = "https://google.com/search"
query = "?q=weather"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

fetch_error_msg = "\nCould not find weather for the provided city. Please enter a different city.\n"

#see if user entered a legitimate city by checking for "weather.com"
def check_fetch(soup):
    weather_link = soup.find("a", string="weather.com")
    if not weather_link:
        print(fetch_error_msg)
        sys.exit()


def show_usage():
    print('\nUsage: get_weather City State \n\n City: Name of city. If the city is more than one word, do not add spaces ("NewYork" or "newyork"). \n State: State ("NY", "ny", or "newyork"). The state argument can also take country names for non-US cities.\n')

def main():
    args = sys.argv
    if len(args) < 3 or len(args) > 4:
        show_usage()
        sys.exit()
    
    state = args[-1]
    city = args[-2]
    if len(args) > 3:
        flag = args[1]
        if flag not in options:
            show_usage()
            sys.exit()
    else:
        #defaulting to current weather 
        flag = "-c"

    soup = make_request(city, state)
    check_fetch(soup)
    dispatch(soup, flag)
    
    sys.exit()

def make_request(city, state): 
    full_url = f'{base_url}{query}+{city}+{state}'
    
    res = requests.get(url=full_url, headers=headers)
    soup = bs4.BeautifulSoup(res.content, features="lxml") 
    return soup

def get_forecasts(soup):
    results = {}
    #extracting the temperature symbol from the text
    degrees_sym = get_degrees_sym(soup)
    container = soup.select("div.wob_df")
    summaries = get_forecast_descr(soup)
    for i, x in enumerate(container):
        #outer div holds both the temp forecasts and corresponding days
        outer_div = x.select('div.QrNVmd')

        #day is the first element in the outer div
        day = outer_div[0].get_text()
        
        #selecting the two spans that hold the high and low temp for each day
        #can expand here to include celsius option
        temps = x.select('span.wob_t')
        high = f'{temps[0].get_text()}{degrees_sym}'
        low = f'{temps[2].get_text()}{degrees_sym}'
        results[day] = {
            'high': high,
            'low': low,
            'descr': summaries[i]
        }
    
    return results

def get_headings(soup):
    city = soup.select_one("div#wob_loc").get_text()
    time = soup.select_one("div#wob_dts").get_text()
    descr = soup.select_one("span#wob_dc").get_text()

    results = {
        'city': city, 
        'time': time,
        'descr': descr
    }

    return results

def get_curr_weather(soup):
    temp = get_curr_temp(soup)
    precip = soup.select_one("#wob_pp").get_text()
    humidity = soup.select_one("#wob_hm").get_text()
    wind = soup.select_one("#wob_ws").get_text()
    return temp, precip, humidity, wind


def get_curr_temp(soup):
    curr_temp = soup.select_one("span#wob_tm.wob_t").get_text()
    temp_sym = get_degrees_sym(soup)
    return f'{curr_temp}{temp_sym}'

def get_degrees_sym(soup):
    temp_sym = soup.select("div.vk_bk.wob-unit")[0].get_text()[:2]
    return temp_sym

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
        high = forecast['high']
        low = forecast['low']
        descr = forecast['descr']
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

def dispatch(soup, flag='-c'):
    display_fn = options[flag]
    display_fn(soup)

def get_forecast_descr(soup):
    imgs = soup.select("div#wob_dp img")
    summaries = []
    for x in imgs:
        summaries.append(x['alt'])
    return summaries

options = {
    '-c':  display_current_weather,
    '-f': display_forecasts
}
   
if __name__ == "__main__":
    main()
