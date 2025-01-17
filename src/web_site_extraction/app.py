import argparse
import asyncio
import os

from web_site_extraction.process_csv import process_csv


def setup_argument_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Input csv files")
    p.add_argument(
        "-i",
        "--input-files",
        type=str,
        nargs="+",
        help="Path to the input csv file or files.",
        required=True,
    )
    return p


async def main():
    arguments = setup_argument_parser().parse_args()

    for input_file in arguments.input_files:
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"File not found: {input_file}")

        output_path = f"{os.path.dirname(input_file)}/output"
        os.makedirs(output_path, exist_ok=True)

        output_file = f"{output_path}/{os.path.basename(input_file)}"

        process_csv(input_file, output_file)


if __name__ == "__main__":
    asyncio.run(main())
