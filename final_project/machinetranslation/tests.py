"""Unit testing for translation.py
"""
import unittest

from translator import french_to_english, english_to_french

class Testenglish_to_french(unittest.TestCase): 
    #Godoy Liam Muñoz Solorzano
    """
    Unit testing for english to french
    """
    def test1(self): 
        """
        Function test english to french
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"),"Hello")        
        self.assertEqual(english_to_french(""), "")

class Testfrench_to_english(unittest.TestCase): 
    #Godoy Liam Muñoz Solorzano
    """
    Unit testing for french to english
    """

    def test1(self): 
        """
        Function test french to english
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"),"Bonjour")
        self.assertEqual(french_to_english(""), "")


unittest.main()
