(FL_Theorie)=

# Flüssigwassertransport - Theorie

Die hier beschriebenen theoretischen Ausführungen stützen sich Großteils auf
{cite}`kalagasidisEvaluationInterfaceMoisture2004` und {cite}`bednarModellingMoistureTransport2004`.

## Erweiterung der Transportgleichung für Diffusion um den Flüssigwasseranteil

Gleichung {eq}`w_conv_eq` beruht auf der Annahme, dass wir in Gleichung {eq}`g_eq` den Anteil für den
FLüssigwassertransport vernachlässigt haben $g_{l} = 0$.

Um diesen in

$$ g = g_{v} + g_{l} $$ (g_eq)

zu berücksichtigen, kann er allgemein folgendermaßen definiert

$$ g_{l} = K \cdot \nabla P_{suc}$$

und eindimensional $ \frac{\partial }{\partial y} = \frac{\partial }{\partial z} = 0 $ vereinfacht werden zu:

$$ g_{l} = K \cdot \frac{d P_{suc}}{dx}$$

Dabei ist $K$ in Sekunden ein Transportkoeffzient der die Flüssigwasserleitung (temperatur- und feuchteabhängig)
beschreibt.

Einsetzen in die allgemeine Definiton des Feuchtefeldes {eq}`w_eq` führt somit auf

$$ \frac{d w}{dt} = - \nabla (g_{v} + g_{l}) + m $$(w_all_eq)

und ermöglicht uns die Beschreibung des zeitabhängigen Feuchtefeldes in kg/m³s bei Berücksichtigung der
Flüssigwasserleitung.

```{note}
In $ g_{v} $ ist der konvektive Term enthalten.
```

Weiters werden wir uns mit der Beschreibung der Kapillarkräfte und der Flüssigwasserleitung beschäftigen um Gleichung
{eq}`w_all_eq` lösen zu können.

[//]: # (## Theoretischer Hintergrund Flüssigwasser.)

[//]: # ()

[//]: # (*Mitschrift VO 01.04.2022:*)

[//]: # ()

[//]: # (## Geschichte)

[//]: # ()

[//]: # (- 1822 Fourier - Ansatz zum Wärmetransport)

[//]: # (- 1850 Graham/Fick - Diffusion)

[//]: # (- Um 1880 Maxwell Stefan Boltzmann Statistische Mechanik/Transporttheorie)

[//]: # (- 1856 Darcy - Ansatz zum Flüssigwassertransport)

[//]: # (- 1940-1970 Krischer, Philipp, de Vries, Luikov Berechnung von Trocknungsvorgängen Bodenkunde – Hydrologie&#40;gesättigte)

[//]: # (  Körper&#41;)

[//]: # (- 1958 Glaser H.: Vereinfachte Berechnung der Dampfdiffusion durch geschichtete Wände bei Ausscheidung von Wasser und)

[//]: # (  Eis. Kältetechnik 10 &#40;1958&#41;, H. 11, 358-364 &#40;Teil 1&#41;, H. 12, 386-390 &#40;Teil 2&#41;.)

[//]: # (- 1991-1995 IEA Annex 24 „Heat, Air and Moisture transport through Insulated Envelopes“)

[//]: # (- 1997-2001 WTA-Arbeitsgruppe „Simulation wärme- und feuchtetechnischer Prozesse“)

[//]: # (- ~ 1985 Kiessl, Häupl, Stopp – Mehrschichtige Baukonstruktionen)

[//]: # (- 1990 Rode – Simulationsprogramm MATCH)

[//]: # (- 1994 Künzel – Simulationsprogramm WUFI)

[//]: # (- 1996 Grunewald – Simulationsprogramm DIM bzw. DELPHIN)

[//]: # (- 2000 Bednar – Simulationsprogramm mit Kopplung zum Raum)

[//]: # (- 2000-2002 EU-Projekt „Heat, Air Moisture Standards Development“)

[//]: # (- 2000-2007 CEN TC89 WI29.3 Erarbeitung EN 15206 „Hygrothermal performance of building components and building elements)

[//]: # (  – Assesment of moisture transfer by numerical simulation“)

[//]: # (- 2003-2007 IEA EBC Annex 41 „Whole building heat air and moisture response“)

[//]: # (- 2010-2014 IEA EBC Annex 55 „ Reliability of Energy Efficient Building Retrofitting Probability Assessment of)

[//]: # (  Performance & Cost”)

[//]: # ()

[//]: # ("1D Simulation bei einer Sanierung stellt Risiko dar wenn das wahre Problem vergessen wird.")

[//]: # ()

[//]: # ()

[//]: # (---------------------------------------------------------)

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

Je kleiner die Kapillare desto höher die Steighöhe, weil das Volumen klein ist im Verhältnis zur Kraft die entlang
dieses Umfangs auftritt. Je größer der Kapillardurchmesser, desto weniger ist die maximale Steighöhe. Zusammenhang
zwischen Porenstruktur und Geschwindigkeit der Flüssigleitung auf Grund von vorhandener Saugspannung.
{numref}`kapillaren`

```{figure} img/FL_Theorie/kapillaren.png
---
height: 250px
name: kapillaren
---
Je kleiner die Kapillare desto höher die Steighöhe, weil 
das Volumen klein ist im Verhältnis zur Kraft die entlang dieses Umfangs auftritt. 
```

#### Bestimmung des Zusammenhanges zwischen Saugspannung und Wassergehalt - Plattenapparat

Ein Versuch zur Messung des Zusammenhanges zwischen Kraft die auf das Wasser wirkt und wie viel Wasser im Porensystem
gehalten werden kann. Als Unterlage für die Probe wird eine Keramikplatte verwendet. Diese hat eine sehr feine
Porenstruktur und wird mit Kaolin beschichtet. Kaolin ist ein feines, eisenfreies, weißes Gestein, auch mit einer feinen
Porenstruktur. Auf diese Platte wird eine gesättigte Probe gelegt, sodass die Porenstruktur des Baustoffes in die
feinere Porenstruktur der Platte übergeht. {numref}`plattenapparat`

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
Saugspannungskurve der jeweiligen Probe. {numref}`saugspannungskurven`

```{figure} img/FL_Theorie/saugspannungskurven.png
---
height: 500px
name: saugspannungskurven
---
Saugspannungskurven verschiedener Probekörper.
```

Wasserdampf in der Luft ist nicht beliebig sondern vom Sättigungsgehalt der Luft abhängig. Die mögliche Sättigung steigt
mit der Temperatur. {numref}`saettigung_luft_diag`

```{figure} img/FL_Theorie/saettigung_luft_diag.png
---
height: 350px
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
werden. Diese Überlegung kann mittels der Sorptionsisotherme eines Materials veranschaulicht werden.
{numref}`sorptionsisotherme`

```{figure} img/FL_Theorie/sorptionsisotherme.png
---
height: 350px
name: sorptionsisotherme
---
Klassische Darstellung einer Sorptionsisotherme. Auf der Abszisse ist die relative Luftfeuchtigkeit und auf der Ordinate 
der korrespondierende Wassergehalt für die jeweiligen Materialien dargestellt.
```

#### Saugspannung – Krümmungsradius der Wasseroberfläche

In einem abgeschlossenem Volumen gefüllt mit Wasser stellt sich über der Wasseroberfläche ein Partialdruck ein der 100 %
relativer Luftfeuchte entspricht. Bei einer gekrümmten Oberfläche werden die Moleküle mehr zurückgehalten. Dadurch ist
die Luftfeuchte darüber < 100 %. {numref}`saugsp_kelvin`

```{note}
Je kleiner der Krümmungsradius desto geringer die relative Luftfeuchtigkeit über der Wasseroberfläche.
```

Der Zusammenhang zwischen relativer Luftfeuchtikeit und Saugspannung wir über die Kelvin Gleichung hergestellt,
Gleichung {eq}`eq_kelvin`.

$$ \varphi = e^{\frac{s}{\rho_{H_{2}O} \cdot R_{H_{2}O} \cdot T}} $$ (eq_kelvin)

Darin ist $\varphi$ die relative Luftfeuchtigkeit, $\rho_{H_{2}O}$ die Dichte von Wasser in kg/m³, $R_{H_{2}O}$ die
Gaskonstante von Wasserdampf mit 462 J/kgK, $T$ die absolute Temperatur in Kelvin und $P_{suc}$ die Saugspannung in
Pascal.

```{figure} img/FL_Theorie/saugsp_kelvin.png
---
height: 250px
name: saugsp_kelvin
---
Saugspannung in einer Pore ist abhängig vom Krümmungsradius.
```

Durch Gleichung {eq}`eq_kelvin` kann ein Zusammenhang zwischen der Sorptionsisotherme und der Saugspannungslurve
herstellen, Abbildung .

```{figure} img/FL_Theorie/feuchtespeicherfu.png
---
height: 600px
name: feuchtespeicherfu
---
Darstellung der Feuchtespeicherfunktion mithilfe der Sorptionsisotherme und Saugspannungskurve.
```

#### Bestimmung des Speicher- und Transportkoeffizienten mit Hilfe von Parameteranpassung von Modellfunktionen

Um numerische Simulationen zu ermöglichen müssen aus den Messpunkte durchgehende FUnktionen erzeugt werden. Es gibt
hierzu verschiedenste Ansätze, ein solcher ist in Gleichung {eq}`eq_feuchtefu` dargestellt.

$$ w(P_{suc}) = \frac{u_{f}}{1 + \left(\frac{P_{suc}}{P_{0}}\right)^{m}} $$ (eq_feuchtefu)

Dabei ist $w(P_{suc})$ der Wassergehalt in Abhängigkeit von der Saugspannung in kg/m³, $P_{suc}$ die Saugspannung in Pa
und sowohl $u_{F}$, $P_{0}$ als auch $m$ freie Parameter zur Anpassung des Kurvenverlaufs.

#### Gibt es einen Zusammenhang zwischen relativer Luftfeuchte und Saugspannung?

Wenn man mit 100 bar eine Saugspannungsmessung durchführt ergibt sich derselbe Feuchtegehalt, wie wenn man einen
Aufsaugversuch bei 95 % relativer Luftfeuchtigkeit durchführt.

```{figure} img/FL_Theorie/sorpt_saug_zusammen.png
---
height: 350px
name: sorpt_saug_zusammen
---

```

### Flüssigwasserleitung

In {cite}`kalagasidisEvaluationInterfaceMoisture2004` wird die Flüssigwasserleitung mittels Gleichung {eq}`K_eq` für
einen fiktiven Probekörper modelliert.

$$ K_{w}(P_{suc}, n) = - \frac{\partial w(P_{suc})}{\partial P_{suc}} \cdot \frac{n + 1}{2 n} \cdot \left(
\frac{A}{300}\right)^{2} \cdot \left(\frac{w(P_{suc}}{300}\right)^{n} \cdot \left( n + 1 - \left(\frac{w(P_
{suc}}{300}\right)^{n}\right)
$$ (K_eq)

Hierbei steht $K_{w}$ für die totale hydraulische Leitfähigkeit in s, $A$ für den Wasseraufnahmekoeffizient in
kg/m²h<sup>0.5</sup>, $p_{suc}$ für die Saugspannung in Pa und $n$ für einen freien Parameter um die Funktion möglichst
gut fitten zu können.

Wobei der Wasssergehalt in Abhängigkeit der Saugspannung für den fiktiven Probekörper definiert ist als

$$ w(P_{suc}) = 300 \cdot (1 + 10^{-6} \cdot P_{suc})^{-1} $$ (w_Psuc)

und der Wasseraufnahmekoeffzient für den fiktiven Probekörper definiert ist mit $A = 10$ kg/m²h<sup>0.5</sup>.

```{figure} img/FL_Theorie/curves_test_materials.png
---
height: 250px
name: curves_test_materials
---
Wassergehalt in Abhängigkeit von der Saugspannung und totale hydraulische Leitfähigkeit für das Testmaterial in 
{cite}`kalagasidisEvaluationInterfaceMoisture2004`. Man erkennt den Einfluss des freien Faktors $n$
```

