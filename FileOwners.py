#!/usr/bin/python3
class FileOwners:

    @staticmethod
    def group_by_owners(files):
        group = {}
        for key, value in sorted(files.items()):
            group.setdefault(value, []).append(key)
        return group

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
