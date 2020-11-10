
class AppConfig:
  BASE_URL = "https://google.com/search"
  QUERY = "?q=weather"
  HEADERS = {
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
  }
  MAX_HOURLY_RESULTS = 8
  FETCH_ERROR_MSG = "\nCould not find weather for the provided city. Please enter a different city.\n"
  USAGE_STATEMENT = '\nUsage: get_weather City State \n\n City: Name of city. If the city is more than one word, do not add spaces ("NewYork" or "newyork"). \n State: State ("NY", "ny", or "newyork"). The state argument can also take country names for non-US cities.\n'

