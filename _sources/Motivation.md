# Motivation

Die Hygrothermik beschäftigt sich, als Teilgebiet der Bauphysik, mit der Beschreibung und Vorhersage von
Transportprozessen auf Bauteilebene. Diese Porzesse beinhalten den Transport von Wärme, Feuchtigkeit und Luft und sind
in der Realität oft ausgelöst und/oder beeinflusst durch externe klimatische Phänomene wie beispielsweise
Sonneneinstrahlung, Regen oder Wind {numref}`building_comp`.

```{figure} img/Motivation/building_comp.png
---
height: 250px
name: building_comp
---
Poröser Baukörper mit Rissen und Luftpfaden. Es wirken sowohl Außen- als auch 
Innenklima auf das Bauteil. {cite}`hagentoftIntroductionBuildingPhysics2001`
```

Baukörper bestehen zumeist aus porösen Baustoffen, wodurch
sowohl [Wärmetransport als auch Massentransport](Wärmebrücken.md) (Feuchte, Luft) stattfinden können. Bei nichtporösen
Stoffen kann weiterhin Wärmeleitung durch Strahlung erfolgen. Die Risse und Luftpfade in {numref}`building_comp`
ermöglichen, abhängig von Ihrer Ausbildung und Beschaffenheit, den relevanten
[konvektiven Transport](Konvektiver_Transport.md) von Wärme und Feuchtigkeit durch das Bauteil. Des Weiteren kann, bei
entsprechend saugfähigen Baustoffen, der
[Flüssigwassertransport](FL_Theorie.md) eine entscheidende Rolle spielen.

All diese Transportprozesse beeinflussen das Bauteilverhalten und können entsprechende Risiken und Schäden mit sich
führen (Schimmelbildung, Eisbildung etc.). Um das bewerten zu können, müssen Simulationsergebnisse ausgewertet,
interpretiert und mit entsprechenden Risikomodellen analysiert werden.

## Energie- und Massenerhaltung

Grundlage unserer Berechnungen ist immer die

- Energieerhaltung und
- Massenerhaltung.

Die Erhaltungssätze müssen immer erfüllt sein. Betrachten wir ein geschlossenes Volumen {numref}`vol_conservation`,
stellvertretend für einen Raum oder ein Bauteil.

```{figure} img/Motivation/vol_conservation.png
---
height: 250px
name: vol_conservation
---
Massenstrom $\dot{m}$ in dem Volumen $V$ umschlossen von der Fläche $S$. {cite}`hagentoftIntroductionBuildingPhysics2001`
```

Der Nettoeintrag muss in dem Volumen gespeichert werden:

$$ \iint_S \dot{m} \,dS = \frac{dM}{dt} $$(m_int_eq)

$M$ steht in Gleichung {eq}`m_int_eq` für die gesamte Masse (Luft oder Feuchtigkeit) in dem Volumen. Dieses
Oberflächenintegral kann wiederum in $N$ Teile aufgespalten werden (z.B. Oberflächen von verschiedenen Bauteilen).

$$ \sum_{i=1}^{N} \iint_{S_{i}} \dot{m} \,dS = \sum_{i=1}^{N} \dot{M}_{i} = \frac{dM}{dt} $$(m_sum_eq)

Dabei beschreibt $\dot{M}_{i}$ den Massenstrom in das Volumen durch das Oberflächenelement $i$.

Dieselbe Formulierung ist analog auch für den Wärmestrom möglich.

$$ \iint_S q \,dS = \frac{dE}{dt} $$(q_int_eq)

Hier steht $E$ in Joule für die Gesamtenergie innerhalb des Volumens V. Aufteilung des oberflächlichen Wärmestromes
führt wiederum auf Gleichung {eq}`q_sum_eq`.

$$ \sum_{i=1}^{N} \iint_{S_{i}} q \,dS = \sum_{i=1}^{N} Q_{i} = \frac{dE}{dt} $$(q_sum_eq)

## Der Nabla-Operator - Anschaulich erklärt

Da uns der Nabla-Operator bei der Beschreibung unserer Transportphänomene als Werkzeug begleiten wird, wird hier der
Versuch gewagt die mathematische Operation in ein möglichst anschauliches physikalisches Verständnis zu überführen.

Der Gauss'sche Integralsatz ermöglicht uns die Transformation eines Oberflächenintegrals in ein Volumenintegral.
Angewendet auf Gleichung {eq}`q_int_eq` führt das auf Gleichung {eq}`q_gauss_eq`.

$$ \iint_S q \,dS = \iiint_V -\nabla \cdot q \,dV=\frac{dE}{dt} $$(q_gauss_eq)

Dabei steht $\nabla \cdot$ für den Nabla-Operator. Das Skalarprodukt zwischen dem Nabla-Vektor (
$\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z}$) und dem Wärmestrom-Vektor $q$
ist somit

$$ \nabla \cdot q = \left(\begin{array}{c} \frac{\partial}{\partial x} \\ \frac{\partial}{\partial y} \\
\frac{\partial}{\partial z} \end{array}\right) \cdot \left(\begin{array}{c} q_{x} \\ q_{y} \\ q_{z} \end{array}\right) =
\frac{\partial q_{x}}{\partial x} + \frac{\partial q_{y}}{\partial y} + \frac{\partial q_{z}}{\partial z} $$(nabla_q_eq)

Wenn wir gedanklich nun das betrachtete Volumen sehr klein werden lassen (z.B. zu einem Punkt), können wir uns
vorstellen, dass der Wärmestrom um diesen Punkt herum physikalisch gesehen konstant ist. Mathematisch gesehen bedeutet
das, dass unser Wärmestrom nun nicht mehr vom Volumen abhängig ist und somit aus dem Integral herausgezogen werden kann.

$$ \lim_{V \to \Delta V} \iiint_V -\nabla \cdot q \,dV\ = \iiint_{\Delta V} -\nabla \cdot q \,d\Delta V\ $$

$$ \iiint_{\Delta V} 1 \ \,d\Delta V\ \cdot -\nabla \cdot q \approx - \Delta V \cdot (\nabla \cdot q) =\frac{dE}{dt} $$

Umgeformt ergibt das:

$$ - \nabla \cdot q =\frac{dE}{dt} \cdot \frac{1}{\Delta V } $$(delta_V_q_eq)

Gleichung {eq}`delta_V_q_eq` hat eine besondere Bedeutung. Sie ermöglicht es den Nabla-Operator physikalisch zu
interpetieren. Er beschreibt die Nettorate des Wärmestromes zu einem Punkt pro Volumseinheit:

$ - \nabla \cdot q $ = Netto Wärmestrom-Eintrag pro Volumseinheit pro Zeiteinheit in J/sm³

Für den Lufmassenstrom können wir schreiben:

$ - \nabla \cdot \dot{m} $ = Netto Luftmassenstrom-Eintrag pro Volumseinheit pro Zeiteinheit in kg/sm³

Und für den Feuchtestrom:

$ - \nabla \cdot g $ = Netto Feuchtestrom-Eintrag pro Volumseinheit pro Zeiteinheit in kg/sm³
