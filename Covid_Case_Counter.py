from bs4 import BeautifulSoup
import requests
import schedule
import time
import config

def get_covid_cases():
    html_text = requests.get('https://www.worldometers.info/coronavirus/')  # go to covid website
    soup = BeautifulSoup(html_text.content, "html.parser")  # parse the data from the website
    covid_cases_header = soup.find('div', class_='maincounter-number').text  # inspect the site and look for this sspecific div area, then grab the plain text from it
    return covid_cases_header.strip()

def get_fb_post_ready(covid_case_number): # function wrapper for the next set of instructions
      PAGE_ID = config.config_secrets['PAGE_ID'] # page id for the page (obviously)
      FB_ACCESS_TOKEN = config.config_secrets['FB_ACCESS_TOKEN']
      msg = "The total number of COVID-19 cases as of today is: " + covid_case_number
      payload = {
          "message": msg,
          "access_token": FB_ACCESS_TOKEN
      }
    return payload


def post_to_fb_request(request_to_send):
    post_url = "https://graph.facebook.com/112632927975496/feed"
    r = requests.post(post_url, data=payload)
    print(r.text) # print the return text from FB servers to make sure the message went through properly or if not look at errors

    return r.text


def main():
    amount_of_global_covid_cases = get_covid_cases()
    payload_to_send = get_fb_post_ready(covid_case_number)
    post_attempt = post_to_fb_request(payload_to_send)
    
    
if __name__ == "__main__":
    main()
    
