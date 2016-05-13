import nltk
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import defaultdict


model_orders = defaultdict(list)
model_order_list = []
pos_dict = defaultdict(list)


def scrape_tweets(url):
    twitter_page = urlopen(url)
    source = BeautifulSoup(twitter_page, "html.parser")
    tweets = source.find_all("p", class_="tweet-text")
    tweets = [str(tweet).replace(str(tweet), re.sub("<[^>]*>", "", str(tweet))) for tweet in tweets]
    return tweets


def mark_tweets(tweet_list):
    all_tweets_string =""
    for tweet in tweet_list:
        all_tweets_string += tweet
    tagged_tweets = nltk.pos_tag(nltk.word_tokenize(all_tweets_string))
    tuples_to_dict(tagged_tweets)


def tuples_to_dict(tuple_list):
    global pos_dict
    tuple_dict = dict(tuple_list)
    new_tuple_dict = defaultdict(list)
    for key, value in tuple_dict.items():
        new_tuple_dict[value].append(key)
    pos_dict = new_tuple_dict


def create_training_haiku_list_phase1():
    global model_order_list
    file = open('haikus.txt', 'r')
    line = nltk.pos_tag(nltk.word_tokenize(file.readline()))
    parts_of_speech_order = [item[1] for item in line]
    for POS in parts_of_speech_order:
        model_order_list.append(POS)


def remove_unhelpful_tags(some_list):
    global model_order_list
    some_list.remove(':')
    model_order_list = some_list


def create_haiku():
    global pos_dict
    haiku = ""
    for pos in model_order_list:
        haiku += pos_dict[pos].pop() + " "
    return haiku


if __name__ == "__main__":
    last_tweets = scrape_tweets("https://twitter.com/kanyewest?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor")
    create_training_haiku_list_phase1()
    remove_unhelpful_tags(model_order_list)
    mark_tweets(last_tweets)
    print(create_haiku())
