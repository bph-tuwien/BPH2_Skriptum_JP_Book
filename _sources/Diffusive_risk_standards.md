# Methoden zur Risikonanalyse bei diffusiven Wärme- und Feuchtetransport

## Risikoanalyse mittels  Temperaturfaktor $f_{R_{Si}}$

Um einschätzen zu können, ob sich bei üblicher Wohnungsnutzung Schimmelpilze an einer Bauteiloberfläche bilden, hat sich
der sogenannte Temperaturfaktor $f_{R_{Si}}$ als sinnvolle Kenngröße für die Planung bewährt. Dieser kann auch bei rein
thermischen Simulationen, was zur Beurteilung von Wärmebrücken manchmal ausreichend ist, zur Bewertung herangezogen
werden.

### Anforderungen

Der Temperaturfaktor ergibt sich aus der Bedingung, dass an einer Oberfläche eine bestimmte Oberflächentemperatur
gewährleistet werden muss {eq}`nu_min_eq`,

$$ T_{O,i} > T_{O,i, min} $$ (nu_min_eq)

um kritische Feuchtigkeitszustände und deren Folgen (z.B. Schimmelbildung, Kondensation etc.)
hintanzuhalten. Der $f_{R_{Si}}$ berechnet sich zu

$$ f_{R_{Si}} = \frac{T_{O,i} - T_{e}}{T_{i} - T_{e}} $$

und der Bemessungstemperaturfaktor $ f_{R_{Si, min}} $ zu

$$ f_{R_{Si, min}} = \frac{T_{O,i, min} - T_{e}}{T_{i} - T_{e}} $$

Somit ist für alle Konstruktionen nachzuweisen, dass

$$ f_{R_{Si}} > f_{R_{Si, min}} $$

auf der gesamten Innenoberfläche (auch an Ecken und Kanten) gilt.

```{tip}
Kondensation tritt auf, wenn an einer Oberfläche eine relative Luftfeuchtigkeit von 100 % erreicht wird (auch kurzfristig).
Das [Risiko für Schimmelbefall](Mould_Index) besteht, wenn über mehrere Tage die Oberflächenfeuchte über 80 % liegt.
```

{numref}`frsi_3d` zeigt die Ergebnisse einer 3D-Simulation für den $ f_{R_{Si}}$ für einen Bauteilanschluss über Eck.

```{figure} img/Wärmebrücke/frsi_3d.png
---
height: 500px
name: frsi_3d
---
Ecken stellen die kritischen Punkte dar. Im Fall einer vollständigen Wärmedämmung an der Außenseite werden
alle Bereiche unkritischer. Im Fall einer Innendämmung werden die Anschlüsse kritischer, während sich das Risiko
an der Fläche deutlich minimiert.
```

```{note}
**Für Wohnungen mit Klimaannahmen gemäß ÖNORM B 8110-2:2020 gilt:**

$$f_{R_{Si}} > 0.71 $$
```

## Abhängigkeit der Wärmeleitung von der relativen Luftfeuchtigkeit

Einer der materialtechnischen Gründe für die Notwendigkeit der gekoppelten Betrachtung von Feuchte- und
Wärmetransportprozessen bei der Beurteilung von Bauteilen, liegt in der **Feuchteabhängigkeit der Wärmeleitfähigkeit von
Baustoffen**.

Wenn poröse Baustoffe Feuchtigkeit aufnehmen, füllen sich die zuvor mit Luft gefüllten Kapillaren mit dieser. Im
Bauwesen ist das zumeist Wasser. Wasser hat im Vergleich zu Luft eine mehr als 20-mal höhere Wärmeleitfähigkeit. Die nun
gefüllten Kapillaren transportieren Wärme nun zu Folge der Leitfähigkeit des Wasser und nicht mehr der Luft. Dadurch
ergibt sich bei steigenden Wassergehalt in Summee ein höherer Wert für die Wärmeleitfähigkeit des Baustoffes.

```{note}
**Wasser hat im Vergleich zu Luft eine mehr als 20-mal höhere Wärmeleitfähigkeit.**

$\lambda_{Wasser} \approx 0.5562 \gg \lambda_{Luft} \approx 0.0262$ W/mK

```

Dieser Zusammenhang kann einerseits durch Messungen bestimmt werden, andererseits gibt es für bestimmte Anwendungsfälle
mathematische Modelle um die Wärmeleitfähigkeit vorherzusagen z.B. {cite}`taoukilMoistureContentInfluence2013` oder auch
{cite}`chaudharyHeatTransferThreephase1968`.

Für die bauphysikalische Praxis hat sich die Formulierung in ÖNORM EN 10456 bewährt:

$$ \lambda(\psi) = \lambda_{Bemessungswert} \cdot e^{f_{\psi} \cdot \psi} $$ (lambda_psi_eq)

### Beinflussung des Wärmestroms durch Feuchtezustände

Laut ÖNORM B 8110-2:2020 muss diese Beeinflussung des Wärmestroms durch Feuchtezustände auch nachgewiesen werden. Dabei
gilt, dass die **Erhöhung des mittleren Wärmestroms $\leq 10\ \%$** betragen muss. Um diesen Nachweis zu führen, kann
folgendermaßen vorgegangen werden:

Die Wärmeleitfähigkeit bei erhöhtem Feuchtigkeitsgehalt in W/mK berechnet sich zu

$$ \lambda(\psi) = \lambda_{Bemessungswert} \cdot e^{f_{\psi} \cdot \psi} $$ (lambda_psi_eq)

wobei $\psi$ für den volumenbezogenen Feuchtigkeitsgehalt in m³/m³ steht und definiert ist als

$$ \psi = \frac{u}{\rho_{Wasser} \cdot d}$$ (psi_eq)

In Gleichung {eq}`lambda_psi_eq` und {eq}`psi_eq` steht $\lambda_{Bemessungswert}$ für den Bemessungswert der
Wärmeleitfähigkeit in W/mK, $f_{\psi}$ für den volumenbezogenen Feuchteumrechnungskoeffizienten $u$ für die
Kondensatmente in kg/m², $\rho_{Wasser}$ für die Rohdichte des Wassers in kg/m³ und $d$ für die betrachtete Schichtdicke
in m.

Der Nachweis der Beeinflussung der Wärmeleitfähigkeit wird bei Bauteilen, welche durch andere Nachweisführungen als
tauglich eingestuft werden, zumeist nicht schlagend werden. Nachfolgendes Beispiel, soll das veranschaulichen.

#### Beispiel: Verringerung des Wärmedurchlasswiderstandes zu Folge des ausgefallenen Kondensats für die vorgegebene Schicht.

In {numref}`psi_ex` sei ein verfeinfachtes diskretisiertes Modell eines Flachdachaufbaues dargestellt für den die
Verringerung der Wärmedurchlasswiderstandes nachgewiesen werden soll.

```{figure} img/Wärmebrücke/psi_ex.png
---
height: 350px
name: psi_ex
---
Vereinfacht diskretisierter Flachdachaufbau.
```

Die aufgetretene Kondensatmenge ist bewusst knapp unter dem Grenzwert der möglichen Feuchteanreicherung ($gc \leq 0.5$
kg/m²) durch Kondensation laut ÖNORM B 8110-2:2020 gewählt.

**Angabe:**

Kondensatmenge für den betrachteten Aufbau $ u = 440 \frac{g}{m^{2}} $

Bemessungswert der Leitfähigkeit der Schicht $ \lambda_{Bemessungswert} = 0.04 \frac{W}{mK} $

Schichtdicke $d = 0.04 m$

Wärmedurchlasswiderstand des Bauteils $R = 5 \frac{m^{2} K}{W}$

$f_{\psi}$ kann ÖNORM EN ISO 10456: 2010: Tabelle 4 entnommen werden:

```{figure} img/Wärmebrücke/f_psi_tab4.png
---
height: 300px
name: f_psi_tab4
---
Auszug aus ÖNORM EN ISO 10456: 2010: Tabelle 4 zur Bestimmung von $f_{\psi}$ verschiedener Materialien.
```

Einsetzen in Gleichung {eq}`lambda_psi_eq` und {eq}`psi_eq` führt auf:

$$ \psi = \frac{u}{\rho_{Wasser} \cdot d} = \frac{0.44}{1000 \cdot 0.04} = 0.011 \frac{m^{3}}{m^{3}}$$

$$ \lambda(0.011) = \lambda_{Bemessungswert} \cdot e^{f_{\psi} \cdot \psi} = 0.04 \cdot e^{4 \cdot 0.011} = 0.042
\frac{W}{mK}$$

$$ \Delta R = \frac{d}{\lambda(0.011)} - \frac{d}{\lambda_{Bemessungswert}} = \frac{0.04}{0.042} - \frac{0.04}{0.04} =
0.048 \frac{m^{2}K}{W} $$

10 % des Wärmedurchlasswiderstandes vom Bauteil wären $ 0.1 \cdot R = 0.5 \frac{m^{2}K}{W}$

Und somit führt der Nachweis auf

$$ 0.048 \ll 0.5 \frac{m^{2}K}{W} $$

```{tip}
Obwohl die gewählte Kondensatmenge nur knapp unter dem normativ möglichen Grenzwer liegt, beträgt die Erhöhung der
Wärmeleitfähigkeit durch Feuchteanreicherung weniger als 1%. Somit liegt der Schluss nahe, dass in den meisten Fällen, 
andere Grenzwerte überschritten werden, bevor der Nachweis der Erhöhung des Wärmestromes schlagend wird.
```
