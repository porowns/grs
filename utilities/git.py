import subprocess
import os


def git_get_changed_files():
    response = subprocess.run(
        ['git', '--no-pager', 'diff', '--name-status'], stdout=subprocess.PIPE)
    return response.stdout.decode('utf-8')


def git_get_untracked_files():
    response = subprocess.run(
        ['git', 'ls-files', '--others', '--exclude-standard'],
        stdout=subprocess.PIPE
    )
    return response.stdout.decode('utf-8')


def git_get_new_directories():
    directories = set()
    response = subprocess.run(
        ['git', 'ls-files', '--others', '--exclude-standard'],
        stdout=subprocess.PIPE
    )
    response = response.stdout.decode('utf-8').split("\n")
    for file in response:
        if file != "":
            directories.add(os.path.dirname(file))
    return directories


def git_get_encodings(file):
    response = subprocess.run(
        ['git', 'check-attr', '-a', file], stdout=subprocess.PIPE)
    response = response.stdout.decode('utf-8')
    file_encoding_lines = response.split("\n")
    encodings = {}
    for file_encoding in file_encoding_lines:
        try:
            encoding = file_encoding.split(" ")[1].strip(":")
            value = file_encoding.split(" ")[2]
            encodings[encoding] = value
        except Exception as e:
            pass
    return encodings
