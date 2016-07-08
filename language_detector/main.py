# -*- coding: utf-8 -*-
"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    for x in LANGUAGES:
	    if x['name'] == 'English':
	        english_list = x['common_words'] #store common english words in a list for easy accessibily
	    elif x['name'] == 'Spanish':
	        spanish_list = x['common_words'] #store common spanish words in a list for easy accessibily
	    elif x['name'] == 'German':
	        german_list = x['common_words'] #store common german words in a list for easy accessibily
	    else:
	    	break
    text_list = text.split()    #Breaks text input into separate words
    
    english_matches = [x for x in english_list if x in text_list] #Creates a list for words in the text that match with english words.
    spanish_matches = [x for x in spanish_list if x in text_list] #Creates a list for words in the text that match with spanish words.
    german_matches = [x for x in german_list if x in text_list] #Creates a list for words in the text that match with german words.
    
    english_hits = len(english_matches)     #Stores the number of english words in the text to allow for comparison
    spanish_hits = len(spanish_matches)     #Stores the number of spanish words in the text to allow for comparison
    german_hits = len(german_matches)       #Stores the number of german words in the text to allow for comparison
    
    language_matches = {"English":english_hits, "Spanish":spanish_hits, "German":german_hits}   #Created a dict to allow for easy lookup and comparisons.
    return (max(language_matches, key=language_matches.get))    #Returns the language with the most word matches in the text.