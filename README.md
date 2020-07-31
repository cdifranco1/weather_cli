# Weather CLI Web-Scraping App
### A simple CLI application to scrape weather info for any given city from google search. 

### Installation (for Mac users) 
Clone the repository and cd into the root directory and run "bash install.sh". This should install the script in /usr/local/bin, and will install the app dependencies into your python site-packages.

### Usage
Once installed, the app can be accessed from any directory by running "get_weather <city> <state>". The "get_weather" command is specified in setup.py and can be customized by updating the console_script. The CLI interface currently currently will accept the following flags: [-c] or [-f]. The [-c] flag will only return the current weather for the given city. The [-f] will return the week's forecast. If no flag is passed, the app will default to returning the current weather.

#### Example Usage:

My-MacBook-Air:~ get_weather -f chicago il

Week's Forecast:


Chicago, IL  
Wednesday 12:00 PM  
Mostly cloudy   


Wed --> High: 79°F Low: 66°F &nbsp; &nbsp; Partly cloudy  
Thu --> High: 77°F Low: 69°F &nbsp; &nbsp; Mostly sunny  
Fri --> High: 80°F Low: 72°F &nbsp; &nbsp; Mostly sunny  
Sat --> High: 87°F Low: 74°F &nbsp; &nbsp; Mostly sunny  
Sun --> High: 92°F Low: 75°F &nbsp; &nbsp; Partly cloudy   
Mon --> High: 84°F Low: 70°F &nbsp; &nbsp; Scattered thunderstorms   
Tue --> High: 80°F Low: 68°F &nbsp; &nbsp; Sunny  



My-MacBook-Air:~ get_weather ny ny

Current Weather:


New York, NY
Thursday 9:00 PM
Clear

Temp: 85°F

Precipitation: 15%
Humidity: 55%
Wind: 2 mph
