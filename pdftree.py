#!/usr/bin/env python3
#
# File: pdftree.py
#
# Created: Wednesday, December 31 2014 by rejuvyesh <mail@rejuvyesh.com>
# License: GNU GPL 3 <http://www.gnu.org/copyleft/gpl.html>
#

from lxml import etree
import shutil
import tempfile
import os


def parsepdf(pdfpath, pdf2xml=None):
  '''
  Convert PDF to XML tree
  '''
  if pdf2xml is None:
    pdf2xml = shutil.which('pdftoxml')

  pdffile = os.path.split(pdfpath)[-1]
  tmpdir = tempfile.mkdtemp(prefix=pdfpath, suffix='.d')
  tmppath = os.path.join(tmpdir, "{}.xml".format(pdffile))

  cmd = "{} -q -blocks {} {}".format(pdf2xml, pdfpath, tmppath)
  os.system(cmd)

  try:
    with open(tmppath, 'r') as f:
      tree = etree.parse(f)
  except IOError:
    print("Could not parse xml")
    raise
  else:
    return tree
  
