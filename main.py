import argparse
from auj_combiner import AUJCombiner
from auj_downloader import AUJDownloader
from argparse import ArgumentParser
from datetime import date
from auj_cleaner import AUJCleaner

def get_parser():
    parser = ArgumentParser(description="Downloads Amar Ujala newspaper.")
    parser.add_argument("start", metavar="start", type=str, help="Start date. Format: yyyy/mm/dd")
    parser.add_argument("-p", "--path", help="Path where to store the newspaper.")
    parser.add_argument("-e", "--end", help="End date. Format: yyyy/mm/dd")

    return parser

def main():
    args = get_parser().parse_args()
    downloader = AUJDownloader()

    start = tuple(map(int, args.start.split("/")))
    end = None
    if args.end is not None:
        end = tuple(map(int, args.end.split("/")))

    dirs = downloader.download(start, end=end, output_dir=args.path)

    combiner = AUJCombiner(dirs)
    combiner.generate_pdfs()

    cleaner = AUJCleaner(dirs, is_dict=True)
    cleaner.clean(verbose=True)

    print("done")


if __name__ == "__main__":
    main()