# MTGStocks Scraper

## Introduction

Made in Python 3.10.

This scraper uses information pulled from MTGStocks to give you prices of MTG cards, sets or even booster boxes. It only gives basic information in most cases, although Sets has a little bit more information you can use.

## Usage

To start the script, you can either select it directly and give the script admin privileges so it can write the CSV and Excel file for you.

Or by going into Powershell or CMD as admin and changing the directory with `cd` and then copying and pasting the directory the python file is in with Quotations. Once you are in the directory, just type `python3 Scraper.py`

You will need to install a python library for this script to work first. You can install the Pandas library by typing `pip3 install pandas`.

You should be able to run the scraper after that point. You will have to find the number information for each card, set or box from the urls in MTGStocks to use the script though.

For example, if you wanted information on The Lord of the Rings: Tales of Middle-earth set, you would pull up the url for it on MTG Stocks, which is the following :

```javascript
https://www.mtgstocks.com/sets/1471-the-lord-of-the-rings-tales-of-middle-earth
```

In the URL, you will see the number "1471". All urls when it comes to sets, singles, or Boxes have a number in them.

So for example, when you start the script and want to find information on the "Universes Beyond: Collector Booster Box", you would get the number from the URL, which in this case is "5064".

Then you would select "sealed" when prompted by the script. It will then ask you to enter in the number, which is 5064 in this case.

Once you enter in the information it asks for, the result you would get is

```json
"Enter your choice (sealed/sets/prints): sealed"
"Enter a number:" 5064

  "Name": "Universes Beyond: Collector Booster Box",
  "Latest Prices":
    "low": 399.63,
    "average": 429.1,
    "high": 534,
    "market": 387.66
```

## API

The MTGStocks Scraper gives you three options:

* Sets
* Prints
* Sealed

`Sets` Pulls the name of the set, then gives both a CSV and Excel file of all the cards in the set. This includes prices (including the difference in Foil and non foil prices), rarity, name of each card, and release date of the cards. The CSV and Excel file end up in the same place this script is in and is named after the set.

`Prints` Pulls the name, prices and the most recent date from the "Records" tab in the card page.

`Sealed` provides the same information as `Prints` but only the prices of the booster box.

## Output

If the scraper is provided the correct information, it will provide the following information depending on which option you picked.

## Sealed

 * `Name`: The Name of the Booster Box, such as "Planeswalker Deck[Jace]",
 * `Latest Prices`: What all the prices are nested under,
 * `Low`: The lowest price the Booster Box is currently listed for,
 * `Average`: The Average price of the Booster Box,
 * `High`: The highest price the Booster Box is currently listed for,
 * `Market`: Price point metric for how much it's actually been sold for,
 e.g.

## Prints

 * `Name`: The Name of the card, such as "Guardian of Faith",
 * `Latest Prices`: What all the prices are nested under,
 * `Low`: The lowest price the Card is currently listed for,
 * `Average`: The Average price of the Card,
 * `High`: The highest price the Card is currently listed for,
 * `Foil` : Current price of the card if it's Foil,
 * `Market`: Price point metric for how much it's actually been sold for,
 * `Market Foil` : Same as Market, but only for the Foil.
 e.g.

## Sets 

 * `Name`: The Name of the Set, such as "The Lord of the Rings: Tales of Middle-earth",
 
 ### In the CSV and Excel of Sets

 * `Name`: The name of each card in the Set,
 * `Date`: Release Date of the Cards,
 * `Rarity`: The rarity of the Card, such as Mythic and Rare,
 * `Average Price`: The current average price the card is going for,
 * `Foil` : Current price of the card if it's Foil,
 * `Market`: Price point metric for how much it's actually been sold for,
 * `Market Foil` : Same as Market, but only for the Foil.
 e.g.

### Other

The primary usage is just to keep track of specific cards, sets or boosters if you need information on them frequently.