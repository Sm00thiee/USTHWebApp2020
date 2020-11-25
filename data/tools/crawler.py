from selenium import webdriver
from termcolor import colored
import os
class CovidImageScraper():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        # self.driver = webdriver.Chrome(chrome_options=options, executable_path=(os.getcwd()+"data/tools/driver/driver.exe"))
        self.driver = webdriver.Chrome(chrome_options=options)
        self.links = []

    def init_link(self):
        with open("data/pages.txt", "r") as f:
            links = f.readlines()
            for link in links:
                self.links.append(link)

    def getLink(self, link):
        try:
            self.driver.get(link)
        except:
            raise Exception(colored("get Link error!", "red"))

    def savePicture(self):
        count = none = already = 0
        try:
            all_data = self.driver.find_elements_by_tag_name('img')
            
            for data in all_data:
                pic_link = str(data.get_attribute("src"))
                if pic_link is not None and str(pic_link) != "None":
                    pic_link = str(pic_link)
                    with open("data/links.txt", "r") as f_r:
                        if (pic_link+"\n") in f_r.readlines():
                            already += 1
                        else:
                            count+=1
                            with open("data/links.txt", "a") as f_w:
                                f_w.write(f"{pic_link}\n")
                else:
                    none+=1
                    # print("This is not a link!")
        except:
            raise Exception(colored("save Picture error!","red"))
        finally:
            print(colored(f"\nAdded: {count} links", "green"))
            print(f"Abort: {none} links!\nAlready: {already} links!\n")

    def run(self):
        self.init_link()
        i = 0
        for link in self.links:
            i+=1
            self.getLink(link)
            self.savePicture()
            if i == 1:
                print(colored(f"Crawled images successful {i} time", 'green'))
            else:
                print(colored(f"Crawled images successful {i} times", "green"))
        self.driver.close()
        
def main():
    crawler = CovidImageScraper()
    crawler.run()
    
if __name__ == "__main__":
    main()

#//*[@id="islrg"]