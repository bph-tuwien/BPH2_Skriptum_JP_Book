# Methoden der Nachweisführung und Risikonanalyse bei Berücksichtigung des konvektiven Wärme- und Feuchtetransports

Die Nachweisführung bei Berücksichtigung des konvektiven Wärme- und Feuchtetransports ist in Österreich nach ÖNORM
8110-2:2020 zu führen. Wenn man aus dem Katalog der nachweisfreien Konstruktionen herausgefallen ist, gilt es entweder
den Nachweis nach

- [Abschnitt 10: Nachweis der Vermeidung schadensverursachender Kondensation bei der Anwendung des Bemessungsklimas](Abschnitt_10)
  oder nach
- [Abschnitt 11: Vereinfachter Nachweis der Vermeidung schadensverursachender Kondensation im Inneren von Bauteilen](Abschnitt_11)

zu führen.

```{figure} img/Konvektion/nw_konstr_10_11.png
---
height: 350px
name: nw_konstr_10_11
---
Ausschnitt aus dem Katalog der nachweisfreien Konstruktionen aus ÖNORM 8110-2:2020. Beispiel für einen Aufbau bei dem, 
bei nicht-erfüllung der Anforderungen, ein Nachweis nach Abschnitt 10 oder 11 gestattet ist.
```

```{figure} img/Konvektion/nw_konstr_10.png
---
height: 350px
name: nw_konstr_10
---
Ausschnitt aus dem Katalog der nachweisfreien Konstruktionen aus ÖNORM 8110-2:2020. Beispiel für einen Aufbau bei dem, 
bei nicht-erfüllung der Anforderungen, ein Nachweis nur nach Abschnitt 10 gestattet ist.
```

Die Methode zur Nachweisführung nach

- **Abschnitt 10** ist die **hygrothermische Simulation**, wobei die Nachweisführung nach

- **Abschnitt 11** mit Hilfe des **"Euro-Glaser-Verfahrens"** erfolgt.

Folgende Unterkapitel sollen Erklärungen und Hilfestellungen zur Interpretation, Verwendung und essenziellen Ergänzungen
der Norm in Bezug auf die Nachweisführung bieten.

[//]: # (```{note})

[//]: # (Die Wahl der konstruktionsabhängig erlaubten Nachweisverfahren ergbt sich einerseits aus der Fehlertoleranz der )

[//]: # (Konstrukltion)

[//]: # (andererseits aus der Validität der Ergebnisse der beiden Verfahren für die zu bewertende Konstruktion.)

[//]: # (```)

```{tip}
Die Nachweisverfahren stützen sich immer auf EN ISO Standards, werden jedoch national um essenzielle Inhalte ergänzt und 
widersprechen sich dadurch manchmal.
```

(Abschnitt_10)=

### Abschnitt 10: Nachweis der Vermeidung schadensverursachender Kondensation bei der Anwendung des Bemessungsklimas -> hygrothermische Simulation

Der Nachweis mittels hygrothermischer Simulation stützt sich auf EN ISO 15026 und wird mittels Annahmen und Ergänzungen
innerhalb der ÖNORM 8110-2:2020 erweitert. Die Ergänzungen auf nationaler Ebene haben gegenüber der europäischen Norm
vorrang und müssen eingehalten werden.

**Die wichtigsten Ergänzungen sind:**

(luft_norm)=

- Ein- und Ausströmung von Luft in Hohlräume von Konstruktionen ist bei der Berechnung des Feuchtehaushaltes zu
  berücksichtigen.
- Berechnung ist für die kritischen Bereiche einer Konstruktion und in geeigneter Dimensionalität durchzuführen.

**Kriterien zur Beurteilung:**

- Einstellung eines eingeschwungenen Zustandes
    - Veränderung d. Feuchteanreicherung $leq$ 1% im Vergleich zum Vorjahr
- Ermittlung von Risikos:
    - Risiko Schimmelpilzwachstums
    - Risiko Eisbildung
    - Risiko Verrottung (organ. Materialien)
- Beeinflussung d. Wärmestroms durch Feuchtezustände
    - Erhöhung d. mittleren Wärmestroms <= 10%

(Abschnitt_11)=

### Abschnitt 11: Vereinfachter Nachweis der Vermeidung schadensverursachender Kondensation im Inneren von Bauteilen -> Modifizierter Euro-Glaser

Der Nachweis mittels "Modifiziertem Euro-Glaser-Verfahrens" stützt sich auf EN ISO 13788 und wird mittels Annahmen und
Ergänzungen innerhalb der ÖNORM 8110-2:2020 erweitert. Das "Euro-Glaser-Verfahren" ist ein erweitertes Glaserverfahren
welches konvektive Transportphänome berücksichtigt.

Dieses vereinfachte Verfahren berücksichtig laut EN ISO 13788 nicht:

- Schwankungen der Materialeigenschaften in Abhängigkeit vom Feuchtegehalt
- kapilalre Saugwirkung und Transport von Feuchte in der flüssigen Phase in Baustoffen
- <del>Luftbewegung aus dem Gebäudeinneren in das Bauteil durch Spalten oder in
  Lufträumen</del> [siehe Eränzung](ergaenzung_11)
- hygroskopisches Verhalten von Baustoffen

(ergaenzung_11)=

**Die wichtigsten Ergänzungen sind:**

- Bei Konstruktionen mit Lufthohlräumen (z. B. Holzrahmenbauwände, Holzbalkendecken) ist anstatt der Diffusionsgleichung
  die Diffusions-/Konvektionsgleichung für Wärme- bzw. Feuchtetransport zu verwenden

Die Diffusions-/Konvektionsgleichungen sind eine auf die Flussdichte bezogene Darstellung unserer im vorherigen Kapitel
[hergeleiteten Lösung](analy_konv) für die konvektiven Transportgleichungen.

$$ q = c \cdot \dot{m}_{Luft} \cdot \left(T_{1} + \frac{T_{1} - T_{2}}{e^{P_{H}} - 1}\right)$$

und

$$ g' = \frac{0.622}{p_{0}} \cdot \dot {m}_{Luft} \cdot \left(p_{1} + \frac{p_{1} - p_{2}}{e^{P_{M}} - 1}\right)$$

Wobei $e^{P_{H}}$ und $e^{P_{M}}$ die modifizierte Peclet-Zahl für den Fall des Wärme- bzw. Feuchtetransports
darstellen:

$$P_{H} = \frac{c \cdot \dot{m}_{Luft}}{\frac{\lambda}{d}}$$

$$P_{M} = \frac{{m}_{Luft} \cdot 0.622 / p_{0}}{\delta_{0}/(\mu \cdot d)}$$

**Kriterien zur Beurteilung:**

- Ohne Anfangsfeuchte
    - Kondensat im Bauteil muss unter $g_{c} < 0.5$ kg/m² liegen
    - Vollständige Austrocknung der in der kühlen Jahreszeit aufgetretenen Feuchte im **1. Sommer**
- Mit Anfangsfeuchte
    - Kondensat im Bauteil muss unter $g_{c} < 0.5$ kg/m² liegen
    - Vollständige Austrocknung der in der kühlen Jahreszeit aufgetretenen Feuchte im **2. Sommer**

### Modifizierter Euro-Glaser

Das Modifizierte Euro-Glaser-Verfahren wurde als solches erstmals in {cite}`nusserEuroGlaserUnterBeachtung2010`
präsentiert:

> Im Zuge der Untersuchungen wurden 50 Einfamilienhäuser hinsichtlich der Anzahl ihrer Elektro- und
> Heizung/Klima/Sanitärinstallationen hin ausgewertet. Mit Hilfe der Verallgemeinerung des Luftvolumenstroms durch diese
> Leckagen auf den Luftvolumenstrom durch ein nicht abgeklebtes Elektrokabel wird eine Volumenstromgleichung hergeleitet
> und vier Luftdichtheitsklassen definiert.

Um den erhöhten Wärme- und Feuchtetransport zu Folge von Leckagen zu berücksichtigen wird für durchströmbare Schichten
die Diffusion-/Konvekitonsgleichung angewendet. {numref}`euro_schichten`

```{figure} img/Konvektion/euro_schichten.png
---
height: 250px
name: euro_schichten
---
Definition der Schichten in denen Diffusion und Diffusion + Konvektion angesetzt wird.
```

Dabei wird auch gezeigt, dass die Berechnungen für den betrachteten Fall auf der sicheren Seite liegen und das Verfahren
für konservative Abschätzungen eine gute erste Näherung darstellt. {numref}`eruoglas_sichere`

```{figure} img/Konvektion/eruoglas_sichere.png
---
height: 400px
name: eruoglas_sichere
---
Euro-Glaser liegt auf der sicheren Seite
```

(Anfangsfeuchte)=

## Berücksichtigung von Anfangsfeuchten bei Verwendung des Euro-Glasers laut 8110-2:2020

Die Berechnung des Bauteiles mit Anfangsfeuchte, ermöglicht es die Toleranz der Konstruktion gegenüber eingedrungenem
Wasser zu bewerten.

Dabei wird ein Feuchtezuschlag von 0.25 kg/m² angesetzt, wenn Konstruktionsteile aus biogenen Werkstoffen zwischen
Schichten liegen deren $s_{d}$-Wert $\geq$ 0.5 m ist. Dieser Feuchtezuschlag wird in der Mitte zwischen den sperrenden
Schichten verortet und für den Monat, wo zuvor das maximale Kondensat aufgetreten ist, angesetzt.

Vorgehensweise:

- Berechnung der Konstruktion ohne Anfangsfeuchte
- Ermittlung des Monats mit maximalem Kondensat
- Ansetzen des Feuchtezuschlages in dem ermittelten Monat
- Ermittlung des Kondesats mit Anfangsfeuchte

(LPF)=

## Berücksichtigung von Leckagen laut 8110-2:2020

Um die [normative Vorgabe bzgl. des Einflusses von Luftströmungen](luft_norm) zu berücksichtigen, kann beispielsweise
ein Luftpfade innerhalb einer Konstruktion definiert werden. Die dafür relevanten Parameter können dem Abschnit 9.2
Strömungswiderstand von Bauteilen entnommen werden.

Entscheidend dabei ist Tabelle 3, welche den Luftvolumenstromkoeffizienten und dessen Wahlkriterien vorgibt:

```{figure} img/Konvektion/luftvolstrom_koeff_tab.png
---
height: 200px
name: luftvolstrom_koeff_tab
---
Tabelle 3 zur Definition des Luftvolumenstromkoeffzienten C.
```

```{tip}
Um auf der sicheren Seite zu liegen, kann Zeile 3 als ungünstigster Fall gewählt werden.
```

(Mould_Index)=

## Mould Index

Zur Bewertung und Analyse der Simulationsergebnisse in Bezug auf Schimmelpilzbildung auf Oberflächen, kann das
VTT-Modell {cite}`ojanenClassificationMaterialSensitivity2011` herangezogen werden. In
{cite}`sarkanyHygrothermischenBauteilsimulationZur` wird eine Zusammenfassung der Entwicklung und des theorethischen
Hintegrundes dieses Modelles gegeben. Nachfolgende Ausführungen werden als direktes Zitat von {cite:
t}`sarkanyHygrothermischenBauteilsimulationZur2019` übernommen.

```{note}
Es wurden im direkten Zitat die Referenzen {cite}`hukkaMathematicalModelMould1999` und {cite}`ojanenClassificationMaterialSensitivity2011` mit den identen Referenzen in diesem Werk ersetzt um die
weiterführende Selbstrecherche bei Bedarf zu vereinfachen.
```

### Mould Index nach Viitanen, Ojanen und Peuhkuri et. al.

Das mathematische Modell für die Simulation des Verrottungsverhaltens von Materialien und die Einstufung des sichtbaren
Schimmelpilzbefalles, in weiterer Folge als Mould Index bezeichnet, wurde erstmals für Materialien aus Holz in
{cite}`hukkaMathematicalModelMould1999`
gezeigt und im Zuge weiterer Forschung verfeinert bis es mit {cite}`ojanenClassificationMaterialSensitivity2011` möglich
war auch das Verhalten anderer Materialien unter zu Hilfenahme diese

Die approbierte gedruckte Originalversion dieser Diplomarbeit ist an der TU Wien Bibliothek verfügbar. The approved
original version of this thesis is available in print at TU Wien Bibliothek. 34 3 Grundlagen Modelles zu beschreiben. In
weiterer Folge wird ein Überblick über die dem Mould Index zu Grunde liegenden Berechnungsverfahren und den
experimentellen Randbedingungen zur Evaluation dieser nach {cite}`hukkaMathematicalModelMould1999` dargelegt.

#### Experimentelle Randbedingungen

Das experimentelle Material bestand aus kleinen Proben mit den Abmessungen 7x15x50 mm. Herangezogen wurden die
Materialien Kiefer und Fichte, wobei nochmals unterschiedliche Oberflächenqualitäten, ofengetrocknet und sägerauh,
betrachtet wurden. {cite}`hukkaMathematicalModelMould1999` Die Veröffentlichung der Ergebnisse findet man in [26], [25]
und [24]. In den Experimenten werden folgende Vorbedingungen in {cite}`hukkaMathematicalModelMould1999` vorausgesetzt:

• Die Proben erreichen die Ausgleichsfeuchte ohne Verzögerung. Die Größe der Versuchsstücke ist demnach als
vernachlässigbar klein zu betrachten und auch die Verzögerung zur Herstellung des Feuchtegleichgewichtes in den
Holzzellen zu Folge der relativen Luftfeuchte der Umgebung.

• Das Schimmelpilzwachstum findet nur an der Oberfläche der Materialien statt. Die Modellierung kommt demnach für die
Eingabedaten mit der Oberflächentemperatur und dem Feuchtegehalt aus.

• Der Schimmelpilz an der Materialoberfläche beeinflusst nicht das Verhalten des Materials gegenüber Feuchteeinflüsse,
wie z.B. Absorptionsverhalten, etc.

Die Beurteilung des Schimmelpilzwachstums erfolgte auf Grundlage eines existierenden StandardIndexes der etwas angepasst
wurde, basierend auf dem visuell feststellbaren Ausmaßes des Wachstums. {cite}`hukkaMathematicalModelMould1999`

"[0] no growth 1 some growth detected only with microscopy 2 moderate growth detected with microscopy (coverage more
than 10%)
3 some growth detected visually 4 visually detected coverage more than 10% 5 visually detected coverage more than 50% 6
visually detected coverage 100%"

Für das mathematische Modell ist diese Skala nicht auf ganzzahlige Werte beschränkt.
{cite}`hukkaMathematicalModelMould1999`

#### Modell Entwicklung

**Günstige Gegebenheiten zum Einsetzen des Schimmelpilzwachstums**

Der Feuchtigkeitsgehalt von Holz ist abhängig von der Umgebungsfeuchte, der Temperatur, der Expositionszeit, den
Abmessungen und des Absorptionspotentials. Des Weiteren kann Wasser auch in der Form von freien Wasser in den Hohlräumen
oder gebunden in den Zellwänden auftreten.[5][8][21] Als hygroskopisches Material ist die Gleichgewichtsfeuchte leicht
beeinflussbar durch die Umgebungsfeuchte. Bei geringem Feuchtegehalt ist das Wasserpotential eine Möglichkeit die
Wasserverfügbarkeit zu beschreiben. Sie wird als die freie Energie des Wassers in einem System relativ zu der Energie
eines Referenz Pools aus purem Wasser definiert.[19] Die Wasseraktivität aw ist ein Maß um die Verfügbarkeit von Wasser
zu beschreiben. Sie ist definiert als Verhältnis aus dem Wasserdampfpartialdruck p und dem Sättigungsdampfdruck p0 eines
Systems. {cite}`hukkaMathematicalModelMould1999` [29] [10]

```{figure} img/Konvektion/mould_math.png
---
height: 350px
name: mould_math
---
Mathematischer Zusammenhang günstiger Gegebenheiten zum Einsetzen des Schimmelpilzwachstums für Materialien aus Holz. {cite}`hukkaMathematicalModelMould1999`
```

$$ a_{w} := \frac{p}{p_{0}} $$

Man erkennt sofort den Zusammenhang zur relativen Luftfeuchte RH. Der aw-Wert kann somit auch definiert werden als die
relative Luftfeuchte bei der sich die Gleichgewichtsfeuchte einstellt.[29][10]

$$RGF = a_{w}\cdot 100 $$

Die Wasseraktivität in der Umgebungsluft oder in den Hohlräumen des Materials ist kritisch für den aktiven
Schimmelpilzwachstum. Die benötigte Zeitperiode bis zum Einsetzen des Schimmelpilzwachstums und das Wachstum selber ist
großteils reguliert durch die Wasseraktivität, die Temperatur, die Expositionszeit und die Oberflächenqualität der
Materialien. Experimente haben gezeigt, dass mögliche Temperaturen die das Schimmelpilzwachstum fördern sich zwischen
0-50°C befinden und die dazugehörige kritische relative Luftfeuchte eine Funktion der Temperatur ist, wie in Abbildung
3.6 dargestellt. Die Temperaturkurve zwischen 5-40°C aus Abbildung 3.6 kann mit einer polynomialen Funktion nach 3.79
beschrieben werden.

$$ RH_{crit} = \begin{cases}-0.00267\cdot T^3 + 0.160\cdot T^2 - 3.13\cdot T + 100.0&\text{wenn $ T\leq 20 $}\\=
80\%&\text{wenn $ T>20 $}\end{cases}$$

Das Verhalten von RHcrit im höheren Temperaturbereich ist eine Approximation, hat aber für praktische Anwendungen kaum
Auswirkungen. {cite}`hukkaMathematicalModelMould1999`

**Größtmögliches Schimmelpilzwachstum**

Es ist bekannt, dass das eingeleitete Schimmelpilzwachstum nicht unbedingt zu visuell erkennbaren Schimmel führt. [25]
Des Weiteren ist das maximal mögliche Schimmelpilzwachstum nach oben hin auch begrenzt unabhängig von Zeit und
bestmöglichen Konditionen. können nach 3.79 für die untere Schranke Mmax = 1 bei zugehöriger relativer RH unabhängig von
der Zeit und für die obere Schranke Mmax = 6 bei 100% relativer Luftfeuchtigkeit angegeben werden. Wobei bei Mmax = 6,
in einem Temperaturbereich von 0-50°C, die gesamte Oberfläche irgendwann von Schimmel bedeckt sein wird. Zwischen diesen
beiden Fixpunkten besagen Experimente, dass der Mould Index eine parabolische Funktion, nach 3.80, annimmt.
{cite}`hukkaMathematicalModelMould1999`

```{figure} img/Konvektion/mould_temp.png
---
height: 250px
name: mould_temp
---
Temperaturabhängige kritische relative Luftfeuchtigkeit benötigt für Schimmelpilzwachstum für verschiedene Werte des Mould Index. {cite}`hukkaMathematicalModelMould1999`
```

$$ M_{max} = 1 + 7\cdot \frac{RH_{crit} - RH}{RH_{crit} - 100} - 2\cdot \left(\frac{RH_{crit} - RH}{RH_{crit} -
100}\right)^2$$

Somit kann nach 3.80 interpretiert werden, dass RHcrit nicht nur von der Temperatur sondern auch vom Mould Index selber
abhängig ist. Zu dieser Erkenntnis kann man kommen, wenn man 3.80 nach RH löst, womit nun ein Zusammenhang zwischen
einem für ein Mmax benötigtes temperaturabhängiges RH hergestellt werden kann. 3.7
{cite}`hukkaMathematicalModelMould1999`

**Wachtumsrate bei günstigen Bedingungen**

Das hier vorgestellte mathematische Modell bildet das Wachstum des Schimmelpilzes nicht in den Zellen der Versuchskörper
ab, da die Proben nur visuell überprüft wurden. Des Weiteren kommt es bei der Berechnung nicht zu einer genauen
Abbildung der während der Studie beobachteten Veränderungen des Schimmelpilzbefalles der Oberfläche. Somit ist der Mould
Index als ein mögliches Maß an Aktivität des Schimmelpilzes an der Holzoberfläche zu interpretieren.
{cite}`hukkaMathematicalModelMould1999` Als Grundlage des Wachstums Modelles stellt Viitanen in [24] die
Regressionsgleichung nach 3.81 vor und beschreibt damit die Zeit (in Wochen) die benötigt wird, um bei konstanter
Temperatur und Feuchtebedingungen das Schimmelpilzwachstum in Gang zu setzen. {cite}`hukkaMathematicalModelMould1999`

$$t_{m} = \exp(-0.68\cdot \ln T - 13.9\cdot \ln RH + 0.14\cdot W - 0.33\cdot SQ + 66.02) $$

Für einen linearen Zusammenhang der Steigerung des Mould Index mit der Zeit, wobei die Zeit in Tagen gemessen wird,
ergibt sich nach 3.81 ein anderer Zusammenhang der Form:

$$ \frac{dM}{dt} = \frac{1}{7\cdot \exp (-0.68\cdot \ln T - 13.9\cdot \ln RH + 0.14\cdot W - 0.33\cdot SQ + 66.02)}$$

wobei M < 1 ist.

Mit Hilfe von 3.82 wird die Anwendbarkeit von 3.81 erweitert auf verschiedene Bedingungen, wie zum Beispiel, dass die
relative Luftfeuchtigkeit immer über RHcrit 3.79 liegt, und die Temperatur sich zwischen 0-50 °C befindet. Der lineare
Zusammenhang der hier zu Grunde gelegt wird ist nur eine mathematische Beschreibung der Verhältnisse im Bereich M < 1,
wobei hier auch jedes andere Wachstumsmodell verwendet werden könnte. Ein Mould Index kleiner als eins indiziert kein
Wachstum der Pilze. {cite}`hukkaMathematicalModelMould1999`

Für ein Voranschreiten des Wachstums ist 3.82 nicht mehr gültig. Es kommt ein weiteres in [24] vorgestelltes Modell zur
Anwendung, dass die Zeit beschreibt, die benötigt wird bis das erste Schimmelpilzwachstum M = 3 sichtbar ist.

$$t_{v} = \exp (-0.74\cdot \ln T - 12.72\cdot \ln RH + 0.06\cdot W + 61.50)$$

Während des Wachstums zwischen M = 1 bis M = 3 wird dem Modell eine konstante Wachstumsrate mit konstanten Bedingungen
zu Grunde gelegt. Dieser Umstand kann durch Kombination von 3.81 und 3.83 beschrieben werden. Wird von 3.82 ausgegangen
liefert die Kombination der vorher erwähnten Gleichungen einen Korrektur-Koeffizienten k1 in der Form von 3.84.

$$k_{1} = \begin{cases}1&\text{wenn $ M<1 $}\\\frac{2}{t_{v}/t_{m}-1}&\text{wenn $ M>1 $}\end{cases}$$

Obwohl 3.84 sich auf konstante Bedingungen bezieht haben Experimente gezeigt, dass der Korrekturkoeffizient auch für
fluktuierende Bedingungen gilt, so lange diese vorteilhaft für das Wachstum sind. Somit kann gesagt werden, dass k1 für
die gesamte Bandbreite ab dem Zeitpunkt der Schimmelpilz sichtbar ist, also M > 1, gilt.
{cite}`hukkaMathematicalModelMould1999`

Unter der Annahme, dass die Wachstumsrate sich um 10% bei Annäherung an den oberen Grenzwert 3.80 verlangsamt, kann
dieser Umstand auch durch einen Korrekturkoeffizienten k2 erfasst werden.

$$ k_{2} = 1 - \exp[2.3\cdot (M - M_{max})] $$

Aus 3.82, 3.84 und 3.85 lässt sich das komplette Modell zur Beschreibung des Schimmelpilzwachstums in günstigen
Bedingungen zusammenfassen als 3.86

$$ \frac{dM}{dt} = \frac{1}{7\cdot \exp (-0.68\cdot \ln T - 13.9\cdot \ln RH + 0.14\cdot W - 0.33\cdot SQ + 66.02)}\cdot
k_{1}\cdot k_{2} $$

Als Anfangswert wird üblicherweise M = 0 gesetzt, wenn Holz, dass in einem Ofen der Temperaturen größer 50 °C aufwies,
getrocknet wurde, betrachtet wird. {cite}`hukkaMathematicalModelMould1999`

**Modell bei nicht-günstigen Bedingungen**

Bei fluktuierender Luftfeuchtigkeit kann durch die gesamte Zeit die in hoher Luftfeuchtigkeit verbracht wurde die Zeit
für den Start des Schimmelpilzwachstums zu einem gewissen Grad quantifiziert werden.[24] Diese Vereinfachung führt aber
dazu, dass es zu einer hohen Schimmelpilz-Aktivität bei Wiederholung von Feuchtezyklen kommt. Um dem entgegenzuwirken
wird berücksichtigt, dass während Trockenzeiten das Schimmelpilzwachstums zurückgeht. Es muss nicht unbedingt zu einer
optischen Veränderung des Schimmelpilzbefalles kommen, jedoch konnte festgestellt werden, dass es nach Trockenzeiten zu
einer begrenzten Verzögerung der Wachstumsrate kommt, falls überhaupt ein Einsetzen des Wachstums stattfindet. Danach
ist die Verzögerung wiederum verlängert. Mathematisch kann diese Verzögerung durch die Zeit die seit der Trockenzeit
vergangen ist (t − t1), ausgedrückt werden.

```{figure} img/Konvektion/calc_sim_mould.png
---
height: 350px
name: calc_sim_mould
---
Vergleich des maximal gemessenen und berechneten Mould Index. {cite}`hukkaMathematicalModelMould1999`
```

$$ \frac{dM}{dt} = \begin{cases}-0.032&\text{wenn $ t-t_{1}\leq 6\ h $}\\ 0&\text{wenn $ 6\ h \leq t-t_{1}\leq 24\ h
$}\\-0.016&\text{wenn $ t-t_{1}> 24\ h $}\end{cases}$$

Die experimentellen Ergebnisse für 3.87 decken Trockenzeiten zwischen 6 Stunden und 14 Tagen ab, jedoch stützt sich die
Gleichung nur auf eine kleine Anzahl von Experimenten und ist somit nur zum Teil aussagekräftig. Der Einfluss von
längeren Trockenzeiten und der von Temperaturen unter 0 °C ist noch wenig erforscht, somit ist die Anwendung von 3.87
zwar für solche Situationen möglich, die Ergebnisse sollten aber hinterfragt werden.
{cite}`hukkaMathematicalModelMould1999`

#### Vergleich der Ergebnisse des Modelles mit experimentellen Daten

3.80 stützt sich auf die Ergebnisse eines 12-wöchigen Versuches unter konstanten Bedingungen. Der Vergleich der
maximalen Werte des Mould Index zwischen mathematischen Modell und Experiment ist in 3.8 gegenübergestellt. Es wurden
nur Punkte die eine klare Grenze des Mould Index hatten betrachtet. Der größte Fehlerwert beträgt 1.2 und ist der
einzige Wert über 0.5 liegt. {cite}`hukkaMathematicalModelMould1999`

In Abbildung 3.9 und Abbildung 3.10 wird ein Vergleich der experimentellen zu den simulierten Daten für das Einsetzen
des Schimmelpilzwachstums und die visuelle Feststellbarkeit des Schimmelpilzes für Kiefer-Splintholz dargestellt. Des
Weiteren werden Vergleiche für Fichtenholz in Abbildung 3.11 und Abbildung 3.12 vorgestellt. Die experimentellen
Ergebnisse zeigen den Mittelwert von 6 parallel gemessenen Proben. Man kann erkennen, dass keine großen systematischen
Fehler zu sehen sind und bei den Vergleichen der Zeitdauer bis Schimmelpizlwachstum einsetzt die Fehler kleiner als 25%
sind. Es sind auch einige sehr große Fehlerwerte zu erkennen, wodurch man darauf schließen kann, dass ein Modell mit nur
wenigen numerischen Parametern nicht ausreichend ist um über den gesamten Temperaturbereich und den der relativen
Luftfeuchtigkeit, vor allem bei höheren Temperaturen, Aussagen über das Schimmelpilzwachstum zu treffen.
{cite}`hukkaMathematicalModelMould1999` Abbildung 3.13 zeigt einen Vergleich bei veränderlichen Bedingungen der
Luftfeuchtigkeit. Dabei wurde die relative Luftfeuchtigkeit zwischen 75% und 95% gehalten und ein periodischer Wechsel
beider Luftfeuchtigkeiten zwischen 6 und 196 Stunden durchgeführt. Die Temperatur wurde konstant bei 20 °C gehalten. 80
% der simulierten Punkte weisen einen Fehler des Einsatzzeitpunktes von weniger als 25 % auf. Der durchschnittliche
Fehler in der simulierten Einsatzzeit beträgt 1%, somit kann man darauf schließen, dass das Modell frei von
systematischen Fehlern ist. {cite}`hukkaMathematicalModelMould1999`

```{figure} img/Konvektion/calc_sim_const.png
---
height: 350px
name: calc_sim_const
---
Vergleich der gemessenen und simulierten Zeitdauer um Schimmelpilzwachstum bei Kiefer-Splintholz unter konstanten Bedingungen hervorzurufen. {cite}`hukkaMathematicalModelMould1999`
```

#### Diskussion des vorgestellten Modelles

Da das mathematische Modell in differentieller Form formuliert ist, ermöglicht es die Berechnung von beliebigen
Temperatur- und Feuchtigkeitsgeschichten auch unter Berücksichtigung von Trockenperioden. Die numerischen Werte der
Parameter gelten nur für reines Kiefer- oder Fichtenholz und versuchen die durchschnittliche Materialantwort auf
Grundlage einer kleinen Versuchsprobenmenge nachzubilden. Die Materialantwort unterscheidet sich jedoch zu gleichen
Teilen in den verschiedenen Proben aus verschiedenen Stämmen der gleichen Holzart wie in verschiedenen Proben
verschiedener Holzarten. Somit wird in {cite}`hukkaMathematicalModelMould1999` darauf verwiesen, dass es möglich sein
sollte durch Korrekturkoeffizienten andere Holzarten abzubilden. Diese These wurde mit
{cite}`ojanenClassificationMaterialSensitivity2011` erweitert und ermöglichte die Darstellung des Verrottungsverhaltens
anderer Materialien auf Grundlage des hier vorgestellten Modelles, worauf im weiteren Verlauf dieses Kapitels noch
eingegangen wird. {cite}`hukkaMathematicalModelMould1999`

Die für das Modell durchgeführten Versuche decken Temperaturen zwischen 5 und 40 °C und relative Luftfeuchtigkeiten von
75 bis 100 % ab. Die Expositionszeit bei konstanten Bedingungen betrug mindestens 12 Wochen und bei veränderlichen 6
oder 24 Wochen. Diese Zeitfenster sind wesentlich geringer als die Zeiten die mit Hilfe dieses Modells normalerweise
simuliert werden. Dadurch ist eine Extrapolation der experimentellen Ergebnisse notwendig, wodurch sich eine gewisse
Unsicherheit bei Betrachtung solcher Situation durch das Modell ergibt. Gerade die Versuche unter veränderlichen
Bedingungen bedürfen einer Revision, da die numerische Lösung in 3.87 noch nicht zufriedenstellend ist.
{cite}`hukkaMathematicalModelMould1999`

Mmax in 3.80 wurde aus Ergebnissen unter konstanten Bedingungen für die Luftfeuchtigkeit abgeleitet. Es ist bekannt,
dass dieser Parameter unter veränderlichen Bedingungen geringer ist, jedoch gibt es bisher keine Aussagen über einen
genauen Wert. Das Modell kann in diesen Bereichen also noch verfeinert werden. Dasselbe gilt auch für Bedingungen mit
veränderlicher Temperatur und konstanter relativer Luftfeuchtigkeit. {cite}`hukkaMathematicalModelMould1999`

```{figure} img/Konvektion/calc_sim_visual.png
---
height: 350px
name: calc_sim_visual
---
Vergleich der gemessenen und simulierten Zeitdauer um Schimmelpilzwachstum bei Kiefer-Splintholz unter konstanten Bedingungen visuell feststellen zu können. {cite}`hukkaMathematicalModelMould1999`
```

```{figure} img/Konvektion/calc_sim_const_pine.png
---
height: 350px
name: calc_sim_const_pine
---
Vergleich der gemessenen und simulierten Zeitdauer um Schimmelpilzwachstum bei Fichte-Splintholz unter konstanten Bedingungen hervorzurufen. {cite}`hukkaMathematicalModelMould1999`
```

```{figure} img/Konvektion/calc_sim_const_pine_vis.png
---
height: 350px
name: calc_sim_const_pine_vis
---
Vergleich der gemessenen und simulierten Zeitdauer um Schimmelpilzwachstum bei Fichte-Splintholz unter konstanten Bedingungen visuell feststellen zu können. {cite}`hukkaMathematicalModelMould1999`
```

### Erweiterung des Modelles auf andere Materialien

Aufbauend auf dem eben vorgestellten Modell zur Beurteilung des Schimmelpilzwachstums auf Holzoberflächen
{cite}`hukkaMathematicalModelMould1999` wurde das Modell zur Berechnung anderer Materialien erweitert und die
Entwicklungen in {cite}`ojanenClassificationMaterialSensitivity2011` zusammengefasst. Hier wird ein Überblick der
Ergebnisse aus {cite}`ojanenClassificationMaterialSensitivity2011` gegeben.

```{figure} img/Konvektion/mould_surf_qual.png
---
height: 350px
name: mould_surf_qual
---
Vergleich der gemessenen und simulierten Zeitdauer um Schimmelpilzwachstum bei Kiefer-Splintholz unter veränderlichen 
Bedingungen der Luftfeuchte hervorzurufen. Oberflächenqualität SQ steht für ofengetrocknete SQ = 1 und 
sägerauhe SQ = 0 Oberflächen.  {cite}`hukkaMathematicalModelMould1999`
```

#### Experimentelle Forschung zur Verbesserung des Modelles

Im Zuge eines groß angelegten dreijährigen Forschungsprojektes am VTT (Technical Research Centre of Finland) und am
Tampere University of Technology wurden statische und dynamische Laborversuche für eine große Anzahl von häufig
verwendeten Baumaterialien (Fichtenbretter, Beton, Porenbeton, Faserbeton, Polyurethan Dämmung mit Papieroberfläche und
polierter Oberfläche, Glaswolle, Polyester Wolle und expandiertes Polysterol) durchgeführt. Als Referenzmaterial wurde
Kiefer-Splintholz verwendet. {cite}`ojanenClassificationMaterialSensitivity2011`

#### Verbesserung des Modelles für Schimmelpilzwachstum

Die Überlegung bestand darin das schon bestehende Modell durch Adaption der Wachstumsraten verschiedener Materialien zu
erweitern. Dies bedurfte der Einführung von Sensitivitätsklassen um das unterschiedliche Materialverhalten abzubilden.
{cite}`ojanenClassificationMaterialSensitivity2011`

#### Anpassung des Mould Index

Bei der Verwendung weiterer Materialien abseits von Holz wurde festgestellt, dass die vom Schimmelpilz bedeckte Fläche
zwar für das menschliche Auge nicht sichtbar, aber unter dem Mikroskop relativ stark ausgeprägt sein konnte 3.14. Diese
Erkenntnisse führten zu einer Anpassung des Mould Index in den Bereichen M = 3 und M = 4 wie in Tabelle 3.1 zu sehen
ist. {cite}`ojanenClassificationMaterialSensitivity2011`

```{figure} img/Konvektion/pur_pic.png
---
height: 350px
name: pur_pic
---
Schimmel in den Poren von Porenbeton (links) und auf der Papieroberfläche von einem PUR-Dämmstoff (rechts). {cite}`ojanenClassificationMaterialSensitivity2011`
```

```{figure} img/Konvektion/tab_mould.png
---
height: 200px
name: tab_mould
---
Angepasster Mould Index. {cite}`ojanenClassificationMaterialSensitivity2011`
```

#### Bedingungen für das Einsetzen des Schimmelpilzwachstums

Die untere Grenze der relativen Luftfeuchtigkeit für das Wachstum von Schimmelpilzen bei empfindlichen Materialien nach
mehreren Monaten, wie beispielsweise Holz, beträgt 80%. Die durch die große Anzahl an Versuche, vorgeschlagenen Grenzen
der relativen Luftfeuchtigkeit anderer Materialien sind weiterhin Approximationen, korrespondieren aber besser mit der
eigentlichen Materialantwort. Für resistentere Materialien wurde die Grenze auf 85% RH gesetzt.
{cite}`ojanenClassificationMaterialSensitivity2011`

#### Intensität des Schimmelpilzwachstums

Der Parameter zur Klassifizierung der Sensitivität von Materialien ist mittels der Intensität des Schimmelpilzwachstums
möglich. Die Versuche unter konstanten Bedingungen lieferten Daten für verschiedene Materialien. Das
Schimmelpilzwachstum dieser Materialien wurde dann mit dem Referenzmaterial des ursprünglichen Modelles,
Kiefer-Splintholz, verglichen. Dadurch ergaben sich Korrekturkoeffizienten um die Eigenschaften des Referenzmaterials so
anzupassen, dass es möglich war auch andere Materialien zu simulieren. In Abbildung 3.15 werden Kurven für das
Schimmelpilzwachstum verschiedener Materialien unter konstanten Bedingungen dargestellt. Es ist zu erkennen, dass die
Baustoffe ein sehr unterschiedliches Verhalten bzgl. Intensität und Verzögerung des Wachstums und den Maximalwerten des
Mould Index aufweisen. Derselbe Versuch wurde auch bei anderen konstanten Bedingungen durchgeführt. Diese Informationen
konnten dann verwendet werden um das bestehende Modell anzupassen. {cite}`ojanenClassificationMaterialSensitivity2011`

```{figure} img/Konvektion/monitor_mould.png
---
height: 350px
name: monitor_mould
---
Monitoring Geschichte des Mould Index verschiedener Materialien bei konstanten Bedingungen für die Temperatur und Luftfeuchtigkeit (+22°C, 97% RH). {cite}`ojanenClassificationMaterialSensitivity2011`
```

Im ursprünglichen Modell wird die Intensität des Schimmelpilzwachstums beschrieben durch 3.88 zuvor in 3.82 dargelegt.

$$ \frac{dM}{dt} = \frac{1}{7\cdot \exp (-0.68\cdot \ln T - 13.9\cdot \ln RH + 0.14\cdot W - 0.33\cdot SQ + 66.02)}\cdot
k_{1}\cdot k_{2} $$

Darin steht W für die Holzart (0=Kiefer, 1=Fichte), SQ für die Oberflächenqualität (0=sägerauhe Oberfläche,
1=ofengetrocknete Oberfläche), t für die Zeit in Stunden und k1 und k2 sind Koeffizienten zur Beschreibung des
Wachstums. Letzteren beiden Koeffizienten, dabei steht k1 für die Intensität des Schimmelpilzwachstums und k2 für die
Dämpfung des Wachstums bei Annäherung an den maximalen Wert des Mould Indexes, werden am angepassten Modell herangezogen
um das Verhalten unterschiedlicher Materialien zu beschreiben. Da das Referenzmaterial bei der Simulation anderer
Baustoffe Kiefer mit einer sägerauhen Oberfläche ist, sind W = 0 und SQ = 0 zu setzen.
{cite}`ojanenClassificationMaterialSensitivity2011`

Die Versuche führten zu neuen Gleichungen 3.89 und 3.90 für den Intensitätskoeffizienten k1, wobei der Index pine in den
Gleichungen für das Referenzmaterial Kiefer steht.

$$ k_{1} = \frac{t_{M=1,pine}}{t_{M=1}}\ wenn\ M<1 $$

und

$$ k_{1} = 2\cdot \frac{(t_{M=3,pine} - t_{M=1,pine})}{(t_{M=3} - t_{M=1})}\ wenn\ M\geq1 $$

Wobei tM=1 die Zeit beschreibt die benötigt wird bis das Wachstum einsetzt (ergo M = 1 erreicht wird) und tM=3 für die
Zeit steht die benötigt wird um M = 3 zu erreichen. k1 wurde für jedes Material in den Versuchen gelöst, was in
Abbildung 3.16 dargestellt wurde. {cite}`ojanenClassificationMaterialSensitivity2011` Um die Handhabbarkeit dieser neuen
Daten zu gewährleisten, wurden Sensitivitätsklassen im Bezug auf das Schimmelpilzwachstum für die Materialien, in
Tabelle 3.2 zu sehen, eingeführt. Durch die kleine Anzahl der Versuchsproben liegt der Einteilung keine statistische
Auswertung zu Grunde, sondern eine Abschätzung durch die Versuchsergebnisse. Die für k1 bestimmten Werte können 3.17
entnommen werden. {cite}`ojanenClassificationMaterialSensitivity2011`

```{figure} img/Konvektion/k_coeff.png
---
height: 350px
name: k_coeff
---
Intensitätskoeffizient für verschiedene Materialien in den Versuchen. {cite}`ojanenClassificationMaterialSensitivity2011`
```

```{figure} img/Konvektion/sens_class.png
---
height: 100px
name: sens_class
---
Einteilung der unterschiedlichen Materialien in Sensitivitätsklassen. {cite}`ojanenClassificationMaterialSensitivity2011`
```

Um die Dämpfung des Wachstums bei Annäherung an den maximalen Wert des Mould Indexes bei vorherrschenden Bedingungen zu
beschreiben liegt k2 Gleichung 3.91 zu Grunde.

$$ k_{2} = max[1-\exp[2.3\cdot (M - M_{max})],0] $$

Dabei hängt der maximale Mould Index Mmax von den vorherrschenden Bedingungen ab. 3.80 wurde für den Einbezug der neuen
Materialien und ihrer Sensitivitätsklassen nach 3.92 angepasst.

$$ M_{max} = A + B\cdot \frac{RH_{crit} - RH}{RH_{crit} - 100} - C\cdot \left(\frac{RH_{crit} - RH}{RH_{crit} -
100}\right)^2 $$

Hierbei hängen die Koeffizienten A, B und C von den Material Klassen ab und RHcrit ist weiterhin der Wert der relativen
Luftfeuchtigkeit bei der gerade das Schimmelpilzwachstum einsetzt. Somit geht Mmax mit der Berücksichtigung der
Sensitivitätsklassen in k2 ein und hat einen direkten Einfluss auf das Simulationsergebnis.
{cite}`ojanenClassificationMaterialSensitivity2011` Für die Verwendung der eben genannten Faktoren wurden die
Materialien in Sensitivitätsgruppen zusammengefasst die den jeweiligen Koeffizienten bestimmte Werte zuordnen. Eine
Übersicht dieser Zuordnung ist in 3.3 zusammengestellt, diese Parameter lagen auch der Modellstudie zu Grunde.
{cite}`ojanenClassificationMaterialSensitivity2011`

```{figure} img/Konvektion/k_diag.png
---
height: 250px
name: k_diag
---
Einteilung des Intensitätskoeffizienten k1 in vier Sensitivitätsklassen. {cite}`ojanenClassificationMaterialSensitivity2011`
```

```{figure} img/Konvektion/k_tab.png
---
height: 100px
name: k_tab
---
Parameter für die unterschiedlichen Sensitivitätsklassen. {cite}`ojanenClassificationMaterialSensitivity2011`
```

#### Verbesserter Abfall des Mould Index

Es erfolgte auch eine Verbesserung von 3.87 zur Berücksichtigung unvorteilhafter Bedingungen des Schimmelpilzwachstums.
Ermittelt wurde der in 3.93 dargelegte Zusammenhang aus einem zyklischen Wechsel der Feuchtigkeitsbedingungen.
{cite}`ojanenClassificationMaterialSensitivity2011`

$$ \frac{dM}{dt} = \begin{cases}-0.000133&\text{wenn $ t-t_{1}\leq 6\ h $}\\ 0&\text{wenn $ 6\ h \leq t-t_{1}\leq 24\ h
$}\\-0.000667&\text{wenn $ t-t_{1}> 24\ h $}\end{cases} $$

Wobei M den Mould Index und t die Zeit beschreibt, die seit t1 vergangen ist, wo die Bedingungen an der kritischen
Oberfläche ein visuell sichtbares Wachstum ermöglichten. {cite}`ojanenClassificationMaterialSensitivity2011` Der
Rückgang des Wachstums für andere Materialien dM dt mat wird durch Hinzunahme eines Relativitätskoeffizienten Cmat
beschrieben mit dessen Hilfe weiterhin das ursprüngliche Modell für Holz verwendet werden kann.
{cite}`ojanenClassificationMaterialSensitivity2011`

$$ \frac{dM}{dt}_{mat} = C_{mat}\cdot v\frac{dM}{dt}_{0} $$

Die Versuchsergebnisse die der Ermittelung von Cmat zu Grunde liegen sind in Abbildung 3.18 dargestellt.
{cite}`ojanenClassificationMaterialSensitivity2011`

```{figure} img/Konvektion/cmat_mould.png
---
height: 350px
name: cmat_mould
---
Rückgang des Schimmelpilzwachstums Cmat verglichen mit der Oberfläche des Referenzmaterials Kiefer. {cite}`ojanenClassificationMaterialSensitivity2011`
```

```{figure} img/Konvektion/climate_exp_mould.png
---
height: 100px
name: climate_exp_mould
---
Klimatischen Bedingungen für die Versuche. {cite}`ojanenClassificationMaterialSensitivity2011`
```

#### Evaluation des verbesserten Modelles für das Schimmelpilzwachstum

Das angepasste Modell wurde mit den Versuchsergebnissen längerer Versuchsstudien verglichen. Die Versuchsbedingungen die
den Berechnungen zu Grunde gelegt wurden und die Evaluation des mathematischen Modelles sind Abbildung 3.19, 3.20 und
3.21 zu entnehmen. Es wurden bei dem Versuch die Bedingungen an der kritischen Oberfläche zwischen beiden Materialien
gemessen. Um das Schimmelpilzwachstum an der Schnittstelle beider Oberflächen darzustellen wurde eine Mischung aus
Kombinationen zwischen den Sensitivitätsklassen und maximal möglichem Wachstum der Klassen gewählt.
{cite}`ojanenClassificationMaterialSensitivity2011` Es zeigte sich, dass an den Schichtgrenzen das Schimmelpilzwachstum
bei Wahl der sensibleren Sensitivitätsklasse ßensible"besser mit den Versuchsergebnissen korrespondierte. Das maximalen
Maß an Schimmel hängt vom Grundmaterial ab. Der Dämpfungsbeiwert für das Wachstum wurde mit 0.25 gewählt. Es konnte eine
relativ gute Korrelation des verbesserten Modelles gezeigt werden, wo auch in den kälteren Perioden die simulierten
Werte wenig von den gemessenen abweichen. {cite}`ojanenClassificationMaterialSensitivity2011`

```{figure} img/Konvektion/sim_exp_beton.png
---
height: 350px
name: sim_exp_beton
---
Vergleich der im Versuch gemessenen und simulierten Daten mit dem Dämpfungsbeiwert für das Wachstum von 0.25 für die Schichtgrenze zwischen PUR mit Papieroberfläche und Beton. {cite}`ojanenClassificationMaterialSensitivity2011`
```

```{figure} img/Konvektion/sim_exp_pine.png
---
height: 350px
name: sim_exp_pine
---
Vergleich der im Versuch gemessenen und simulierten Daten mit dem Dämpfungsbeiwert für das Wachstum von 0.25 für die Schichtgrenze zwischen Glaswolle und Fichtenbretter. {cite}`ojanenClassificationMaterialSensitivity2011`
```

#### Diskussion der Ergebnisse

Eine Verbesserung des ursprünglich Modelles konnte durch die Möglichkeit der Simulation anderer Materialien erzielt
werden. Dies ist durch eine entsprechende Anpassung der Parameter für die Intensität und die maximalen Werte des
Schimmelpilzwachstums bei Berücksichtigung der jeweiligen Materialien möglich. Es erfolgte auch eine Anpassung der
kritischen Werte der relativen Luftfeuchtigkeit, welche benötigt wird für die Beschreibung des Wachstums und Rückgangs
des Mould Index bei kalten oder trockenen Perioden. Damit ist allgemein eine bessere Aussage über den Einsatz und
Verlauf des Schimmelpilzwachstums auf Materialober- und Grenzflächen zwischen Materialien möglich. Eine weitere
Verbesserung besteht nun in der Auswahl der entsprechenden Sensitivitätsklassen für die verschiedenen Materialien.
{cite}`ojanenClassificationMaterialSensitivity2011`

## Nachweis der Holzverrottung

Zum Nachweis der Holzverrottung kann beispielsweise das Modell von Viitanen {cite}`ModellingDurabilityWooden` oder auch
das in den WTA-Merkbättern beschriebene verwendet werden {cite}`FeuchtetechnischeBewertungHolzbauteilen`. Hier wird das
Modell aus den WTA-Merkblättern vorestellt.

**Für den vereinfachten Nachweis der Verrottung gilt:**

> Die relative Porenluftfeucte im Massivholzprodukt darf 95 % bei 0 °C und 86 % bei 30 °C
> im Tagesmittel nicht überschreiten. {cite}`FeuchtetechnischeBewertungHolzbauteilen`

```{figure} img/Konvektion/verrottung.png
---
height: 350px
name: verrottung
---
Ausschnitt der Darstellung im WTA-Merkblatt für den Nachweis für Verrottung.
```

Eine Auswertung einer hygrothermischen Simulation für den Nachweis eines fehlerhaften Flachdaches mittels diesem
Verfahren ist in {numref}`verrottung_num` zu sehen.

```{figure} img/Konvektion/verrottung_num.png
---
height: 350px
name: verrottung_num
---
Auswertung einer hygrothermischen Simulation für den Nachweis eines fehlerhaften Flachdaches mittels WTA-Merkblatt-
Verfahren für die Verrottung von MAssivholz.
```

## Nachweis der Tragfähigkeit

Zum Nachweis der Tragfähigkeit von Bauteilen aus Holz kann das in den WTA-Merkbättern beschriebene Verfahren verwendet
werden {cite}`FeuchtetechnischeBewertungHolzbauteilen`.

**Für den vereinfachten Nachweis der Tragfähigkeit gilt:**

> Bauteile aus Holz und Holzwerkstoffe werden in Abhängigkeit ihrer Umgebungsbedingungen in Nutzungsklassen gemäß EN
> 1995-1-1 eingestuft. Die Verwendbarkeit der Bauprodukte ist entsprechend dieser Nutzungsklassen sicherzustellen. So darf
> beispielsweise in der Nutzungsklasse 2 die maximale Materialfeuchte (Tagesmittelwert) be Holzwerkstoffen 18 M-% nicht
> übersteigen. Eine vorübergehende Auffeuchtung auf 20 M-% (Holzwerkstoffe) kann im ersten Jahr toleriert werden, sofern
> diese innerhalb von 3 Monaten rücktrocknen kann und die Anforderungen der Gebrauchstauglichkeit erfüllt werden.

Die Massenprozent für ein diskretisierten Element $i$ der Simulaiton lassen sich mittels

$$ M\ \% = \frac{w_{i}}{\rho_{i}} $$

berechnen. Dabei steht $w_{i}$ für den Wassergehalt und $\rho_{i}$ die Dichte in jeweils kg/m³.

```{figure} img/Konvektion/tragf_num.png
---
height: 350px
name: tragf_num
---
Auswertung einer hygrothermischen Simulation für den Nachweis eines fehlerhaften Flachdaches mittels WTA-Merkblatt-
Verfahren für die Tragfähigkeit.
```

```{note}
Die Zusammenfassung der wichtigsten Eckpunkte zum Nachweis Holzverrottung und Tragfähigkeit kann in dem entsprechenden
WTA-Merkblatt {cite}`FeuchtetechnischeBewertungHolzbauteilen` gefunden werden.
```

## Angaben im Bericht

In ÖNORM 8110-2:2020 werden Ihnen inhaltliche Vorgaben bzgl. Ihres technischen Berichtes gemacht die es einzuhalten
gilt:

- Darstellung des zugrunde gelegten Planungsstandes
- Standort
- nachvollziehbare Darstellung des Konzeptes zur Vermeidung schadensverursachender Wasser dampfkondensation im Inneren
  und an der Oberfläche von Bauteilen
- die aus dem Konzept resultierenden Bemessungsklimata für den Innen- und den Außenbereich
- außenseitige, standortbezogene, lokale Randbedingungen (z. B. solare Einstrahlung, langwelliger Strahlungsaustausch
  Beschattung durch Nachbargebäude und/oder Bäume, Photovoltaik-Anlagen, Schlagregen)
- Angaben aus der Gebäudetechnikplanung zu raumlufttechnischen Anlagen und der anzunehmenden Druckdifferenz über die
  Konstruktion
- Darstellung der relevanten technischen Eigenschaften der Konstruktion
- Für den Nachweis der Vermeidung von schadensverursachender Wasserdampfkondensation im Inneren von Bauteilen: —
  Begründung der Wahl des Verfahrens (siehe Abschnitt 8, Abschnitt 10 und Abschnitt 11)
- bei Verfahren nach Abschnitt 10 und Abschnitt 11 Darstellung der Einhaltung der Kriterien
- Nachweis der Vermeidung von schadensverursachender Wasserdampfkondensation an der Oberfläche von Bauteilen:
    - anzuwendender Bemessungstemperaturfaktor
    - Temperaturfaktor des Bauteils