from bs4 import BeautifulSoup
import requests
import schedule
import time
import config

def get_covid_cases():
    html_text = requests.get('https://www.worldometers.info/coronavirus/')  # go to covid website
    soup = BeautifulSoup(html_text.content, "html.parser")  # parse the data from the website
    covid_cases_header = soup.find('div', class_='maincounter-number').text  # inspect the site and look for this sspecific div area, then grab the plain text from it
    return covid_cases_header

def post_to_fb(): # function wrapper for the next set of instructions
      PAGE_ID = config.config_secrets['PAGE_ID'] # page id for the page (obviously)
      FB_ACCESS_TOKEN = config.config_secrets['FB_ACCESS_TOKEN']
      msg = "The total number of COVID-19 cases as of today is: " + get_covid_cases().strip()
      post_url = "https://graph.facebook.com/112632927975496/feed"
      payload = {
          "message": msg,
          "access_token": FB_ACCESS_TOKEN
      }
      r = requests.post(post_url, data=payload)
      print(r.text) # print the return text from FB servers to make sure the message went through properly or if not look at errors

schedule.every().day.at("12:00").do(display_cases) # timer for function to run only if the time matches the value in quotes. otherwise do nothing.
schedule.every().day.at("00:00").do(display_cases)

while 1: # While 1, do function, since function is always 1, it always runs forever
    schedule.run_pending()
    time.sleep(1)

