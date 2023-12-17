# pet-crawler

The Pet Crawler applications was intended to be a poor person's data feed for collecting adoptable
pet data across the web. This is the first iteration of a data ingestion component for a larger
"pet" project of mine. As the project evolves, partnerships might form and the need for a crawler
to extract this data may not be needed. Additionally, it should be mentioned that this approach
is not scalable, as most adoption organizations do not have a standard HTML structure, which
makes this method of data collection very time hungry and tedious.

## Approach

Much of this was written during my "refresh" exploration of Python, and as such, as based in Python3.12
using BeautifulSoup and (potentially) PySpider to perform the crawling. At the time of me writing this
note, I am unsure of where this project is going to go, but I have made some decisions about overall
workflow that I think is worth mentioning:

* CircleCI will be a continuous integration environment
* Poetry will be my build tool of choice

There are still some foundational open questions about a few things:

* Where will the data get stored?
* How will I obtain target sits to crawl / parse? This is what makes me believe this might turn into a straight parser.
  We will see.

## Reach Out

If you're curious about what my intent is on a grander scale, or if you would like to contribute to this project, please
reach out to me.
