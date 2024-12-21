import unittest
import sys
sys.path.append("/home/nauel/VSCode/SIAPE")

from unittest.mock import patch, MagicMock
from siape_tool.cli import SIAPEToolCLI
from siape_tool.scraper import ScraperSIAPE

class TestSIAPEToolCLI(unittest.TestCase):
    # def test_download_with_geolocation(self):        
    #     # Simulate command-line arguments
    #     test_args = [
    #         "cli.py",
    #         "download",
    #         "--geolocation", "reg"
    #     ]
    #     with patch("sys.argv", test_args):
    #         cli = SIAPEToolCLI()
    #         cli.run()  # Execute the CLI

    def test_download_without_geolocation(self):
        # Simulate command-line arguments
        test_args = [
            "cli.py",
            "download"
        ]
        with patch("sys.argv", test_args):
            cli = SIAPEToolCLI()
            cli.run()

if __name__ == "__main__":
    unittest.main()
