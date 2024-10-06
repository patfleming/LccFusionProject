@echo off
REM Run the pre-processing script for each YAML file

python preprocess_terms.py _data\components.yml

REM Start Jekyll server
bundle exec jekyll serve

pause
