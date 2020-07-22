# Weather CLI App
### A simple CLI application to scrape weather information from google for a given city. 

### Installation (for Mac users) 
Clone the repository and cd into the root directory and run "bash install.sh". This should install the script in /usr/local/bin, and will install the app dependencies into your python site-packages.

### Usage
Once installed, the app can be accessed from any directory by running "get_weather <city> <state>". The "get_weather" command is specified in setup.py and can be customized by updating the console_script. The CLI interface currently currently will accept the following flags: [-c] or [-f]. The [-c] flag will only return the current weather for the given city. The [-f] will return the week's forecast. If no flag is passed, the app will default to returning the current weather.

