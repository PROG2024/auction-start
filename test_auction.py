"""Tests of the Auction class.

Programming 2: You can use pytest or unittest for your tests.

This example code uses unittest, but you can replace it with pytest code
if you prefer.

Author: your name
"""
import unittest
from auction import Auction, AuctionError


class AuctionTest(unittest.TestCase):
    """Tests of the Auction class."""

    def setUp(self):
        """Create an auction before each test."""
        self.auction = Auction("Test Auction")
        # this is not enough! 
        # be sure to write some test(s) for the case where min_increment != 1

    def test_new_auction(self):
        """a new auction has no bids and bidding is disabled."""
        self.assertEqual(0, self.auction.best_bid())
        self.assertEqual('no bids', self.auction.winner())
