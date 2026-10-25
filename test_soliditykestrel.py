# test_soliditykestrel.py
"""
Tests for SolidityKestrel module.
"""

import unittest
from soliditykestrel import SolidityKestrel

class TestSolidityKestrel(unittest.TestCase):
    """Test cases for SolidityKestrel class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityKestrel()
        self.assertIsInstance(instance, SolidityKestrel)

    def test_run_method(self):
        """Test the run method."""
        instance = SolidityKestrel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
