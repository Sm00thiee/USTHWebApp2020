from termcolor import colored
def add(website):
    with open("data/pages.txt", "r") as f_r:
        if (website+'\n') in f_r.readlines():
            print(colored("\nThis website has already in the list!", "red"))
        else:
            with open("data/pages.txt", "a") as f_a:
                f_a.write(f"{website}\n")
            print(colored("\nSuccessfully added the website", "green"))