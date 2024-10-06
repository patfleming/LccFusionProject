# Scans through all Markdown files in the specified directories and replaces the terms with the corresponding Liquid tags or reverses the substitution.
# The terms are defined in a YAML file. The script reads the YAML file and replaces the terms in the Markdown files.
# The script skips files with specific names or extensions.
# The script is run from the command line with the YAML file as an argument.
# The script can be customized by changing the MARKDOWN_DIRS, SKIP_FILES, and SKIP_EXTENSIONS variables.
# The script is compatible with Jekyll sites using Liquid tags.
# The script is compatible with Python 3.6 and above.
# The script requires the PyYAML package, which can be installed via pip.
# The script should be placed in the root directory of the Jekyll site.
# The script should be run from the command line with the following command:
# python preprocess_terms.py terms.yml
# python preprocess_terms.py terms.yml -r
#
import os
import yaml
import re
import sys
import argparse

# Files to skip (exact file names or extensions)
SKIP_FILES = ['terminology.md']  # Add files you want to skip
SKIP_EXTENSIONS = ['.yml']  # Add extensions you want to skip

def load_terms(terms_file):
    with open(terms_file, 'r', encoding='utf-8') as f:
        terms = yaml.safe_load(f)
    return terms

def should_skip_file(file_name):
    # Check if the file name matches any in the skip list
    if file_name in SKIP_FILES:
        return True
    # Check if the file has an extension in the skip list
    if any(file_name.endswith(ext) for ext in SKIP_EXTENSIONS):
        return True
    return False

def replace_terms_in_content(content, terms, data_file_name, reverse=False):
    if reverse:
        # Reverse substitution: Replace Liquid variables back to original terms
        for key, value in terms.items():
            # Construct regex pattern to match the Liquid variable
            # Allow for optional whitespace and filters
            pattern = r'\{\{\s*site\.data\.%s\.%s(?:\s*\|\s*[^}]*)?\s*\}\}' % (re.escape(data_file_name), re.escape(key))
            # Use re.IGNORECASE and re.DOTALL
            content = re.sub(pattern, value, content, flags=re.IGNORECASE)
    else:
        # Forward substitution: Replace terms with Liquid variables
        for key, value in terms.items():
            # Use word boundaries to match whole words only
            pattern = r'\b%s\b' % re.escape(value)
            liquid_variable = '{{ site.data.%s.%s }}' % (data_file_name, key)
            content = re.sub(pattern, liquid_variable, content, flags=re.IGNORECASE)
    return content

def process_markdown_files(terms_file, reverse=False):
    terms = load_terms(terms_file)
    data_file_name = os.path.splitext(os.path.basename(terms_file))[0]

    # Directories containing your Markdown files
    MARKDOWN_DIRS = ['.']  # Add other directories if needed

    for directory in MARKDOWN_DIRS:
        for root, _, files in os.walk(directory):
            for filename in files:
                if should_skip_file(filename):
                    # Skip the file
                    continue

                if filename.endswith('.md') or filename.endswith('.markdown'):
                    filepath = os.path.join(root, filename)
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()

                    new_content = replace_terms_in_content(content, terms, data_file_name, reverse=reverse)

                    # Only write back if changes were made
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        action = "Reversed" if reverse else "Processed"
                        print(f"{action} {filepath}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Preprocess terms in Markdown files.')
    parser.add_argument('terms_file', help='Path to the YAML file containing terms')
    parser.add_argument('-r', '--reverse', action='store_true', help='Reverse the substitution of terms')
    args = parser.parse_args()

    terms_file = args.terms_file
    reverse = args.reverse
    process_markdown_files(terms_file, reverse=reverse)
