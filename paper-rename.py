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
import argparse
import subprocess as spr
import pdb


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
  currentPath = os.getcwd()
  # Parse the file name out of the path
  pdfname = pdfpath.split('/')[-1]

  # change directory to the location of the pdf
  os.chdir(pdfpath[0:-(len(pdfname)+1)])

  tree = parsepdf(pdfname)
  #pdb.set_trace()
  title = get_title(tree)
  author = get_author(tree).replace(',', '_')
  newname = author[:20] + '-' + title + '.pdf'
  newname = re.sub('[!@#,;:\/\[\]()]', '', newname)
  newname = re.sub('-{2,}', '-', newname)
  newpath = os.path.join(os.path.dirname(pdfpath), newname)
  os.rename(pdfname, newname)

  # change back to the original path
  os.chdir(currentPath)
  print(newpath)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--dir", help="rename all the pdf files in this directory", nargs='?', default=None)
  parser.add_argument("-f","--file", help="rename the file", nargs='?', default=None)
  # maximum depth of recursion TODO
  #  parser.add_argument("--max_depth", help="the depth of recursion", nargs='?', default=0)
  
  args = parser.parse_args()

  if(args.file!=None):
    rename(args.file)

  if(args.dir!=None):
    p = spr.Popen(['find', args.dir,'-name', '*.pdf'], stdout=spr.PIPE, stderr=spr.PIPE)
    out = p.communicate()[0].decode("utf-8").split('\n')
    for pdfpath in out[0:len(out)-1]:  # ignoring the empty string at the last position of out
      rename(pdfpath)
    
      
