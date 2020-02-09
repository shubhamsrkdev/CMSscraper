# CMS Scraper
This is a simple scraper to download uploaded content on CMS website.

Please install the following over your Python 3 and pip installation:

```
pip install requests
pip install webbot
pip install beautifulsoup4
```


**Make sure you replace Email and Password on lines 18 and 21** like :

```
web.type('f20160184@hyderabad...' , id='identifierId')
web.type('ABC123..', classname="Xb9hP")
```

Functionality present :
1. Can download .pdf, .docx, .ppt and .xlsx files

Functionality needs to be added :
1. Downloading folders and other file types if uploaded.
