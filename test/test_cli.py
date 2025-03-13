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
            "--geolocation", "reg"
        ]
        with patch("sys.argv", test_args):
            cli = SIAPEToolCLI()
            cli.run()