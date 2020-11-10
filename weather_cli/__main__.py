import sys, bs4, requests
from weather_cli.config import AppConfig
from weather_cli.display import display_current_weather, display_forecasts

display_options = {
    '-c':  display_current_weather,
    '-f': display_forecasts
}

def show_usage():
    print(AppConfig.USAGE_STATEMENT)

#see if google search returned weather for given city by looking for weather.com link
def check_fetch(soup):
    weather_link = soup.find("a", string="weather.com")
    if not weather_link:
        print(AppConfig.FETCH_ERROR_MSG)
        sys.exit()


# application entry point
def main():
    args = sys.argv
    if len(args) < 3 or len(args) > 4:
        show_usage()
        sys.exit()
    
    state = args[-1]
    city = args[-2]
    if len(args) > 3:
        flag = args[1]
        if flag not in display_options:
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
    full_url = f'{AppConfig.BASE_URL}{AppConfig.QUERY}+{city}+{state}'
    
    res = requests.get(url=full_url, headers=AppConfig.HEADERS)
    soup = bs4.BeautifulSoup(res.content, features="lxml") 
    return soup


def dispatch(soup, flag='-c'):
    display_fn = display_options[flag]
    display_fn(soup)

   
if __name__ == "__main__":
    main()
