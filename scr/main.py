from webpreview import webpreview
from bs4 import BeautifulSoup
import requests
import re


# get time definition (min., sec., hours.)
def check_time(time_element):
    if "seconds" in time_element:
        return "seconds"
    
    elif "minutes" in time_element:
        return "minutes"
    
    elif "hours" in time_element:
        return "hours"
    
    else:
        return "error"

# check if the time is "still x"
def check_still(time_element):
    if "still" in time_element:
        return True
    
    else:
        return False

class doomsday():

    # get current doomsday-clock time
    def time(type): #type = full, raw, html
        try:
            # doomsday-clock time url
            URL = "https://thebulletin.org/doomsday-clock/"


            # get time element
            page = requests.get(URL)
            content = BeautifulSoup(page.content, "html.parser")
            time_element_html = str(content.find("h2", class_="fl-heading"))
            """
            # response

            <h2 class="fl-heading">
            <span class="fl-heading-text">A time of unprecedented danger: It is 90 seconds to midnight</span>
            </h2>
            """

            # get time out of the html element
            time_element = str(time_element_html.replace("h2", ""))
            time_definit = check_time(time_element)
            time_still   = check_still(time_element)
            time_element = str(re.search(r'\d+', time_element).group())

            # return the full message with extra text
            if type == 0:
                if time_still == True:
                    time_element = str("still "+time_element+" "+time_definit+" to midnight")
                if time_still == False:
                    time_element = str(time_element+" "+time_definit+" to midnight")
            
            # return just number without any extra values/text
            elif type == 1:
                time_element = str(time_element+" "+time_definit)

            # return pure html
            elif type == 2:
                time_element = str(time_element_html)


            return str(time_element)
        except Exception as e:
            return e
    

    # get image of the current doomsday-clock image
    def img():
        try:
            # doomsday-clock wiki page
            URL = "https://en.wikipedia.org/wiki/Doomsday_Clock"


            # get clock element
            page = requests.get(URL)
            content = BeautifulSoup(page.content, "html.parser")
            image_element_raw = content.find("img", class_="thumbimage")
            image_element_raw = image_element_raw['src']
            image_element = "https:"+image_element_raw


            return str(image_element)
        except Exception as e:
            return e


"""
print (doomsday.img())
print (doomsday.time(type=0))
"""