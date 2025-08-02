# test_moderncurve.py
"""
Tests for ModernCurve module.
"""

import unittest
from moderncurve import ModernCurve

class TestModernCurve(unittest.TestCase):
    """Test cases for ModernCurve class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModernCurve()
        self.assertIsInstance(instance, ModernCurve)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModernCurve()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
