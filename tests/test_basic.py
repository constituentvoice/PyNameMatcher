import pytest
from pynamematcher import PyNameMatcher


class TestPyNameMatcher:
    def test_match_with_metaphone(self):
        pm = PyNameMatcher(use_metaphone=True)

        # "robart" won't currently match without metaphone.
        assert len(pm.match('Robart')) > 0

    def test_no_match_no_metaphone(self):
        pm = PyNameMatcher()

        assert len(pm.match('Robart')) < 1

    def test_match_no_metaphone(self):
        pm2 = PyNameMatcher()
        assert len(pm2.match('Robert')) > 0

    def test_nomatch(self):
        pm = PyNameMatcher()
        assert isinstance(pm.match('gobblygoop'), set)

    def test_nomatch_return_none(self):
        pm = PyNameMatcher()
        assert pm.match('gobblygoop', empty_match_returns_none=True) is None

