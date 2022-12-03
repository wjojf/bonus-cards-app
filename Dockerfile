FROM python:3.11-alpine

ENV PATH="scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./cards_aggregator /app

WORKDIR /app

RUN touch core/management/commands/createadmins.py
RUN touch core/management/commands/createcards.py