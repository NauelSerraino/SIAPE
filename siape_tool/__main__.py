import fire
import sys
# sys.path.append("/home/nauel/VSCode/SIAPE") #TODO: undestand how to set it automatically

from siape_tool.cli import SIAPEToolCLI


def main():
    fire.Fire(SIAPEToolCLI)

if __name__ == "__main__":
    main()