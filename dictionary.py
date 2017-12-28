#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 14:26:50 2017

@author: russell
"""
# create data
import json
dictionary = json.load(open('dictionary_data.json'))


# define function
from difflib import get_close_matches
def define_this():
    word=input("Enter a word/phrase to define or 'q' to quit: ")
    if word.lower() != 'q':
        try:
            for definition in dictionary[word]:
                print(definition)
        except:
            try:
                for definition in dictionary[word.lower()]:
                    print(definition)
            except:
                try: 
                    for definition in dictionary[word.lower().title()]:
                        print(definition)
                except:
                    try:
                        for definition in dictionary[word.upper()]:
                            print(definition)
                    except:
                        try:
                            print('Sorry, that has no definition. Did you mean '+\
                                str(get_close_matches(word,dictionary.keys())[0])+\
                                '?'
                                )
                        except:
                            print('Sorry, that has no definition.')
        define_this()

# execute function
define_this()
