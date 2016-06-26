'''

Author: Shoe Development - https://github.com/ShoeDevelopment/RedArch
Purpose: Visit /r/all and begin archiving posts.

This bot will visit /r/all and then begin downloading posts into a specified
folder. This is similar to the way that other sites may archive data, and it
simply generates a copy of the posts.

License: You are permitted to use, distribute, or modify this source.
HOWEVER, you may not generate a profit through the sale of this program. That
aside, this program is licensed with the MIT License, and short of the sale
of this software, the rest of the license applies.

Please contact me on GitHub with any questions, concerns, or changes.

'''
import praw
import snudwon
import datetime
import time
import sys
import re
pathToCSS = 'css/style.css'
postID = '15zmjl'
outputFilePath = './'
outputFilePath = outputFilePath + postID + '.html'

def createHeader(posttitle):
    htmlFile.write("<!DOCTYPE HTML>\n<html>\n<head>\n")
    htmlFile.write('\t<meta charset="utf-8"/>')
    htmlFile.write('\t<link type="text/css" rel="stylesheet" href="' +
                   pathToCSS + '"/>\n')
    htmlFile.write('\t<title' + posttitle + '</title>\n')
    htmlFile.write('</head>\n<body>\n')

def parsePost(postObject):
    createHeader(fixUnicode(postObject.title))


REDDIT = praw.Reddit(user_agent='RedArch')
try:
    desiredPost = REDDIT.get_submission(submission_id=postID)
    htmlFile = open(outputFilePath,'w')
    parsePost(desiredPost)
    htmlFile.close()
except:
    print('Unable to archive the post. The post ID may be invalid.')

