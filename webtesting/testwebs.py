from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open('pyyython.txt', 'r') as document:
    websites = {}
    for line in document:
        line = line.split()
        websites[line[0]] = line[1:]


with open("results.txt", "w") as text_file:
    for k,v in websites.iteritems():
        driver = webdriver.Firefox()
        driver.get(v)
    #assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
    #assert "No results found." not in driver.page_source
        text_file.write(k)
        driver.close()
text_file.close()


