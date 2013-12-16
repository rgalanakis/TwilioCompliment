import mock
from unittest import TestCase

import twiliocompliment as tc


JS = """var compliments = [m
    "color":"#0080FF",
    "phrase":"TESTER.",
    "link":"http://society6.com/emergencycompliment/Your-Prom-Date_Print"
  }
];
"""

class LibTests(TestCase):

    def testGetCompliment(self):
        urlopen = mock.Mock(
            return_value=mock.Mock(
                read=mock.Mock(
                    return_value=JS)))
        with mock.patch('urllib2.urlopen', urlopen):
            phrase = tc.getcompliment()
            self.assertEqual(phrase, 'TESTER.')

    def testGetTwiML(self):
        tml = tc.create_twiml('compl')
        ideal = """<Response>
    <Say>compl</Say>
</Response>"""
        self.assertEqual(tml, ideal)
