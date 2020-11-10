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

def get_forecast_descr(soup):
  imgs = soup.select("div#wob_dp img")
  summaries = []
  for x in imgs:
      summaries.append(x['alt'])
  return summaries