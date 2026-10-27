# Motiverande ledarskap: förberedelse inför dag 2

Självstudiekurs som deltagarna gör mellan kurstillfälle 1 och 2. En enda fristående HTML-fil (`index.html`) som bygger på samma upplägg som förberedelsen inför dag 1, men nu i GR:s grafiska profil.

## Innehåll

| Del | Tid | Innehåll |
|---|---|---|
| Inledning | | Översikt över de fyra delarna och hur kursen fungerar |
| 1. Pröva MI i ett möte | 15 min | MI-påminnaren (nio MI-detaljer från dag 1), plan för vad deltagaren ska testa, reflektionsfrågorna b–d |
| 2. Psykologisk trygghet | 1 tim | Webbinarium (Health Competence, ca 55 min), påminnelse ur kap 4 s. 84–86, flerval, skrivuppgift |
| 3. Feedback i dialog | 20 min | Film (**platshållare**), sammanfattning av s. 91–94, ordna stegen i följd, skrivuppgifterna c och d |
| 4. Bemöta samtalsutmaningar | 20 min | Sammanfattning av s. 114–115, sortera repliker (fälla eller stöd), reflektionsfrågorna c–e |
| Kunskapskoll och svar | 5 min | Sex frågor där svarsalternativen blandas, sammanställningen "Ta med till dag 2" (PDF eller kopiera text) |

Totalt ca 2 timmar.

## Lägga in filmen om feedback i dialog

Öppna `index.html` och sök på `FEEDBACK_FILM_URL` (högst upp i skriptet, längst ner i filen). Klistra in Vimeo-länken mellan citattecknen, till exempel:

```js
var FEEDBACK_FILM_URL = "https://vimeo.com/1234567890/abcdef1234";
```

Fungerar både med och utan privacy-hash. Så länge fältet är tomt visar kursen texten "Filmen kommer snart".

## Grafisk profil

Bygger på GR:s grafiska manual (2018):

* Profilfärgerna används som plattor och mönster, aldrig som textfärg. Texten är svart eller vit beroende på platta.
* Varje avsnitt börjar med ett omslag i manualens hierarki (nivå 2, nivå 3, rubrik, ingress) där en färgplatta och en mönsterhalva ligger bredvid varandra. Plattans färg skiljer sig från mönstrets två färger.
* Typsnitt: Franklin Gothic (Libre Franklin på webben) som manualens reserv för ITC Conduit, och Georgia för brödtext.
* Inga versaler. Listor med siffror eller fyllda punkter. Ikoner med en färg och en ihålig cirkel. Droppsymbolen används för tidsangivelser.
* Logotypen (liggande) sitter uppe till höger, i positiv version i ljust läge och negativ version i mörkt läge.
* Mönstret är ritat i samma anda som GR:s kartmönster och är inte originalfilen.

## Begreppsregler (samma som dag 1)

* **framkalla** / **framkallande**
* **affirmationer** (inte "bekräftelser")
* **framåtväg**
* Grundbehoven hör till **självbestämmandeteorin (SDT)**, inte till MI

## Teknik

* Fristående HTML utan byggsteg. Typsnittet hämtas från Google Fonts, och logotyperna ligger inbäddade i filen.
* Svar och progress sparas i webbläsaren (localStorage).
* Röstinmatning på svenska (sv-SE) i alla tio fritextrutor.
* Filmer startar först vid klick (Vimeo). Film och mikrofon kräver https.
* Publicering: lägg filen i ett nytt GitHub-repo kopplat till Netlify, på samma sätt som för dag 1.
* Källfilerna ligger i `src/` (sidan), `logo/` (logotyperna) och `tools/build.py` (bygger `index.html`).
