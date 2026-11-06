# R2 Gestaltung und Bedienbarkeit: Belege für die Kaffee-Simulation

> Recherche für `simulation/KONZEPT.md` (Phase 1, Strang 2), Stand 04.11.2026. Werkzeug: eine Seite, offline, Deutsch, Nutzung 10 bis 15 Minuten zu zweit, oft am Handy (390 px), auch am Laptop (1366 px). Kontrastrechnung: `simulation/recherche/r2_kontrast.py` (Ausgabe in Abschnitt C).

**Zum Prüfstatus.** „Volltext“: Ich habe die Quelle geladen und die Stelle gelesen. Bei PDF-Dateien habe ich den Text selbst mit `pdftotext` ausgelesen; die Zitate sind daraus kopiert. Bei Webseiten liefert das Abrufwerkzeug den Wortlaut über eine Zwischenzusammenfassung mit dem Auftrag „wörtlich“; kleine Abweichungen in Zeichensetzung sind dort nicht ganz auszuschließen. „Abstract“: nur die Zusammenfassung gelesen. „Sekundärquelle“: Aussage stammt aus einer anderen, genannten Quelle. „Nicht geprüft“: nur Bibliodaten bestätigt (Crossref), Inhalt nicht gelesen; solche Quellen tragen keine Anforderung.

## A. Übersicht der Quellen

| Nr. | Kurzbeleg | Prüfstatus | Begründete Anforderung an das Werkzeug |
|---|---|---|---|
| Q1 | Ainsworth 2006, Learning and Instruction (DeFT) | Sekundärquelle (Q2, gleiche Autorin, gleicher Rahmen) | Zahl, Reihenfolge und Verknüpfung der Darstellungen bewusst festlegen |
| Q2 | Ainsworth und Van Labeke 2002, Workshop-Beitrag zu DeFT | Volltext | Übersetzen zwischen Diagramm und Zahlen unterstützen (Zeitzeiger koppelt Rechenwerte an Kurven); Lesehilfe für das Diagramm |
| Q3 | Plass, Homer und Hayward 2009, J. Computing in Higher Education | nicht geprüft | keine (gestrichen) |
| Q4 | Mayer 2024, Educational Psychology Review (15 Prinzipien mit Effektstärken) | Volltext | Kohärenz, Signalisierung, räumliche und zeitliche Nähe, Segmentierung, Vortraining umsetzen |
| Q5 | Mayer 2020, Multimedia Learning, 3. Aufl. | Sekundärquelle (Q4, Tabelle 6 „from Mayer, 2021“) | wie Q4 |
| Q6 | Mayer und Fiorella (Hrsg.) 2021, Cambridge Handbook of Multimedia Learning, 3. Aufl. | Sekundärquelle (Q4) | nur Verweis auf weitere Prinzipien |
| Q7 | Moreno und Mayer 2007, Educational Psychology Review | nicht geprüft | keine eigene; Übertrag auf Simulationen ist meine Folgerung |
| Q8 | Sweller, van Merriënboer und Paas 2019, Educational Psychology Review | Volltext | Regler stufenweise freischalten (einfach zu komplex), Profi-Modus, Zusammenarbeit zu zweit nutzen |
| Q9 | Sweller, van Merriënboer und Paas 1998, Educational Psychology Review | Sekundärquelle (Q8) | wie Q8 |
| Q10 | Shah und Hoeffner 2002, Educational Psychology Review | nicht geprüft | keine eigene |
| Q11 | Franconeri et al. 2021, Psychological Science in the Public Interest | Abstract | Arbeitsgedächtnis entlasten, Aufmerksamkeit lenken, Konventionen einhalten |
| Q12 | Huestegge und Philipp 2011, Attention, Perception, and Psychophysics | Volltext | Beschriftung räumlich an die Kurven (direkt), aber ohne Textgedränge |
| Q13 | Cleveland und McGill 1984, JASA | Sekundärquelle (Q14) | Energievergleich als Säulen (Länge auf gemeinsamer Achse), nicht als Flächen |
| Q14 | Heer und Bostock 2010, CHI | Volltext | wie Q13 |
| Q15 | Okabe und Ito 2008, Color Universal Design (Webseite) | Volltext | Farbe plus Linienart und Form; direkte Beschriftung; Helligkeitsunterschied zwischen Farben |
| Q16 | Wong 2011, Nature Methods | Abstract (Vorschau) | bis 8 % der Männer betroffen: Farbsehschwäche ist im Seminarraum der Normalfall |
| Q17 | Machado, Oliveira und Fernandes 2009, IEEE TVCG | Volltext (Projektseite mit Matrizen) | Simulationsmatrizen für die Farbprüfung |
| Q18 | WCAG 2.2, W3C-Empfehlung vom 12.12.2024 (erstmals 05.10.2023) | Volltext | Kontrast 4,5:1 und 3:1, Farbe nicht allein, Umbruch bei 320 px, Tastatur, Fokus, Ziehen ersetzbar, Ziel 24 px, Name/Rolle/Wert, Statusmeldungen |
| Q19 | W3C „Understanding WCAG 2.2“ zu 1.4.10, 1.4.11, 2.4.11, 2.5.7, 4.1.3 | Volltext | Kurven 3:1; Zahleneingabe neben Regler; angeheftetes Bild darf Fokus nicht verdecken; Ergebnisansage mit role="status" |
| Q20 | WAI-ARIA Authoring Practices: Slider Pattern | Volltext | Tastenbelegung und ARIA-Werte der Regler |
| Q21 | WAI-ARIA Authoring Practices: Tabs Pattern | Volltext | Rollen und Tasten der Reiterleiste |
| Q22 | ARIA in HTML, W3C-Empfehlung | Volltext | natives `input type="range"` statt eigener ARIA-Regler |
| Q23 | W3C WAI Images Tutorial: Complex Images | Volltext | zweiteilige Textalternative (kurz und lang) für das Diagramm |
| Q24 | Watson 2017, Accessible SVG line graphs | Volltext | Datentabelle zusätzlich, weil SVG-Semantik uneinheitlich unterstützt wird |
| Q25 | MDN: prefers-reduced-motion | Volltext | Animationen abschaltbar |
| Q26 | Sana, Weston und Cepeda 2013, Computers and Education | Volltext | Gerät nur mit gezielter Aufgabe; keine Ablenkung auf der Seite |
| Q27 | Sung, Chang und Liu 2016, Computers and Education (Metaanalyse) | Abstract | mobile Geräte im Unterricht mit mittlerem Nutzen, wenn eingebunden |
| Q28 | Apple Human Interface Guidelines: Accessibility | Volltext | Bedienelemente 44 mal 44 pt (Standard), mindestens 28 pt |
| Q29 | Android Developers: Make apps more accessible | Volltext | Trefferfläche mindestens 48 mal 48 dp |
| Q30 | Hoober 2013, UXmatters | Volltext | Griff wechselt ständig: keine Bedienung, die eine bestimmte Hand voraussetzt |
| Q31 | Coyier 2021, CSS-Tricks | Volltext (Sekundärquelle für das iOS-Verhalten) | Eingabefelder mindestens 16 px Schrift |
| Q32 | MDN: inputmode | Volltext | Zahlenfeld mit `inputmode="decimal"` |
| Q33 | Laakso 2020, GOV.UK Technology Blog | Volltext | kein `type="number"`; Text mit `inputmode` |
| Q34 | Sunwall 2024, Nielsen Norman Group: Tabs, Used Right | Volltext | wenige, kurze Reiter; am Handy Akkordeon |
| Q35 | Harley 2015, Nielsen Norman Group: Slider Design | Volltext | für genaue Werte Regler plus Eingabe |
| Q36 | Nielsen 1993/2014, Nielsen Norman Group: Response Times | Volltext | Reaktion auf Regler innerhalb 0,1 s |
| Q37 | van der Meij und de Jong 2003, EARLI-Beitrag | Abstract | Dyna-Linking hilft nicht sicher: nur schlank umsetzen |

## B. Die Quellen im Einzelnen

### B1 Mehrere Darstellungen

#### Q1 Ainsworth (2006)

- **Angabe:** Ainsworth, S. (2006). DeFT: A conceptual framework for considering learning with multiple representations. *Learning and Instruction*, 16(3), 183-198. <https://doi.org/10.1016/j.learninstruc.2006.03.001>
- **Fundstelle:** ganzer Artikel (Rahmen aus Design, Funktionen, Aufgaben).
- **Prüfstatus:** Sekundärquelle. Verlagsseite und Repositorium (Nottingham) lieferten Fehler 403; Bibliodaten über OpenAlex bestätigt (16(3), 183-198). Inhalt gelesen in Q2 (gleiche Autorin, gleicher Rahmen, vier Jahre früher).
- **Zitat:** keines (Stelle nicht selbst gesehen).
- **Kernaussage (über Q2):** Ob mehrere Darstellungen helfen, hängt von ihrer Funktion, ihrer Gestaltung (Zahl, Reihenfolge, Unterstützung beim Übersetzen) und den Aufgaben ab, die Lernende dabei lösen müssen.
- **Anforderung:** Für jede Darstellung (Diagramm, Rechenwerte, Tabelle, Energie) Funktion und Zeitpunkt festlegen; nicht alles gleichzeitig zeigen.
- **Trägt nicht:** Zahlen oder konkrete Grenzwerte; der Artikel ist ein Rahmen, keine Studie.

#### Q2 Ainsworth und Van Labeke (2002)

- **Angabe:** Ainsworth, S. und Van Labeke, N. (2002). *Using a Multi-Representational Design Framework to Develop and Evaluate a Dynamic Simulation Environment.* Beitrag zum International Workshop on Dynamic Visualizations and Learning, Tübingen (Institut für Wissensmedien). <https://www.iwm-tuebingen.de/workshops/visualization/ainsworth.pdf> (PDF erstellt Juni 2002, 9 Seiten, ohne Seitenzahlen).
- **Fundstelle:** Abschnitte „Constraining Functions“, „Tasks“, „Design“.
- **Prüfstatus:** Volltext.
- **Zitate:** „a very large number of studies have observed that learners find translating between representations difficult“ (Tasks). „This can range from no support through to highlighting and on to full dyna-linking where behaviour on one representation is reflected onto another.“ (Design, Translation). „familiar concrete representations such as simple animations are often employed in simulations to support interpretation of complex and unfamiliar representations such as graphs“ (Constraining Functions).
- **Kernaussage:** Lernende müssen Format und „Operatoren“ jeder Darstellung lernen (beim Graphen Achsen, Steigung, Schnittpunkte) und vor allem die Beziehung zwischen den Darstellungen herstellen, was ihnen schwerfällt; Gestaltungsgrößen sind Verteilung der Information, Form, Übersetzungshilfe, Zahl und Reihenfolge.
- **Anforderung:** (a) Lesehilfe zum Diagramm vor der ersten Frage (Achsen, Raumtemperatur, Sprung bei Milchzugabe, Schnittpunkt). (b) Übersetzungshilfe: ein Zeitzeiger im Diagramm, dessen Zeitpunkt die Rechenwerte zeigen; Fokus oder Zeigen auf einen Rechenwert hebt die zugehörige Kurve hervor. (c) Eine Becher-Grafik (Füllstand, Farbe) nur, wenn sie das Diagramm erklärt, nicht als Schmuck.
- **Trägt nicht:** Wirksamkeitsnachweis für Dyna-Linking (siehe Q37).

#### Q3 Plass, Homer und Hayward (2009)

- **Angabe:** Plass, J. L., Homer, B. D. und Hayward, E. O. (2009). Design factors for educationally effective animations and simulations. *Journal of Computing in Higher Education*, 21(1), 31-61. <https://doi.org/10.1007/s12528-009-9011-x>
- **Prüfstatus:** nicht geprüft. Bibliodaten über Crossref bestätigt; Springer, LearnTechLib und ein Bibliotheksspiegel verlangen Anmeldung oder lieferten 403; Crossref enthält kein Abstract.
- **Zitat, Kernaussage, Anforderung:** keine. Ein Suchmaschinenauszug nennt einen Befund (dynamische Darstellungen nur wirksam, wenn darstellend statt schmückend); das ist nicht an der Quelle gesehen und wird nicht verwendet.

#### Q37 van der Meij und de Jong (2003)

- **Angabe:** van der Meij, J. und de Jong, T. (2003). *Learning with multiple representations: Supporting students' translation between representations in a simulation-based learning environment.* Beitrag zur 10. EARLI-Konferenz, Padua. <https://research.utwente.nl/en/publications/learning-with-multiple-representations-supporting-students-transl/>
- **Fundstelle:** Abstract.
- **Prüfstatus:** Abstract.
- **Zitat:** „The results of this study did not lead to significant results between conditions.“
- **Kernaussage:** Getrennte, dynamisch verknüpfte und integrierte Darstellungen in einer Physik-Simulation (90 Lernende, 16 bis 18 Jahre) unterschieden sich im Lernerfolg nicht signifikant.
- **Anforderung:** Verknüpfung der Darstellungen schlank halten (Zeitzeiger, Hervorheben), nicht als Hauptmerkmal ausbauen.
- **Trägt nicht:** Aussage über die Zeitschriftenfassung von 2006 (Learning and Instruction 16, 199-212); die habe ich nicht gelesen.

### B2 Multimedia-Prinzipien

#### Q4 Mayer (2024)

- **Angabe:** Mayer, R. E. (2024). The Past, Present, and Future of the Cognitive Theory of Multimedia Learning. *Educational Psychology Review*, 36, Artikel 8. <https://doi.org/10.1007/s10648-023-09842-1> (offen zugänglich).
- **Fundstelle:** Tabelle 6, S. 20 von 25 („Fifteen principles of multimedia instructional design (from Mayer, 2021)“); Randbedingungen S. 19; Simulation als Medium S. 16.
- **Prüfstatus:** Volltext.
- **Zitate (Tabelle 6, mit Effektstärke d und Zahl der Tests):**
  - Kohärenz: „People learn better when extraneous material is excluded rather than included“ (0,86; 19).
  - Signalisierung: „People learn better when cues are added that highlight the organization of the essential material“ (0,69; 16).
  - Räumliche Nähe: „People learn better when corresponding words and pictures are presented near rather than far from each other on the page or screen“ (0,82; 9).
  - Zeitliche Nähe: „People learn better when corresponding words and pictures are presented simultaneously rather than successively“ (1,31; 8).
  - Segmentierung: „People learn better when a multimedia lesson is presented in user-paced segments rather than as a continuous unit“ (0,67; 7).
  - Vortraining: „People learn better from a multimedia lesson when they know the names and characteristics of the main concepts“ (0,78; 10).
  - Generative Aktivität: „People learn better when they are guided in carrying out generative learning activities during learning“ (0,71; 44).
  - Randbedingungen (S. 19): „Each principle is subject to boundary conditions“.
- **Kernaussage:** Die Prinzipien stammen aus Versuchen mit Lehrbotschaften aus Wort und Bild; Mayer zählt Simulationen ausdrücklich zu den Medien solcher Botschaften (S. 16), betont aber Randbedingungen.
- **Anforderung (Übertrag auf die Simulation, meine Folgerung):**
  - Kohärenz: keine Schmuckgrafik, keine Hintergrundbilder, keine Animation ohne Aussage im Simulationsbereich; Erklärtexte in Reitern statt neben dem Diagramm.
  - Signalisierung: Schnittpunkt und größter Unterschied im Diagramm markiert und beschriftet; die zur aktuellen Frage gehörende Kurve oder Kennzahl hervorgehoben.
  - Räumliche Nähe: Kurvennamen direkt an die Kurven, Einheit direkt am Wert, Rechenwerte neben den Reglern (Aufbau des Lernzentrums erfüllt das), Frage und Diagramm auf einem Bildschirm sichtbar.
  - Zeitliche Nähe: Kurven und Rechenwerte ändern sich während der Reglerbewegung mit (siehe Q36).
  - Segmentierung: Fragen einzeln, mit „Weiter“ durch die Lernenden.
  - Vortraining: Begriffe (Mischtemperatur, Raumtemperatur, kA) und Leseweise des Diagramms vor der ersten Frage.
- **Trägt nicht:** Die Effektstärken stammen aus Studien mit Erklärungen, nicht aus Simulationen zum Ausprobieren; die Werte sind keine Vorhersage für dieses Werkzeug. Modalität (gesprochener Text) ist im Seminarraum nicht sinnvoll und wird nicht übernommen.

#### Q5 Mayer (2020), Multimedia Learning, 3. Auflage

- **Angabe:** Mayer, R. E. (2020). *Multimedia Learning* (3. Aufl.). Cambridge University Press. <https://doi.org/10.1017/9781316941355> (Crossref: online 25.06.2020, Druck 09.07.2020; Q4 zitiert das Buch als 2021).
- **Prüfstatus:** Sekundärquelle (Q4, Tabelle 6 ist „from Mayer, 2021“). Buch nicht gelesen.
- **Anforderung:** wie Q4; für Zitate Q4 verwenden.

#### Q6 Mayer und Fiorella (2021), Cambridge Handbook

- **Angabe:** Mayer, R. E. und Fiorella, L. (Hrsg.) (2021). *The Cambridge Handbook of Multimedia Learning* (3. Aufl.). Cambridge University Press. <https://doi.org/10.1017/9781108894333> (Crossref: Druck 30.11.2021; Q4 zitiert 2022).
- **Prüfstatus:** Sekundärquelle (Q4, S. 19: „Many more principles are described in the wider literature, such as in The Cambridge Handbook of Multimedia Learning“).
- **Anforderung:** keine eigene.

#### Q7 Moreno und Mayer (2007)

- **Angabe:** Moreno, R. und Mayer, R. (2007). Interactive multimodal learning environments. *Educational Psychology Review*, 19(3), 309-326. <https://doi.org/10.1007/s10648-007-9047-2>
- **Prüfstatus:** nicht geprüft. Bibliodaten über Crossref; Springer verlangt Anmeldung, kein Abstract in Crossref. Ein Suchmaschinenauszug nennt fünf Prinzipien (geleitete Aktivität, Reflexion, Rückmeldung, Kontrolle, Vortraining); nicht an der Quelle gesehen.
- **Folge:** Die Frage „welche Multimedia-Prinzipien gelten auch für interaktive Simulationen“ beantworte ich nicht mit diesem Artikel, sondern mit Q4 (Simulation als Medium genannt, Randbedingungen betont) und Q8 (Segmentierung und Selbststeuerung gegen flüchtige Information). Das ist eine Folgerung, kein Beleg.

### B3 Kognitive Belastung

#### Q8 Sweller, van Merriënboer und Paas (2019)

- **Angabe:** Sweller, J., van Merriënboer, J. J. G. und Paas, F. (2019). Cognitive Architecture and Instructional Design: 20 Years Later. *Educational Psychology Review*, 31, 261-292. <https://doi.org/10.1007/s10648-019-09465-5> (offen zugänglich).
- **Fundstelle:** S. 268 (Split-Attention-Effekt), S. 277 (Expertise-Umkehr, flüchtige Information), S. 279 (isolierte Elemente, einfach zu komplex, kollektives Arbeitsgedächtnis).
- **Prüfstatus:** Volltext.
- **Zitate:** S. 279: „simple-to-complex sequencing, where learners first practice simple, low element interactivity versions of a task and only later increasingly more complex versions of this task“. S. 277: „with increasing expertise, the above effects first decrease in size, then disappear, and can eventually reverse“. S. 277: „a number of compensatory strategies are available such as self-pacing or segmentation“. S. 268: „This split-attention effect can be prevented by physically integrating the diagram and the solution statements“. S. 279: „collaborative learners can be considered as a single information processing system consisting of multiple, limited working memories“.
- **Kernaussage:** Neue, stark verflochtene Information überlastet das Arbeitsgedächtnis; helfen Reihenfolge von einfach zu komplex (zuerst einzelne Elemente), integrierte statt getrennte Informationsquellen und Selbststeuerung; für Fortgeschrittene können diese Hilfen schaden; Zusammenarbeit erweitert die Verarbeitungskapazität.
- **Anforderung:**
  - Freischaltung in Stufen. Stufe 1: nur der Regler zur Vorab-Frage (Zeitpunkt der Milchzugabe) plus Raumtemperatur als feste Anzeige. Stufe 2 (nach Frage 1): Milchtemperatur, Milchmenge, Raumtemperatur. Stufe 3 (nach Frage 3 oder auf Wunsch): kA, Becher 3, Deckel, Messpunkte. Je Stufe höchstens 3 neue Regler (Zahl ist meine Festlegung, siehe Trägt nicht).
  - Knopf „Alle Regler zeigen“ für Fortgeschrittene und für die TL (Expertise-Umkehr).
  - Schritt-für-Schritt-Fragen mit eigenem Tempo (Selbststeuerung, Segmentierung).
  - Fragen für zwei Personen formuliert („Sagen Sie erst zu zweit voraus“), passt zum kollektiven Arbeitsgedächtnis.
- **Trägt nicht:** eine Höchstzahl an Reglern. Die Quelle nennt keine Zahl; „höchstens 3 neue Regler je Stufe“ ist eine Gestaltungsentscheidung (Stärke schwach). Die Angabe „7 plus minus 2“ ist hier nicht geprüft und wird nicht verwendet.

#### Q9 Sweller, van Merriënboer und Paas (1998)

- **Angabe:** Sweller, J., van Merriënboer, J. J. G. und Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review*, 10(3), 251-296. <https://doi.org/10.1023/A:1022193728205>
- **Prüfstatus:** Sekundärquelle (Q8 fasst den Artikel als Ausgangspunkt zusammen, Abstract S. 261). Nicht selbst gelesen.
- **Anforderung:** wie Q8; zitiert wird Q8.

### B4 Diagrammgestaltung und Farbe

#### Q10 Shah und Hoeffner (2002)

- **Angabe:** Shah, P. und Hoeffner, J. (2002). Review of graph comprehension research: Implications for instruction. *Educational Psychology Review*, 14(1), 47-69. <https://doi.org/10.1023/A:1013180410169>
- **Prüfstatus:** nicht geprüft. Bibliodaten über Crossref; Springer und Deep Blue (Michigan) lieferten Anmeldeseite oder 403. Q2 zitiert den Artikel für die Aussage, das Lesen von Darstellungen sei „an inherently contextualised activity“.
- **Anforderung:** keine eigene.

#### Q11 Franconeri et al. (2021)

- **Angabe:** Franconeri, S. L., Padilla, L. M., Shah, P., Zacks, J. M. und Hullman, J. (2021). The Science of Visual Data Communication: What Works. *Psychological Science in the Public Interest*, 22(3), 110-161. <https://doi.org/10.1177/15291006211051956> (Erratum 2022, 23(1), 41-42).
- **Fundstelle:** Abstract (über PubMed, PMID 34907835).
- **Prüfstatus:** Abstract. Volltext: Sage lieferte 403, die NSF-Fassung ist zu groß für das Abrufwerkzeug.
- **Zitat:** „Effective graphics avoid taxing working memory, guide attention, and respect familiar conventions.“ Und: „Extracting global statistics is fast, but comparing between subsets of values is slow.“
- **Kernaussage:** Gute Grafiken entlasten das Arbeitsgedächtnis, lenken die Aufmerksamkeit und halten Konventionen ein; Vergleiche zwischen Teilmengen sind langsam.
- **Anforderung:** Der Vergleich, um den es geht (Tasse 1 gegen Tasse 2), wird direkt angezeigt (Differenz als Zahl und als markierte Strecke), nicht dem Auge überlassen. Konventionen: Zeit nach rechts, Temperatur nach oben, Einheiten an den Achsen.
- **Trägt nicht:** die konkreten Empfehlungen des Volltexts (direkte Beschriftung, Farbwahl); die habe ich nicht gesehen.

#### Q12 Huestegge und Philipp (2011)

- **Angabe:** Huestegge, L. und Philipp, A. M. (2011). Effects of spatial compatibility on integration processes in graph comprehension. *Attention, Perception, and Psychophysics*, 73, 1903-1915. <https://doi.org/10.3758/s13414-011-0155-1>
- **Fundstelle:** S. 1904 (Einleitung), Abstract S. 1903.
- **Prüfstatus:** Volltext.
- **Zitat:** „However, in complex or dense graphs, direct labeling easily results in visual cluttering of textual elements and, thus, cannot be considered a panacea.“ (S. 1904)
- **Kernaussage:** Wenn die Legende räumlich zu den Datenelementen passt, verstehen Lernende Graphen schneller und blicken seltener zwischen Daten und Legende hin und her; direkte Beschriftung wird empfohlen, kann aber in dichten Graphen zu Textgedränge führen.
- **Anforderung:** Kurvennamen direkt am rechten Kurvenende (höchstens 2 bis 3 Wörter, z. B. „Tasse 1: Milch sofort“); bei Überlappung der Beschriftungen (Kurven liegen am Ende eng beieinander) automatisch versetzen oder mit einer kurzen Führungslinie anbinden; keine separate Farblegende. Wenn doch eine Legende nötig ist (z. B. Messpunkte), in derselben Reihenfolge wie die Kurven von oben nach unten.
- **Trägt nicht:** Lernwirkung; gemessen wurden Antwortzeiten und Blickwechsel bei Erwachsenen.

#### Q13 Cleveland und McGill (1984) und Q14 Heer und Bostock (2010)

- **Angaben:** Cleveland, W. S. und McGill, R. (1984). Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods. *Journal of the American Statistical Association*, 79(387), 531-554. <https://doi.org/10.1080/01621459.1984.10478080>. Heer, J. und Bostock, M. (2010). Crowdsourcing graphical perception: using Mechanical Turk to assess visualization design. *Proceedings of CHI 2010*, 203-212. <https://doi.org/10.1145/1753326.1753357>, PDF: <https://homes.cs.washington.edu/~jheer/files/2010-MTurk-CHI.pdf>
- **Fundstelle:** Heer und Bostock S. 205 (Nachbau der Rangfolge) und S. 206 (Fläche gegen Position).
- **Prüfstatus:** Q14 Volltext; Q13 Sekundärquelle über Q14 (Kopie des Originals lieferte 503, Crossref ohne Abstract).
- **Zitat (Q14, S. 206):** „psychophysical theory [7, 34] predicts area to perform worse than angle, and both to be significantly worse than position.“ S. 205: „position encoding still significantly outperformed length encoding.“
- **Kernaussage:** Werte auf einer gemeinsamen Achse (Position) werden genauer verglichen als Längen, Winkel und vor allem Flächen; der Nachbau bestätigt die Rangfolge von Cleveland und McGill.
- **Anforderung:** Wenn die Seite die abgegebene Wärme zeigt: als zwei Säulen nebeneinander auf gemeinsamer Nulllinie (in kJ, mit Zahl), nicht als Fläche zwischen Kurve und Raumlinie. Eine Fläche höchstens als Zusatz zur Veranschaulichung, nicht für den Vergleich.
- **Trägt nicht:** die Frage, ob eine Fläche unter der Kurve physikalisch besser verstanden wird; das ist Fachdidaktik (Strang 3).

#### Q15 Okabe und Ito (2008)

- **Angabe:** Okabe, M. und Ito, K. (2002, zuletzt geändert 24.09.2008). *Color Universal Design (CUD): How to make figures and presentations that are friendly to Colorblind people.* <https://jfly.uni-koeln.de/color/>
- **Fundstelle:** Abschnitte „Most important practical points“, „Set of colors“, „Avoid situation where texts and objects are obscured with the background“.
- **Prüfstatus:** Volltext (Webseite). Die Farbwerte der Palette stehen dort nur im Bild, nicht im Text.
- **Zitate:** „Show difference BOTH in color and shape (solid and dotted lines, different symbols, various hatching, etc.)“. „label elements of the graph on the graph itself rather than making a separate color-coded key“. „Avoid the combination of colors that have the same brightness but different only in hue.“ Zum Anteil: „One in twelve Caucasian (8%), one in 20 Asian (5%), and one in 25 African (4%) males“.
- **Kernaussage:** Unterschiede doppelt kodieren (Farbe und Form), direkt beschriften, Farben auch in der Helligkeit unterscheiden.
- **Anforderung:** Tasse 1 durchgezogen, Tasse 2 gestrichelt, Raumlinie gepunktet und dünner; Messpunkte je Becher eigene Form (Kreis, Quadrat, Dreieck), gefüllt in der Kurvenfarbe; Kurvenfarben mit Helligkeitsabstand (siehe Abschnitt C: heutige Palette hat Delta L* rund 30 zwischen Tasse 1 und Tasse 2).
- **Trägt nicht:** Kontrastwerte; dafür WCAG (Q18).

#### Q16 Wong (2011)

- **Angabe:** Wong, B. (2011). Points of view: Color blindness. *Nature Methods*, 8, 441. <https://doi.org/10.1038/nmeth.1618>
- **Prüfstatus:** Abstract (sichtbarer Anfang des Artikels; Rest hinter Bezahlschranke, Palette nur im Bild).
- **Zitat:** „as many as 8 percent of men and 0.5 percent of women experience the common form of red-green color blindness“.
- **Kernaussage:** Rot-Grün-Schwäche ist häufig; Grafiken sollen dafür gestaltet sein.
- **Anforderung:** In einer Gruppe von 30 Studierenden mit 80 % Männern sind rechnerisch knapp 2 Betroffene zu erwarten (30 · (0,8 · 8 % + 0,2 · 0,5 %) = 1,95; Gruppengröße und Anteil sind Annahmen). Die Farbprüfung für Protanopie und Deuteranopie gehört in die Abnahme.
- **Trägt nicht:** die Farbwerte der Palette (nicht gesehen).

#### Q17 Machado, Oliveira und Fernandes (2009)

- **Angabe:** Machado, G. M., Oliveira, M. M. und Fernandes, L. A. F. (2009). A Physiologically-based Model for Simulation of Color Vision Deficiency. *IEEE Transactions on Visualization and Computer Graphics*, 15(6), 1291-1298. <https://doi.org/10.1109/TVCG.2009.113>; Matrizen: <https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html>
- **Fundstelle:** Tabelle 1 der Projektseite (Schweregrad 1,0).
- **Prüfstatus:** Volltext der Projektseite (Matrizen abgeschrieben und im Skript verwendet); Artikel selbst nicht gelesen.
- **Zitat:** keines (nur Zahlen übernommen).
- **Kernaussage:** 3 mal 3 Matrizen bilden RGB-Farben auf ihre Wahrnehmung bei Protanopie, Deuteranopie und Tritanopie ab.
- **Anforderung:** Grundlage der Farbprüfung in Abschnitt C.
- **Trägt nicht:** Die Seite sagt nicht, ob die Matrizen auf lineare oder gammakodierte Werte anzuwenden sind; ich rechne linear. Die Schwellen für „unterscheidbar“ sind meine Faustregel.

### B5 Barrierefreiheit

#### Q18 WCAG 2.2

- **Angabe:** W3C (2024). *Web Content Accessibility Guidelines (WCAG) 2.2.* W3C Recommendation 12 December 2024. <https://www.w3.org/TR/2024/REC-WCAG22-20241212/> (aktuelle Fassung <https://www.w3.org/TR/WCAG22/>). Erste Empfehlung am 05.10.2023 (W3C-Meldung <https://www.w3.org/news/2023/web-content-accessibility-guidelines-wcag-2-2-is-a-w3c-recommendation/>).
- **Prüfstatus:** Volltext (Kriterien an der Quelle gelesen).
- **Kriterien, Wortlaut (Auszug) und Anforderung:**

| Nr. (Stufe) | Wortlaut (Auszug) | Anforderung an das Werkzeug |
|---|---|---|
| 1.1.1 (A) | „If non-text content is a control or accepts user input, then it has a name that describes its purpose.“ | Diagramm mit Textalternative; jeder Regler und Knopf mit sichtbarem Namen |
| 1.4.1 (A) | „Color is not used as the only visual means of conveying information, indicating an action, prompting a response,“ | Linienart, Form, direkte Beschriftung zusätzlich zur Farbe |
| 1.4.3 (AA) | „The visual presentation of text and images of text has a contrast ratio of at least 4.5:1“ | alle Texte einschließlich Kurvenbeschriftung, Achsen, Rechenwerte mindestens 4,5:1 |
| 1.4.4 (AA) | „can be resized without assistive technology up to 200 percent without loss of content or functionality.“ | Schrift in rem; bei 200 % kein Abschneiden |
| 1.4.10 (AA) | „Vertical scrolling content at a width equivalent to 320 CSS pixels;“ | bei 320 px Breite kein waagrechtes Scrollen der Seite |
| 1.4.11 (AA) | „The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent color(s):“ | Kurven, Punkte, Raumlinie, Reglerspur und Reglerknopf, Fokusring mindestens 3:1 |
| 2.1.1 (A) | „All functionality of the content is operable through a keyboard interface“ | alles per Tastatur, auch Messwerte eintragen und Becher an/aus |
| 2.3.3 (AAA) | „Motion animation triggered by interaction can be disabled, unless the animation is essential“ | Animationen bei `prefers-reduced-motion: reduce` aus (Stufe AAA, also „sollte“) |
| 2.4.7 (AA) | „the keyboard focus indicator is visible.“ | sichtbarer Fokus an jedem Element |
| 2.4.11 (AA) | „When a user interface component receives keyboard focus, the component is not entirely hidden due to author-created content.“ | angeheftetes Diagramm am Handy darf fokussierte Regler nicht verdecken |
| 2.4.13 (AAA) | „is at least as large as the area of a 2 CSS pixel thick perimeter of the unfocused component“ | Fokusring 2 px, 3:1 zwischen fokussiert und nicht fokussiert („sollte“) |
| 2.5.5 (AAA) | „The size of the target for pointer inputs is at least 44 by 44 CSS pixels“ | Zielwert 44 px („sollte“) |
| 2.5.7 (AA) | „All functionality that uses a dragging movement for operation can be achieved by a single pointer without dragging,“ | Regler auch per Tippen auf die Spur, Plus/Minus oder Zahleneingabe |
| 2.5.8 (AA) | „The size of the target for pointer inputs is at least 24 by 24 CSS pixels“ | Untergrenze 24 px für jedes Ziel („muss“) |
| 4.1.2 (A) | „the name and role can be programmatically determined; states, properties, and values that can be set by the user can be programmatically set;“ | Regler, Kontrollkästchen, Reiter mit Name, Rolle, Wert |
| 4.1.3 (AA) | „status messages can be programmatically determined through role or properties such that they can be presented to the user by assistive technologies without receiving focus.“ | geänderte Kennzahlen als Statusmeldung |

- **Relative Luminanz (Glossar):** „if RsRGB <= 0.04045 then R = RsRGB/12.92 else R = ((RsRGB+0.055)/1.055) ^ 2.4“ und „L = 0.2126 * R + 0.7152 * G + 0.0722 * B“; Hinweis dort: Vor Mai 2021 stand 0,03928 statt 0,04045. Das Skript rechnet mit 0,04045.
- **Trägt nicht:** Lernwirkung. AAA-Kriterien sind keine Pflicht für Konformität AA.

#### Q19 W3C „Understanding WCAG 2.2“

- **Angaben:** W3C WAI. *Understanding SC 1.4.11 Non-text Contrast* <https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html>; *1.4.10 Reflow* <https://www.w3.org/WAI/WCAG22/Understanding/reflow.html>; *2.4.11 Focus Not Obscured (Minimum)* <https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html>; *2.5.7 Dragging Movements* <https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html>; *4.1.3 Status Messages* <https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html>
- **Prüfstatus:** Volltext.
- **Zitate:** 1.4.11 (Graphical Objects, Liniendiagramm): „The lines should have 3:1 contrast against their background“. 1.4.10: „320 CSS pixels is equivalent to a starting viewport width of 1280 CSS pixels wide at 400% zoom.“ 2.4.11: „Typical types of content that can overlap focused items are sticky footers, sticky headers, and non-modal dialogs.“ und Technik „C43: Using CSS scroll-padding to un-obscure content“. 2.5.7: „an input beside a slider could allow any user to enter a precise value for the slider.“ 4.1.3: „make users aware of important changes in content that are not given focus“.
- **Kernaussage:** Kurven brauchen 3:1 gegen den Hintergrund (außer die Information steht auch anders bereit, etwa in einer Tabelle); 320 px entsprechen 1280 px bei 400 % Zoom; angeheftete Bereiche dürfen den Fokus nicht verdecken; ein Zahlenfeld neben dem Regler ist eine zulässige Alternative zum Ziehen; Ergebnisänderungen ohne Fokuswechsel ansagen.
- **Anforderung:** siehe Folgerungen F1, F6, F9, F10.
- **Trägt nicht:** Diagramme sind im Text zu 1.4.10 nicht ausdrücklich ausgenommen; ausgenommen sind „images required for understanding (such as maps and diagrams)“. Das Diagramm darf also feste Seitenverhältnisse haben, die Seite drumherum muss umbrechen.

#### Q20 WAI-ARIA APG: Slider

- **Angabe:** W3C WAI. *ARIA Authoring Practices Guide: Slider Pattern.* <https://www.w3.org/WAI/ARIA/apg/patterns/slider/>
- **Fundstelle:** Abschnitte „Keyboard Interaction“, „WAI-ARIA Roles, States, and Properties“.
- **Prüfstatus:** Volltext.
- **Zitate:** „Right Arrow: Increase the value of the slider by one step.“ „Page Up (Optional): Increase the slider value by an amount larger than the step change made by Up Arrow.“ „the aria-valuetext property is set to a string that makes the slider value understandable“. Warnung: „Some users of touch-based assistive technologies may experience difficulty utilizing widgets“.
- **Kernaussage:** Regler: Pfeiltasten ein Schritt, Bild auf/ab größerer Schritt, Pos1/Ende Grenzwerte; Wert als verständlicher Text; Beschriftung über `aria-labelledby`.
- **Anforderung:** `aria-valuetext` mit Einheit und Bedeutung („Milch nach 10 Minuten“, „Milchtemperatur 8 °C“); Bild-Tasten 10 Schritte. Wegen der Warnung zu Touch-Bildschirmlesern: Plus/Minus-Knöpfe und Zahlenfeld zusätzlich.
- **Trägt nicht:** Empfehlung für native Elemente; die steht in Q22.

#### Q21 WAI-ARIA APG: Tabs

- **Angabe:** W3C WAI. *ARIA Authoring Practices Guide: Tabs Pattern.* <https://www.w3.org/WAI/ARIA/apg/patterns/tabs/>
- **Prüfstatus:** Volltext.
- **Zitate:** „Tabs are a set of layered sections of content, known as tab panels, that display one panel of content at a time.“ „It is recommended that tabs activate automatically when they receive focus as long as their associated tab panels are displayed without noticeable latency.“ „The active tab element has the state aria-selected set to true and all other tab elements have it set to false.“
- **Kernaussage:** Reiterleiste mit `tablist`, `tab`, `tabpanel`, `aria-selected`, `aria-controls`, `aria-labelledby`; Tab-Taste springt in die Leiste auf den aktiven Reiter, Pfeiltasten wechseln (umlaufend), Pos1/Ende optional.
- **Anforderung:** genau diese Rollen und Tasten; automatische Aktivierung (die Texte sind statisch, also ohne Verzögerung).
- **Trägt nicht:** ob Reiter für die Inhalte die richtige Form sind; siehe Q34.

#### Q22 ARIA in HTML

- **Angabe:** W3C. *ARIA in HTML.* W3C Recommendation (Fassung REC-html-aria-20260811, 11.08.2026). <https://www.w3.org/TR/html-aria/>
- **Prüfstatus:** Volltext (Tabellenzeile und Abschnitt 1 gelesen).
- **Zitat:** Zeile `input type=range`: implizite Rolle „role=slider“; Abschnitt 1: „NOT RECOMMENDED for authors to set the ARIA role and aria-* attributes to values that match“ (die impliziten Werte).
- **Kernaussage:** Ein natives Schieberegler-Element hat die Rolle `slider` schon eingebaut; doppelte ARIA-Angaben sind nicht empfohlen.
- **Anforderung:** Regler als `<input type="range">` mit `<label>`, nicht als selbst gebautes `div` mit ARIA; nur `aria-valuetext` ergänzen.

#### Q23 W3C WAI Images Tutorial: Complex Images

- **Angabe:** W3C WAI. *Images Tutorial: Complex Images.* <https://www.w3.org/WAI/tutorials/images/complex/>
- **Prüfstatus:** Volltext.
- **Zitat:** „In these cases, a two-part text alternative is required.“ und „The second part is the long description“.
- **Kernaussage:** Diagramme brauchen eine kurze Beschreibung (was ist es) und eine lange (welche Information zeigt es); die lange kann aus Überschriften, Text und Tabelle in `<figcaption>` bestehen.
- **Anforderung:** `<figure>` mit dem SVG (kurzer Name über `<title>`), darunter eine Kurzbeschreibung, die sich mit den Reglern ändert („Tasse 2 ist nach 30 min um 1,4 K kühler“), und eine aufklappbare Wertetabelle.
- **Trägt nicht:** ein Beispiel für Liniendiagramme (das Tutorial zeigt ein Säulendiagramm).

#### Q24 Watson (2017)

- **Angabe:** Watson, L. (2017, 09.09.). *Accessible SVG line graphs.* tink.uk. <https://tink.uk/accessible-svg-line-graphs/>
- **Prüfstatus:** Volltext.
- **Zitate:** „The solution is to use the technique for creating accessible SVG tables as your starting point.“ „The state of SVG accessibility support in browsers and screen readers is still highly inconsistent“.
- **Kernaussage:** Ein SVG-Liniendiagramm lässt sich mit ARIA-Tabellenrollen lesbar machen, die Unterstützung ist aber uneinheitlich; eine Tabellenansicht der Daten zusätzlich ist ratsam.
- **Anforderung:** Im SVG nur `role="img"` mit Namen und Kurzbeschreibung; die Daten als echte HTML-Tabelle außerhalb des SVG (robuster als ARIA im SVG). Achsenbeschriftungen und Gitter im SVG für Bildschirmleser ausblenden (`aria-hidden="true"`).
- **Trägt nicht:** den heutigen Stand der Unterstützung (Stand 2017).

#### Q25 MDN: prefers-reduced-motion

- **Angabe:** MDN Web Docs. *prefers-reduced-motion.* <https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion>
- **Prüfstatus:** Volltext.
- **Zitat:** „Such animations can trigger discomfort for those with vestibular motion disorders.“ Browserstand: „Widely available“ seit Januar 2020.
- **Anforderung:** Bei `reduce` keine Übergänge der Kurven, kein Abspielen der Abkühlung als Film; Endzustand sofort zeigen. Ein „Abspielen“-Knopf (falls gebaut) startet nie von selbst.

### B6 Handy und Laptop im Seminarraum

#### Q26 Sana, Weston und Cepeda (2013)

- **Angabe:** Sana, F., Weston, T. und Cepeda, N. J. (2013). Laptop multitasking hinders classroom learning for both users and nearby peers. *Computers and Education*, 62, 24-31. <https://doi.org/10.1016/j.compedu.2012.10.003>
- **Fundstelle:** S. 27 (Versuch 1), S. 29 (Versuch 2), S. 30 (Empfehlungen).
- **Prüfstatus:** Volltext (offen zugängliche Fassung, CC BY-NC-ND).
- **Zitate:** S. 27: „participants who multitasked scored 11% lower on a post-lecture comprehension test“. S. 29: „Those in view of a multitasking peer scored 17% lower on a post-lecture comprehension test“. S. 30: „A ban on laptops is extreme and unwarranted.“ und „This could include incorporating the laptop into real-time classroom exercises.“
- **Kernaussage:** Fachfremde Nebentätigkeit am Laptop während einer Vorlesung senkt das Verständnis bei Nutzern und bei Sitznachbarn; die Autoren raten nicht zum Verbot, sondern zu Geräteeinsatz in Übungen während der Veranstaltung.
- **Anforderung:** Das Gerät dient einer festen Aufgabe: Fragen stehen auf der Seite, keine Links nach außen in der Simulationsansicht, keine Benachrichtigungen oder Pop-ups; die TL gibt Anfang und Ende vor (10 bis 15 Minuten).
- **Trägt nicht:** Smartphones, Paararbeit und gezielte Aufgaben wurden nicht untersucht (simulierte Vorlesung, Laptops, 40 und 38 Studierende).

#### Q27 Sung, Chang und Liu (2016)

- **Angabe:** Sung, Y.-T., Chang, K.-E. und Liu, T.-C. (2016). The effects of integrating mobile devices with teaching and learning on students' learning performance: A meta-analysis and research synthesis. *Computers and Education*, 94, 252-275. <https://doi.org/10.1016/j.compedu.2015.11.008>
- **Fundstelle:** Abstract (Hochschulbibliographie NTNU, <https://scholar.lib.ntnu.edu.tw/en/publications/the-effects-of-integrating-mobile-devices-with-teaching-and-learn-2/>).
- **Prüfstatus:** Abstract.
- **Zitat:** „moderate mean effect size of 0.523 for the application of mobile devices to education“.
- **Kernaussage:** Über 110 Studien (1993 bis 2013) hinweg haben in den Unterricht eingebundene mobile Geräte einen mittleren positiven Effekt auf Lernleistung.
- **Anforderung:** Handy-Nutzung bewusst einplanen (die Seite ist für 390 px gebaut, nicht nur „auch lauffähig“).
- **Trägt nicht:** Simulationen im Besonderen; Laptops, PDAs und Handys sind gemischt; Moderatoren nicht gelesen.

#### Q28 Apple Human Interface Guidelines: Accessibility

- **Angabe:** Apple. *Human Interface Guidelines: Accessibility.* <https://developer.apple.com/design/human-interface-guidelines/accessibility> (gelesen über die Datenfassung der Seite, abgerufen 04.11.2026).
- **Fundstelle:** Abschnitt „Mobility“, Tabelle der Bedienelementgrößen; Abschnitt „Vision“, Schriftgrößen.
- **Prüfstatus:** Volltext.
- **Zitat:** „Strive to meet the recommended minimum control size for each platform to ensure controls and menus are comfortable for all when tapping and clicking.“ Tabelle: iOS, iPadOS „Default control size“ 44x44 pt, „Minimum control size“ 28x28 pt. „Consider spacing between controls as important as size.“ Schrift iOS: Standard 17 pt, Minimum 11 pt.
- **Kernaussage:** 44 mal 44 pt ist die Standardgröße, 28 mal 28 pt die Untergrenze; Abstand zählt so viel wie Größe.
- **Anforderung:** Knöpfe, Reiter und Reglerknöpfe mit Trefferfläche 44 mal 44 CSS-px (meine Annahme: mit `width=device-width` entspricht in Safari auf iOS 1 CSS-px etwa 1 pt); Fließtext 17 px am Handy.
- **Trägt nicht:** „44 pt als Mindestmaß“: Apple nennt 44 pt als Standard, nicht als Minimum. Gilt für Apps, nicht für Webseiten.

#### Q29 Android Developers: Make apps more accessible

- **Angabe:** Google. *Make apps more accessible.* Android Developers. <https://developer.android.com/guide/topics/ui/accessibility/apps>
- **Fundstelle:** Abschnitt „Use large, simple controls“.
- **Prüfstatus:** Volltext. (Material Design selbst, m3.material.io, war für das Abrufwerkzeug nicht lesbar.)
- **Zitat:** „we recommend that each interactive UI element have a focusable area, or touch target size, of at least 48dpx48dp. Larger is even better.“
- **Anforderung:** bestätigt 44 bis 48 px als Zielgröße für Touch.
- **Trägt nicht:** Webseiten; die Angabe gilt für Android-Apps.

#### Q30 Hoober (2013)

- **Angabe:** Hoober, S. (2013, 18.02.). How Do Users Really Hold Mobile Devices? *UXmatters.* <https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php>
- **Prüfstatus:** Volltext.
- **Zitat:** „made 1,333 observations of people using mobile devices“; „Users change the way they're holding their phone very often“. (Die Prozentzahlen stehen dort mit Gedankenstrich und werden hier umschrieben: von 780 Personen, die den Bildschirm berührten, hielten 49 % das Gerät einhändig, 36 % in einer Hand mit Bedienung durch die andere, 15 % mit beiden Händen.)
- **Kernaussage:** Fast die Hälfte bedient einhändig, aber der Griff wechselt oft.
- **Anforderung:** Wichtige Bedienelemente (Regler, Plus/Minus, „Weiter“) über die ganze Breite erreichbar und groß; nichts, das nur in einer Bildschirmecke liegt; keine Gesten mit zwei Fingern.
- **Trägt nicht:** eine „Daumenzone“ als Karte (nicht gesehen); Seminarraum (beobachtet wurde im Alltag); Stand 2013.

#### Q31 Coyier (2021)

- **Angabe:** Coyier, C. (2021, 04.05.). 16px or Larger Text Prevents iOS Form Zoom. *CSS-Tricks.* <https://css-tricks.com/16px-or-larger-text-prevents-ios-form-zoom/>
- **Prüfstatus:** Volltext; für das iOS-Verhalten Sekundärquelle (der Artikel nennt keine Apple-Quelle, er stützt sich auf einen Hinweis von J. W. Comeau).
- **Zitat:** „as soon as the font-size is 15px or less, the viewport will zoom into that input.“
- **Anforderung:** Alle Eingabefelder (Messwerte, Zahlenfelder der Regler) mit Schriftgröße mindestens 16 px; Zoom nicht per `maximum-scale` oder `user-scalable=no` sperren (das widerspräche 1.4.4).
- **Trägt nicht:** offizielle Zusage von Apple; das Verhalten kann sich ändern.

#### Q32 MDN: inputmode

- **Angabe:** MDN Web Docs. *inputmode.* <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode>
- **Prüfstatus:** Volltext.
- **Zitat:** `decimal`: „Fractional numeric input keyboard containing the digits and decimal separator for the user's locale (typically . or ,).“
- **Anforderung:** Zahlenfelder `inputmode="decimal"`; das Programm akzeptiert Komma und Punkt (deutsche Tastatur zeigt das Komma).

#### Q33 Laakso (2020)

- **Angabe:** Laakso, H. (2020, 24.02.). Why the GOV.UK Design System team changed the input type for numbers. *GOV.UK Technology Blog.* <https://technology.blog.gov.uk/2020/02/24/why-the-gov-uk-design-system-team-changed-the-input-type-for-numbers/>
- **Prüfstatus:** Volltext.
- **Zitat:** „Users can accidentally increase or decrease the number using the scroll wheel“.
- **Kernaussage:** `type="number"` hat Bedienprobleme (Mausrad ändert Werte, stilles Verwerfen von Eingaben, Spracheingabe); besser Textfeld mit `inputmode`.
- **Anforderung:** Zahlenfelder als `type="text"` mit `inputmode="decimal"`, eigene Prüfung mit sichtbarer Fehlermeldung (z. B. „Bitte eine Zahl zwischen 0 und 100 °C“).
- **Trägt nicht:** Dezimalzahlen (der Beitrag behandelt ganze Zahlen, `numeric`).

#### Q34 Sunwall (2024): Tabs, Used Right

- **Angabe:** Sunwall, E. (2024, 02.08.; geprüft 02.09.2026). Tabs, Used Right. *Nielsen Norman Group.* <https://www.nngroup.com/articles/tabs-used-right/> (Neufassung eines Beitrags von J. Nielsen, 2007).
- **Prüfstatus:** Volltext.
- **Zitate:** „When users don’t need to simultaneously see information presented under different tabs.“ (Bedingung für Reiter). „Tab labels should usually be 1-2 words.“ „The fewer tabs, the better.“ „When the number of tabs overflows the tab list, the tab bar often becomes a carousel.“ „Accordions are particularly useful on mobile devices, where they work better than tabs due to the limited screen space.“ „Use at least two selection indicators to enhance the visual salience of the selected tab.“
- **Kernaussage:** Reiter nur für Inhalte, die nicht gleichzeitig gebraucht werden; wenige, kurze Beschriftungen; am Handy eher Akkordeon; gewählten Reiter doppelt kennzeichnen.
- **Anforderung:** Neun Reiter passen bei 390 px nicht in eine Zeile. Empfehlung: am Laptop Reiterleiste, am Handy (unter 600 px) dieselben Abschnitte als Akkordeon; oder die Reiter bündeln (z. B. „Probier aus“, „Ergebnisse lesen“, „Versuche“, „Parameter“, „Modell“ mit den vier Modell-Abschnitten darin). Die Fragen („Probier aus“) sind beim Arbeiten ständig nötig: nicht in einem Reiter verstecken, sondern direkt unter der Simulation zeigen.
- **Trägt nicht:** Lernwirkung; Usability-Erfahrung, keine Studie.

#### Q35 Harley (2015): Slider Design

- **Angabe:** Harley, A. (2015, 13.09.). Slider Design: Rules of Thumb. *Nielsen Norman Group.* <https://www.nngroup.com/articles/gui-slider-controls/>
- **Prüfstatus:** Volltext.
- **Zitate:** „Sliders work best when the specific value does not matter to the user, but an approximate value is good enough.“ „whenever the exact value matters, sliders are not okay.“
- **Anforderung:** In den Fragen kommen genaue Werte vor („Milch nach 10 min“): Regler mit fachlicher Schrittweite (Zeit 1 min, Temperatur 1 K, Menge 5 ml), Plus/Minus je ein Schritt und Zahlenfeld. Aktueller Wert als Text neben dem Reglernamen, nicht unter dem Finger.
- **Trägt nicht:** die Kombination Regler plus Zahlenfeld (der Artikel empfiehlt sie nicht ausdrücklich; Q19 zu 2.5.7 tut es).

#### Q36 Nielsen (1993, ergänzt 2014): Response Times

- **Angabe:** Nielsen, J. (1993, ergänzt 2014). Response Times: The 3 Important Limits. *Nielsen Norman Group.* <https://www.nngroup.com/articles/response-times-3-important-limits/>
- **Prüfstatus:** Volltext.
- **Zitat:** „0.1 second is about the limit for having the user feel that the system is reacting instantaneously,“
- **Anforderung:** Kurven und Rechenwerte innerhalb 100 ms nach jeder Reglerbewegung neu gezeichnet (auf einem Mittelklasse-Handy prüfen); sonst Rechnung vereinfachen oder während des Ziehens nur Kurven, nach dem Loslassen auch Tabelle und Statusmeldung.
- **Trägt nicht:** Lernwirkung.

## C. Farbprüfung

**Methode.** Skript `simulation/recherche/r2_kontrast.py` (Python 3, numpy). Kontrast nach der WCAG-Formel (relative Luminanz mit Schwelle 0,04045, Q18). Simulation der Farbsehschwäche mit den Matrizen von Machado et al. (Q17, Schweregrad 1,0), angewandt auf linearisierte sRGB-Werte. Farbabstand CIEDE2000 (Delta E 00) und Helligkeitsabstand Delta L* in CIELAB (D65). Selbsttest im Skript: Schwarz auf Weiß 21:1, #767676 auf Weiß 4,54:1, #777777 auf Weiß 4,48:1, CIEDE2000-Prüfpaar 2,0425 (bestanden). Faustregel für Linien (meine, keine Norm): Delta E 00 ab 20 gut, 10 bis 20 nur mit Linienart, unter 10 verwechselbar.

### C1 Kontrast der heutigen Farben

| Rolle | Farbe | gegen #ffffff | gegen #f6f5f2 | Urteil |
|---|---|---|---|---|
| Tasse 1 | #8b5a2b | 5,84:1 | 5,36:1 | Text und Grafik in Ordnung |
| Tasse 2 | #222222 | 15,91:1 | 14,59:1 | in Ordnung |
| Becher 3 | #4a7fb0 | 4,24:1 | 3,89:1 | als Linie in Ordnung (3:1), als Beschriftung zu hell (unter 4,5:1) |
| Akzent | #1f4e9e | 7,95:1 | 7,29:1 | in Ordnung |
| Grau-Text | #5f5f5a | 6,42:1 | 5,89:1 | in Ordnung |
| Rot | #b03a2e | 6,02:1 | 5,52:1 | in Ordnung |
| Raumlinie | #9a9993 | 2,86:1 | 2,62:1 | **zu hell**, verfehlt 3:1 (1.4.11) |

### C2 Unterscheidbarkeit der heutigen Farben (Delta E 00, in Klammern Delta L*)

| Paar | normal | Protanopie | Deuteranopie | Tritanopie |
|---|---|---|---|---|
| Tasse 1 / Tasse 2 | 30,7 (29,5) | 27,5 (26,7) | 31,0 (31,2) | 31,2 (29,3) |
| Tasse 1 / Becher 3 | 39,9 (8,8) | 42,4 (14,0) | 43,5 (5,6) | 46,2 (9,7) |
| Tasse 2 / Becher 3 | 35,7 (38,3) | 37,3 (40,7) | 34,9 (36,8) | 37,9 (39,0) |
| Tasse 1 / Raumlinie | 28,2 (20,4) | 28,2 (23,1) | 25,1 (18,8) | 29,0 (20,6) |
| Becher 3 / Raumlinie | 25,0 (11,6) | 23,2 (9,1) | 26,3 (13,2) | 25,8 (10,9) |
| **Tasse 1 / Rot** | 18,0 (0,8) | **5,7 (4,8)** | **1,5 (1,3)** | 11,0 (0,7) |
| Becher 3 / Akzent | 17,1 (17,2) | 16,9 (16,7) | 16,0 (17,1) | 15,2 (14,9) |

**Befund.** Die heutige Palette ist im Kern gut: Tasse 1, Tasse 2 und Becher 3 unterscheiden sich bei jeder simulierten Farbsehschwäche deutlich, weil sie sich in der Helligkeit unterscheiden (Okabe und Ito: keine Farben gleicher Helligkeit). Zwei Mängel: (1) Die Raumlinie verfehlt 3:1. (2) Rot #b03a2e und Tasse 1 #8b5a2b fallen bei Deuteranopie zusammen (Delta E 00 = 1,5) und bei Protanopie fast (5,7). Wo Rot im Diagramm neben Tasse 1 vorkommt (z. B. Markierung oder Warnung), ist es für Betroffene nicht von Tasse 1 zu unterscheiden. Dazu: Becher 3 ist als Beschriftungsfarbe zu hell.

**Gegenprobe.** Eine auf 4,5:1 abgedunkelte Okabe-Ito-Palette (#a64b00, #0067a6, #007a5a) erfüllt alle Kontraste, ist aber schlechter: Die drei Farben haben fast dieselbe Helligkeit (Delta L* 1 bis 3), Tasse 2 und Becher 3 fallen bei Tritanopie zusammen (7,5), Becher 3 und Raumlinie bei Deuteranopie (4,1). Nicht empfohlen.

### C3 Vorschlag (kleinste Änderung)

| Rolle | heute | Vorschlag | gegen #ffffff | gegen #f6f5f2 | Linienart |
|---|---|---|---|---|---|
| Tasse 1 (Milch sofort) | #8b5a2b | #8b5a2b (bleibt) | 5,84:1 | 5,36:1 | durchgezogen, 3 px |
| Tasse 2 (Milch später) | #222222 | #222222 (bleibt) | 15,91:1 | 14,59:1 | gestrichelt, 3 px |
| Becher 3 | #4a7fb0 | **#3d70a3** | 5,19:1 | 4,76:1 | strichpunktiert, 2,5 px |
| Raumlinie | #9a9993 | **#8a8984** (Beschriftung in #5f5f5a) | 3,50:1 | 3,21:1 | gepunktet, 1,5 px |
| Rot im Diagramm | #b03a2e | **im Diagramm vermeiden**; Markierungen (Schnittpunkt, größter Unterschied) in #222222 mit eigener Form und Zahl; falls eine Signalfarbe nötig ist: **#a0306a** (Purpurrot), immer mit Form und Text; #b03a2e nur außerhalb des Diagramms, immer mit Text | 6,72:1 | 6,16:1 | |
| Akzent (Knöpfe, Fokus) | #1f4e9e | #1f4e9e (bleibt) | 7,95:1 | 7,29:1 | nicht im Diagramm verwenden |
| Grau-Text | #5f5f5a | #5f5f5a (bleibt) | 6,42:1 | 5,89:1 | |

Unterscheidbarkeit des Vorschlags (Delta E 00, Reihenfolge normal / Protanopie / Deuteranopie / Tritanopie): Tasse 1 / Tasse 2: 30,7 / 27,5 / 31,0 / 31,2; Tasse 1 / Becher 3: 39,3 / 41,5 / 43,7 / 44,2; Tasse 2 / Becher 3: 31,4 / 32,9 / 30,9 / 33,4; Tasse 1 / Raumlinie: 24,7 / 23,8 / 21,7 / 25,5; Becher 3 / Raumlinie: 25,1 / 23,3 / 26,5 / 25,0. Alle vier Linienrollen liegen damit bei jeder simulierten Farbsehschwäche über 20. Purpurrot: gegen Tasse 1 35,1 / 35,1 / 23,1 / 9,3 (Rot-Grün-Problem behoben), aber gegen Tasse 2 31,6 / 19,7 / 21,8 / 32,0 und gegen Becher 3 38,0 / 14,3 / 17,7 / 59,5. Mit nur zwei Wahrnehmungsachsen bei Dichromasie (Helligkeit, Blau-Gelb) gibt es neben vier Linienfarben keine fünfte, die sich von allen sicher abhebt; deshalb Markierungen über Form und Text, nicht über Farbe. Becher 3 und Akzent liegen bei 10 bis 12, deshalb Akzent nicht im Diagramm. Alle Werte stehen in der Skriptausgabe.

## D. Folgerungen für das Werkzeug

Prüfbare Anforderungen mit Zahlenwert. Stärke: **stark** = Norm oder Volltext mit klarer Aussage; **mittel** = Volltext, aber Übertrag nötig; **schwach** = meine Festlegung oder nur Abstract.

| Nr. | Anforderung (prüfbar) | Belege | Stärke |
|---|---|---|---|
| F1 | Alle Texte, auch Kurvenbeschriftungen, Achsen und Rechenwerte, haben gegen ihren Hintergrund (#ffffff und #f6f5f2) mindestens 4,5:1; Kurven, Messpunkte, Raumlinie, Reglerspur, Reglerknopf und Fokusring mindestens 3:1. Prüfung mit `r2_kontrast.py` für jede Farbe der Seite. | Q18 (1.4.3, 1.4.11), Q19 | stark |
| F2 | Keine Information nur über Farbe: Tasse 1 durchgezogen, Tasse 2 gestrichelt, Becher 3 strichpunktiert, Raumlinie gepunktet; Messpunkte Kreis, Quadrat, Dreieck. Prüfung: Ausdruck in Graustufen, alle Kurven benennbar. | Q18 (1.4.1), Q15, Q16 | stark |
| F3 | Palette nach C3: Becher 3 #3d70a3, Raumlinie #8a8984, kein Rot #b03a2e im Diagramm, Akzent nicht im Diagramm, Markierungen über Form und Zahl. Die vier Linienrollen (Tasse 1, Tasse 2, Becher 3, Raumlinie) haben paarweise bei simulierter Protanopie, Deuteranopie und Tritanopie Delta E 00 mindestens 20, Tasse 1 gegen Tasse 2 Delta L* mindestens 20. | eigene Rechnung (C), Q15, Q17 | mittel (Schwellen sind Faustregel) |
| F4 | Direkte Beschriftung: Kurvennamen am rechten Kurvenende (höchstens 3 Wörter), bei Überlappung versetzt mit Führungslinie; keine separate Farblegende für die Kurven; Schnittpunkt und größter Unterschied markiert und mit Zahl beschriftet. | Q15, Q12, Q4 (Signalisierung d = 0,69; räumliche Nähe d = 0,82), Q11 | mittel |
| F5 | Trefferfläche jedes Bedienelements (Knöpfe, Reiter, Kontrollkästchen, Reglerknopf, Plus/Minus) mindestens 44 mal 44 CSS-px; keine unter 24 mal 24 CSS-px (Pflicht); sichtbarer Abstand zwischen benachbarten Zielen. | Q18 (2.5.8 Pflicht, 2.5.5 Ziel), Q28, Q29 | stark für 24 px, mittel für 44 px |
| F6 | Jeder Regler: natives `input type="range"` mit sichtbarem `<label>`, Wert mit Einheit als Text daneben, `aria-valuetext` mit Bedeutung, fachliche Schrittweite (Zeit 1 min, Temperaturen 1 K, Menge 5 ml), Plus/Minus-Knöpfe (je ein Schritt) und Zahlenfeld (`type="text"`, `inputmode="decimal"`, Komma und Punkt erlaubt). Tastatur: Pfeile ein Schritt, Bild auf/ab 10 Schritte, Pos1/Ende Grenzen. Kein Wert nur durch Ziehen erreichbar. | Q18 (2.1.1, 2.5.7, 4.1.2), Q19 (2.5.7), Q20, Q22, Q32, Q33, Q35 | stark |
| F7 | Alle Eingabefelder mit Schriftgröße mindestens 16 px; Fließtext am Handy 17 px; Zoom nie gesperrt (`user-scalable` nicht auf `no`, kein `maximum-scale`); bei 200 % Textgröße nichts abgeschnitten. | Q31, Q28, Q18 (1.4.4) | mittel (iOS-Verhalten nur Sekundärquelle) |
| F8 | Bei 320 CSS-px Breite kein waagrechtes Scrollen der Seite; Diagramm skaliert über `viewBox` auf volle Breite; Reihenfolge am Handy: Diagramm, Knöpfe als Zeile, aktuelle Frage, Regler, Rechenwerte. Prüfung bei 320, 390 und 1366 px. | Q18 (1.4.10), Q19 | stark |
| F9 | Wenn das Diagramm am Handy angeheftet bleibt: höchstens 45 % der Bildschirmhöhe, nur im Hochformat (im Querformat bei Höhe unter 500 px nicht anheften), `scroll-padding-top` gleich der Höhe des angehefteten Bilds; kein fokussierter Regler wird ganz verdeckt. | Q18 (2.4.11), Q19 (C43) | stark für „nicht verdeckt“, schwach für 45 % und 500 px |
| F10 | Ein Bereich mit `role="status"` sagt nach dem Loslassen eines Reglers die Kernzahlen in einem Satz an (Endtemperaturen, Unterschied, Zeitpunkt), ohne den Fokus zu verschieben; nicht bei jedem Zwischenschritt des Ziehens. | Q18 (4.1.3), Q19 | stark |
| F11 | Diagramm als `<figure>`: SVG mit `role="img"` und Namen, Kurzbeschreibung, die sich mit den Werten ändert, und aufklappbare HTML-Wertetabelle (Zeit in 5-min-Schritten; Spalten Tasse 1, Tasse 2, Raum, eingetragene Messwerte); Gitter und Achsenzahlen im SVG mit `aria-hidden`. | Q18 (1.1.1), Q23, Q24, Q19 (1.4.11: Tabelle als andere Form) | stark |
| F12 | Sichtbarer Fokus an jedem Element: Rahmen 2 px durchgehend in #1f4e9e mit 2 px Abstand, mindestens 3:1 gegen die Nachbarfarben; nie `outline: none` ohne Ersatz. | Q18 (2.4.7, 1.4.11, 2.4.13) | stark |
| F13 | Kurven und Rechenwerte folgen dem Regler innerhalb 100 ms (auf einem Mittelklasse-Handy gemessen); keine selbst startenden Animationen; bei `prefers-reduced-motion: reduce` keine Übergänge. | Q36, Q4 (zeitliche Nähe d = 1,31, Übertrag), Q25, Q18 (2.3.3) | mittel |
| F14 | Freischaltung in drei Stufen: zuerst nur der Regler zur Vorab-Frage (Zeitpunkt der Milchzugabe), dann höchstens 3 weitere Regler je Stufe; Knopf „Alle Regler zeigen“; vor der ersten Frage eine Lesehilfe zum Diagramm (höchstens 3 Sätze, Achsen, Raumtemperatur, Sprung bei Milchzugabe); Fragen einzeln mit „Weiter“. | Q8 (S. 277, 279), Q4 (Vortraining d = 0,78; Segmentierung d = 0,67; Kohärenz d = 0,86), Q2 | mittel (Reihenfolge), schwach (Zahl 3) |
| F15 | Erklärtexte: am Laptop Reiterleiste nach APG (Rollen `tablist`/`tab`/`tabpanel`, Pfeiltasten, automatische Aktivierung, gewählter Reiter mit zwei Merkmalen), Beschriftungen 1 bis 2 Wörter; unter 600 px Breite dieselben Abschnitte als Akkordeon oder höchstens so viele Reiter, wie in eine Zeile passen. Die Fragen stehen nicht in einem Reiter, sondern direkt unter der Simulation; in der Simulationsansicht keine Links nach außen. | Q21, Q34, Q26, Q4 (räumliche Nähe) | mittel |

Zusatz zu den Darstellungen (ohne eigene Nummer, schwach): Zeitzeiger im Diagramm koppelt die Rechenwerte an einen Zeitpunkt (Q2); Energie, falls gezeigt, als zwei Säulen auf gemeinsamer Nulllinie statt als Fläche (Q13, Q14).

## E. Gestrichen oder nur eingeschränkt

- **Plass, Homer und Hayward (2009), Moreno und Mayer (2007), Shah und Hoeffner (2002):** nicht im Text gelesen (Anmeldung oder 403, kein Abstract in Crossref). Sie tragen keine Anforderung. Die Übertragung der Multimedia-Prinzipien auf eine interaktive Simulation ist meine Folgerung aus Q4 und Q8, kein Beleg.
- **Ainsworth (2006):** nur über den Workshop-Beitrag von 2002 (Q2). Im Konzept Q2 zitieren oder Ainsworth 2006 als „Rahmen, beschrieben in Ainsworth und Van Labeke 2002“ kennzeichnen.
- **Franconeri et al. (2021):** nur Abstract; keine Einzelempfehlung (direkte Beschriftung, Farben) daraus ableiten.
- **Cleveland und McGill (1984):** nur über Heer und Bostock (2010). Relevant nur für die Frage Säulen gegen Flächen bei der Energie.
- **Effektstärken nach Mayer:** aus Lehrbotschaften (Erklärungen mit Bildern), nicht aus Simulationen zum Ausprobieren; nicht als erwarteter Effekt des Werkzeugs nennen. Modalitätsprinzip (gesprochener Text) entfällt im Seminarraum.
- **Zahl der Regler:** keine Quelle nennt eine Höchstzahl. „Höchstens 3 neue Regler je Stufe“ ist eine Festlegung; „7 plus minus 2“ ist nicht geprüft und gestrichen.
- **Apple „44 pt Mindestmaß“:** Apple nennt 44 mal 44 pt als Standardgröße, 28 mal 28 pt als Minimum, und das für Apps. Für die Seite gilt verbindlich nur WCAG 2.5.8 (24 px); 44 px ist Ziel (2.5.5 ist AAA).
- **Material Design 48 dp:** Seite m3.material.io nicht lesbar; ersetzt durch die Android-Entwicklerdokumentation (Q29), gleiche Zahl.
- **iOS-Zoom unter 16 px:** keine Apple-Dokumentation gefunden; nur CSS-Tricks (Q31). Als Vorsichtsregel behalten, Stärke mittel.
- **Sana et al. (2013):** Laptops in einer simulierten Vorlesung mit fachfremder Nebentätigkeit; Smartphones und Paararbeit mit gezielter Aufgabe nicht untersucht. Trägt „Ablenkung vermeiden, Aufgabe vorgeben“, nicht „Handy schadet“.
- **Sung et al. (2016):** nur Abstract; Moderatoren (z. B. Gerätetyp, Fach) nicht gelesen.
- **Hoober (2013):** Alltagsbeobachtung, kein Seminarraum; keine Daumenzonen-Karte verwendet.
- **Dyna-Linking:** Q37 fand keinen signifikanten Unterschied; Verknüpfung der Darstellungen schlank halten.
- **Farbprüfung:** Machado-Matrizen linear angewandt (Seite sagt nichts dazu); Schwellen für Delta E 00 sind Faustregeln; dünne Linien wirken weniger farbig als Flächen, deshalb Linienart immer zusätzlich.
- **Zustand in der Adresse, Druckansicht:** keine Quelle geprüft. Als „kann“ möglich (Teilen eines Zustands durch die TL, Neuladen ohne Verlust), aber ohne Beleg; nicht in die Muss-Anforderungen.
- **Reiter gegen lange Seite:** Nur Usability-Erfahrung (Q34), keine Lernstudie. Die Entscheidung Reiter oder Akkordeon am Handy ist eine Gestaltungsfrage für die TL.
