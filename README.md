# USTH Web crawler - GROUP 5

## Introduction

    - This website is built for the Final Project of the course: USTH Web Application - Intake 2019-2020, ICT Department.
    - The website is a COVID-19 X-RAY IMAGE REPRESENTATION, where images are crawled automatically from another website.
    - The whole system is built mainly on Python (Libraries used: selenium, flask, termcolor,..), HTML, CSS and JavaScript.

## Installation

1. Setup the environment
For best experience:
    - This automation setup is for Windows 64bits only.
    - Update your web browser either Chrome or Firefox to the latest version.
```console
python setup.py
```
2. Run the website locally by run:
* Manage the data:
```console
python data/manage.py
```

* Run website locally:
```console
python app.py
```

* Open web browser and connect into *127.0.0.1:5000/*.

## HOW IT WORKS:

1. In 'tools' folder, there are two tool files, namely 'crawler.py' and 'addWebpage.py'.
    - addWebpage.py is a tool to add a new website link to the list, in order to crawl image data. (1)
    - crawler.py is tool to get image links from websites added to the list from step (1), using python selenium (retrieving css selectors), then write crawled links into a file named 'data/links.txt'.
    
2. With python flask, the crawled links are automatically updated onto the website.

3. For more information, view our [documentation](https://docs.google.com/document/d/1bM8w23ge77J3hhJFH-npvPDKrf3ZHwGpgl65mByK6cg/).


## Group members:
1. Lê Trọng Hoàng - BI9-241 **_Leader_**
2. Đoàn Trung Kiên - BI9-130 _member_
3. Nguyễn Thế Trung - BI9-224 _member_
4. Lưu Quý Nhân - BI9-178 _member_
5. Trần Đức Quang - BI8-144 _member_
