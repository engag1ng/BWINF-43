Jede Datei beschreibt die beiden Labyrinthe. In der 1. Zeile werden Breite n und Höhe m der beiden Labyrinthe angegeben. Danach werden die Labyrinthe nacheinander jeweils so definiert:

m Zeilen mit je n-1 Einträgen: Für jede Labyrinthzeile wird für jedes Feld angegeben, ob rechts davon eine vertikale Wand ist oder nicht. Eine 1 steht für eine Wand, eine 0 für keine Wand.

m-1 Zeilen mit je n Einträgen: Für jede Labyrinthzeile wird für jedes Feld angegeben, ob unterhalb des Feldes eine horizontale Wand ist oder nicht. Eine 1 steht für eine Wand, eine 0 für keine Wand.

1 Zeile: Anzahl g der Gruben.

g Zeilen: Pro Zeile die Koordinate einer Gruben im Labyrinth im Format x y. Die Koordinate (0,0) entspricht der Startposition, also der oberen linken Eckposition. Gibt es keine Gruben, folgen direkt die Angaben für das zweite Labyrinth beginnend bei den Angaben zu den vertikalen Wänden.

Die Datei labyrinthe0.txt entspricht dem Beispiel aus der Aufgabenstellung und wird hier erläutert. Die Zeilennummerierung ist in den Dateien nicht enthalten und dient der besseren Verständlichkeit der Beschreibung. Für eine visuelle Unterstützung bietet es sich an, die Aufgabenstellung vorliegen zu haben.

 1: 3 3
 2: 1 0
 3: 1 1
 4: 0 1
 5: 0 0 0
 6: 0 0 0
 7: 0
 8: 1 0
 9: 0 1
10: 0 0
11: 0 0 0
12: 1 1 0
13: 1
14: 0 2

Es handelt sich um zwei Labyrinthe mit den Maßen 3 x 3. Zeile 2 bis 4 beschreiben die vertikalen Wände in den einzelnen Labyrinthzeilen des ersten Labyrinths. Beispielsweise ist in der ersten Labyrinthzeile zwischen dem ersten und zweiten Feld eine Wand, zwischen dem zweiten und dritten Feld nicht. Zeile 5 und 6 beschreiben die horizontalen Wände des ersten Labyrinths. In diesem Labyrinth sind keine horizontalen Wände vorhanden. Die 0 in Zeile 7 sagt aus, dass es keine Gruben gibt. Damit ist die Beschreibung des ersten Labyrinths abgeschlossen.
Es folgen in Zeile 8 bis 10 direkt die Angaben für die vertikalen Wände des zweiten Labyrinths. Aus Zeile 12 ist ersichtlich, dass an Position eins und zwei unterhalb der zweiten Labyrinthzeile im zweiten Labyrinth Wände existieren. Zeile 13 gibt an, dass es im zweiten Labyrinth eine Grube gibt. Sie ist laut Zeile 14 an Position (0,2).