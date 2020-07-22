import sys, bs4, requests

base_url = "https://google.com/search"
query = "?q=weather"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

def show_usage():
    print('\nUsage: get_weather City State \n\n City: Name of city. If the city is more than one word, do not add spaces ("NewYork" or "newyork"). \n State: State abbreviation ("NY" or "ny")\n')

def main():
    args = sys.argv
    if len(args) < 3 or len(args) > 4:
        show_usage()
        sys.exit()
    
    if len(args) > 3:
        flag = args[1]
        city = args[2]
        state = args[3]
        soup = make_request(city, state)
        dispatch(soup, flag)
    else:
        city = args[1]
        state = args[2]
        soup = make_request(city, state)
        dispatch(soup)
    
    sys.exit()

def make_request(city, state): 
    full_url = f'{base_url}{query}+{city}+{state}'
    
    res = requests.get(url=full_url, headers=headers)
    soup = bs4.BeautifulSoup(res.content, features="lxml") 
    return soup

def get_forecasts(soup):
    results = {}
    container = soup.select("div.wob_df")
    for x in container:
        #outer div holds both the temp forecasts and corresponding days
        outer_div = x.select('div.QrNVmd')

        #day is the first element in the outer div
        day = outer_div[0].get_text()

        #extracting the temperature symbol from the text
        temp_symbol = outer_div[-1].get_text()[-1]
        
        #selecting the two spans that hold the high and low temp for each day
        #can expand here to include celsius option
        temps = x.select('span.wob_t')
        high = f'{temps[0].get_text()}{temp_symbol}'
        low = f'{temps[2].get_text()}{temp_symbol}'
        results[day] = {
            'high': high,
            'low': low
        }
    
    return results

def print_headings(headings):
    print("\n")
    for heading in headings.values():
        print(f'{heading}')

def get_headings(soup):
    city = soup.select("div#wob_loc")[0].get_text()
    time = soup.select("div#wob_dts")[0].get_text()
    descr = soup.select("span#wob_dc")[0].get_text()

    results = {
        'city': city, 
        'time': time,
        'descr': descr
    }

    return results

def get_curr_temp(soup):
    curr_temp = soup.select("span#wob_tm.wob_t")[0].get_text()
    return curr_temp

def print_curr_temp(curr_temp):
    print(f'\nTemp: {curr_temp}\n')

def print_forecasts(forecasts):
    print("\n")
    for day in forecasts:
        forecast = forecasts[day]
        high = forecast.get('high')
        low = forecast.get('low')
        print(f'{day} --> High: {high} Low: {low}')
    print("\n")

def display_current_weather(soup):
    print("\nCurrent Weather:")
    print_headings(get_headings(soup))
    print_curr_temp(get_curr_temp(soup))

def display_forecasts(soup):
    print("\nWeek's Forecast:")
    print_headings(get_headings(soup))
    print_forecasts(get_forecasts(soup))

def dispatch(soup, flag='-c'):
    display_fn = options[flag]
    display_fn(soup)

options = {
    '-c':  display_current_weather,
    '-f': display_forecasts
}
   
if __name__ == "__main__":
    main()
