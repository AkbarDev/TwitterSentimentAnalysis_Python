# Overview

I have considered 1000 tweets for this project. I have fetched them from MongoDB locally, which I obtained in the previous assignment. I have considered only the 
messages or texts and ignored all other metadata. I have cleaned all the ‘RT’ from the tweets. Since I have considered the tweets that were already cleaned, therefore I 
have not performed any further cleaning. For creating bag of words for each tweet, I have created a separate function named “word_count”. The logic I have used is to 
first split each word from the sentence and then maintain their counts. For checking if words in the bag of words are positive or negative, I have obtained the list of 
positive and negative words from an online source. These files are to be placed in the project’s root directory. For displaying and tagging each tweet as either positive 
or negative, I have stored the output in a separate csv file named: partA.csv. Apart from tweet and polarity, I have also created separate columns for positive and 
negative words found in the respective tweet. If the number of positive and negative words are same, the tweet is considered to be neutral. For visualization, I have 
stored all the positive and negative words occurring in tweets in a separate csv file named: file_visualization.csv.

## File description

* sentiment_analysis.py: script file for sentiment analysis logic
* partA.csv: csv file for results of sentiment analysis (tweet & polarity)
* positive-words.txt: supporting file required for the program to run
* negative-words.txt: supporting file required for the program to run
* file_visualization.csv: file to used for visualization
