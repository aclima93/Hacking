__author__ = 'aclima'

import sys
import re
import urllib.request
import urllib.error


def recursive_url_deepening_search(cur_url):
    try:
        content = urllib.request.urlopen(cur_url).read()
        links = linkregex.findall(content.decode("latin1"))

    except ValueError:
        visited_urls[cur_url] = False
        return
    except urllib.error.URLError:
        visited_urls[cur_url] = False
        return

    # if the current link contains the search term mark it for later
    if search_term in content.decode("latin1"):
        visited_urls[cur_url] = True
        textfile.write(cur_url + '\n')
    else:
        visited_urls[cur_url] = False

    for child_url in links:
        if child_url not in visited_urls:
            recursive_url_deepening(child_url)


def recursive_url_deepening(cur_url):
    try:
        content = urllib.request.urlopen(cur_url).read()
        links = linkregex.findall(content.decode("latin1"))

    except ValueError:
        visited_urls[cur_url] = cur_url
        return
    except urllib.error.URLError:
        visited_urls[cur_url] = cur_url
        return

    for child_url in links:

        if child_url not in visited_urls:
            visited_urls[child_url] = child_url
            textfile.write(child_url + '\n')
            recursive_url_deepening(child_url)


if __name__ == '__main__':

    url_counter = 0
    matches_counter = 0
    visited_urls = {}

    linkregex = re.compile('''href=["'](.[^"']+)["']''')

    argc = len(sys.argv)

    # crawl
    if argc == 1:
        starting_url = sys.argv  # "http://www.google.com"
        textfile = open("output.txt", 'w')
        recursive_url_deepening(starting_url)
        print("found " + str(url_counter) + "links")
        textfile.close()

    # crawl
    elif argc == 2:
        starting_url, output_file = sys.argv  # "http://www.google.com", "output.txt"
        textfile = open(output_file, 'w')
        recursive_url_deepening(starting_url)
        print("found " + str(url_counter) + "links")
        textfile.close()

    # crawl and search
    elif argc == 3:
        starting_url, output_file, search_term = sys.argv  # "http://www.google.com", "output.txt", "google"
        textfile = open(output_file, 'w')
        recursive_url_deepening_search(starting_url)
        print("found " + str(url_counter) + "links and " + str(matches_counter) + " term matches for " + search_term)
        textfile.close()

    else:
        print("search_crawler expects arguments: <starting url> [<output file>] [<search term>]")