#!/usr/bin/python3

class Palindrome:

    @staticmethod
    def is_palindrome(word):
        return word.lower() == word[::-1].lower()

print(Palindrome.is_palindrome('Deleveled'))
