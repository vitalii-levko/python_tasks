#!/usr/bin/python3

class Palindrome:

    @staticmethod
    def is_palindrome(word):
        idx = -1
        mid = len(word) / 2
        for character in word:
            if character.lower() != word[idx].lower():
                return False
            idx -= 1
            if -idx > mid:
                break
        return True

print(Palindrome.is_palindrome('Deleveled'))
