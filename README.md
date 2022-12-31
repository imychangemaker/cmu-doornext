# Application with Data-Focused Python: DoorNext

DoorNext is a one-stop platform for settlers to search for neighborhood information in a quick and convenient manner. Our vision is to help settlers to envision their future life when moving next to a new neighborhood. Relocation has always been a traumatic experience with all the uncertainties. We believe there is no better way to get informed quickly for decision making. DoorNext erases all the hassle by providing you comprehensive details of a certain neighborhood, including demographics, events, and weather. You could fully utilize our platform before, during and after your moving.

## Technology

**Python 3.8**

Make sure that the below mentioned packages with corresponding version are installed. Otherwise, the program may not compile, or the output may deviate from the expected outcome.
1. matplotlib (version 3.4.3 or above)
2. pandas (version 1.3.3)
3. beautifulsoup4 (version 4.10.0 or above)
4. requests (version 2.25.1)
5. json5
6. selenium (version 3.141.0 or above)
7. seaborn (version 0.11.1 or above)
8. numpy
9. tkinter
10. datetime
11. urllib3
12. pillow (version 8.3.2 or above)
13. opencv-python (version 4.2.0 or above)
14. imageio (version 2.9.0 or above)

## Installation

**Minimum Hardware requirements**

* Modern Operating System: Windows 8 or higher; Mac OS X 10.11 or higher, 64-bit; Linux: RHEL 6/7, 64-bit (almost all libraries also work in Ubuntu) 
* x86 64-bit CPU (Intel / AMD architecture)
* 2 GB or higher RAM
* 2 GB free disk space

**Installing WebDriver for Chrome** - This is a requirement for the Selenium package.
1. Before downloading chromedriver, check Google Chrome version, make sure it's updated. (To check the Chrome version: Go to Settings and on the left navigation, click on About Chrome).
![image](https://user-images.githubusercontent.com/48016878/210124359-c00e14fe-4bae-4db5-b5a2-6a277b80d405.png)
2. As per the chrome version, download the [chrome driver](https://chromedriver.chromium.org/downloads)
![image](https://user-images.githubusercontent.com/48016878/210124456-f678bc2e-6341-419d-a2d6-5229ae0fddbf.png)
3. Download the extension as per your operating system and store the **chromedriver** in the project directory under the **driver** folder
![image](https://user-images.githubusercontent.com/48016878/210124468-ede612bf-bdf3-4763-90fa-9c375a6232c8.png)
4. Unzip the chromedriver and install the driver.\
a. For Mac Users - Allow the chromedriver to be installed. You will find this in System Preference under Security & Privacy - General tab (this step needs to be done while running the program).\
b. For Windows Users - Allow the chromedriver to be installed. (If you are unable to install the same just add an exception in the firewall)

**Installing Anaconda Navigator and PyCharm**

1. Download [Anaconda Navigator](https://www.anaconda.com/products/individual)
![image](https://user-images.githubusercontent.com/48016878/210124499-7f618da5-c177-467e-ab81-46a563030cd6.png)
2. Follow on screen instructions
![image](https://user-images.githubusercontent.com/48016878/210124592-3206ba3e-d61b-446d-8ab5-e1324683a513.png)
3. Download [PyCharm (Community Version)](https://www.jetbrains.com/pycharm/download/#section=mac.) software
![image](https://user-images.githubusercontent.com/48016878/210124604-3400ab61-e14d-4ec3-853c-5ffc1c41ea23.png)
4. Install the software on your computer by following the on-screen instructions.
5. Launch PyCharm from Anaconda Navigator. It is highly recommended to use PyCharm instead of other IDEs due to known bugs in other environments.
![image](https://user-images.githubusercontent.com/48016878/210124611-6fcf7321-bcff-42a5-b61d-89a4b6ec14be.png)
6. Set up your Python Interpreter (If not already set by default) - Refer to the sample
![image](https://user-images.githubusercontent.com/48016878/210124616-c9b74ab5-ecd8-4a85-bd17-216fcb3420c8.png)
7. Open Terminal or Command Prompt and install the below mentioned packages. If necessary, please also install the latest version of the other in-built packages in the Technology section.
* pip install selenium
* pip install opencv-python
* pip install tkinter
8. Once setting up all the software and installing the packages, open the Project (DoorNext) in PyCharm and execute the app.py file.

## Run

DoorNext gets your input and returns you different categories of data based on your location or area of interest. The screenshot below shows the home page, which is the main menu.

![image](https://user-images.githubusercontent.com/48016878/210124641-2568b97b-002b-47f9-915c-19b3037e1095.png)

**How to use DoorNext?**

For detailed demo, you may visit the [video](https://youtu.be/r3tU4bMWe4s).

1. On the home page, input the area name or zip code that you want to search the information for. The search is case insensitive, and the default value is Pittsburgh.
![image](https://user-images.githubusercontent.com/48016878/210124650-4496627e-ad8f-4ef0-911f-c5415f32029e.png)
2. Click “search” to start browsing the information for your neighborhood. It will automatically return you the vaccination data. You can also navigate to the other pages using the sidebar directly instead of clicking “search”.

**Six categories of information**
1. Vaccination: COVID-19 vaccination data
![image](https://user-images.githubusercontent.com/48016878/210124661-3b3527ab-c732-4a74-b392-2d0bac9709e0.png)
2. Demographics: Political parties and crime rates
![image](https://user-images.githubusercontent.com/48016878/210124665-925cfed8-c66c-41f8-8a1f-950956626ba6.png)
3. Weather: Current atmospheric data
![image](https://user-images.githubusercontent.com/48016878/210124670-f197b1cb-5fed-409d-882b-f8b8f03d4f71.png)
4. Volunteering: Occurring volunteering activity data
![image](https://user-images.githubusercontent.com/48016878/210124675-a3f81eb7-5b10-4f89-9e25-285354b47a41.png)
5. Events: Occurring events data
![image](https://user-images.githubusercontent.com/48016878/210124679-bc04b46f-06de-463f-8899-8ef4c028743c.png)
Here you can choose to view the events in a map format by clicking “Event Map” on the sidebar. The button will only appear when you click “Events”.
![image](https://user-images.githubusercontent.com/48016878/210124681-8a2114e7-1db4-42b9-87b1-30b6e999634a.png)
6. Housing: Available housing listings
![image](https://user-images.githubusercontent.com/48016878/210124687-9a4a3111-879d-4bd6-9afb-7a73f6c703f2.png)

The “More Statistics” tab summarizes the aggregated statistics of the real estimate market in the neighborhood. Again, the button will only appear when you click “Housing”.
![image](https://user-images.githubusercontent.com/48016878/210124693-5047b0e9-ab40-4725-85e5-883a22b8d7aa.png)


## Expected Warnings

Depending on the matplotlib version, the graph appearance may change.

## Credits

We would like to express special thanks to\
● [IQAir - Air quality](https://www.iqair.com/us/air-pollution-data-api)\
● [All Events](https://allevents.in)\
● [CDC](https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD)\
● [CraigList](https://pittsburgh.craigslist.org/d/apartments-housing-for-rent/search/apa)\
● [Create the Good](https://createthegood.aarp.org/volunteer-search/)\
● [Weather](https://www.timeanddate.com/weather/usa/pittsburgh)\
● [Demographics - Crime rate](https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate)\
● [Demographics - Political Affiliations](https://www.pewforum.org/religious-landscape-study/compare/party-affiliation/by/state/)\
● [Mapbox](https://gist.github.com/busybus/b316596556933f7697671fd33f31fe87)\
● [freeCodeCamp.org](https://www.youtube.com/watch?v=YXPyB4XeYLA) for tkinter course\
● OpenStreetMap\
● Stack Overflow community

## Contributors
Ashlyn Im | manyii@andrew.cmu.edu\
Jesus Herrera | jeherrer@andrew.cmu.edu\
Mariano Hernandez | marianoh@andrew.cmu.edu\
Mohil Jain | mohilj@andrew.cmu.edu

## Couse Details

As a project of course:\
Institution: Carnegie Mellon University\
Term: 2021 Fall\
Code: 95-888 Data Focused Python\
Instructor: Prof. John K. Ostlund

