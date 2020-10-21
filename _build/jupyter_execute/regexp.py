# Regexp

%%bash
mongoimport -d demo --drop -c contacts adressen.json

%%bash
mongo demo --quiet

db.contacts.find({"address.city": /Am/})