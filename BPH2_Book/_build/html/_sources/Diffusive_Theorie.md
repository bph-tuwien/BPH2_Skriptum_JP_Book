# Theorethische Grundlagen des diffusiven Wärme- und Feuchtetransportes

Wenn eine Koppelung zwischen Wärme- und Feuchtetransport in einer Berechnung besteht spricht man allgemein von einer
hygrothermischen Simulation. Diese Koppelung bringt den Vorteil, dass der Einfluss des Feuchtegehaltes auf die
Wärmeleitfähigkeit berücksichtigt werden kann. Die Differentialgleichungen, welche für solche Berechnungen miteinander
gekoppelt werden müssen, werden im folgenden vorgestellt, mit dem Ziel ein Verständnis für die unterliegenden Grundlagen
und Konzepte zu vermitteln.

## Allgemeine Transportgleichungen Diffusion

### Wärmetransport

Bei Betrachtung der Wärmeleitung ergibt sich aus Gleichung {eq}`delta_V_q_eq`

$$ \rho c \frac{\partial T}{\partial t} = -\nabla \cdot q + h $$(dT_eq)

Dabei beschreibt $h$ (J/(m³s)) eine Wärmequelle. Diese kann ausgelöst sein durch mechanisches Heizen, chemische
Reaktionen etc. Der Wärmefluss q (J/(m²s) ist für den diffusiven eindimensionalen Fall definiert als

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

## Numerische Lösung einer partiellen Differentialgleichung am Beispiel der Wärmeleitung

## Randbedingungen