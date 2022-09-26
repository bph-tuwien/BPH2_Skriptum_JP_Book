# Theorethische Grundlagen des diffusiven Wärme- und Feuchtetransportes

Wenn eine Koppelung zwischen Wärme- und Feuchtetransport in einer Berechnung besteht spricht man allgemein von einer
hygrothermischen Simulation. Diese Koppelung bringt den Vorteil, dass der Einfluss des Feuchtegehaltes auf die
Wärmeleitfähigkeit berücksichtigt werden kann. Die Differentialgleichungen, welche für solche Berechnungen miteinander
gekoppelt werden müssen, werden im folgenden vorgestellt, mit dem Ziel ein Verständnis für die unterliegenden Grundlagen
und Konzepte zu vermitteln.

## Allgemeine Transportgleichungen Diffusion

Bei Betrachtung der

### Wärmetransport

Bei Betrachtung der Wärmeleitung ergibt sich aus Gleichung {eq}`delta_V_q_eq`

$$ \rho c \frac{\partial T}{\partial t} = -\nabla \cdot q + h $$(dT_eq)

Dabei beschreibt $h$ (J/(m³s)) eine Wärmequelle. Diese kann ausgelöst sein durch mechanisches Heizen, chemische
Reaktionen etc.

Der Wärmefluss q (J/(m²s) ist definiert als

$$ q = q_{diff} + q_{conv}$$ (q_diff_conv_eq)

wobei $q_{diff}$ den diffusiven Anteil und $q_{conv}$ den durch Konvektion tranportierten Anteil des Wärmeflusses
beschreibt. Bei Vernachlässigung konvektiver Phänomene können wir $q_{conv} = 0$ setzen.

Für den diffusiven eindimensionalen Fall ist $q$ definiert als

$$ q = q_{diff} = \lambda \cdot \frac{T - (T + \Delta T)}{\Delta x}$$(q_delta_x_eq)
$$ q = -\lambda \cdot \frac{\Delta T}{\Delta x}$$(q_delta_x_eq)

```{figure} img/Wärmebrücke/q_steady_state_wall.png
---
height: 350px
name: q_steady_state_wall
---
Stationärer Wärmefluss durch ein finites Wandstück.
```

Gleichung {eq}`q_delta_x_eq` kann bei Grenzwertbetrachtung $\lim \limits_{\Delta x \to 0}$ übergeführt werden in den
Differentialoperator

$$ q = -\lambda \cdot \frac{d T}{d x}$$(q_dx_eq)

Mehrdimensional verallgemeinern lässt sich Gleichung {eq}`q_dx_eq` mittels des Nabla-Operators zu

$$ q = -\lambda \cdot \nabla T$$(q_nabla_eq)

```{note}
$\lambda$ kann eine vektorielle Größe sein wodurch richtungsabhängigen Wärmeleitfähigkeiten berücksichtigt werden können. 
Falls also $\lambda_{x} \neq \lambda_{y} \neq \lambda_{z}$. 
```

Gleichung {eq}`q_nabla_eq` eingesetzt in Gleichung {eq}`dT_eq` führt auf

$$ \frac {\lambda}{\rho c} \frac{\partial T}{\partial t} = \nabla \cdot (\nabla T) = \nabla^{2}T$$(dT_laplace_eq)

Dabei beschreibt $\nabla^{2}$ den Laplace-Operator:

$$ \nabla^{2} = \frac{\partial^{2}}{\partial x^{2}} + \frac{\partial^{2}}{\partial y^{2}} + \frac{\partial^{2}}{\partial
z^{2}} $$

$$ \nabla^{2}T = \frac{\partial^{2}T_{x}}{\partial x^{2}} + \frac{\partial^{2}T_{y}}{\partial y^{2}} +
\frac{\partial^{2}T_{z}}{\partial z^{2}} $$

### Feuchtetransport

Analog zum Wärmetransport kann der Feuchtetransport durch Gleichung {eq}`w_eq` beschrieben werden:

$$ \frac{\partial w}{\partial t}  = - \nabla \cdot g + m $$ (w_eq)

Hier steht $\frac{\partial w}{\partial t}$ für die Veränderung des Wassergehaltes in kg/m³s, $g$ für die
Feuchtestromdichte in kg/(m²s) und m für eine Feuchtequelle in kg/(m³s). Die Feuchtestromdichte setzt sich in porösen
Medien zusammen aus der

- Dampfdiffusionsstromdichte $g_{v}$ und
- Flüssigwasserstromdichte $g_{l}$.

$$ g = g_{v} + g_{l} $$ (g_eq)

Wenn wir vorübergehend den Flüssigwassertransport vernachlässigen $g_{l} = 0$, was bei entsprechenden Randbedingungen
eine [valide Annahme](Randbedingungen_Diffusive) darstellt, setzt sich die Dampfdiffusionsstromdichte $g_{v}$, ähnlich
wie der Wärmefluss {eq}`q_diff_conv_eq`, aus einem diffusiven und konvektiven Anteil zusammen

$$ g = g_{v} = g_{diff} + g_{conv} $$ (g_diff_conveq)

Bei Vernachlässigung konvektiver Phänomene können wir wiederum $g_{conv} = 0$ setzen. Den noch verbleibenden Anteil der
Feuchtstromdichte können wir in porösen Medien über das Fick'sche Gesetz beschreiben.

```{figure} img/Wärmebrücke/g_steady.png
---
height: 350px
name: g_steady
---
Feuchtestromdichte durch ein finites poröses Wandstück.
```

Dabei wird die Diffusion in ruhender Luft in Abhängigkeit gesetzt zu dem Dampfdruckgradienten $\Delta v$ und einer
Transportkonstante $\delta_{v}$.

$$ g = g_{diff} = \delta_{v} \cdot \frac{v - (v + \Delta v)}{\Delta x} $$

$$ g = -\delta_{v} \cdot \frac{\Delta v}{\Delta x} $$ (g_delta_eq)

$$ g = -\frac{D}{\mu} \cdot \frac{\Delta v}{\Delta x} $$ (g_delta_eq)

Hierbei steht D (m²/s) für den temperaturabhängigen Diffusionskoeffizienten ruhender Luft, wobei $T$ in Grad Celsius
einzusetzen ist

$$ D = (22.2 + 0.14 \cdot T) \cdot 10^{-6}$$

und $\mu$ für einen Faktor den Widerstand zu beschreiben der zu Folge des porösen Mediums besteht. Dieser Widerstand
entsteht einerseits durch

- Reduktion des Vorhandenen Raumes für Diffusion und andererseits
- zu Folge der längeren Wege die ein Dampf-Teilchen zu Folge eines Porennetzwerkes zurücklegen muss.

Analog zum Wärmefluss kann Gleichung {eq}`g_delta_eq` bei Grenzwertbetrachtung $\lim \limits_{\Delta x \to 0}$
übergeführt werden in den Differentialoperator

$$ g = -\delta_{v} \cdot \frac{d v}{\Delta x} $$ (g_dx_eq)

und mittels des Nabal-Operator mehrdimensional verallgemeinert werden zu

$$ g = - \delta_{v} \cdot \nabla v $$ (g_nabla_eq)

## Numerische Lösung einer partiellen Differentialgleichung am Beispiel der Wärmeleitung

(Randbedingungen_Diffusive)=

## Randbedingungen

Der Wärmeübergangswiderstand $R_{s}$ in m²K/W setzt sich aus dem konvektiven $\alpha_{c}$ und und radiativen
Wärmeübergangskoeffizienten $\alpha_{r}$ zusammen:

$$ R_{s} = \frac{1}{\alpha_{c} + \alpha_{r}}$$(R_s_eq)

### Konvektiver Wärmeübergangskoeffizient

Für Innenräume ist der konvektive Wärmeübergangskoeffizient definiert als:

| Richtung des Wärmestroms | $\alpha_{c,i}$ in /m²K |
|--------------------------|------------------------|
| aufwärts                 | 5                      |
| horizontal               | 2.5                    |
| abwärts                  | 0.7                    |

Für Außenoberflächen ist $\alpha_{c,e}$ vorrangig abhängig von der Windgeschwindigkeit v in m/s:

$$ \alpha_{c,e} = 4 + 4 \cdot v $$

### Radiativer Wärmeübergangskoeffizient

Der radiative Wärmeübergangskoeffizient $\alpha_{r}$ berechnet sich mittels des Emissionsgrades $\epsilon$, der
Stefan-Boltzmann-Konstante $\sigma$ ($5.67 \cdot 10^{-8}$ W/m²K<sup>4</sup>), der mittleren
Außenoberflächentemperatur $T_{se}$ und der mittleren Himmelstemperatur $T_{sky}$ in Kelvin.

$$ \alpha_{r} = \epsilon \cdot 4 \cdot \sigma \cdot \left(\frac{T_{se} + T_{sky}}{2}\right)^{3} $$ (alpha_r_eq)

Für übliche Verhältnisse kann der radiative Wärmeübergangskoeffizient jedoch angenähert werden zu:

$$ \alpha_{r} \approx 5 \cdot \epsilon $$




