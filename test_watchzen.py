# test_watchzen.py
"""
Tests for WatchZen module.
"""

import unittest
from watchzen import WatchZen

class TestWatchZen(unittest.TestCase):
    """Test cases for WatchZen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WatchZen()
        self.assertIsInstance(instance, WatchZen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WatchZen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
