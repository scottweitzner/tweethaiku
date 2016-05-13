import nltk
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import defaultdict


model_orders = defaultdict(list)


def scrape_tweets(url):
    twitter_page = urlopen(url)
    source = BeautifulSoup(twitter_page, "html.parser")
    tweets = source.find_all("p", class_="tweet-text")
    tweets = [str(tweet).replace(str(tweet), re.sub("<[^>]*>", "", str(tweet))) for tweet in tweets]
    return tweets


def create_training_haikus(haiku_list):
    file = open('haikus.txt', 'r')
    i = 0
    for line in file:
        line = nltk.pos_tag(nltk.word_tokenize(line))
        parts_of_speech_order = [item[1] for item in line]
        for POS in parts_of_speech_order:
            haiku_list[i].append(POS)
        i += 1


words = scrape_tweets("https://twitter.com/kanyewest?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor")
create_training_haikus(model_orders)
