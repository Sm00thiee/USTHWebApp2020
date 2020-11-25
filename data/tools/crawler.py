from selenium import webdriver
from termcolor import colored
import os, time
class CovidImageScraper():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=(os.getcwd()+"/data/tools/driver/driver.exe"))
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.links = []
        self.count = self.none = self.duplicated = 0

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
        count = none = duplicated = 0
        all_data = []
        try:
            for index in range(2, 12):
                data = self.driver.find_element_by_css_selector(f'div.td_module_19:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)')
                                                                #'div.td_module_19:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)')
                all_data.append(data)
            for data in all_data:
                pic_link = str(data.get_attribute("data-img-url"))
                if pic_link is not None and str(pic_link) != "None":
                    pic_link = str(pic_link)
                    if len(pic_link) <= 100:
                        with open("data/links.txt", "r") as f_r:
                            if (pic_link+"\n") in f_r.readlines():
                                duplicated += 1
                            else:
                                count+=1
                                with open("data/links.txt", "a") as f_w:
                                    f_w.write(f"{pic_link}\n")
                    else:
                        none += 1
                else:
                    none+=1
                    # print("This is not a link!")
        except:
            print(colored("\nSave Picture error!\n","red"))
        
        self.count += count
        self.none += none
        self.duplicated += duplicated
        print(colored(f"\nAdded: {count} links", "green"))
        print(colored(f"Abort: {none} links!", "yellow"))
        print(f"Duplicated: {duplicated} links!\n")

    def run(self, pages=1):
        self.init_link()
        number_of_page = 0
        link = self.links[0]
        for i in range(1, pages+1):
            number_of_page+=1
            self.getLink(f"{link}{i}/")
            time.sleep(0.25)
            self.savePicture()
            if number_of_page == 1:
                print(colored(f"Crawled images successful {i} time", 'green'))
            else:
                print(colored(f"Crawled images successful {i} times", "green"))
        
        self.driver.close()
        print("\n"+"-"*15 + colored("   IN TOTAL   ","green") + "-"*15+"\n")
        print(colored(f"\nAdded: {self.count} links", "green"))
        print(colored(f"Abort: {self.none} links!", "yellow"))
        print(f"Duplicated: {self.duplicated} links!\n")
        print("-"*44)
        
        
def main():
    crawler = CovidImageScraper()
    crawler.run(12)
    
if __name__ == "__main__":
    main()

#//*[@id="islrg"]
