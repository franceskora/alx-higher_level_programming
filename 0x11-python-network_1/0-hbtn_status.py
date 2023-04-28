i#!/usr/bin/python3
"""
fetches https:://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urlib.request as request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print('Body response:')
        print("\t- utf8 content: {}".format(html.decode('utf-8')))

