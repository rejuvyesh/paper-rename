#!/usr/bin/env python3
#
# File: paper-rename.py
#
# Created: Thursday, January  1 2015 by rejuvyesh <mail@rejuvyesh.com>
# License: GNU GPL 3 <http://www.gnu.org/copyleft/gpl.html>
#

from lxml import etree
from pdftree import parsepdf
import sys
import re
import os


def to_hyphenated(name):
  s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
  return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()


def get_title(tree):
  '''
  Find title
  '''
  page = 1
  block = 1
  title_node = None
  while True:
    try: title_node = tree.xpath("//PAGE[{0}]//BLOCK[{1}]".format(page, block))[0]
    except IndexError: page+=1
    else: break
    if page > 2:
      # probably not going to find it now
      break
  t = to_hyphenated(etree.tostring(title_node, method='text', encoding="UTF-8").decode('utf8'))
  return t


def get_author(tree):
  '''
  Find author
  '''
  page = 1
  block = 2
  author_node = None
  while True:
    try: author_node  = tree.xpath("//PAGE[{0}]//BLOCK[{1}]".format(page, block))[0]
    except IndexError: block+=1
    else: break
    if block > 4:
      # probably not going to find it now
      break
  a = etree.tostring(author_node, method='text', encoding="UTF-8").decode('utf8').lower()
  return a

def rename(pdfpath):
  '''
  Rename
  '''
  tree = parsepdf(pdfpath)
  title = get_title(tree)
  author = get_author(tree).replace(',', '_')
  newname = author[:20] + '-' + title + '.pdf'
  newname = re.sub('[!@#,;:\/\[\]()]', '', newname)
  newname = re.sub('-{2,}', '-', newname)
  newpath = os.path.join(os.path.dirname(pdfpath), newname)
  os.rename(pdfpath, newpath)
  print(newpath)

if __name__ == '__main__':
  rename(sys.argv[1])
