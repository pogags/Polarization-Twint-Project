# Polarization & a Divided America

*Project by Paul Gagliardi and James Duchesneau*

## Overview

As Americans, it can seem that we are more divided than we have ever been when it comes to politics. Anecdotally, the civil unrest of 2020 and January 6th riots at the capital point towards a public that is increasingly polarized and partisan. In this study, we look to see if we can catch any objective clues that would allow us to show numerical proof that we are truly living in more divided times.

Have we become more polarized?
### Strategy

The best way to understand what people think about topics in tweets is to utilize language. To adress our research question, we will be creating data by pulling tweets, and using data science methods to analze the text data.

### Content

Reference the [Project Writeup](Polarization%20%26%20a%20Divided%20America.pdf) for a detailed summary of findings and more info on this project. 

To see how the graphic were generated and how data was processed, see [Generate Graphs](GenerateGraphs.ipynb).

To see how the Tweets were pulled, see [Pull Tweets](PullTweets.ipynb).

## Data
### Tweets

We examined tweets from November across five years (2016-2020) and five topics to examine how language has changed. The five topics we used were chosen because of their political significance as well as their tendency to be hotly debated and catalysts for polarization. The topics are:  
• Abortion  
• Education  
• Gun Control  
• Healthcare  
• Immigration  

~500 Tweets were pulled from each subject at each timeframe, meaning roughly 2500 for each subject and 12500 total.

### Metrics

For this project, we examined two metrics and utilized a third visual representation strategy to try and pull together a picture of how the language over these topics have changed.  
• Sentiment Analysis using [NLTK](https://www.nltk.org/)  
• [Extreme Word](extremewords.txt) Count   
• Word Cloud (visual representation)  

## Twint

This project relied heavily on [twint](https://github.com/twintproject/twint), a python package that allows for older tweets to be scraped from Twitter without the use of the Twitter API. A example is listed [here](twintPullExample.py). 

### Limitations
Due to the nature of the twint package and how it scrapes Twitter, the [PullTweets](PullTweets.ipynb) file can occasionally struggle with pulling every CSV correctly the first time. If a CSV is not being generated, simply try running the cell or the specific line of code to generate that CSV again. This may take one or several tries.

If this does not work, simply use the files listed in the [TweetCSV-archive](TweetCSV_archive) folder.

# Conclusion

Based on the data we collected, and specifically focusing on the extreme word counts, it is hard to deny that there is quality evidence for continuing polarization among the American public, at least when it comes to the politics around the topics of Abortion, Education, Gun Control, Healthcare, and Immigration. Extreme word use **doubled** for nearly every topic, and increased in all topics.

We do not have as strong evidence for continued division when examining sentiment analysis, but we do see some. Negative sentiment on Education is indicating more division and passion in that area (educations extreme words also doubled) and we saw much less neutrality and more opinionated opinions surrounding the area of healthcare (extreme words more than doubled here).

Combining these observations, we can confidently conclude that Healthcare and Education show strong evidence that they are quickly becoming more controversial/polarizing, whereas Gun Control, Immigration, and Abortion have decent evidence for becoming more controversial/polarizing.
