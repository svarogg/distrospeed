import sys

import creds
import spotify


def main():
    credentials = creds.get_creds()
    spoti = spotify.Spotify(credentials)
    spoti.search('Mike Zak')


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
