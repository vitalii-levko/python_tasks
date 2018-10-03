# python_tasks

## Palindrome

A palindrome is a word that reads the same backward or forward.

Write a function that checks if a given word is a palindrome. Character case should be ignored.

For example, _is_palindrome("Deleveled")_ should return _True_ as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.

```python
class Palindrome:

    @staticmethod
    def is_palindrome(word):
        return None

print(Palindrome.is_palindrome('Deleveled'))
```

## File Owners

Implement a _group_by_owners_ function that:

* Accepts a dictionary containing the file owner name for each file name.
* Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary _{'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}_ the _group_by_owners_ function should return _{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}_.

```python
class FileOwners:

    @staticmethod
    def group_by_owners(files):
        return None

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
```

## Hypotenuse

Write a function to calculate the hypotenuse of a right angled triangle.

For example, _find_hypotenuse_ function should return _5.0_ for the values A(0,4), B(0,0) and C(3,0).

```python
class Hypotenuse:

    @staticmethod
    def find_hypotenuse(x1, y1, x2, y2):
        return None

print(Hypotenuse.find_hypotenuse(0, 0, 3, 4))
```