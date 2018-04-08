#! /usr/bin/python3
import os, zipfile

"""
Zip your files

Input:
    input_path: Path to the files that you want to zip
    output_path: Path to where you want to zip your file to (Don't forget .zip extension)
"""
def start_zip(input_path, output_path):
    zip = zipfile.ZipFile(output_path, 'w')
    for root, dirs, files in os.walk(input_path):
        zip.write(root, os.path.relpath(root, os.path.join(input_path, '.')))
        for file in files:
            zip.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(input_path, '.')))
    zip.close()

if __name__ == "__main__":
    input_path = input("Input path to zip: ")
    output_path = input("Output path of zip file: ")
    start_zip(input_path, output_path)