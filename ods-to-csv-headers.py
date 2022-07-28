#
# - ODS files are just ZIP files and all data is contained within
# - The goal of this script is to convert an ODS file to CSV
#
# DEVELOPER NOTES:
# - Note that ElementTree was not used on purpose
#

import os
import sys
from zipfile import ZipFile
from xml.dom import minidom

# Check if a file name and sheet name were provided.
#
if len(sys.argv) < 4:
    print('Please specify a file to convert, a sheet name, and columns count.')
    exit()

ods_file_name = sys.argv[1]
sheet_name = sys.argv[2]
column_count = int(sys.argv[3])

print('=' * 64)
print('File:\t{}'.format(ods_file_name))
print('Sheet:\t{}'.format(sheet_name))
print('=' * 64)

# This will contain all bold style names, it will be filled with data after opening the ODS file.
#
bold_styles = []

# =================================================================================================
# Utility functions
# =================================================================================================

def process_text(text):
    # this is a <text:p> thing
    #
    # Iterate all Nodes aggregate TEXT_NODE
    clean_text = []
    for node in text:
        if node.nodeType == node.TEXT_NODE:
            clean_text.append(node.data)
        else:
            # the only case (for now) where a node is non-text is if this is a formatted word within
            # the cell, for example (and for now the only example) a bold-formatted text, in this
            # case the node tag name would be "text:span" which is the only kind of inner nodes this
            # script supports for now
            #
            is_bold = node.tagName == 'text:span' and node.getAttribute('text:style-name') in bold_styles
            open_tag = close_tag = ''
            if is_bold:
                open_tag = '<b>'
                close_tag = '</b>'
            clean_text.append('{}{}{}'.format(open_tag, process_text(node.childNodes), close_tag))

    return ''.join(clean_text)


def get_cell_text(row):
    # rows usually contain <text:p>
    text = row.getElementsByTagName('text:p')
    if text and len(text) >= 1:
        return '<br/>'.join([process_text(t.childNodes) for t in text])
    
    # fallback 
    return ""


# =================================================================================================
# Open the ODS file to get the conents
#
with ZipFile(ods_file_name) as ods_file:
    # Only interested in 'content.xml' as it contains 'base' styles (i.e. bold formatting etc.)
    with ods_file.open('content.xml') as ods_content:
        # internally ODS saves stuff in the XML format
        #
        xml_content = ods_content.read()

        # The actual content of the spreadsheets is locaated in:
        # <office:document-content> -> <office:body> -> <office:spreadsheet>
        # For now we only care about the first spreadsheet which would be the
        # first child of <office:body>
        #
        document_content = minidom.parseString(xml_content)

        # Before processing the actual data we need to pull all BOLD styles
        #
        all_automatic_styles = document_content.getElementsByTagName('office:automatic-styles')

        for automatic_styles in all_automatic_styles:
            for automatic_style in automatic_styles.childNodes:
                for style in automatic_style.childNodes:
                    if style.tagName == 'style:text-properties' and style.getAttribute('fo:font-weight') == 'bold':
                        bold_styles.append(automatic_style.getAttribute('style:name'))

        # Now get to convert the actual data in the provided sheet
        #
        all_spreadsheets = document_content.getElementsByTagName('office:spreadsheet')

        first_spredsheet = all_spreadsheets[0]
        tables = [table for table in first_spredsheet.getElementsByTagName('table:table')]
        table = next((table for table in tables if table.getAttribute('table:name') == sheet_name), None)

        if table is None:
            print('Sorry, could not find sheet named "{}".'.format(sheet_name))
            exit()

        rows = table.getElementsByTagName('table:table-row')[1:]

        print('\nTotal rows to process: {}'.format(len(rows)))

        # Open a CSV file to write to
        #
        with open('{}.csv'.format(os.path.splitext(ods_file_name)[0]), 'w', encoding='utf-8') as csv_file:
            first = True
            for row in rows:
                base_cells = [cell for cell in row.getElementsByTagName('table:table-cell')]
                flat_cells = []
                for cell in base_cells:
                    repeat_count = cell.getAttribute('table:number-columns-repeated')
                    if repeat_count:
                        for repeated in range(int(repeat_count)):
                            flat_cells.append(cell)
                    else:
                        flat_cells.append(cell)

                cells = [get_cell_text(cell) for cell in flat_cells[0:column_count]]
                valid_cells = ['{}'.format('""' if not cell else '"{}"'.format(cell)) for cell in cells]
                cell_len = len(valid_cells)
                if len(''.join(valid_cells)) != 0:
                    line_data = '\t'.join(valid_cells)
                    csv_file.write('{}{}'.format('' if first else '\n', line_data))
                first = False
