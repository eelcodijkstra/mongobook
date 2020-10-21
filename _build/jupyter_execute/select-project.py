# Selectie en projectie

%%bash
mongoimport -d demo --drop -c contacts adressen.json

%%bash
mongo demo --quiet

db.contacts.find({})


```{toctree}
:hidden:
:titlesonly:


regexp
intro
content
```
