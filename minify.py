from pybtex.database import parse_file
bib_data = parse_file('anthology.bib')

for entry in bib_data.entries:
    if "address" in bib_data.entries[entry].fields:
        bib_data.entries[entry].fields.pop("address")
    if "month" in bib_data.entries[entry].fields:
        bib_data.entries[entry].fields.pop("month")

    if "url" in bib_data.entries[entry].fields and "doi" in bib_data.entries[entry].fields:
        bib_data.entries[entry].fields.pop("url")

    if "editor" in bib_data.entries[entry].persons:
        bib_data.entries[entry].persons.pop("editor")


bib_data.to_file("anthology.min.bib", bib_format="bibtex")