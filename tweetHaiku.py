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


def mark_tweets(tweet):
    tagged_tweets = nltk.pos_tag(nltk.word_tokenize(tweet))
    return tuples_to_multi_dict(tagged_tweets)


def tuples_to_multi_dict(tuple_list):
    tuple_dict = dict(tuple_list)
    new_tuple_dict = defaultdict(list)
    for key, value in tuple_dict.items():
        new_tuple_dict[value].append(key)
    return new_tuple_dict


def create_training_haikus(haiku_list):
    file = open('haikus.txt', 'r')
    i = 0
    for line in file:
        line = nltk.pos_tag(nltk.word_tokenize(line))
        parts_of_speech_order = [item[1] for item in line]
        haiku_list[i].append(parts_of_speech_order)
        i += 1
    print(haiku_list)


words = scrape_tweets("https://twitter.com/kanyewest?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor")
create_training_haikus(model_orders)
