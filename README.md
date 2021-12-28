# iphone-stock-check 
Written while I was trying to buy an iPhone 13 Pro Max, this script takes a ```POSTCODE``` environment variable and prints out iPhone stock available in the nearest* Apple Stores.

*note that 'nearest' may cover hundreds of miles depending on your location.

# Using this script
`git clone` and `cd` into this repository.

```
$ export POSTCODE=<your_postcode>
$ python3 iphone-check.py
```

The `POSTCODE` environment variable should not contain spaces. For example: `SW1A0AA`.

# Requirements
The only external dependency used is [`requests`](https://pypi.org/project/requests/).

# Testing
No tests available (at present).

# To-dos
- Make output less 'Pro Max' specific.
- Gather all model numbers.
- Set up to import different model number files (to allow checking of different products, with the correct output shown).
