import sys, bs4, requests

base_url = "https://forecast.weather.gov/"
query = "MapClick.php?"
city_key = "CityName="
state_key = "&state="


def show_usage():
    print('Usage: forecast [City] [State (IL)]')

def main():
    if len(sys.argv) < 3:
        show_usage()
        sys.exit()
    
    soup = make_request()
    forecasts = get_forecasts(soup)
    for day, val in forecasts.items():
        print(f'\n{day} --> {val}\n')
    
    sys.exit()
   

def make_request(): 
    city = sys.argv[1]
    state = sys.argv[2]
    full_url = f'{base_url}{query}{city_key}{city}{state_key}{state}'
   
    res = requests.get(full_url)
    soup = bs4.BeautifulSoup(res.text, features='html.parser') 
    return soup

def get_forecasts(soup):
    labels = soup.select(".forecast-label")
    forecasts = soup.select(".forecast-text")

    result = {}
    for label, forecast in zip(labels, forecasts):
        result[label.get_text()] = forecast.get_text()

    return result


   
if __name__ == "__main__":
    main()    
