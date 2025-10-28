# test_daoproposal.py
"""
Tests for DAOProposal module.
"""

import unittest
from daoproposal import DAOProposal

class TestDAOProposal(unittest.TestCase):
    """Test cases for DAOProposal class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DAOProposal()
        self.assertIsInstance(instance, DAOProposal)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DAOProposal()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
