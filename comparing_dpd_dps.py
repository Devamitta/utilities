import csv
from os.path import basename

csv_file = '../spreadsheets/dps-dpd-ex.csv'

with open(csv_file) as f, \
        open('filtered_csv/plus_case.csv', 'w') as plus_case, \
        open('filtered_csv/meaning_1.csv', 'w') as meaning_1, \
        open('filtered_csv/meaning_lit.csv', 'w') as meaning_lit, \
        open('filtered_csv/root_pali.csv', 'w') as root_pali, \
        open('filtered_csv/root_base.csv', 'w') as root_base, \
        open('filtered_csv/construction.csv', 'w') as construction, \
        open('filtered_csv/derivative.csv', 'w') as derivative, \
        open('filtered_csv/suffix.csv', 'w') as suffix, \
        open('filtered_csv/phonetic.csv', 'w') as phonetic, \
        open('filtered_csv/compound_type.csv', 'w') as compound_type, \
        open('filtered_csv/compound_construction.csv', 'w') as compound_construction, \
        open('filtered_csv/sanskrit.csv', 'w') as sanskrit, \
        open('filtered_csv/variant.csv', 'w') as variant, \
        open('filtered_csv/commentary.csv', 'w') as commentary, \
        open('filtered_csv/example_1.csv', 'w') as example_1, \
        open('filtered_csv/example_2.csv', 'w') as example_2, \
        open('filtered_csv/notes.csv', 'w') as notes:
    dict_reader = csv.DictReader(f, delimiter='\t')
    out_files = [plus_case, meaning_1, meaning_lit, root_pali, root_base,
                 construction, derivative, suffix, phonetic, compound_type, compound_construction, sanskrit, variant, commentary, example_1, example_2, notes]
    dict_writers = {}
    for file in out_files:
        name = basename(file.name)[:-4]
        if name.startswith('meaning'):
            headings = ['id', 'pali_1', 'meaning_1', 'meaning_lit']
        else:
            headings = ['id', 'pali_1', name]
        dict_writers[name] = csv.DictWriter(file, headings)
        dict_writers[name].writeheader()

    for row in dict_reader:
        for name in dict_writers.keys():
            dpd_name = 'DPD_' + name
            if row[name] and not row[dpd_name]:
                if name.startswith('meaning'):
                    filtered_row = {'id': row['id'], 'pali_1': row['pali_1'],
                                    'meaning_1': row['meaning_1'], 'meaning_lit': row['meaning_lit']}
                else:
                    filtered_row = {
                        'id': row['id'], 'pali_1': row['pali_1'], name: row[name]}
                dict_writers[name].writerow(filtered_row)
