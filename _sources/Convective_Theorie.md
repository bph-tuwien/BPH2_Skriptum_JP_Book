# Theoretische Grundlagen des konvektiven Wärme- und Feuchtetransportes

Wenn wir uns an Gleichung {eq}`q_diff_conv_eq` und {eq}`g_diff_conv_eq`
im [vorhergehenden Kapitel](resources/Diffusive_Theorie.md) zurückerinnern, haben wir uns zu diesem Zeitpunkt nur mit dem
diffusiven Therm beschäftigt und den konvektiven vernachlässigt $q_{conv} = g_{conv} = 0$. Um konvektiven Transport zu
berücksichtigen setzen wir $q_{conv} \neq 0 $ und $g_{conv} \neq 0$ und erweitern unsere beschreibenden Gleichungen um
diese Therme.

## Darcy's Gesetz - Massenstrom zu Folge von Druckdifferenzen

Faserdämmstoffe wie beispielsweise aus Mineralwolle oder Zellulose sind auf Grund Ihrer Struktur von Luft durchströmbar.
Dadurch kann in solchen Baustoffen der konvektive Wärme- und Feuchtetransport einen maßgebedenden Einfluss auf das
hygrothermische Verhalten haben. Der konvektive Transport kann, bei unzureichender oder nicht vorhandener Luftdichtheit,
entweder durch natürliche Konvektion (thermischer Auftrieb) oder erzwungener Konvektion (Druckdifferenzen) ausgelöst
werden.

Ähnlich zu den Formulierungen für die Wärme- und Feuchtestromdichte, kann auch die Massenstromdichte zu Folge
Luftströmung mit Hilfe Darcy's Gesetz definiert werden. Wir betrachten hier die Formulierung ohne Berücksichtigung des
Auftriebs, für den Fall, dass der Auftrieb einen maßgebenden Einfluss hat, kann das Gesetz laut
{cite}`wangNumericalMethodCalculating2001` erweitert werden.

```{note}
Später werden wir sehen, dass diese Formulierung nicht nur zur Beschreibung poröser Materialien verwendet werden kann, 
sondern auch die Grundlage für die
Modellierung von Luftpfaden durch Baustoffe darstellt.
```

Für den eindimensionalen Fall ist $\dot{m}_{a}$ definiert als

$$ \dot{m}_{a} = \frac{\rho_{a} \cdot k}{\mu} \frac{P - (P + \Delta P)}{\Delta x} $$

$$ \dot{m}_{a} = -\frac{\rho_{a} \cdot k}{\mu} \frac{\Delta P}{\Delta x} $$(m_delta_x_eq)

In Gleichung {eq}`m_delta_x_eq` steht $\rho_{a}$ für die Dichte der Luft in kg/m³, $\mu$ für die dynamische Viskosität
der Luft, $k$ für die Permeabiliät des porösen Materials in m² und $P$ für den jeweiligen Luftdruck in Pa.

```{figure} img/Konvektion/m_steady_state_wall.png
---
height: 250px
name: m_steady_state_wall
---
Massenstrom durch ein poröses finites Wandstück. {cite}`hagentoftIntroductionBuildingPhysics2001`
```

Gleichung {eq}`m_delta_x_eq` kann bei Grenzwertbetrachtung $\lim \limits_{\Delta x \to 0}$ übergeführt werden in den
Differentialoperator

$$ \dot{m}_{a} = -\frac{\rho_{a} \cdot k}{\mu} \frac{dP)}{dx} $$ (m_delta_x_eq)

und mittels des Nabla Operators verallgemeinert werden zu

$$ \dot{m}_{a} = - \frac{\rho_{a} \cdot k}{\mu} \nabla P $$(m_nabla_eq)

```{note}
Auf Grund der bauphysikalischen Relevanz beschäftigen wir uns vorrangig mit Massenströmen deren Gas aus Luft besteht.
Entsprechende Anpassung der Parameter ermöglichen auch die Abbildung anderer Fluide oder Gase. 
{cite}`hagentoftIntroductionBuildingPhysics2001`
```

## Erweiterung der Grundgleichungen um ihre konvektiven Therme

### Konvektiver Wärmetransport

Bei Berücksichtigung von Konvektion wird die Wärmestromdichte beschrieben durch

$$ q = q_{diff} + q_{conv}$$ (q_diff_conv_2_eq)

wobei $q_{conv} \neq 0 $ und definiert ist durch

$$ q_{conv} = \dot{m}_{a} \cdot c_{p}T $$

Dabei beschreibt $\dot{m}_{a}$ (kg/(m²s)) die Massenstromdichte pro Zeiteinheit durch ein poröses Medium zu Folge eines
Druckgradienten, $c_{p}$ die spezifische Wärmekapazität (J/kgK) bei konstantem Druck (gilt für Gase) und T die
Temperatur in Kelvin.

Damit kann der für bauphysikalische Berechnungen relevante Wärmestrom komplett beschrieben werden als:

$$ q = - \lambda \nabla T + \dot{m}_{a} \cdot c_{p} T $$ (q_ges_eq)

Einsetzen in Gleichung {eq}`dT_eq` führt auf die **beschreibende partielle Differentialgleichung des Temperaturfeldes:**

$$ \rho c \frac{\partial T}{\partial t} = \nabla \cdot (\lambda \nabla T - \dot{m}_{a} \cdot c_{p} T) + h $$(dT_ges_eq)

### Konvektiver Feuchtetransport

Analog zur Wärmestromdichte kann auch die Feuchtestromdichte um ihren konvektiven Einfluss erweitert werden. Das führt
auf

$$ g = - \delta_{v} \cdot \nabla v + \frac{\dot{m}_{a}}{\rho_{a}} \cdot v$$(g_ges_eq)

Einsetzen in Gleichung {eq}`w_eq` führt auf die **beschreibende partielle Differentialgleichung des Feuchtefeldes:**

$$\frac{\partial w}{\partial t} = \nabla \cdot \delta_{v} \cdot \nabla v - \frac{\dot{m}_{a}}{\rho_{a}} \cdot v + m $$(w_conv_eq)

### Einfluss des Lufttransportes auf den Wärme- und Feuchtetransport

$$ Q_{cd} = - A \lambda \frac{dT}{dx} + c_{pa} \dot{M}_{a} \cdot T(x) $$(Qcd_con_eq)

Gleichung {eq}`Qcd_con_eq` kann für den [stationären eindimensionalen Fall gelöst werden](analy_konv) und führt auf

$$ Q_{cd} = c_{pa} \dot{M}_{a} \cdot \frac{T(0) \cdot e^{L/\ell} -T(L)}{e^{L/\ell} - 1}$$ (Qcd_con_sol_eq)

mit der normalisierten, dimensionslosen Temperatur

$$ T'(x) = \frac{T(x) - T_{1}}{T_{2} - T{1}} = \frac{e(x/\ell) - 1}{e(L/\ell - 1) } $$

Für diese Vereinfachung wird die modifizierte Peclet-Zahl $Pe^{*}$ eingeführt. Diese ist definiert als das Verhältnis

$$ Pe^{*} = \frac{L}{\ell} $$

wobei

$$ \ell = \frac{A \lambda}{c_{pa} \dot{M}_{a}} $$

```{figure} img/Konvektion/peclet_num.png
---
height: 350px
name: peclet_num
---
Temperatur Profil durch ein finites Wandelement für unterschiedliche $L/\ell = Pe^{*}$. {cite}`hagentoftIntroductionBuildingPhysics2001`
```

$Pe^{*}$ ist negativ wenn $\dot{M}_{a}$ negativ ist. Der Einfluss der modifizierten Peclet Zahl auf den
Temperaturverlauf kann {numref}`peclet_num` entnommen werden.

Die Größe $\ell$ charakterisiert das Verhältnis zwischen diffusiven und konvektiven Wärmefluss und damit auch den
Einfluss des konvektiven Transportes auf den Gesamttransport.

Die $Pe^{*}$ findet sich auch normativ bei den Diffusions-/Konvektionsgleichungen in Abschnitt 11 von ÖNORM 8110-2:2020
wieder. Dort wird jedoch die immer die Flussdichte und nicht der Wärmefluss betrachtet.

```{note}
Bei Vernachlässigung von Flüssigwassertransport kann der Feuchtetransport analog betrachet und gelöst werden.
```

(analy_konv)=

#### Analysthische Lösung der Differentialgleichung für den stationären eindimensionalen Fall

Da sich die normative Darstellung der in Gleichung {eq}`Qcd_con_sol_eq` folgt, wird nachfolgend ein kurzer Beweis für
dessen Gültigkeit erbracht.

Gleichung {eq}`Qcd_con_eq` kann für den stationären eindimensionalen Fall und wenn $-\frac{d}{dx}Q_{cd} = 0$
folgendermaßen gelöst werden.

Gleichung {eq}`Qcd_con_eq` kann umgestellt werden 
und mit Hilfe der Definiton von $\ell$ wie folgt dargestellt werden

$$ \frac{Q_{cd}}{c_{pa} \dot{M}_{a}} = T(x) - \ell \cdot \frac{dT}{dx} $$

Mit Hilfe nachfolgendem Ansatz

$$ -\ell e^{x/\ell}\frac{d}{dx}\left(e^{-x/\ell} T(x)\right) = T(x) - \ell \cdot \frac{dT}{dx} $$(ansatz_eq)

kann folgender Zusammenhang aufestellt werden

$$ \frac{d}{dx}(e^{-x/\ell} T(x)) = - \frac{e^{-x/\ell}}{\ell} \cdot \left(T(x) - \ell \cdot \frac{dT}{dx}\right) = -
\frac{e^{-x/\ell}}{\ell} \cdot \frac{Q_{cd}}{c_{pa} \dot{M}_{a}}$$

Integrieren über die Länge $L$ des betrachteten finiten Stückes führt auf

$$ \int_{0}^{L} \frac{d}{dx}(e^{-x/\ell} T(x)) \,dx \ = - \int_{0}^{L} \frac{e^{-x/\ell}}{\ell} \cdot \frac{Q_{cd}}{c_
{pa} \dot{M}_{a}} \,dx$$

$$ \left[e^{-x/\ell} T(x)\right]_{0}^{L} = - \frac{1}{\ell} \cdot \frac{Q_{cd}}{c_{pa} \dot{M}_{a}} \int_{0}^{L}
e^{-x/\ell} \,dx$$

$$ \left[e^{-x/\ell} T(x)\right]_{0}^{L} = - \frac{1}{\ell} \cdot \frac{Q_{cd}}{c_{pa} \dot{M}_{a}}
\left[-\ell e^{-x/\ell}\right]_{0}^{L}$$

und entsprechendes Umformen ergibt

$$ e^{-L/\ell} T(L) - 1 \cdot T(0) = - \frac{1}{\ell} \cdot \frac{Q_{cd}}{c_{pa} \dot{M}_{a}} (-\ell) \left(e^{-L/\ell}

- 1\right) \quad | \cdot e^{L/\ell} $$

$$ T(L) - T(0) \cdot e^{L/\ell} = - \frac{1}{\ell} \cdot \frac{Q_{cd}}{c_{pa} \dot{M}_{a}} (-\ell) \left(1 - e^{L/\ell}
\right) \quad | \cdot (-1) $$

$$ T(0) \cdot e^{L/\ell} -T(L) =\frac{Q_{cd}}{c_{pa} \dot{M}_{a}} \left(e^{L/\ell} - 1 \right)\\$$

$$ Q_{cd} = c_{pa} \dot{M}_{a} \cdot \frac{T(0) \cdot e^{L/\ell} -T(L)}{e^{L/\ell} - 1}\\ $$

## Fehlertoleranz von Bauteilen

Bauteile können durch witteriche Exposition während der Bauzeit, Abweichungen der Ausführung von der ideellen Planung
oder unbeabsichtigten Ausführungsfehlern immer wieder unvorhergesehenen hygrothermischen Belastungen ausgesetzt sein.
Eine für die bauphysikalische Planung adaptierte Einstufung von Unsicherheiten wurde in
{cite}`bednarRiskManagementProbabilistic2015` nach {cite:t}`mcmanusFrameworkUnderstandingUncertainty2007` vorgestellt:

> "**Lack of knowledge** is defined as facts that are unknown or known only imprecisely that is needed to assess performance of the concept: examples include prior
> building usage, possible salt contents, etc.
>
> **Lack of definitions** is defined as aspects of the project that are undecided or not
> specified: for example, future use and maintenance, neighbouring buildings, available
> funding and associated criteria.
>
> **Statistically characterized variables** are defined as inputs that cannot always
> be known precisely but can be statistically characterized or at least bounded: for
> example, typical material properties (e.g. thermal conductivity, liquid transport coefficient, etc.) are not a single number but are statistically characterized variables.
> The future airtightness of the building envelope is typically a bounded value. If the
> renovation is conducted according to current state of the art practices, the future
> building airtightness is higher than the current state. The future climate conditions
> are also a bounded variable.
>
> **Known Unknowns** are defined as aspects known to influence building performance,
> but have entirely unknown values: for example, the impact of future occupants on
> the building constructions (e.g. hanging up pictures, placing furniture, etc.), animals
> that might intrude a construction, destruction by sabotage or climate change.
>
> **Unknown Unknowns** are defined as aspects that are unknown by definition. A
> very conservative mitigation strategy might help to handle current unknown aspects
> in the future."


Diese zu erwartenden Ungewissheiten können nach {cite:t}`mcmanusFrameworkUnderstandingUncertainty2007` als "Known
Unknowns" deklariert werden. Um diese "Known Unknowns" in hygrothermischen Berechnungen zu berücksichtigen hat sich der
Begriff der Fehlertoleranz in der bauphysikalischen Bemessung etabliert. Das Konzept der Fehlertoleranz einer
Baukonstruktion lässt sich mittels der von {cite:t}`bednarthomasHygrothermischenBauteilsimulationRisikomanagement2016`
gewählten Beschreibung der Tauglichkeit einer Baukonstruktion definieren:

> "Tauglich ist in dem Sinne eine Konstruktion, wenn sie bei üblicher Nutzung keine
> Schimmelpilzbildung an der Oberfläche oder im Inneren aufweist, Holzwerkstoffe
> nicht verrotten, keine thermischen und hygrischen Längenänderungen zu Zerstörung
> führen, Metalle keine überdurchschnittlichen Korrosionsraten aufweisen und an der
> Außenseite Algenwachstum oder Ablagerungen die optische Erscheinung störend
> verändern."

Bei der Nachweisführung von Bauteilen findet sich diese Konzept normativ geregelt wieder in Form von

- [Anfangsfeuchten](Anfangsfeuchte),
- dem Ansetzen von künstlichen [Luftpfaden](LPF) oder
- Vereinfachungen in der Berechnung um auf der sicheren Seite zu bleiben (z.B. Vernachlässigung der solaren Strahlung).

## Luftvolumenstromkoeffzienten - Hintergrund

Der Ursprung der in ÖNORM 8110-2:202 angeführten Luftvolumenstromkoeffizienten zu Definition von [Leckagen](LPF) liegt
in {cite}`nusserProposalModifiedGlaserMethod2011` wo erstmals ein adabptiertes Glaserverfahren vorgestellt wird um den
konvektiven Transport von Wärme- und Feuchtigkeit zu berücksichtigen. Diese Berücksichtigung soll, abhängig von der
Ausführungsqualität, es ermöglichen die Anfälligkeit eines Bauteiles auf Fehler zu erfassen.

```{note}
Mann könnte auch sagen, dass die Anfälligkeit eines Bauteiles im Umkehrschluss der Kehrwert der 
Fehlertoleranz eines Bauteiles ist.
```

Diese Kategorisierung der Ausführungsqualität wurde dann in {cite}`nusserEuroGlaserUnterBeachtung2010a` nachgeschärft und
wurde mittels F-Klassen berücksichtigt:

```{figure} img/Konvektion/f_konv.png
---
height: 250px
name: f_konv
---
Kategorisierung der F-Klassen. {cite}`nusserEuroGlaserUnterBeachtung2010a`
```

Für die Norm {cite}`onormONORM8110220202020` wurde das Verfahren weiter präzisiert und ist nun Tabelle 3 zu entnehmen:

```{figure} img/Konvektion/luftvolstrom_koeff_tab.png
---
height: 200px
name: luftvolstrom_koeff_tab
---
Tabelle 3 zur Definition des Luftvolumenstromkoeffzienten C.
```
