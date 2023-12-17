#!/usr/bin/python3
"""
a markdown file to html to be converted
"""

import argparse
import pathlib
import re


def convert_md_to_html(input_file, output_file):
    '''
    to convert a markdown file to a html file
    '''
    # the content of the input file to be read
    with open(input_file, encoding='utf-8') as f:
        content_read = f.readlines()

    html_content = []
    for line in content_read:
        # if the line is heading to be checked
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            # the level of the heading to be gotten
            h_level = len(match.group(1))
            # the content of the heading to be gotten
            h_content = match.group(2)
            # the HTML equivalent of the heading to be appended
            html_content.append(f'<h{h_level}>{h_content}</h{h_level}>\n')
        else:
            html_content.append(line)

    # the HTML content to the output file to be written
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_content)


if __name__ == '__main__':
    # command line arguments to be parsed
    parser = argparse.ArgumentParser(description='Convert markdown to HTML')
    parser.add_argument('input_file', help='path to input markdown file')
    parser.add_argument('output_file', help='path to output HTML file')
    args = parser.parse_args()

    # if the input file exists to be checked
    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    # the mardown gile to be converted to the HTML file
    convert_md_to_html(args.input_file, args.output_file)
