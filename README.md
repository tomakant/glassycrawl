===================
#Welcome to the Glassdoor Review Summarizer!

###The Project

This project was designed to help job hunters gain a better understanding of overall employee sentiment by looking at Glassdoor reviews from present and past employees. 

The web app that I created is called Glassy Crawl, and has dual functionality: 1. Search for companies based on certain attributes such as work life balance, great coworkers or free lunches. 2. Search for individual employers to return word clouds of frequently occurring words in pros and cons reviews.

###The Data Collection Process

I built a web crawler utilizing import.io to scrape Glassdoor.com employee reviews for about 1,000 companies. The import.io tool allowed me to train examples and pull out elements from a company's review page based on HTML/CSS properties. After five training examples were given, import.io crawls Glassdoor for other company review pages with similar HTML and CSS tags as the training examples. I set up the crawler to grab only the first 300 reviews for each employer, which can then be saved as a *.csv* or _.json_ file for exporting. 

I utilized a TF-IDF Vectorizer with 15,000 features in order to create my model. Users can specify multiple attributes that they are looking for in an employer and run the search. The vectorizer will then search the employer database where those attributes appeared the most. 

![alt text](https://github.com/tomakant/glassycrawl/blob/master/static/import.io.png "import.io")

###The code

The code for this project was written primarily in python, leveraging the following libraries: sklearn, pandas, numpy, NLTK, and wordcloud. On the web development side, HTML, CSS, Javascript, Flask, and Twitter Bootstrap were used to build out the web app. 

###Using GlassyCrawl
<html>
<div style="text-align:center" markdown="1">
[alt text](https://github.com/tomakant/glassycrawl/blob/master/static/_images/web_app.png "WebApp")
</div>
</html>

####By Attribute
Type one or more attributes (separated by commas) that you are looking for in your next employer.
<div style="text-align:center" markdown="1">
![alt text](https://github.com/tomakant/glassycrawl/blob/master/static/_images/attributes.png "Attributes")
</div>

####By Employer
Search for employers within the database. Be sure to select the employer from the dropdown menu that populates.

<div style="text-align:center" markdown="1">
![alt text](https://github.com/tomakant/glassycrawl/blob/master/static/_images/pros_cons.png "ProsCons")
</div>
