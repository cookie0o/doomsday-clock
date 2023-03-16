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


def status():
    try:
        # doomsday-clock time url
        URL = "https://thebulletin.org/doomsday-clock/"


        # get time element
        page = requests.get(URL)
        content = BeautifulSoup(page.content, "html.parser")
        time_element = str(content.find("h2", class_="fl-heading"))
        """
        # response

        <h2 class="fl-heading">
        <span class="fl-heading-text">A time of unprecedented danger: It is 90 seconds to midnight</span>
        </h2>
        """

        # get time out of the html element
        time_element = str(time_element.replace("h2", ""))
        time_definit = check_time(time_element)
        time_still   = check_still(time_element)
        time_element = str(re.search(r'\d+', time_element).group())

        if time_still == True:
            time_element = str("still "+time_element+" "+time_definit+" to midnight")
        if time_still == False:
            time_element = str(time_element+" "+time_definit+" to midnight")


        return str(time_element)
    except Exception as e:
        return e