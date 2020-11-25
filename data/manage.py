from .tools.crawler import CovidImageScraper
from .tools.addWebpage import add
from termcolor import colored


def menu():
    print("""
    0. Quit
    1. Add more website to pages.txt
    2. Crawl more picture list to links.txt
    """)


def main():
    run = True
    cmd_list = [0, 1, 2]
    while run:
        cmd = ""
        while cmd not in cmd_list:
            menu()
            cmd = int(input("Your command: "))
            if cmd == 0:
                run = False
                break
            elif cmd == 1:
                web = input("Enter link want to add: ")
                add(web)
            elif cmd == 2:
                crawler = CovidImageScraper()
                crawler.run()
            else:
                print(colored("\n It's not a function.", "red"))


if __name__ == "__main__":
    main()
