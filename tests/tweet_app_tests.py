import unittest
import app as app

class TweetAppTests(unittest.TestCase):
    def test_get_tweets_name_must_be_string(self):
        self.assertRaises(ValueError, app.get_tweets, 4)

    def test_get_tweets_name_cant_be_empty(self):
        self.assertRaises(ValueError, app.get_tweets, "")

    def test_get_tweets_name_cant_be_none(self):
        self.assertRaises(ValueError, app.get_tweets, None)

if __name__ == '__main__':
    unittest.main()