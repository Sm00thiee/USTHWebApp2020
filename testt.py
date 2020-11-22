from selenium import webdriver
import requests
file = open('pageList.txt')
videoList = file.readlines()
print(videoList)

class CovidImageScraper():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(chrome_options=options)
    def getLink(self):
        self.driver.get(videoList[0])
    def getPicture(self):
        all_data = self.driver.find_elements_by_tag_name('img')
        for data in all_data:
            print(data.get_attribute("src") + "\n")
scraper = CovidImageScraper()
scraper.getLink()
scraper.getPicture()

#//*[@id="islrg"]