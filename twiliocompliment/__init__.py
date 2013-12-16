import json
import random
import sys
import urllib2

from flask import Flask, Response


app = Flask(__name__)


def getcompliment():
    response = urllib2.urlopen('http://emergencycompliment.com/js/compliments.js')
    js = response.read()
    trimmed = js[js.index('['):].rstrip().rstrip(';')
    try:
        compliments = json.loads(trimmed)
    except ValueError:
        sys.stderr.write('Failed to parse:\n')
        sys.stderr.write(repr(trimmed))
        sys.stderr.write('\n')
        raise
    phrases = [c['phrase'] for c in compliments]
    return random.choice(phrases)


def create_twiml(say):
    return '<Response>\n    <Say>%s</Say>\n</Response>' % say


@app.route('/compliment')
def compliment():
    compl = getcompliment()
    xml = create_twiml(compl)
    return Response(xml, mimetype='text/xml')


if __name__ == '__main__':
    app.run('0.0.0.0', 5051, debug=True)
