# `anthology.bib` minified

A minified version of the official [aclanthology.bib](https://aclanthology.org/) without _address_, _editor_, _month_, and duplicate _url+doi_ fields. Except for _address_, they are not rendered by ACL Natbib style anyway.

Get it here: [https://raw.githubusercontent.com/zouharvi/anthology-bib-small/main/anthology.min.bib](https://raw.githubusercontent.com/zouharvi/anthology-bib-small/main/anthology.min.bib) or:
```
curl https://raw.githubusercontent.com/zouharvi/anthology-bib-small/main/anthology.min.bib > anthology.min.bib
```


## Size difference

```bash
> ls -lh anthology.bib anthology.min.bib
58M anthology.bib
41M anthology.min.bib
```