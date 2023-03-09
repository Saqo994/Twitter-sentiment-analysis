from textblob import TextBlob
import tweepy
from textblob.sentiments import NaiveBayesAnalyzer
import telebot
from telebot import types

bot = telebot.TeleBot("YOUR TOKEN")




def twitter(word):
    sentence = "Program to analyse"
    analysis = TextBlob(sentence).sentiment

    api_key = 'YOUR KEY'
    api_secret = 'YOUR SECRET'
    access_token = 'YOUR TOKEN'
    access_token_secret = 'YOUR TOKEN SECRET'

    twitter = tweepy.OAuthHandler(api_key, api_secret)
    twitter.set_access_token(access_token, access_token_secret)
    api = tweepy.API(twitter)

    corpus_tweets = api.search_tweets({word}, count=200)
    for tweet in corpus_tweets:
        print(tweet.text)

    blob_object = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
    analysis = blob_object.sentiment
    text1 = analysis
    return text1

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("If you know my destination, choose the topic.Else click HERE.")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Hi, {0.first_name}!".format(message.from_user), reply_markup=markup)



@bot.message_handler(content_types=["text"])
def func(message):
    if(message.text == "If you know my destination, choose the topic.Else click HERE."):
        bot.send_message(message.chat.id, text="Im checking the positive, negative or neutral attitude of the selected topic based on the last 200 tweets on Twitter.Now, please type topic.")
    else:
        bot.send_message(message.chat.id, "Wait a minute, please!")
        bot.send_message(message.chat.id, twitter(message.text))


bot.polling(none_stop=True, interval=0)





