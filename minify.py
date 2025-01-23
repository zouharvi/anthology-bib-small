import re
from pybtex.database import parse_file
bib_data = parse_file('anthology.bib')

for entry in bib_data.entries:
    if "address" in bib_data.entries[entry].fields:
        bib_data.entries[entry].fields.pop("address")
    if "month" in bib_data.entries[entry].fields:
        bib_data.entries[entry].fields.pop("month")

    if "url" in bib_data.entries[entry].fields and "doi" in bib_data.entries[entry].fields:
        bib_data.entries[entry].fields.pop("url")

    if "editor" in bib_data.entries[entry].persons and "author" in bib_data.entries[entry].persons:
        bib_data.entries[entry].persons.pop("editor")

bib_data.to_file("anthology.min.bib", bib_format="bibtex")

# read file again
with open("anthology.min.bib", "r") as file:
    data = file.read()
# remove empty lines
data = re.sub(r'\n\s*\n', '\n', data)
# remove spaces at the beginning of the line
data = re.sub(r'^\s+', '', data, flags=re.MULTILINE)


# replace all publisher with a variable
data = re.sub(r'publisher = "Association for Computational Linguistics",', r'publisher = ACL,', data)
data = '@STRING(ACL = "Association for Computational Linguistics")\n' + data

# TODO: replace booktitle the same way

# write file
with open("anthology.min.bib", "w") as file:
    file.write(data)