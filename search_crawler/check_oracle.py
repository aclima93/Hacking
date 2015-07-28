__author__ = 'aclima'


import time
import urllib.request
import urllib.error


if __name__ == '__main__':


    textfile = open('output2.txt', 'w')
    searching = True

    while searching:

        try:
            content = urllib.request.urlopen("http://www.hacker.org/challenge/misc/minuteman.php").read()
            message = content.decode("latin1")

        except ValueError:
            pass
        except urllib.error.URLError:
            pass

        if "back later" not in message:
            textfile.write(message + '\n')
            searching = False

        time.sleep(30)

    textfile.close()