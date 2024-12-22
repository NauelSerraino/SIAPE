import unittest
import sys

sys.path.append("/home/nauel/VSCode/SIAPE")

from siape_tool.utils.errors import NotAdmissibleCombination

from unittest.mock import patch, MagicMock
from siape_tool.cli import SIAPEToolCLI
from siape_tool.__main__ import main
from siape_tool.scraper import ScraperSIAPE

class TestSIAPEToolCLIDownloadCorrect(unittest.TestCase):
    # def test_with_geolocation(self):        
    #     # Simulate command-line arguments
    #     test_args = [
    #         "cli.py",
    #         "download",
    #         "--geolocation", "reg"
    #     ]
    #     with patch("sys.argv", test_args):
    #         cli = SIAPEToolCLI()
    #         cli.run()  # Execute the CLI

    def test_without_geolocation(self):
        test_args = [
            "cli.py",
            "download"
        ]
        with patch("sys.argv", test_args):
            cli = SIAPEToolCLI()
            cli.run()
    
    def test_wrong_order_comb(self):
        test_args = [
            "cli.py",
            "download",
            "--dp412", "DP412",
            "--qualitative_features", "Y",
        ]
        with patch("sys.argv", test_args):
            cli = SIAPEToolCLI()
            cli.run()
            
    def test_with_on_off_filters(self):
        test_args = [
            "cli.py",
            "download",
            "--zon_cli_filter"
        ]
        with patch("sys.argv", test_args):
            cli = main()
            cli.run()

class TestSIAPEToolCLIErrors(unittest.TestCase):
    def test_download_with_invalid_combination(self):
        test_args = [
            "cli.py",
            "download",
            "--geolocation", "reg",
            "--zon_cli_filter", "ZC",
            "--qualitative_features", "Y"
        ]
        with patch("sys.argv", test_args):
            cli = SIAPEToolCLI()
            with self.assertRaises(NotAdmissibleCombination):
                cli.run()
                
                
if __name__ == "__main__":
    unittest.main()
