# Constellation Quiz &middot; [![Python 3.9.4](https://img.shields.io/badge/python-3.9.4-blue.svg)](https://www.python.org/downloads/release/python-394/) [![Flask 1.1.2](https://img.shields.io/badge/flask-1.1.2-blue.svg)](https://pypi.org/project/Flask/)  
Written for [UWA CITS3403 semester 1 2021 project](https://teaching.csse.uwa.edu.au/units/CITS3403/)  
Constellation quiz is a web app designed to teach people about constellations, made with HTML, CSS, Flask, JQuery, and Bootstrap.  

**Authors:**  
Adam Chen #22988367 (Adam301c)  
Geraldine Chin #22972043 (de-ceased)  
Jakub (Kuba) Wysocki #22716248 (kuba, 22716248)  
James Van Ravestein #22730755 (j-vanrav, WeeJimmyy)  

# Project Timeline:  
**14/04 - Initial meeting:**  
![20210414_184446](https://user-images.githubusercontent.com/54944385/115646677-3a43c680-a355-11eb-864e-f98daa3cf477.jpg)  
[In image: Page layout sketch, list of page sections required and quiz ideas. Page sections listed: 1. Intro, 2. Sky overview, 3. Constellation overview, 4. Quiz, 5. Page navigation/progress bar]
* Project ideas & requirements
* Page minimalist aesthetic and layout, content structure, user experience, audio (music/ sound effects)
* Gamified quiz experience: connect-the dots or finding constellation in image
* This week: complete page mock-up with introduction, overview, constellation, navigation and quiz sections

**21/04 Meeting:**  
* Group task delegation, general organisation
* Technologies required, including virtual environments and flask
* Improving user experience: move most text to optional hidden sections, have key info visible initially
* Crediting image sources
* Fix CSS image spam with JavaScript
* Fix nav bar vanishing behind some images
* This week: incorporate required technologies, general page improvements

**28/04 Meeting:**  
* Flask and databases

**05/05 Meeting:**  
* Flask remodel, database integration
* Remodel page layout, css and info
* authentication
* testing: unit tests and selenium
* complete test on another page

**12/05 Meeting:**  
* Priority: Finish quiz
* Priority: Finish database
* Priority: Finish testing suite
* Cleaning up page design (CSS and content structure)
* Password validation
* Fancy quiz questions: e.g. connect the dots

**15/05 Meeting:**  
* Finish quiz, incorporating the database
* Database migrations
* Implement viewing quiz question scores from database on profile page
* Selenium testing
* CSS and content finishing touches, professional look and feel
* Fix or remove nav bar
* Incorporate quality-of-life JavaScript wherever possible

**16/05 Meeting:**  
* Selenium tests  
* CSS, Layout, responsiveness for different screen sizes  
* Nav bar/ progress indicator  
* Improve quiz user experience and improve feedback (per question and question type results)  
* Route user to profile after quiz  
* Pre-load images  
* Password changing functionality  

# Documentation:  
**Installation**  
```
$ sudo apt install python3
$ sudo apt install python3-pip
$ sudo apt-get install python3-setuptools
$ git clone https://github.com/22716248/Agile-Web-Dev-Proj-1
$ pip3 install -r requirements.txt
```

**Execution**  
```
$ flask run
```

**Viewing Databases**  
```
$ python
>>> from app import db
>>> from app.models import User, Score
>>> User.query.all()
```

**Running Unit Tests**
```
$ python -m unittest tests
```
The unit tests also check each pages functionality and how the app interacts with the database.  
Further explanations for each unit test are in comments of unittests.py  

**Running Selinium Tests**
```
$ python .\selenium-webdriver-tests.py
```
These Selinium tests run through the functionality of the webpage by emulating a user registering, logging in, and taking a test.  

**Example User**
```
username: testuser
password: 1111
```
# Resources:  
**Sources:**  
https://www.thoughtco.com/constellations-pictures-gallery-4122769  
https://en.wikipedia.org/wiki/Constellation  
https://www.thoughtco.com/how-to-find-the-cygnus-constellation-4172706  
https://www.skyatnightmagazine.com/advice/southern-hemisphere-cheat-sheet/  
https://en.wikipedia.org/wiki/Urania%27s_Mirror  
https://in-the-sky.org/data/constellations_list.php  
https://www.constellation-guide.com/  
https://favicon.io/emoji-favicons/milky-way  
https://suberic.net/~dmm/astro/constellations.html  
https://xtrp.io/blog/2020/02/05/scroll-progress-bar-in-js-and-css/  
