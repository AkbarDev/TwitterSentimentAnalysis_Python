import io
import pymongo
import csv
import re

# setup connection to mongoDB
host = "mongodb://localhost:27017/"
database = "Asgmt3"
my_client = pymongo.MongoClient(host)
my_db = my_client[database]
data = my_db.twitter
twitterData = data.find()

tweetCount = 0  # initial tweet count
max_tweetCount = 1000  # considering 1000 tweets
pWords = []  # list to store positive words for each tweet
nWords = []  # list to store negative words for each tweet
table_heading = ["Tweet", "Message/tweets", "happy_words", "sad_words", "polarity"]
print "fetching & processing data from", host

# storing all the positive words from external file
positive_words = []
file = io.open("positive-words.txt", "r")
positive_words = file.readlines()
file.close()

# storing all the negative words from external file
negative_words = []
file = io.open("negative-words.txt", "r")
negative_words = file.readlines()
file.close()


# creating bag of words, counting occurrence of each word reference:
# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php
def word_count(str):
    counts = dict()
    words = str.lower().split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


# creating a separate file that will be used for visualization
file_visualization = open("file_visualization.csv", "wb")
writer_pn = csv.writer(file_visualization)
writer_pn.writerow(["Positive and negative words", "Polarity"])

with open('partA.csv', 'wb') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(table_heading)  # writing table headings as first row in output file
    for item in twitterData:
        tweetCount = tweetCount + 1  # tracking the tweetCount, later will use it as serial number in output
        if tweetCount == max_tweetCount + 1:  # considering 1000 tweets
            break
        if item["tweet"] is not None:
            # cleaning RT from tweets
            item["tweet"] = re.sub('RT', "", item["tweet"])
            # storing tweets in a list
            list = word_count(item["tweet"]).keys()
            # checking for positive words in the tweet
            for word in positive_words:
                if word.strip() in list:
                    # storing positive words from the tweet
                    writer_pn.writerow([word.strip(), "positive"])              # adding positive words to visualization file
                    pWords.append(word.strip())
            # checking for negative words in the tweet
            for word in negative_words:
                if word.strip() in list:
                    # storing negative words from the tweet
                    writer_pn.writerow([word.strip(), "negative"])              # adding positive words to visualization file
                    nWords.append(word.strip())
            if len(pWords) == len(nWords) == 0:
                # tweet polarity is neutral if there are no positive or negative words
                writer.writerow([tweetCount, item["tweet"], "", "", "neutral"])
            if len(pWords) > len(nWords):
                # tweet polarity is positive if number of positive words is greater than negative words
                writer.writerow([tweetCount, item["tweet"], ', '.join(pWords), "", "positive"])
            if len(nWords) > 0:
                if len(pWords) == len(nWords):
                    # tweet polarity is neutral if number of positive words is equal to negative words
                    writer.writerow([tweetCount, item["tweet"], ', '.join(pWords), ', '.join(nWords), "neutral"])
            if len(pWords) < len(nWords):
                # tweet polarity is negative if number of positive words is equal to negative words
                writer.writerow([tweetCount, item["tweet"], "", ', '.join(nWords), "negative"])
            # emptying the pWords & nWords lists for next tweet
            pWords = []
            nWords = []

print "Output file created with name : partA.csv"