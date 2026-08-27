

# Materialparameter


## Wärmeleitfähigkeit

Die Wärmeleitfähigkeit W/(K*m) ist von Material zu Material unterschiedlich und beschreibt, welcher Wärmestrom pro Längeneinheit eines Materials übertragen werden kann. Grundlegend wurde λ im Jahr 1822 von J. B. Fourier in Abhängikeit zur Temperatur und Druckabhängigkeit mit dem Wärmeleitfähigkeit beschrieben [1]. Zur Berechnung der Wärmestromdichte in Feststoffen (weil im Skript genutzt) werden Wärmeleitung, Wärmestrahlung und Wärmekonvektion, welche dem Gradienten der Temperatur proportional ist, genutzt und daraus das Fourier´sche Gesetz abgeleitet [2]: 

$$ \dot{q} = - \lambda \cdot \nabla T $$
[2]
### Messung
Die Wärmeleitfähigkeit kann durch die Messung der Wärmestromdichte mehrerer analytischer Methoden bestimmt werden. Welche Methode genutzt wird, hängt stark von Material und Aufbau ab. Grundlegend ist das Prinzip der Messmethoden einfach: Eine Probe wird unter definierten Randbedingungen einem bekannten Wärmeeintrag ausgesetzt und aus der Temperaturdifferenz der Platten der Wärmestrom bestimmt [3]. 
Die gängigsten analytischen Verfahren für die Bestimmung der Wärmeleitfähigkeit [6]:
- Palttengerät nach ISO 8302;
- Wärmestrommessplatte-Gerät nach ISO 8301;
- geregelter oder kalibrierter Heizkasten nach ISO 8990.

Nach Bestimmung des Wärmestroms kann die Wärmeleitfähigkeit mittels folgender Formel abgeleitet werden:

$$
\lambda = \frac{Q \cdot l}{A \cdot t \cdot \Delta T}
$$

Mit den Definitionen

$$
\dot{q} = \frac{Q}{t \cdot A}, \quad
l = \Delta x, \quad
\frac{\Delta T}{\Delta x} = \nabla T
$$

lässt sich dies schrittweise umformen:

$$
\lambda = \frac{\dot{q} \cdot l}{\Delta T}
$$

$$
\lambda = \frac{\dot{q} \cdot \Delta x}{\Delta T}
$$

$$
\lambda = \frac{\dot{q}}{\frac{\Delta T}{\Delta x}}
= \frac{\dot{q}}{\nabla T}
$$
[3]

Um normgerecht bauen zu können, ist der Einfluss von Feuchteeinträgen in Bauteilen in bezug auf die Wärmeleitfähigkeit von großen Interesse. Dieser Zusammenhang erschließt sich mit dem Gedanken, dass Fluide und Gase unterschiedlich effizient Energie leiten und somit dass λ nicht nur von Druck und Temperatur abhängig ist, sondern auch vom Leitwert des spezifischen Gases oder Fluids, welches in den Porenzwischenräumen in einem Material mit eingeschlossen ist. (Bei zunehmenden Wassergehalt verringert sich die Wärmestrahlung, sowie -konvektion und die Wärmeleitung nimmt zu, da die Wärmeleitfähigkeit des Wassers größer ist als die des Luftgemisches). Um Wärmeleitkoeffizienten von verschiedenen Materialien mit Feuchteeintrag zu bestimmen, wird entweder bei bekannter Struktur des Materials die trockene Probe bemessen und mittels der Konzentration und des Feuchtigkeitsverhältnisses bestimmt:

$$ \lambda = \lambda_\text{trocken} + c \cdot \frac{w}{w_\text{trocken}} $$

Oder eine trockene und eine gesättigte Probe werden gemessen und die analysiert, wie sich die Leitfähigkeit je nach Feutigkeitsverhältnis ändert [4]. 



## Die spezifische Wärmekapazität

Die spez. Wärmekapazität ist eine Messgröße und gibt an in wie weit Moleküle eines Mediums die Fähigkeit haben Energie speichern zu können. Dieser Wert ist wichtig, da die Wärmekapaziät die Enthalpie mit dessen Temperatur verknüpft.

Es gibt zwei verschiedene Ansätze zur Beschreibung der Wärmekapazität idealer Gase: die isobare Wärmekapazität $c_p$ ​ bei konstantem Druck und die isochore Wärmekapazität $c_v$ ​ bei konstantem Volumen. Im Folgenden liegt der Fokus auf $c_p$ ​ , das angibt, wie viel Wärme pro Masseeinheit benötigt wird, um ein Gas bei konstantem Druck um eine bestimmte Temperatur zu erwärmen. $c_p$ ​ hängt im Wesentlichen nur von der Temperatur ab und steigt mit ihr meist an, weil bei höheren Temperaturen zusätzliche Molekülschwingungen angeregt werden. [5] 

### Messung 

Die Bestimmung der Wärmekapazität erfolgt durch die Messung des Wärmestroms und der Heizrate. Der Quotient aus beiden Größen liefert die erforderliche Wärmemenge pro Temperaturänderung $(dQ/dT)_p$, aus der sich bei bekannter Probenmasse $m$ die spezifische Wärmekapazität $c_p$ berechnen lässt. Diese Methode liegt meist der dynamischen Differenzkalorimetrie (DSC) zugrunde, bei der Wärmestrom $(dQ/dt)$ und Heizrate $(dT/dt)$ kontinuierlich über den Temperaturbereich aufgezeichnet werden:

$$ c_p = m^{-1} \cdot C_p = m^{-1} \cdot (\frac{dQ}{dT})_p$$

$C_p$: die Gesamtwärmekapazität [$kJ  \cdot K^{-1}$]

$(\frac{dQ}{dT})_p$: Die erforderliche Wärmemenge $dQ$, um die Temperatur der Substanz um $dT$ zu erhöhen[$kJ \cdot  K^{-1}$]

Diese Gleichung gilt in einem Temperaturbereich, in dem die Substanz keinen Phasenübergang erster Ordnung zeigt.

Der Quotient $(\frac{dQ}{dT})$ kann durch Division des Wärmestroms durch die Heizrate erhalten werden:

$$(dQ/dT) = \frac{(dQ/dt)}{(dT/dt)}$$

$(dQ/dt)$: Der Wärmestrom[$kJ \cdot s^{-1}$]

$(dT/dt)$: Die Heizrate [$K \cdot s^{-1}$].

Die Messwerte für $c_p$ können aus der  ÖNORM EN ISO 10456 [6] entnommen werden.


## Feuchtetransport von Wasserdampf
Der Feuchtetransport innerhalb poröser Bauteile erfolgt in Gasphase hauptsächlich durch Diffusion. Die thermische Eigenbewegung von Molekülen führen bei einer Konzentrationsdifferenz zu einem Teilchenstrom, welcher als Ausgleichprozess verstanden werden kann. [2]

Formal lässt sich Diffusion eines Stoffes A als Relativbewegung seiner mittleren Teilgeschwindigkeiten $w_A$ gegenüber einer Bezugsgeschwindigkeit $w$ beschreibe. Die Diffusionsstromdichte ist dann definiert als [1]
$$ j_A := c_A   \cdot (w_A - w)$$
$j_A$: Diffusionsstromdichte des Stoffes A [$\frac{mol}{m^2 \cdot s}$]

$c_A$: Molare Konzentration des Stoffes A   [$\frac{mol}{m^3}$]

Für das Zweistoffgemisch Wasserdampf-Luft folgt aus dem Fick´schen Gesetz, dass die Diffusion proportional zum Konzentrationsgradienten ist [1]:
$$j_A = -D_{AB}   \cdot \frac{(dc_A)}{(dy)}$$

$D_AB$: Diffusionskoeffizient im Gemisch A-B [$\frac{m^2}{s}$]

Diese Beziehung wird meist über den Wasserdampfpartialdruck $p_v$ statt über die Konzentration formuliert, da sich der Partialdruck messtechnisch leichter erfassen lässt. Mit der thermischen Zustandsgleichung idealer Gase $c_v = \frac{(p_v)}{(R_v \cdot T)}$ ergibt sich die Wasserdampfstromdichte in freier, ruhiger Luft zu [1]
$$ j_v = - \frac{(D_v(T))}{R_v \cdot T}$$
$D_v(T)$: Temperaturabhängiger Diffusionskoeffizient von Wasserdampf in Luft [$\frac{m^2}{s}$]

$R_v$: Spezifische Gaskonstante von Wasserdampf[$\frac{J}{kg \cdot K}$]

Im Porenraum eines Baustoffs wird die Diffusion durch die Feststoffmatrix teils unterbrochen. Dieser Effekt entsteht durch die Porösität, welche angibt, welcher Anteil der Querschnittsfläche überhaupt durchlässig ist. In Folge dessen gibt die die Tortousität als  Maß für die Länge der tatsächlichen Diffusionswege im Vergleich zum direkten, geradlinigen Weg, die "Umwege" der Diffusionsgradienten an [2].

Beide Effekte werden in der Bauphysik nicht getrennt behandelt, sondern zusammenfassend in der Wasserdampfdiffusionswiderstandszahl $\mu$
erfasst.$\mu$ gibt das Verhältnis der Diffusionsstromdichte in ruhiger, freier Luft zu jener im porösen Medium an. Sie beschreibt also, um welchen Faktor der Baustoff die Diffusion gegenüber freier Luft behindert [2].

Damit lässt sich Gleichung (3) auf poröse Materialien erweitern:

$$ j_v = - \frac{D_v(T)}{\mu  \cdot R_v \cdot T}$$

Der Diffusionskoeffizient von Wasserdampf in Luft $D_v(T)$, nimmt mit der Temperatur zu. Da diese Zunahme in guter Näherung linear angenommen werden kann, lässt sich der temperaturabhängige Vorfaktor $\frac{D_v(T)}{R_v \cdot T}$ für praktische Anwendungen als näherungsweise konstant zusammenfassen[2]. Man definiert dazu die Wasserdampfpermeabilität der Luft $\delta_a$, sodass sich Gleichung (4) vereinfacht zu

$$ j_v = -\frac{\delta_a}{\mu} \cdot \nabla p_v$$

Die Gleichung zeigt, dass der Feuchtestrom durch ein Bauteil allein vom Partialdruckgefälle des Wasserdamps und der materialspezifischen $\mu$-Wert bestimmt wird [2].

##  Feuchtespeicherung

Die Speicherung von Feuchte in Baustoffen kann im festen, flüssigen oder gasförmigen zustand vorliegen. Je nachdem, welcher Zustand im Porenraum vorherrscht, ändert sich grundlegend, wie das Wasser im Material gebunden ist und wie es sich fortbewegt. Deshalb unterscheidet man mehrere charakteristische Feuchtebereiche, die jeweils einen eigenen Speicher- und Transportmechanismus beschreiben [2].

Die Feuchtigkeitsbereiche werden durch die Feuchtespeicherfunktion für den gesamten Feuchtebereich generieren. Sie besteht aus der Sorptionsisotherme und der Saugspannungsmessung [2].

## Die Sorptionsisotherme 
Die Sorptionsisotherme wird Messtechnisch bestimmt und beschreibt den Feuchtegehalt an der inneren Oberflächde eines Baustoffs als Funktion der relativen Luftfeuchte bei konstanter Temperatur [2]. 

Das Messprinzip der Sorptionsisotherme wird in der EN ISO 12571 beschrieben und gibt an in welcher Luftfeuchte oder Konstantklimate über wässrigen Lösungen spezielle Geräte konfiguriert werden müssen. Ziel ist es damit Materialproben bis zum Gleichgewicht einzulagern und in Folge den Wassergehalt zu bestimmen [2].

Es gibt zwei grundlegende Prozesse, mit denen ein Baustoff Feuchte mit der umgebenden Luft austauscht. Die Adsorption, bei der Wasserdampfmoleküle bei steigender Luftfeuchte an den inneren Oberflächen andocken und der Feuchtegehalt im Baustoff zunimmt, und Desorption, bei der das Material diese Feuchte bei sinkender Luftfeuchte wieder abgibt. Beide Vorgänge zusammen bilden die Sorptionsisotherme und geben genau den Feuchtebereich an, in dem ein Baustoff Wasser ausschließlich über Adsorption aus der umgebenden Luft aufnimmt bis dieser das Feuchtegleichgewicht erreicht. Der sogenannte hygroskopische Feuchtebereich erstreckt sich von 0\% relativer Luftfeuchte bis zu einerr Gleichgewichtsfeuchte von etwa 95\%. Wenn die Umgebungsluftfeuchte jedoch abnimmt, gibt das Material die eingelagerte Feuchte wieder ab, also disorbiert (ist das ein wort?). Dieser Prozess findet ebenfalls nur innerhalb des Sorptionsfeuchtebereichs statt [2][7]. 

Ab einer relativen Luftfeuchte von etwa 95\% beginnt der überhygroskopische Feuchtebereich. In diesem Bereich wird Wasser durch Feuchteretention durch die Kapillarkräfte innerhalb von Poren gehalten und lagern sich somit nicht nur an den Oberflächen ab. Dieser Effekt zeigt sich in der Feuchtespeicherfunktion als die Saugspannungskurve, welche den Kapillarwasserbereich charakterisiert. Um die Saugspannungskurve festzulegen muss bemessen werden. Hierbei werden gesättigte Proben durch Anlegen eines externen Drucks bis uzum Gelichgewicht befeuchtet. Die Messmethoden sind in ISO 11274 genormt [2][7]. 

Über dem Kapillarwasserbereich liegt der Übersättigungsbereich, der über die freie Wassersättigung hinausgeht und nur unter besonderen Bedingungen, wie etwa durch äußeren Druck oder Unterdruck, durch sehr lange Wasserlagerung (bei der eingeschlossene Porenluft sich allmählich im Wasser löst und entweicht) oder durch Kondensation beim Unterschreiten des Taupunkts, erreicht werden kann [2][8]. Im Gegensatz zum Kapillarwasserbereich, der sich über eine eindeutige Saugspannungskurve beschreiben lässt, existiert im Übersättigungsbereich kein stabiler Gleichgewichtszustand mehr, die relative Luftfeuchte liegt konstant bei 100%.. Erst durch das vollständige Verdrängen der restlichen, in feinsten Poren eingeschlossenen Luft wird schließlich die maximale Sättigung erreicht, bei dieser der gesamte offene Porenraum mit Wasser gefüllt ist [8].

 
## Approximation der Feuchtespeicherfunktion
 
Die Feuchtespeicherfunktion lässt sich durch folgende Gleichung an jeweilige Materialien approximieren [7]:


$$ u(p_c) = \frac{u_f}{1+\frac{p_c}{p_{k1}}} = \frac{u_f}{1+(\frac{\rho_w \cdot R_D \cdot T \cdot ln(\phi)}{p_{k1}})^{pk1}}$$

$p_{k1}, p_{k2}$: freie Parameter [-]

$R_D$: Gaskonstante für Wasserdampf [$\frac{J}{kg\cdot K}$]

$T$: absolute Temperatur [K]

$u_f$: freie kapillare Wassersättigung [$\frac{kg}{m^3}$]

$\rho_w$: Dichte von Wasser [$\frac{kg}{m^3}$]

$\varphi$: relative Luftfeuchte [-]

$p_c$: Kapillardruck [Pa]

Die beiden freien Parameter $p_{k1}$ und $p_{k2}$ werden materialspezifisch berechnet, indem man die beiden gemessenen Sorptionsfeuchten bei 80% und 95% relativer Luftfeuchte in die Gleichung einsetzt. [7]







[1]: Baehr, H.D. and Stephan, K. (10. Aufl.) Wärme- und Stoffübertragung. Berlin, Heidelberg: Springer

[2]: WTA (2014) Merkblatt 6-2: Simulation wärme- und feuchtetechnischer Prozesse (Ausgabe 12/2014/D). Wissenschaftlich-Technische Arbeitsgemeinschaft für Bauwerkserhaltung und Denkmalpflege.

[3]: Salmon, D. (2001) Thermal conductivity of insulations using guarded hot plate apparatus. Measurement Science and Technology, 12(12). doi:10.1088/0957-0233/12/12/201.

[4]: Künzel, H.M. (1995) Simultaneous heat and moisture transport in building components: One- and two-dimensional calculation using simple parameters. Stuttgart: Fraunhofer Institute of Building Physics.

[5] Stephan, P., Kabelac, S., Kind, M., Mewes, D., Schaber, K. und Wetzel, T. (Hrsg.) (2019) VDI-Wärmeatlas (12. Auflage). Berlin, Heidelberg: Springer Vieweg.

[6]: ÖNORM EN ISO 10456 (2010) Baustoffe und Bauprodukte – Wärme- und feuchtetechnische Eigenschaften – Tabellierte Bemessungswerte und Verfahren zur Bestimmung der wärmeschutztechnischen Nenn- und Bemessungswerte (ISO 10456:2007 + Cor 1:2009, konsolidierte Fassung, Ausgabe 2010-02-15). Wien: Austrian Standards International.

[7]: Holm, A.; Krus, M.; Künzel, H.M.: Approximation der Feuchtespeicherfunktion aus einfach bestimmbaren Kennwerten. IBP-Mitteilung, 29 (2002), Nr. 406. Fraunhofer-Institut für Bauphysik (IBP), Stuttgart/Holzkirchen.

[8]: Krus, M.; Künzel, H.M.: Flüssigtransport im Übersättigungsbereich. IBP-Mitteilung, 22 (1995), Nr. 270. Fraunhofer-Institut für Bauphysik (IBP), Stuttgart/Holzkirchen.
