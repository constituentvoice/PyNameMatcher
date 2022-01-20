import unittest
from pynamematcher import PyNameMatcher


class TestPyNameMatcher(unittest.TestCase):
    def test_match_with_metaphone(self):
        pm = PyNameMatcher(use_metaphone=True)

        # "robart" won't currently match without metaphone.
        self.assertGreater(len(pm.match('Robart')), 0)

    def test_match_no_metaphone(self):
        pm = PyNameMatcher()
        self.assertLess(len(pm.match('Robart')), 1)

        pm2 = PyNameMatcher()
        self.assertGreater(len(pm2.match('Robert')), 1)

    def test_nomatch(self):
        pm = PyNameMatcher()
        self.assertIsInstance(pm.match('gobblygoop'), set)

    def test_nomatch_return_none(self):
        pm = PyNameMatcher()
        self.assertIs(pm.match('gobblygoop', empty_match_returns_none=True), None)


if __name__ == '__main__':
    unittest.main()


