# `anthology.bib` minified

A minified version of the official [aclanthology.bib](https://aclanthology.org/) without _address_, _editor_, _month_, and duplicate _url+doi_ fields. Except for _address_, they are not rendered by ACL Natbib style anyway (most papers).
It also uses some variable compression to keep it under 50MB.
Updated up to August 01 2025.

Get it here: [https://raw.githubusercontent.com/zouharvi/anthology-bib-small/main/anthology.min.bib](https://raw.githubusercontent.com/zouharvi/anthology-bib-small/main/anthology.min.bib) or:
```
curl https://raw.githubusercontent.com/zouharvi/anthology-bib-small/main/anthology.min.bib > anthology.min.bib
```

## Update August 2025

The ACL anthology is [now split](https://github.com/acl-org/acl-anthology/pull/5766) to `anthology-1.bib`, `anthology-2.bib`, etc which are each <50MB and can thus be uploaded to Overleaf.

## Size difference

```bash
ls -lh anthology.bib anthology.min.bib
> 67M anthology.bib
> 42M anthology.min.bib
```

## To reproduce

```bash
python3 minify.py
```
