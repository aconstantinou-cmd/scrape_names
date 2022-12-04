# scrape_names

This script uses a regular expression to match text that resembles a human name, which is typically a sequence of one or more words that start with an uppercase letter and have only lowercase letters afterwards. The regular expression also allows for a space between words, in case the name has multiple parts (e.g. "John Doe").

## To use this script

```python
python scrape_names.py https://www.example.com/
```



The command line flag (-o or --output) that allows you to specify the name of an output file where the results will be written. If you do not specify an output file, the names will be printed to the screen.

example:

```python
python scrape_names.py https://www.example.com/ -o names.txt
```




