#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys

#vFileStr = "table1.html"
vCellSep = "|"
vOutputType = "table"
vHorizLine = 0 # Table: horizontal line after every row
vHeader = 0    # Headlines: add header to every sub heading except first

def print_help():
    print('''Usage:
cat <html_file> | ./h2o.py [OPTIONS] ...

OPTIONS:
    -tt  - output into table
    -th  - output into headlines
    -tl  - output into list
    -l   - table: put horizontal line after every row
    -h   - headings: put header names (first row) into every heading. Do not output first row.
    --help - print this help screen''')
    return

# process cli options
for arg in sys.argv[1:]:
    if arg == '-tt':
        vOutputType = 'table'
    elif arg == '-th':
        vOutputType = 'headline'
    elif arg == '-tl':
        vOutputType = 'list'
    elif arg=='-l':
        vHorizLine = 1
    elif arg=='-h':
        vHeader = 1
    elif arg=='--help':
        print_help()
        sys.exit(0)
    else:
        print("Unknown option: " + arg)
        print_help()
        sys.exit(1)

#with open(vFileStr, 'r') as vFile:
#    s=BeautifulSoup(vFile)

s = BeautifulSoup(sys.stdin)

# --- table ---
if vOutputType == 'table':
    for vTable in s.find_all('table'):
        for vRow in vTable.find_all('tr'):
            vCells = []
            for vCell in vRow.find_all(['th', 'td']):
                vCells.append(vCell.get_text().strip().splitlines())
            vMaxHeight = 0
            for vCell in vCells:
                if len(vCell) > vMaxHeight:
                    vMaxHeight = len(vCell)
            for x in range(0, vMaxHeight):
                for vCell in vCells:
                    print(vCellSep, end="")
                    if x < len(vCell):
                        if len(vCell[x]) > 0:
                            txt = vCell[x].replace(vCellSep, '<vert_line>')
                            if vCell[x][0] == '-':
                                print('\'' + txt, end="")
                            else:
                                print(txt, end="")
                print()
            if vRow.parent.name == 'thead':
                print(vCellSep + "-")
            elif vHorizLine == 1:
                print(vCellSep + "-")
        if vHorizLine == 0:
            print(vCellSep + "-")
        print("\n\n")

# --- headline ---
if vOutputType == 'headline':
    for vTable in s.find_all('table'):
        print('* table')
        vHeaderNames=[]
        vTmpPref = '   + '
        vTmpPrefix = vTmpPref
        for vRowNr, vRow in enumerate(vTable.find_all('tr')):
            if vRowNr != 0 or vHeader != 1:
                print('*', end="")
            for vCellNr, vCell in enumerate(vRow.find_all(['th', 'td'])):
                txt = vCell.get_text().strip()
                if vRowNr == 0 and vHeader == 1:
                    vHeaderNames.append(txt)
                    continue
                if vHeader == 1:
                    vTmpPrefix = vTmpPref + vHeaderNames[vCellNr] + ' :: '
                if vCellNr == 0:
                    print("* " + txt.replace('\n', '. '))
                else:
                    print(vTmpPrefix + txt.replace("\n", "\n     "))
            #print()
        print("\n\n")

# --- list ---
if vOutputType == 'list':
    for vTable in s.find_all('table'):
        for vRow in vTable.find_all('tr'):
            for vCellNr, vCell in enumerate(vRow.find_all(['th', 'td']), 1):
                txt = vCell.get_text().strip().replace("\n", "\n  ").strip()
                if vCellNr == 1:
                    print('+ ' + txt.replace('\n', '. '), end="")
                elif vCellNr == 2:
                    print(" :: " + txt)
                else:
                    print("  " + txt)
        print("\n\n")
