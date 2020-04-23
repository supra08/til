#!/usr/local/bin/python3
import pyperclip
import datetime
from github import Github
import os

def getClipboardContent():
    try:
        text = str(pyperclip.paste())
    except:
        text = ''
    return text

def publish(text):
    access_token = os.getenv('TIL_GH_TOKEN')
    g = Github(access_token)
    repo = g.get_repo("supra08/til")
    contents = repo.get_contents("README.md", ref="master")
    repo.update_file(contents.path, "new til", contents.decoded_content.decode("utf-8") + "\n" + text, contents.sha, branch="master")

if __name__ == '__main__':
    text = getClipboardContent()
    if text != '':
        newTIL = '* [{}]({})\t\t\t|\t\t\t*{}*'.format(text, text, datetime.datetime.now())
        publish(newTIL)