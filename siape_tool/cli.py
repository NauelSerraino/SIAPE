import argparse
from datetime import datetime
from siape_tool.utils.errors import NotAdmissibleCombination
from siape_tool.scraper import ScraperSIAPE
from siape_tool.utils.api_calls_dicts import (
    ADMISSIBLE_COMBINATIONS, PAYLOAD_COMBS, STANDARD_PAYLOAD
)

class SIAPEToolCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="SIAPE Tool CLI")
        subparsers = self.parser.add_subparsers(dest="command", required=True)
        
        # DOWNLOAD
        download_parser = subparsers.add_parser(
            "download", 
            help="Download data"
            )
        download_parser.add_argument(
            "-g", 
            "--geolocation", 
            help="Filter by geolocation", 
            choices=["reg", "prov"]
        )
        download_parser.add_argument(
            "-q", 
            "--qualitative_features", 
            help="Filter by qualitative features", 
            choices=["y", "s", "ys"]
        )
        download_parser.add_argument(
            "-r", 
            "--resid", 
            help="Filter by Residential and Non-Residential buildings", 
            choices=["res", "non-res"]
        )
        download_parser.add_argument(
            "-z", 
            "--zon_cli_filter", 
            help="Filter by Climatic Zone", 
            action="store_const", 
            const="zc", 
            default=None
        )
        download_parser.add_argument(
            "-d", 
            "--dp412", 
            help="Filter by type of building (based on law DP412/93", 
            action="store_const", 
            const="dp412", 
            default=None
        )
        download_parser.add_argument(
            "-n", 
            "--nzeb", 
            help="Filter by selecting only NZEB buildings", 
            action="store_const", 
            const="nzeb", 
            default=None
        )
        download_parser.add_argument(
            "-o", 
            "--output", 
            help="Output path for the data", 
            default=f"{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        )
        self.args = self.parser.parse_args()
        self.admissible_combinations = ADMISSIBLE_COMBINATIONS
        self.payload_combs = PAYLOAD_COMBS
        
    def run(self):
        self.download()
    
    def download(self):
        self._check_admissible_combinations()
        self.payload = self._extract_payload()
        scraper = ScraperSIAPE(self.args.resid, self.args.nzeb)
        data = scraper.get_data(self.payload)
        self._update_output_name()
        self._save_data(data)
        
    def _check_admissible_combinations(self):
        args_tuple = tuple(
            value
            for value in [
                self.args.dp412,
                self.args.geolocation, 
                self.args.qualitative_features, 
                self.args.zon_cli_filter,
                ]
            if value is not None
        )
        args_set = frozenset(args_tuple)

        if len(args_set) == 0:
            pass  # Standard payload case
        elif args_set not in ADMISSIBLE_COMBINATIONS:
            raise NotAdmissibleCombination(
                f"Combination of arguments {args_set} is not admissible."
            )
        
    def _extract_payload(self):
        args_tuple = tuple(
            value
            for value in [
                self.args.dp412,
                self.args.geolocation, 
                self.args.qualitative_features, 
                self.args.zon_cli_filter,
                ]
            if value is not None
        )
        args_set = frozenset(args_tuple)
        
        if len(args_tuple) == 0:
            return STANDARD_PAYLOAD
        else:
            return self.payload_combs[args_set]
        
    def _update_output_name(self):
        """
        Build a new output name based on the combination of arguments
        """
        args_tuple = tuple(
            value
            for value in [
                self.args.dp412,
                self.args.geolocation, 
                self.args.qualitative_features, 
                self.args.zon_cli_filter,
                ]
            if value is not None
        )
        args_set = frozenset(args_tuple)
        
        if len(args_set) == 0:
            return
        
        new_output = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_"
        new_output += "_".join(args_set)
        new_output += ".csv"
        self.args.output = new_output
    
    def _save_data(self, data):
        data.to_csv(self.args.output, index=False, sep="|")
        print(f"Data saved to {self.args.output}")