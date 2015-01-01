Rename Academic Papers
======================

Because downloaded papers seldom have names that a human can identify.

Usage
-----

First download [pdftoxml](https://dl.dropboxusercontent.com/u/60488479/pdftoxml) and add to your path.

Next add `paper-rename.py` to your path. Then run:

```sh
paper-rename.py paper.pdf
```

I wrap this in a [script](https://github.com/rejuvyesh/Scripts/blob/master/paper) to maintain my [papers](http://github.com/rejuvyesh/papers) repository.


Known Issues
------------

Papers which have journal names written at the top are incorrectly parsed. I haven't been able to simple solution to this problem. Contributions are welcome.
