# HTML-table-to-Org-table
Python3 script for converting HTML tables to ORG tables/headlines/lists.
It reads HTML table from stdin and outputs org table/headline/list to stdout.
After converting, the table cells need to be aligned in Emacs org-mode (just press `<tab>` when cursor is on the table)

# Requirements
* python3
* bs4 (Beautiful Soup) python module

# Help
run `./h2o.py --help`

# Usage Examples:

```
curl -s https://docs.python.org/3/library/itertools.html | ./h2o.py -th -h
cat table.html | ./h2o.py
cat table.html | ./h2o.py -tl | putclip # copy to clipboard after converting (putclip from cygwin)
```
