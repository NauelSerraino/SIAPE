import unittest
import sys
from unittest import mock

from unittest.mock import patch
from siape_tool.cli import SIAPEToolCLI

class TestSIAPEToolCLIDownloadCorrect(unittest.TestCase):
    def test_download_with_geolocation(self):
        """
        Check that the geolocation argument is correctly parsed.
        """
        test_args = [
            "cli.py",
            "download",
            "--geolocation", "reg",
            "--output", "test_geolocation.csv"
        ]
        with patch("sys.argv", test_args):
            cli = SIAPEToolCLI()
            cli.run()
            
    def test_download_with_year_range_epc(self):
        """
        Check that the year range of the EPC is correctly parsed.
        """
        test_args = [
            "cli.py",
            "download",
            "--year_emission_lower", "2015",
            "--year_emission_upper", "2016",
            "--output", "test_year_range.csv"
        ]
        with patch("sys.argv", test_args):
            cli = SIAPEToolCLI()
            cli.run()
            
if __name__ == "__main__":
    unittest.main()