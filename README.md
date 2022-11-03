# Links: 

## Presentation Link:
https://docs.google.com/presentation/d/13--jr1EjUs3x9Z0JhQVQ63RcAD37qgR8t10Dt4ej23k/edit?usp=sharing

## Dashboard Presentation:
https://docs.google.com/presentation/d/1Fbdeag4vSCsL9-5nd2GrHZuVQTGI6RN9MP3OGq_jNjQ/edit?usp=sharing

## Dashboard Demonstration:
https://drive.google.com/file/d/1X_HcvBglTtG5OsedopCgpoCq4zTon7WE/view?usp=sharing

# Communication Protocols:
The team has established a Slack channel in which to issue any communications.  If needed, video meets through Zoom, Google Meets, Teams, etc. can also be arranaged using the Slack channel.

# Outline:
Outline is availabe in Presentation link and Dashboard Presentation Link.

## Data Source:
The data used in this project is sourced from https://www.seanlahman.com/baseball-archive/statistics/. This is a large database of baseball data in various formats such as csv, MySQL, SQLite, or MS Access that is maintained and updated primarily by Sean Lahman. The best description of the data comes straight from the website readme found at https://www.seanlahman.com/files/database/readme2021.txt:
>This database contains pitching, hitting, and fielding statistics for Major League Baseball from 1871 through 2021. It includes data from the two current leagues (American and National), the four other "major" leagues (American Association, Union Association, Players League, and Federal League), and the National Association of 1871-1875.
>This database was created by Sean Lahman, who pioneered the effort to make baseball statistics freely available to the general public. What started as a one man effort in 1994 has grown tremendously, and now a team of researchers have collected their efforts to make this the largest and most accurate source for baseball statistics available anywhere. (See Acknowledgements below for a list of the key contributors to this project.)
>None of what we have done would have been possible without the pioneering work of Hy Turkin, S.C. Thompson, David Neft, and Pete Palmer (among others). All baseball fans owe a debt of gratitude to the people who have worked so hard to build the tremendous set of data that we have today. Our thanks also to the many members of the Society for American Baseball Research who have helped us over the years. We strongly urge you to support and join their efforts. Please visit their website (www.sabr.org).

## Question(s) to Answer:
The question we seek to answer is that which baseball statistics, if any, can be used to accurately predict a team's win/loss ratio for a given season. We will compare the accuracy of prediction between several different baseball statistics to determine which gives the best prediction or perhaps which combination of baseball statistics yields the best prediction.

## Database: 
Currently hosted locally within SQL. All SQL related files can be found in their relevant folder. These files include images of uploaded data in PgAdmin, a schema for SQL, an ERD, and a final exported csv after a join occurred. 

## Machine Learning:
Linear Regression & *MAYBE* multi-variable linear regression depending on progress. Examples of linear regression ML are present in ML branch. 

## Dashboard
Work has begun on integrating ML into Flask to create a prediction webpage which covers our interactive portion of the final. HTML, CSS, and App.Py files are currently available on Dasboard branch. The created Flask Dashboard meets all requirements based on provided rubric. 

## Group Roles:
Square - David Poole

Triangle - Bruce Cowen

Circle - Shared.

X - Dylan Scott

## Github Branches:
Main - David Poole

MLAnalysis - Bruce Cowen

Dashboard - Dylan Scott

## Technology Used:
### Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis along with excel and the various functiosn that reside within excel. Further analysis will be completed using Python once we drill down the specific data that we want.

### Database Storage
PgAdmin and SQL are the database and platform we will be using to integrate our data. We will integrate our data using Flask and hope to host it using Heroku.

### Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. The type of machine learning we will use will be supervised machine learning. We will create both a linear regression model and a multivariate linear regression model to determine which fits our needs better. We will not need to use a Deep Learning Model as our data is pretty straightforward.

### Dashboard
In addition to using a Flask template, we will also integrate D3.js for a fully functioning and interactive dashboard. Additionally, we will hopefully integrate the ML process into our webpage so that it can predict the outcomes of inputs. It will be hosted locally with the intent to push to a cloud based platform. 

## References
- https://www.baseball-reference.com
- https://www.fangraphs.com
- https://www.seanlahman.com/baseball-archive/
- https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/
- https://towardsdatascience.com/deploying-machine-learning-models-into-a-website-using-flask-8582b7ce880

