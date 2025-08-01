import re
from pybtex.database import parse_file
import requests
import gzip
import shutil
import os


print("Downloading anthology.bib.gz")
url = "https://aclanthology.org/anthology.bib.gz"
response = requests.get(url, stream=True)


with open("anthology.bib.gz", mode="wb") as file:
    file.write(response.content)

print("Extracting anthology.bib")
with gzip.open('anthology.bib.gz', 'rb') as f_in:
    with open('anthology.bib', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("Parsing anthology.bib")
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
print("Reading anthology.bib again with Unicode")
with open("anthology.min.bib", "r", encoding="utf8") as file:
    data = file.read()


print("Running replacements")
# remove empty lines
data = re.sub(r'\n\s*\n', '\n', data)
# remove spaces at the beginning of the line
data = re.sub(r'^\s+', '', data, flags=re.MULTILINE)


# replace all publishers with a variable
data = re.sub(r'publisher = "Association for Computational Linguistics",', r'publisher = ACL,', data)
data = '@STRING(ACL = "Association for Computational Linguistics")\n' + data

# TODO: replace booktitle the same way

# write file
print("Writing anthology.min.bib")
with open("anthology.min.bib", "w", encoding="utf8") as file:
    file.write(data)
    
print("Deleting Temp Files")    
os.remove("anthology.bib")
os.remove("anthology.bib.gz")