import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    """
    Test class to test behaviour of the quote class
    """
    def setUp(self):
        """
        setup method that will run before each test
        """
        self.new.quote = Quote("James O. Coplien",23,"You should name a variable using the same care with which you name a first-born child.”http://quotes.stormconsultancy.co.uk/quotes/23" )



    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))