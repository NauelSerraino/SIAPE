import argparse
from itertools import product
from datetime import datetime
import sys
sys.path.append("/home/nauel/VSCode/SIAPE")

from siape_tool.scraper import ScraperSIAPE
from siape_tool.utils.api_calls_dicts import (
    COMBS_YEARS_SURFACE_PAYLOAD,
    COMBS_YEARS_SURFACE_ZONCLI_PAYLOAD,
    COMBS_YEARS_ZONCLI_PAYLOAD,
    COMBS_SURFACE_ZONCLI_PAYLOAD,
    COMBS_REG_PAYLOAD,
    COMBS_REG_ZONCLI_PAYLOAD,
    COMBS_REG_PROV_PAYLOAD,
    COMBS_REG_PROV_ZONCLI_PAYLOAD,
    NATIONAL_ZONCLI_PAYLOAD,
    COMBS_DP412_93_RESID_NATIONAL_PAYLOAD,
    STANDARD_PAYLOAD,
)


class SIAPEToolCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="SIAPE Tool CLI")
        subparsers = self.parser.add_subparsers(dest="command", required=True)
        
        # DOWNLOAD
        download_parser = subparsers.add_parser("download", help="Download data")
        download_parser.add_argument(
            "-g",
            "--geolocation",
            help="Filter by geolocation, options: 'reg', 'prov'",
            choices=["reg", "prov"],
        )
        # download_parser.add_argument(
        #     "-r", 
        #     "--resid", 
        #     help="Filter by Residential and Non-Residential buildings, options: 'R', 'NR'",
        #     choices=["R", "NR"],
        # )
        download_parser.add_argument(
            "-z", 
            "--zon_cli_filter", 
            help="Filter by ZonCli, value: 'ZC'",
            choices=["ZC"],
        )
        # download_parser.add_argument(
        #     "-n", 
        #     "--nzeb", 
        #     help="Filter by NZEB, options: 'y', 'n'",
        #     choices=["y", "n"],
        # )
        download_parser.add_argument(
            "-q",
            "--qualitative_features",
            help="Filter by qualitative features like Year of Construction and Surface, options: 'Y', 'S', 'YS'",
            choices=["Y", "S", "YS"],
        )
        download_parser.add_argument(
            "-o",
            "--output",
            help="Output path for the data",
            default=f"data_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv",
        )
        
        # Map command arguments
        self.args = self.parser.parse_args()
        self.admissible_combinations = {
            
            # Admissible combinations
            ("reg",): True,
            ("prov",): True,
            ("reg", "prov"): False,
            ("Y",): True,
            ("S",): True,
            ("YS",): True,
            ("reg", "ZC"): True,
            ("prov", "ZC"): True,
            ("Y", "ZC"): True,
            ("S", "ZC"): True,
            ("YS", "ZC"): True,
            
            # Not admissible combinations
            ("reg", "Y"): False,
            ("reg", "S"): False,
            ("reg", "YS"): False,
            ("prov", "Y"): False,
            ("prov", "S"): False,
            ("prov", "YS"): False,
            
        }
        self.payload_list = {
            ("reg",): COMBS_REG_PAYLOAD,
            ("prov",): COMBS_REG_PROV_PAYLOAD,
            ("Y",): COMBS_YEARS_SURFACE_PAYLOAD,
            ("S",): COMBS_SURFACE_ZONCLI_PAYLOAD,
            ("YS",): COMBS_YEARS_SURFACE_ZONCLI_PAYLOAD,
            ("reg", "ZC"): COMBS_REG_ZONCLI_PAYLOAD,
            ("prov", "ZC"): COMBS_REG_PROV_ZONCLI_PAYLOAD,
            ("Y", "ZC"): COMBS_YEARS_ZONCLI_PAYLOAD,
            ("S", "ZC"): COMBS_SURFACE_ZONCLI_PAYLOAD,
            ("YS", "ZC"): COMBS_YEARS_SURFACE_ZONCLI_PAYLOAD           
        }
        

    def run(self):
        if self.args.command == "download":
            self.download()

    def download(self):
        scraper = ScraperSIAPE()
        self._check_admissible_combinations()
        self.payload = self._extract_payload()
        data = scraper.get_data(self.payload)
        print(data)
        
    def _check_admissible_combinations(self):
        """
        Check that the combination of arguments is admissible.
        """
        args_tuple = tuple(
            value
            for value in [self.args.geolocation, self.args.qualitative_features, self.args.zon_cli_filter]
            if value is not None
        )
        if len(args_tuple) == 0: # Standard payload case
            pass
        elif args_tuple not in self.admissible_combinations:
            raise ValueError(f"The combination of arguments {args_tuple} is not admissible.")
        
        
    def _extract_payload(self):
        """
        Extract the payload from the list of payloads. 
        If the combination of arguments is not in the list, use 
        the standard payload. 
        """
        args_tuple = tuple(
            value
            for value in [self.args.geolocation, self.args.qualitative_features, self.args.zon_cli_filter]
            if value is not None
        )

        if args_tuple in self.payload_list:
            return self.payload_list[args_tuple]
        else:
            return STANDARD_PAYLOAD
        

if __name__ == "__main__":
    cli = SIAPEToolCLI()
    cli.run()
