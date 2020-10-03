# -*- coding: utf-8 -*-
import requests
import json
from naomi import plugin


# The speechhandler plugin represents something that Naomi does
# in response to a request from the user. This is often a spoken
# response, but can also be an action like turning on a light or
# sending an email. It is the functional equivalent of a skill on
# most other assistant platforms.
# For details about writing a speech handler, see:
# https://projectnaomi.com/dev/docs/developer/plugins/speechhandler_plugin.html
class NewsPlugin(plugin.SpeechHandlerPlugin):
    # Intents describe how your plugin may be activated.
    # At the simplest level, just write all the things you think
    # someone might say if they wanted to activate your
    # plugin. Finally, supply a link to the handle method,
    # which Naomi will use when your intent is selected.
    def intents(self):
        return {
            'NewsIntent': {
                'locale': {
                    'en-US': {
                        'keywords': {
                            'NewsKeyword': [
                                'news',
                                'headlines',
                                'articles'
                            ],
                            'CategoryKeyword': [
                                'business',
                                'entertainment',
                                'general',
                                'health',
                                'science',
                                'sports',
                                'technology'
                            ],
                            # 'LanguageKeyword': [
                            #     'ar',
                            #     'de',
                            #     'en',
                            #     'es',
                            #     'fr',
                            #     'he',
                            #     'it',
                            #     'nl',
                            #     'no',
                            #     'pt',
                            #     'ru',
                            #     'se',
                            #     'ud',
                            #     'zh'
                            # ],
                            'CountryKeyword': [
                                'United Arab Emirates',#ae
                                'Argentina',#ar
                                'Austria',#at
                                'Australia',#au
                                'Belgium',#be
                                'Bulgaria',#bg
                                'Brazil',#br
                                'Canada',#ca
                                'Switzerland',#ch
                                'China',#cn
                                'Colombia',#co
                                'Cuba',#cu
                                'Czech Republic',#cz
                                'Germany',#de
                                'Egypt',#eg
                                'France',#fr
                                'United Kingdom',#gb
                                'Great Britain',#gb
                                'UK',#gb
                                'Greece',#gr
                                'Hong Kong',#hk
                                'Hungary',#hu
                                'Indonesia',#id
                                'Ireland',#ie
                                'Israel',#il
                                'India',#in
                                'Italy',#it
                                'Japan',#jp
                                'Korea',#kr
                                'Lithuania',#lt
                                'Latvia',#lv
                                'Morocco',#ma
                                'Mexico',#mx
                                'Malaysia',#my
                                'Nigeria',#ng
                                'Netherlands',#nl
                                'Norway',#no
                                'New Zealand',#nz
                                'Philippines',#ph
                                'Poland',#pl
                                'Portugal',#pt
                                'Romania',#ro
                                'Serbia',#rs
                                'Russian Federation',#ru
                                'Russia',#ru
                                'Saudi Arabia',#sa
                                'Sweden',#se
                                'Singapore',#sg
                                'Slovenia',#si
                                'Slovakia',#sk
                                'Thailand',#th
                                'Turkey',#tr
                                'Taiwan',#tw
                                'Ukraine',#ua
                                'United States of America',#us
                                'United States'#us
                                'US',#us
                                'Venezuela',#ve
                                'South Africa'#za
                            ]
                        },
                        'regex': {
                            'Query': [
                                " for (?P<Query>) on ",
                                " for (?P<Query>) using ",
                                " for (?P<Query>) in the ",
                                " for (?P<Query>.*)$",
                                " about (?P<Query>.*)$"
                            ],
                            'Source': [
                                " search (?P<Source>) for ",
                                " on (?P<Source>.*)$",
                                " using (?P<Source>.*)$"
                            ]
                        },
                        'templates': [
                            'all {NewsKeyword} about {Query}'
                            'search for {Query} using {Source}',
                            'search for {Query} on {Source}',
                            'search {Source} for {Query}',
                            'top {NewsKeyword} about {Query}',
                            'top {NewsKeyword} in {CountryKeyword}',
                            'top {CategoryKeyword} {NewsKeyword} in {CountryKeyword}',
                            'search for {Query} in the {NewsKeyword}',
                            "read the {NewsKeyword}",
                            "what is in the {NewsKeyword}",
                            "what is happening in the {NewsKeyword}",
                            "what is today's {NewsKeyword}"
                        ]
                    }
                },
                'action': self.handle
            }
        }

    # The handle method is where you pick up after Naomi has
    # identified your intent as the one the user was attempting
    # to activate.
    def handle(self, intent, mic):
        # The intent parameter is a structure with information about
        # the user request. intent['input'] will hold the transcription
        # of the user's request.
        #text = intent['input']

        api_key='API_KEY'
        top_headlines = "https://newsapi.org/v2/top-headlines" + "&apiKey=" + api_key
        top_headline_query = "https://newsapi.org/v2/top-headlines?q=" + Query + "&apiKey=" + api_key
        top_headline_sources = "https://newsapi.org/v2/top-headlines?sources=" + Source + "&apiKey=" + api_key
        top_headline_country = "https://newsapi.org/v2/top-headlines?country=" + CountryKeywordAdjustment + "&apiKey=" + api_key
        top_headline_category = "https://newsapi.org/v2/top-headlines?category=" + CategoryKeyword + "&apiKey=" + api_key
        top_headline_country_category = "https://newsapi.org/v2/top-headlines?country=" + CountryKeywordAdjustment + "?category=" + CategoryKeyword + "&apiKey=" + api_key
        everything = "https://newsapi.org/v2/everything?q=" + Query + "&apiKey=" + api_key














        response = requests.get(url)
        jsondoc = str(response.content, 'utf-8')
        jokedata = json.loads(jsondoc)
        response = jokedata["joke"]

        # The mic parameter is a microphone object that you can
        # use to respond to the user.
        mic.say(response)