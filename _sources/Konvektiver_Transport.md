# Konvektiver Stofftransport und Wärmestransport

Der konvektive Transport von Wärme- und Feuchtigkeit ist einer der treibenden Prozesse bei der Entstehung von Schäden.
Konvektiver Transport ist immer von Luftdruck-Differenzen abhängig und kann, je nach seiner Größe, diffusive Prozessen
beschleunigen (Auffeuchtung), verlangsamen oder umkehren (Trocknung). Durch die schwere Beherrschbarkeit dieses
Phänomens ist eine der höchsten Prioritäten in der Planung die saubere Ausführung von luftdichten Hüllen, um somit die
Undruchströmbarkeit von Bauteilen zu gewährleisten. Durch Abnutzung während der Lebensdauer von Bauwerken oder auch
Ausführungsfehler können jedoch immer wieder ungewollte Strömungspfade entstehen. Um Bauteilen eine gewisse Redundanz
gegenüber dieser unvorhergesehener Leckagen zu ermöglichen wurde das Konzept der Fehlertoleranz von Bauteilen
entwickelt, welches insbesondere in der hygrothermischen Simulation einen besonderen Stellenwert hat.

```{figure} img/Wärmebrücke/psi_ex.png
---
height: 350px
name: psi_ex
---
Möglicher Luftpfad für Konvektion in einem vereinfachten Holz-Flachdachaufbau.
```

Die Beurteilung der hygrothermischen Simulationsergebnisse ist erst durch entsprechende Risikoanalysen möglich. Mit
Hilfe des Mould Index kann Risiko für Schimmelpilzbildung auf Oberflächen kategorisiert werden, Verrottungsrisiko und
Tragfähigkeit müssen ebenfals überprüft werden. Dem Mould Index wird in diesem Kapitel besondere Aufmerksamkeit
geschenkt, da dieses Modell (VTT-Modell) einem groß angelegten Forschungsprojekt entsprungen und sehr gut dokumentiert
ist. Des Weiteren ermöglicht die tiefere Auseinadersetzung mit dem VTT-Modell die Limitationen solcher Modelle im
allgemeinen besser zu verstehen und bei der Anwendung die Ergebnisse kritisch zu Hinterfragen.

```{figure} img/Konvektion/bt_sim.png
---
height: 250px
name: bt_sim
---
```

```{figure} img/Konvektion/bt_rot.png
---
height: 250px
name: bt_sim
---
Simulationsergebnis in Bezug auf das Risiko einer Schimmelpilzbildung: In der Bestandskonstruktion im Inneren 
herrschen entsprechende Temperaturen und Feuchtigkeiten über so lange Zeiträume, dass das Wachstum von Schimmelpilzen 
ermöglicht wird.
```

## Überblick über das Kapitel

Um eine Grundlage für das tiefere Verständnis dieser Konzepte zu schaffen werden die

- **Beschreibenden Differentialgleichungen auf die konvektiven Therme erweitert**

und die

- **Hintergründe zur vereinfachten Bescshreibung konvektiver Phänomene mittels Luftvolumenstromkoeffizienten**

und dadurch das

- **Vereinfachte Modell zu Abbildung von Leckagen in hygrothermischen Simulationen**

hergeleitet.

In Bezug auf die Anwendung wird die

- **Fehlertoleranz - Methoden um Redundanz zu gewährleisten**

diskutiert und

- **Methoden zur Risikoanalyse (Holzverrottung, Tragfähigkeit, Schimmelpilzbildung auf Oberflächen)**

dargelegt.


