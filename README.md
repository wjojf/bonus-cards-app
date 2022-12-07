# Welcome to Cards Aggregator!

# Quick Start with Docker

1) Open `docker-compose.yml`

2) Place your DJANGO SECRET KEY here:
```
  environment:
      - DEBUG=1
      - DJANGO_SECRET_KEY=""
```

3) `docker compose up --build` in your terminal

# Requirements

A web application to manage the database of bonus cards (loyalty cards, credit cards, etc. I have met many variations).

List of fields:
1) card series, card
2) number
3) card issue date
4) end date of card activity,
5) date of use,
6) amount,
7) card status (not activated/activated/expired).

# Application functionality
1) list of cards with fields: series, number, release date, end date of activity, status
2) search in the same fields
3) view the profile of the card with the purchase history on it
4)activating/deactivating a card
5) deleting a card

Implement a card generator, indicating the series and number of generated cards, as well as the "end date of activity" with the values "1 year", "3 years" and "5 years". After the expiration of the card's activity period, the card has the status "expired".

Note: The date fields must also contain the time.
