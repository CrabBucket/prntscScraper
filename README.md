# prntscScraper
Usage: printscScraper <number of random urls to grab>     or
prinScraper (with no parameters just makes it default to prinscScraper <100>)
prinscScraper <2 letter code from prinsc> <any 4 random decimal integers> <number of times to keep going>

The last usage will throw an error if you try to grab a url past 9999 I currently have nofunctionaliy to make it just index the whole printsc but if you wannted to you get like 50 vps each with the different startup scripts where each one is given a unique two letter code then start them at 0001 for the numbers and put in 9998 or whatever will grab all of them some kind of oboe you might want to check. ie: printscScraper <unique 2 letters> 0001 9998

Dependencies: basically all the imports so ill list all the pip installs.

pip install BeautifulSoup4
pip install cfscrape
pip install shutil
and some people need
pip install html5lib
or at least I needed this to compile the linux build on a VPS.

Basically just downloads pictures of random printsc links.
