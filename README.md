# Motiverande ledarskap: förberedelse inför dag 2

Självstudiekurs som deltagarna gör mellan kurstillfälle 1 och 2. En enda fristående HTML-fil (`index.html`) som bygger på samma upplägg som förberedelsen inför dag 1 men med en ny, neutral formgivning.

## Innehåll

| Del | Tid | Innehåll |
|---|---|---|
| Inledning | | Översikt över de fyra delarna och hur kursen fungerar |
| 1. Pröva MI i ett möte | 15 min | MI-påminnaren (nio MI-detaljer från dag 1), plan för vad deltagaren ska testa, reflektionsfrågorna b–d |
| 2. Psykologisk trygghet | 1 tim | Webbinarium (Health Competence, ca 55 min, öppnas på Vimeo eftersom inbäddning är spärrad), läsning av kap 4 s. 84–86 med sammanfattning och flerval, skrivuppgift |
| 3. Feedback i dialog | 20 min | Film (Vimeo, ca 3 min), sammanfattning av s. 91–94, ordna stegen i följd, skrivuppgifterna c och d |
| 4. Bemöta samtalsutmaningar | 20 min | Sammanfattning av s. 114–115, sortera repliker (fälla eller stöd), reflektionsfrågorna c–e |
| Kunskapskoll och svar | 5 min | Sex frågor där svarsalternativen blandas, sammanställningen "Ta med till dag 2" (PDF eller kopiera text) |

Totalt ca 2 timmar.

## Byta filmen om feedback i dialog

Öppna `index.html` och sök på `FEEDBACK_FILM_URL` (högst upp i skriptet, längst ner i filen). Klistra in Vimeo-länken mellan citattecknen, till exempel:

```js
var FEEDBACK_FILM_URL = "https://vimeo.com/1234567890/abcdef1234";
```

Fungerar både med och utan privacy-hash. Filmen är inlagd (vimeo.com/1239539193). Om fältet töms visar kursen texten "Filmen kommer snart".

## Formgivning

* Neutral formgivning utan koppling till någon organisations grafiska profil (ingen logotyp, inga profilfärger).
* Varje avsnitt har ett enfärgat omslag i en jordnära, djup färg: skog (inledning), terrakotta (del 1), plommon (del 2), ockra (del 3), bläck (del 4) och oliv (avslutning). Vit text på de mörka färgerna, mörk text på ockra.
* Typsnitt: Arial överallt.
* Klickbart och inte klickbart skiljs åt:
  * Klickbart: knappar (fyllda eller med kantlinje i knappfärgen) och valrutor med kantlinje som markeras vid hovring.
  * Inte klickbart: textrutor utan kantlinje och fyllda markörer (a, b, c).
* Droppsymbolen visar tidsåtgången för varje del.

## Begreppsregler (samma som dag 1)

* **framkalla** / **framkallande**
* **affirmationer** (inte "bekräftelser")
* **framåtväg**
* Grundbehoven hör till **självbestämmandeteorin (SDT)**, inte till MI

## Teknik

* Fristående HTML utan byggsteg. Inga externa typsnitt eller bilder.
* Svar och progress sparas i webbläsaren (localStorage).
* Röstinmatning på svenska (sv-SE) i alla tio fritextrutor.
* Filmer startar först vid klick (Vimeo). Film och mikrofon kräver https.
* Publicering: lägg filen i ett nytt GitHub-repo kopplat till Netlify, på samma sätt som för dag 1.
* Källfilerna ligger i `src/` (sidan) och `tools/build.py` (bygger `index.html`).
