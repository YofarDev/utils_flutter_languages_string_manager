
import xlsxwriter
import pandas as pd
from typing import Optional
from xlsxwriter.worksheet import (
    Worksheet, cell_number_tuple, cell_string_tuple)

main_file = "languages.dart"
excel_file = "strings.xlsx"
codes = ["en", "fr"]


class Group:
    def __init__(self, title, child):
        self.child = child
        self.title = title


def get_groups():
    with open(main_file) as f:
        lines = f.readlines()

    firstTitle = False
    lastTitle = ""
    map = []
    i = 0
    for line in lines:
        str = line.lstrip()
        if (str.startswith("///")):
            firstTitle = True
            str = str.replace("///", "")
            str = str.replace("\n", "")
            lastTitle = str
        else:
            if firstTitle:
                str = line.replace("String get ", "")
                str = str.replace(" ", "")
                str = str.replace(";", "")
                str = str.replace("\n", "")
                if not ('}' in str) and (len(str) > 0):
                    g = Group(lastTitle, str)
                    map.append(g)

    children = []
    groups = []
    last = map[0].title
    for g in map:
        if last == g.title:
            children.append(g.child)
        else:
            groups.append(Group(last, children))
            last = g.title
            children = []
            children.append(g.child)
    groups.append(Group(last, children))
    return groups


def init_xlsx(w):
    w.write(0, 0, "Title")
    i = 1
    for c in codes:
        w.write(0, i, c)
        i = i+1
    i = 1
    for g in groups:
        w.write(i, 0, "#{}".format(g.title))
        i = i+1
        for child in g.child:
            w.write(i, 0, child)
            i = i+1


def get_translations(code, strings):
    translations = []
    nextL = False
    with open("language_{}.dart".format(code)) as f:
        lines = f.readlines()
        for l in lines:
            if nextL:
                str = l.replace("\"", "")
                str = str.replace(";\n", "")
                translations.append(str.lstrip())
                nextL = False
            else:
                for s in strings:
                    if "String get {} =>".format(s) in l:
                        if (l.replace(" ", "").startswith("Stringget")):
                            if (";" not in l):
                                nextL = True
                            else:
                                str = l.replace(
                                    "String get {} =>".format(s), "")
                                str = str.replace(";\n", "")
                                str = str.replace("\"", "")
                                translations.append(str.lstrip())

    return translations


def write_xlxs(w):
    j = 1
    for code in codes:
        i = 2
        for g in groups:
            w.set_row(i-1, cell_format=data_format2)
            for t in get_translations(code, g.child):
                w.write(i, j, t)
                i = i+1
            i = i+1
        j = j+1


def get_column_width(worksheet: Worksheet, column: int) -> Optional[int]:
    """Get the max column width in a `Worksheet` column."""
    strings = getattr(worksheet, '_ts_all_strings', None)
    if strings is None:
        strings = worksheet._ts_all_strings = sorted(
            worksheet.str_table.string_table,
            key=worksheet.str_table.string_table.__getitem__)
    lengths = set()
    for row_id, colums_dict in worksheet.table.items():  # type: int, dict
        data = colums_dict.get(column)
        if not data:
            continue
        if type(data) is cell_string_tuple:
            iter_length = len(strings[data.string])
            if not iter_length:
                continue
            lengths.add(iter_length)
            continue
        if type(data) is cell_number_tuple:
            iter_length = len(str(data.number))
            if not iter_length:
                continue
            lengths.add(iter_length)
    if not lengths:
        return None
    return max(lengths)


def set_column_autowidth(worksheet: Worksheet, column: int):
    maxwidth = get_column_width(worksheet=worksheet, column=column)
    if maxwidth is None:
        return
    if column != 0:
        maxwidth = maxwidth/2
    worksheet.set_column(first_col=column, last_col=column, width=maxwidth)


groups = get_groups()
workbook = xlsxwriter.Workbook(excel_file)
w = workbook.add_worksheet()
data_format1 = workbook.add_format({'bold': True, 'bg_color': '#FF0000', 'border': 1,
                                    'align': 'left',
                                    'font_size': 10, })
data_format2 = workbook.add_format({'bold': True, 'bg_color': '#FFA6A6'})
w.set_row(0, cell_format=data_format1)
init_xlsx(w)
write_xlxs(w)

i = len(codes)
while i >= 0:
    set_column_autowidth(w, i)
    i = i-1


workbook.close()
