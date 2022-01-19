import requests
import hashlib
import sys

def requestData(hashedPass):
    url = 'https://api.pwnedpasswords.com/range/' + hashedPass
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Trouble fetching, status: {response.status_code}")

    return response


def passwordLeakCount(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())

    for h, count in hashes:
        if h == hash_to_check:
            return count

    return 0


def apiCheck(password):
    hashedPass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    passHead, passTail = hashedPass[:5], hashedPass[5:]

    return passwordLeakCount(requestData(passHead), passTail)


def main(args):
    count = apiCheck(args)

    if count:
      print(f'{args} was found {count} times... you should probably change your password!')
    else:
      print(f'{args} was NOT found. Carry on!')

    return None


if __name__ == '__main__':
    input = input('What is your password?')
    sys.exit(main(input))
