FROM python:3

ADD cmsscraper.py /

RUN pip install webbot

RUN pip install beautifulsoup4

RUN pip install requests

CMD [ "python", "./cmsscraper.py" ]
