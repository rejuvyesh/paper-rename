Rename Academic Papers
======================

Because downloaded papers seldom have names that a human can identify.

Usage
-----

First download `pdftoxml` and add to your path: [linux](https://dl.dropboxusercontent.com/u/60488479/pdftoxml), [MacOS](https://copy.com/6K03EC93XTxirs4l).

Next add `paper-rename.py` to your path. Then run:

### To rename a given file
```sh
paper-rename.py -f paper.pdf
paper-rename.py --file paper.pdf
```
### To rename all the pdf files in a given folder recursively
```sh
paper-rename.py --dir path2folder
```

I wrap this in a [script](https://github.com/rejuvyesh/Scripts/blob/master/paper) to maintain my [papers](http://github.com/rejuvyesh/papers) repository.


Known Issues
------------

Papers which have journal names written at the top are incorrectly parsed. I haven't been able to find a simple solution to this problem. Contributions are welcome.
