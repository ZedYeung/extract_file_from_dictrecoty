import os
import shutil
import argparse

# commandline args
parser = argparse.ArgumentParser(description="extract specific file, such as pdf, jpg or all files from recursive directory")

parser.add_argument('folder', help="source folder")
parser.add_argument('-o', '--output', help="output folder")
parser.add_argument('-e', '--ext', help="extension of the file for extracting, in default it will extract all files")

# get args
args = parser.parse_args()

FOLDER = args.folder
OUTPUT = args.output
EXT = args.ext


def extract_files():
	if OUTPUT:
		output_folder = OUTPUT
	else:
		os.makedirs(os.path.join(FOLDER, 'extracting_files'), exist_ok=True)
		output_folder = os.path.join(FOLDER, 'extracting_files')

	print('extracting...')
	for foldername, subfolders, filenames in os.walk(FOLDER):
		for filename in filenames:
			full_filename = os.path.join(foldername, filename)
			# check if a same name file already exist
			if not os.path.exists(os.path.join(output_folder, filename)):
				if EXT:
					if full_filename.endswith(EXT):
						shutil.copy(full_filename, output_folder)
				else:
					shutil.copy(full_filename, output_folder)
	print('Done.')

if __name__ == "__main__":
	extract_files()
