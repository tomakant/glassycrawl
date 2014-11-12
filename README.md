===================
#Welcome to the Glassdoor Review Summarizer!

###The Project

This project was designed to help job hunters gain a better understanding of overall employee sentiment by looking at Glassdoor reviews from present and past employees. 

The web app that I created is called Glassy Crawl, and has dual functionality. Users can search for companies based on certain attributes such as work life balance, great coworkers or free lunches. 

###The Data Collection Process

I built a web crawler utilizing import.io to scrape Glassdoor.com employee reviews for about 1,000 companies. The import.io tool allowed me to train examples and pull out elements from a company's review page based on HTML/CSS properties. After five training examples were given, import.io crawls Glassdoor for other company review pages with similar HTML and CSS tags as the training examples. I set up the crawler to grab only the first 300 reviews for each employer, which can then be saved as a *.csv* or _.json_ file for exporting. 

I utilized a TF-IDF Vectorizer with 15,000 features in order to create my model. Users can specify multiple attributes that they are looking for in an employer and run the search. The vectorizer will then search the employer database where those attributes appeared the most. 

![alt text](https://github.com/tomakant/glassycrawl/blob/master/static/import.io.png "import.io")

###The code

Python Libraries used include Sklearn, Pandas, NLTK, Flask

Through the course of the project, I learned a lot about web development using HTML, CSS, JavaScript and Python Flask.



![alt text](https://github.com/tomakant/glassycrawl/blob/master/static/Glassdoor.png "Glassdoor")
