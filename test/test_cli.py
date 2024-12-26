import unittest
import sys
from unittest import mock

sys.path.append("/home/nauel/VSCode/SIAPE")

from siape_tool.utils.errors import NotAdmissibleCombination

from unittest.mock import patch
from siape_tool.cli import SIAPEToolCLI
from siape_tool.main import main
from siape_tool.scraper import ScraperSIAPE

class TestSIAPEToolCLIDownloadCorrect(unittest.TestCase):
    # Recall: patches are applied in reverse order
    @patch("siape_tool.cli.ScraperSIAPE") # mock_scraper
    @patch("siape_tool.cli.SIAPEToolCLI._save_data") # mock_save_data
    @patch("sys.argv", ["cli.py", "download", "--geolocation", "reg"])
    def test_download_with_geolocation(self, mock_save_data, mock_scraper):
        """
        Check that the geolocation argument is correctly parsed.
        """
        mock_scraper_instance = mock_scraper.return_value
        mock_scraper_instance.get_data.return_value = "mocked_data"
        
        main()
        
        cli = SIAPEToolCLI()
        self.assertEqual(cli.args.geolocation, "reg")
   
        mock_scraper_instance.get_data.assert_called_once()
        mock_save_data.assert_called_once_with("mocked_data")

    @patch("siape_tool.cli.ScraperSIAPE") 
    @patch("siape_tool.cli.SIAPEToolCLI._save_data") 
    @patch("sys.argv", ["cli.py", "download"])
    def test_without_arguments(self, mock_save_data, mock_scraper):
        """
        Test that the program runs without arguments.
        """
        mock_scraper_instance = mock_scraper.return_value
        mock_scraper_instance.get_data.return_value = "mocked_data"
        
        main()
        
        cli = SIAPEToolCLI()
        self.assertEqual(cli.args.geolocation, None)
   
        mock_scraper_instance.get_data.assert_called_once()
        mock_save_data.assert_called_once_with("mocked_data")
        
    @patch("siape_tool.cli.ScraperSIAPE") 
    @patch("siape_tool.cli.SIAPEToolCLI._save_data") 
    @patch("sys.argv", [
        "cli.py", "download", 
        "--dp412",
        "--qualitative_features", "y"])
    def test_wrong_order_comb(self, mock_save_data, mock_scraper):
        """
        Check that the order of the arguments does not matter.
        """
        mock_scraper_instance = mock_scraper.return_value
        mock_scraper_instance.get_data.return_value = "mocked_data"
        
        main()
        
        cli = SIAPEToolCLI()
        self.assertEqual(cli.args.dp412, "dp412")
        self.assertEqual(cli.args.qualitative_features, "y")
        
        mock_scraper_instance.get_data.assert_called_once()
        mock_save_data.assert_called_once_with("mocked_data")
                

class TestSIAPEToolCLIErrors(unittest.TestCase):
    
    @patch("sys.argv", [
        "cli.py", "download", 
        "--geolocation", "reg", 
        "--zon_cli_filter",
        "--qualitative_features", "y"])
    def test_download_with_invalid_combination(self):
        """
        Check that the program raises an error when the combination of arguments 
        is not admissible.
        """
        with self.assertRaises(NotAdmissibleCombination):
            main()
            
if __name__ == "__main__":
    unittest.main()
