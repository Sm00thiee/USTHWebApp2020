from .tools.crawler import CovidImageScraper
from .tools.addWebpage import add
from termcolor import colored
from os import system
def menu():
    print("\n"+"-"*20+ colored(" DATA MANAGEMENT SYSTEM ", "green") + "-"*20)
    print("""
    0. Quit program
    1. Add more website to pages.txt
    2. Crawl more picture list to links.txt
    """)
    print("-"*64)

def input_number_of_page(page=0):
    try:
        page = int(input("Enter number of page that you want to crawl (from 1 to 12): "))
    except:
        print(colored("\nWrong format!\n", 'red'))
        return input_number_of_page()
    finally:
        if page < 1 or page > 12:
            print(colored("\nOut of value!\n", "red"))
            return input_number_of_page()
        else:
            return int(page)

def input_command(cmd=0):
    try:
        cmd = int(input("Your command: "))
    except:
        print(colored("\nWrong format of command!\n", 'red'))
        return input_command()
    finally:
        if cmd <0 or cmd >2:
            print(colored("\nThe command is out of value!\n", "red"))
            return input_command()
        else:
            return int(cmd)

def input_type_of_web(web=0):
    try:
        print("""
        1. Chrome
        2. Firefox
        """)
        web = int(input("Your type of web: "))
    except:
        print(colored("\nWrong format of type!\n", 'red'))
        return input_command()
    finally:
        if web not in (1, 2):
            print(colored("\nThe type is out of value!\n", "red"))
            return input_type_of_web()
        else:
            return int(web)
def main():
    run = True
    cmd_list = [0, 1, 2]
    while run:
        cmd = ""
        while cmd not in cmd_list:
            menu()
            cmd = input_command()
        if cmd == 0:
            run = False
            break
        elif cmd ==1:
            web = input("Enter link want to add: ")
            add(web)
        elif cmd == 2:
            crawler = CovidImageScraper(input_type_of_web())
            number_of_page = input_number_of_page()
            print("\n"+ colored("-"*10,"cyan") + colored("   Start crawling!   ", 'green') + colored("-"*10,"cyan") +'\n')
            crawler.run(int(number_of_page))
        else:
            print(colored("\n It's not a function.", "red"))



if __name__ == "__main__":
    system("clear")
    main()
