import base64, pathlib
root = pathlib.Path('/home/claude/mi-kurs')
src = (root/'src/kurs.html').read_text(encoding='utf-8')
def uri(p): return 'data:image/png;base64,' + base64.b64encode((root/'logo'/p).read_bytes()).decode()
src = src.replace('{{LOGO_POS}}', uri('gr-liggande-positiv.png')).replace('{{LOGO_NEG}}', uri('gr-liggande-negativ.png'))
head, body = src.split('<!--BODY-->')
(root/'artifact.html').write_text(head + body, encoding='utf-8')
site = ('<!DOCTYPE html>\n<!--\n  Självstudiekurs: Motiverande ledarskap, förberedelse inför dag 2.\n'
        '  Fristående fil. Bygger på Handbok för ledarhjältar (Edler, Hartelius, Ehrenborg, 2024), kap 4 och 5.\n'
        '  Grafisk profil: Göteborgsregionen (grafisk manual 2018).\n-->\n'
        '<html lang="sv">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n'
        + head + '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
(root/'index.html').write_text(site, encoding='utf-8')
print(len(site))
