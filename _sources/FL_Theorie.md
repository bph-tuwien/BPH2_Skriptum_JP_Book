(FL_Theorie)=
# Flüssigwassertransport - Theorie
Theoretischer Hintergrund Flüssigwasser.

*Mitschrift VO 01.04.2022:*

## Geschichte

- 1822 Fourier - Ansatz zum Wärmetransport
- 1850 Graham/Fick - Diffusion
- Um 1880 Maxwell Stefan Boltzmann
    Statistische Mechanik/Transporttheorie
- 1856 Darcy - Ansatz zum Flüssigwassertransport 
- 1940-1970 Krischer, Philipp, de Vries, Luikov
       Berechnung von Trocknungsvorgängen
       Bodenkunde – Hydrologie(gesättigte Körper)
- 1958 Glaser H.: Vereinfachte Berechnung der Dampfdiffusion durch geschichtete Wände bei Ausscheidung von Wasser und Eis. 
                  Kältetechnik 10 (1958), H. 11, 358-364 (Teil 1), H. 12, 386-390 (Teil 2).
- 1991-1995 IEA Annex 24
  „Heat, Air and Moisture transport through Insulated Envelopes“
- 1997-2001 WTA-Arbeitsgruppe
  „Simulation wärme- und feuchtetechnischer Prozesse“
- ~ 1985 Kiessl, Häupl, Stopp – Mehrschichtige Baukonstruktionen
- 1990 Rode – Simulationsprogramm MATCH
- 1994 Künzel – Simulationsprogramm WUFI
- 1996 Grunewald – Simulationsprogramm DIM bzw. DELPHIN
- 2000 Bednar – Simulationsprogramm mit Kopplung zum Raum
- 2000-2002 EU-Projekt
  „Heat, Air Moisture Standards Development“
- 2000-2007 CEN TC89 WI29.3 Erarbeitung EN 15206
  „Hygrothermal performance of building components and
  building elements – Assesment of moisture transfer by
  numerical simulation“
- 2003-2007 IEA EBC Annex 41 „Whole building heat air and moisture response“
- 2010-2014 IEA EBC Annex 55 „ Reliability of Energy Efficient Building Retrofitting
  Probability Assessment of Performance & Cost”

"1D Simulation bei einer Sanierung stellt Risiko dar wenn das wahre Problem vergessen wird."


---------------------------------------------------------
## Feuchtetransport und –speicherung

Diffusion können wir gut beschreiben
   
Gleichung für Diffusion hier

$$
g_{v} = - \delta_{p} \cdot \frac{\partial p}{\partial x}
$$ (eq_g_v)

### Feuchtespeicherung

Feuchte kann sich in einem Material in all seinen Aggregatzuständen einlagern:

- Fest $\rightarrow$ Eis
- Flüssig $\rightarrow$ Wasser
- Gasförmig $\rightarrow$ Wasserdampf

Wenn man Baustoffen Wasser in flüssiger Form zuführt, ändert sich der Wassergehalt. Wenn es kalt genug ist findet eine 
Wandlung der Moleküle in Eis statt. Neben flüssigem Wasser haben wir, dort wo noch Luft vorhanden ist, auch Wasserdampf. 
Dieser Wasserdampf ist auch im Gleichgewicht mit dem Wasser selber.



Erklärung der Begriffe: Freie Wassersättigung/Vakuum Sättigung

#### Kapillarkräfte

Die meisten Baustoffoberflächen haben anziehende Kräfte auf Wasser.

```{figure} img/FL_Theorie/gasbeton_mikro.png
---
height: 250px
name: gasbeton_mikro
---
Aufnahme von Gasbeton. Sehr kleine Poren ($\leq$ 1000 $\mu m$) bilden Porennetzwerk in dem Wasser transportiert werden 
kann.
```

Je kleiner die Kapillare desto höher die Steighöhe, weil 
das Volumen klein ist im Verhältnis zur Kraft die entlang dieses Umfangs auftritt. Je größer Kapillardurchmesser, desto 
weniger ist die maximale Steighöhe. Zusammenhang zwischen Porenstruktur und Geschwindigkeit der Flüssigleitung auf Grund 
von vorhandener Saugspannung. {numref}`kapillaren`

```{figure} img/FL_Theorie/kapillaren.png
---
height: 250px
name: kapillaren
---
Je kleiner die Kapillare desto höher die Steighöhe, weil 
das Volumen klein ist im Verhältnis zur Kraft die entlang dieses Umfangs auftritt. 
```

#### Bestimmung des Zusammenhanges zwischen Saugspannung und Wassergehalt - Plattenapparat

Ein Versuch zur Messung des Zusammenhanges zwischen Kraft die auf das Wasser wirkt und wie viel Wasser im Porensystem gehalten werden 
kann. Als Unterlage für die Probe wird eine Keramikplatte verwendet. Diese hat eine sehr feine Porenstruktur und wird 
mit Kaolin beschichtet. Kaolin ist ein feines, eisenfreies, weißes Gestein, auch mit einer feinen Porenstruktur. Auf 
diese Platte wird eine gesättigte Probe gelegt, sodass die Porenstruktur des Baustoffes in die feinere Porenstruktur der Platte 
übergeht. {numref}`plattenapparat`
```{figure} img/FL_Theorie/plattenapparat.png
---
height: 250px
name: plattenapparat
---
Je kleiner die Kapillare desto höher die Steighöhe, weil 
das Volumen klein ist im Verhältnis zur Kraft die entlang dieses Umfangs auftritt. 
```
Es wird nun schrittweise der Luftdruck über der Probe erhöht, was zu einer graduellen Entleerung der jeweiligen Poren 
führt, je nachdem wann der Luftdruck die Saugspannung in der Pore überschreitet. {numref}`druck_pore_versuch`

```{figure} img/FL_Theorie/druck_pore_versuch.png
---
height: 250px
name: druck_pore_versuch
---
Schematische Darstellung des zeitlichen Verlaufs eines Versuchs im Plattenapparat. Entleerung der Poren wenn 
$ P_{suc} < P_{Luft} $. 
```

Minisken verhindern, dass es luftundicht wird, dadurch kann der Druck aufrechterhalten werden, doch das Wasser kann 
abrinnen.

**Versuchsablauf:**

- Erhöhung des Drucks
- Warten bis sich für die jeweilige Stufe ein Gleichgewicht eingestellt hat. (es rinnt kein Wasser mehr ab)
- Wiegen der Probe
- Wiederholen bis die Probe trocken ist.

Dieser Vorgang, abhängig von der Probe, kann zum Teil bis zu einem Monat dauern. Als Ergebnis erhält man die 
Saugspannungskurve der jeweiligen Probe.  {numref}`saugspannungskurven`

```{figure} img/FL_Theorie/saugspannungskurven.png
---
height: 250px
name: saugspannungskurven
---
Saugspannungskurven verschieddener Probekörper.
```

Wasserdampf in der Luft ist nicht beliebig sondern vom Sättigungsgehalt der Luft abhängig.  Die mögliche Sättigung 
steigt mit der Temperatur. {numref}`saettigung_luft_diag`

```{figure} img/FL_Theorie/saettigung_luft_diag.png
---
height: 250px
name: saettigung_luft_diag
---
Diagramm zur Bestimmung des Wassergehaltes in der Luft abhängig von der Temperatur und relativen Luftfeuchtigkeit. 
Sättigungsgealt steigt mit der Temperatur.
```

Wenn wir uns das bei einem Material ansehen, bemerken wir das Phänomen, dass die Materialoberfläche Bindungskräfte auf 
das Wasserdampfmolekül hat. Abhängig davon kann mit einer gewissen Wahrscheinlichkeit solch ein Wasserdampfmolekül an 
der Materialoberfläche hängen bleiben. Die Geschwindikeit der Bewegung der Moleküle hängt von der Temperatur ab. Je 
höher die Luftfeuchte ist, desto stärker wird die Schicht der angelagerten Wasserdampfmoleküle. Durch die Bindungskräfte 
können dadurch an dieser Schicht wesentlich mehr Wasserdampfmoleküle im Gleichgewicht stehen, als in der Luft selber.
{numref}`wasserdampfmolekuele` <br>

```{figure} img/FL_Theorie/wasserdampfmolekuele.png
---
height: 250px
name: wasserdampfmolekuele
---
Vereinfachte Darstellung der Anlagerung von Wasserdampfmolekülen auf eine Materialoberfläche.
```

Der Zusammenhang zwischen Konzentration und Temperatur kann am besten durch die relative Luftfeuchtigkeit ausgedrückt
werden. Diese Überlegung kann mittels der Sorptionsisotherme eines Materials veranschaulicht werden. {numref}`sorptionsisotherme`

```{figure} img/FL_Theorie/sorptionsisotherme.png
---
height: 250px
name: sorptionsisotherme
---
Klassische Darstellung einer Sorptionsisotherme. Auf der Abszisse ist die relative Luftfeuchtigkeit und auf der Ordinate 
der korrespondierende Wassergehalt für die jeweiligen Materialien dargestellt.
```

#### Saugspannung – Krümmungsradius der Wasseroberfläche

In einem abgeschlossenem Volumen gefüllt mit Wasser stellt sich über der Wasseroberfläche ein Partialdruck ein der 100 % 
relativer Luftfeuchte entspricht. Bei einer gekrümmten Oberfläche werden die Moleküle mehr 
zurückgehalten. Dadurch ist die Luftfeuchte darüber < 100 %. {numref}`saugsp_kelvin`

```{admonition} Hinweis
Je kleiner der Krümmungsradius desto geringer die relative Luftfeuchtigkeit über der Wasseroberfläche.
```

Der Zusammenhang zwischen relativer Luftfeuchtikeit und Saugspannung wir über die Kelvin Gleichung hergestellt, 
Gleichung {eq}`eq_kelvin`.

$$
  \varphi = e^{\frac{s}{\rho_{H_{2}O} \cdot R_{H_{2}O} \cdot T}}
$$ (eq_kelvin)

| Parameter       |   | Beschreibung                        |
|-----------------|---|-------------------------------------|
| $\varphi$       |   | relative Luftfeuchte                |
| $\rho_{H_{2}O}$ |   | Dichte von Wasser in $kg/m³$        |
| $R_{H_{2}O}$    |   | Gaskonstante von Wasserdampf 462 $J/kgK$ |
| $T$             |   | Absolute Temperatur in $K$          |
| $s$             |   | Saugspannung in Pa                  |


```{figure} img/FL_Theorie/saugsp_kelvin.png
---
height: 250px
name: saugsp_kelvin
---

```

Durch Gleichung {eq}`eq_kelvin` kann ein Zusammenhang zwischen der Sorptionsisotherme und der Saugspannungslurve 
herstellen, Abbildung . 

```{figure} img/FL_Theorie/feuchtespeicherfu.png
---
height: 250px
name: feuchtespeicherfu
---
Darstellung der Feuchtespeicherfunktion mithilfe der Sorptionsisotherme und Saugspannungskurve.
```

#### Bestimmung des Speicher- und Transportkoeffizienten mit Hilfe von Parameteranpassung von Modellfunktionen

Um numerische Simulationen zu ermöglichen müssen aus den Messpunkte durchgehende FUnktionen erzeugt werden. Es gibt 
hierzu verschiedenste Ansätze, XXX Lit refs XXX, einer davon ist in Gleichung {eq}`eq_feuchtefu` dargestellt.

$$
w(s) = \frac{u_{f}}{1 + \left(\frac{s}{s_{0}}\right)^{p}}
$$ (eq_feuchtefu)

| Parameter |     | Beschreibung                           |
|-----------|-----|----------------------------------------|
| $w$       |     | Wassergehalt in $kg/m³$                |
| $s$       |     | Saugspannung in Pa                     |
| $u_{F}$   |     | Freier Parameter zur Anpassung         |
| $s_{0}$   |     | Freier Parameter zur Anpassung         |
| $p$       |     | Freier Parameter zur Anpassung gfhbfgh |

#### Gibt es einen Zusammenhang zwischen relativer Luftfeuchte und Saugspannung?

Wenn man mit 100 bar eine Saugspannungsmessung durchführt ergibt sich derselbe Feuchtegehalt, wie wenn man einen 
Aufsaugversuch bei 95 % relativer Luftfeuchtigkeit durchführt.

```{figure} img/FL_Theorie/sorpt_saug_zusammen.png
---
height: 250px
name: sorpt_saug_zusammen
---

```