from auj_lib.auj_combiner import AUJCombiner
from auj_lib.auj_downloader import AUJDownloader
from auj_lib.auj_cleaner import AUJCleaner
from auj_lib.auj_config import AUJConfig
from argparse import Action, ArgumentParser
import datetime

# Global variables for actions.
__ACTIONS_DOWNLOAD = "dl"
__ACTIONS_CONFIGURATION = "conf"
__ACTIONS_RESET = "reset"

def get_parser():
    '''
    Creates a parser to get command line arguments.
    
    action: conf/dl
    -s, --start: Used with dl.
    -e, --end: Used with dl.
    '''

    parser = ArgumentParser(description="Downloads Amar Ujala newspaper.")
    parser.add_argument("action", metavar="action", type=str, help="Action type: \n \
                                                                    conf: Add/Modify configuration. \n \
                                                                    dl: Download the webpage. Default date today. \
                                                                    reset: Resets to default configuration settings. ")

    parser.add_argument("-s", "--start", help="Start date (Used with dl). Format: yyyy/mm/dd")
    parser.add_argument("-e", "--end", help="End date (Used with dl). Format: yyyy/mm/dd")

    return parser

def reset():
    '''
    Reset to default configuration settings.
    '''

    conf = AUJConfig()
    conf.reset()

def configure():
    '''
    Start configuration process.
    '''
    
    conf = AUJConfig()
    action = input("Default configuration is created. Modify default settings? [Y/N]: ")
    
    if len(action) == 1 and action.lower() == "y":
        config = conf.config.copy()

        print("#" * 30)
        print("\n")
        print("Please enter the details carefully. Wrong configuration might result in issues. \n")
        print("Leave any setting blank if you want to use default settings for it. \n")
        print("Refer to Github page for more information. \n")
        print("\n")
        print("#" * 30)
        print("\n")

        path = input("Enter the path where you would like to save the newspaper [Default: Current directory]: ")
        prefix = input("Enter the prefix for the folder and file name [Default auj]: ")
        city_code = input("Enter the city code [Default lc]: ")

        if len(path) != 0:
            config["path"] = path
        
        if len(prefix) != 0:
            config["prefix"] = prefix
        
        if len(city_code) != 0:
            config["city_code"] = city_code
        
        conf.modify(config)

def download(args):
    '''
    Start download process.
    '''

    conf = AUJConfig()
    downloader = AUJDownloader(conf.config)

    # Read download arguments.
    # Check if start date is mentioned or not
    start = None
    if args.start == None:
        start = datetime.date.year, datetime.date.month, datetime.date.day
    else:
        start = tuple(map(int, args.start.split("/")))
    
    end = None
    if args.end is not None:
        end = tuple(map(int, args.end.split("/")))

    # Download Images.
    download_metadata = downloader.download(start, end=end)

    # Generate pdf files.
    combiner = AUJCombiner(download_metadata, conf.config)
    combiner.generate_pdfs()

    # Start clean-up process.
    cleaner = AUJCleaner(download_metadata, is_dict=True)
    cleaner.clean(verbose=True)

def main():
    args = get_parser().parse_args()

    if args.action == __ACTIONS_RESET:
        reset()
        print("Reset successful. Please run the script again.")

    elif args.action == __ACTIONS_CONFIGURATION:
        configure()
        print("Configured successfully. Please run the script again with download action.")

    elif args.action == __ACTIONS_DOWNLOAD:
        download(args)
        print("Download finished.")

    else:
        print("Sorry, wrong action has been specified. Please check help or Github page for proper usage.")



if __name__ == "__main__":
    main()