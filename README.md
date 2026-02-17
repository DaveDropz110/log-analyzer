# Log Analyzer

A Python command-line tool that analyzes application log files and counts event severity levels.

## Problem it solves
Systems produce large log files that are hard to inspect manually.  
This tool summarizes activity instantly by counting:

- INFO events
- WARNING events
- ERROR events
- Unknown lines

## How to run

1. Clone the repository
2. Place a log file in the folder
3. Run:

python analyzer.py

4. Enter the file name when prompted

## Example log file

INFO User login
ERROR Invalid password
WARNING Disk almost full
INFO File downloaded

## Example output

--- Log Summary ---
Total lines: 4
INFO: 2
WARNING: 1
ERROR: 1
Unknown: 0

## Skills demonstrated
- File processing
- String parsing
- Defensive programming
- Error handling
- Command-line interaction
