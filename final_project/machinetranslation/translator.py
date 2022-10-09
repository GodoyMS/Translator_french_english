"""This file translates from english to french and french to english"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
apikey_lt=IAMAuthenticator("vg7kPENua9nsny6UJTAPBJO1bIEZIbiGmNYaKDYLNBPf")
VERSION_LT="2018-05-01"
language_translator=LanguageTranslatorV3(authenticator=apikey_lt, version=VERSION_LT)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """This function translates from english to french
    """
    if english_text!="":
        english_to_french = language_translator.translate(text=english_text, model_id="en-fr").get_result()
        french_text=english_to_french["translations"][0]["translation"]
    else:
        french_text=""

    return french_text

def french_to_english(french_text):
    """This function translates from french to english"""
    if french_text!="":
        french_to_english = language_translator.translate(text=french_text, model_id="fr-en").get_result()
        english_text=french_to_english["translations"][0]["translation"]
    else:
        english_text=""
    return english_text
