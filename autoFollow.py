# needs to change interpreter to python 2.7
# usage: python autoFollow.py yourUsername yourPassword hisOrHerUsername followersOrFollowing

import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'/home/superuser/Documents/geckodriver')

browser.get("https://steemit.com/login.html")
linkElem= browser.find_element_by_name('username')
linkElem.send_keys(sys.argv[1])

passElem= browser.find_element_by_name('password')
passElem.send_keys(sys.argv[2])
passElem.submit()
sleep(7)

#link to steemian to get his followers
name = sys.argv[3]
followers_or_followed = sys.argv[4]
steemian = "https://steemit.com/@" + name + "/" + followers_or_followed
browser.get(steemian)
bodyElem = browser.find_element_by_tag_name('body')
sleep(5)

# wait until the usernames are loaded
print "Usernames are loading... please wait."
try:
    while browser.find_element_by_xpath(".//div[@class='LoadingIndicator loading-overlay']"):
        sleep(1)
except Exception as msg:
    #print msg
    print "Yaay, usernames are now loaded. Lets follow them!"


#until it sees a NEXT button, it finds FOLLOW button and clicks if somebody can be followed
#all the people are loaded in the browser at once, no PAGE_DOWN needed
while browser.find_element_by_xpath("//div[@class='button tiny hollow float-right ']"):
    #find the follow button
    try:
        for s in browser.find_elements_by_xpath("//td[@width='250']"):
            follow = 'FOLLOW'
            followBut = s.find_element_by_xpath(".//label[@class='button slim hollow secondary ']")
            #if inside the HTML element is FOLLOW, than click on it and sleep a second
            if s.find_element_by_xpath(".//label[@class='button slim hollow secondary ']").text == follow:
                followBut.click()
                #sleep(1)
    except Exception as msg:
        print "we are done!"
    # find NEXT button and click on it, than wait 5 seconds to load page
    next = browser.find_element_by_xpath("//ul[@class='pager']")
    nextClick = next.find_element_by_xpath("//div[@class='button tiny hollow float-right ']")
    nextClick.click()
    sleep(3)
