# Hochwasserzentralen API

Das Länderübergreifendes Hochwasserportal (LHP) bietet auf https://www.hochwasserzentralen.de über die hier dokumentierte API Informationen zur Hochwassersituation in Deutschland an. Betreiber des LHP sind das Bayerische Landesamt für Umwelt (LfU) und die Landesanstalt für Umwelt Baden-Württemberg (LUBW).

Die Urheberrechte an den veröffentlichten Daten liegen nach [Auskunft der Betreiber](https://www.hochwasserzentralen.de/impressum) bei der für das jeweilige Bundesland zuständigen Hochwasserzentrale bzw. beim jeweiligen Pegelbetreiber.


## get_infospegel.php

**URL:** https://www.hochwasserzentralen.de/webservices/get_infospegel.php

Liefert über einen POST-request Infos zu einem Pegel.


**Body-Parameter:** *pgnr* (Optional)

Pegelname, z.B. HE_24820206


## get_infosbundesland.php

**URL:** https://www.hochwasserzentralen.de/webservices/get_infosbundesland.php

Liefert über einen POST-request Infos zu einem Bundesland. 

 
**Body-Parameter:** *id* (Optional)

Bundesland-Kürzel, z.B. HE.


## get_lagepegel.php

**URL:** https://www.hochwasserzentralen.de/webservices/get_lagepegel.php

Liefert über einen GET-request Infos zur Lage der Pegel mit Pegelnummern.



## bundesland.{version}.geojson

**URL:** https://www.hochwasserzentralen.de/vhosts/geojson/bundesland.{version}.geojson

Liefert über einen GET-request ein Geojson der Bundesländer, wobei als Pfad-Parameter **version** ein Datum im Format YYYYMMDD anzugeben ist (z.B. 20211130).


## Beispiel

```bash
result=$(curl -m 60 --location --request POST 'https://www.hochwasserzentralen.de/webservices/get_infospegel.php' \--form 'pgnr="HE_24820206"')
```

