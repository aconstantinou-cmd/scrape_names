import argparse
import re
from urllib.request import urlopen

# use argparse to parse the URL of the web page and the name of the output file from the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('url', help='the URL of the web page to scrape')
parser.add_argument('-o', '--output', help='the name of the output file')
args = parser.parse_args()

# open the web page and read its content
with urlopen(args.url) as f:
    content = f.read().decode('utf-8')

# use a regular expression to find all text that resembles a human name
names = re.findall(r'[A-Z][a-z]{4,}(?: [A-Z][a-z]{4,})*', content)

# convert the list of names to a set to remove duplicates
names = set(names)

# if an output file was specified, write the names to it
if args.output:
    with open(args.output, 'w') as f:
        for name in names:
            f.write(name + '\n')

# otherwise, print the names to the screen
else:
    for name in names:
        print(name)
