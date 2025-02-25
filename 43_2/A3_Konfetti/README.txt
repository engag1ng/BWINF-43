Jede Datei beschreibt einen zerschnittenen Aushang und ist so aufgebaut:

1. Zeile: Zwei ganze Zahlen r und c, sowie ein Zeichen t:

	r ist die Anzahl der Personen = Zeilen des Aushangs.

	c ist die Anzahl der Termine = Spalten des Aushangs.

	t gibt an, ob Annas Zeile in dem Beispiel bekannt (y) oder unbekannt (n) ist.

Folgende r Zeilen: Jeweils c durch Leerzeichen getrennte Zeichen. y steht für einen möglichen, n für einen unmöglichen Zeitslot, ? für ein unleserliches Zeichen.

Wenn Annas Zeile nicht bekannt ist, ist die Beschreibung des Aushangs abgeschlossen

Ist Annas Zeile bekannt, folgt eine letzte Zeile: Annas richtig geordnete Terminangaben wieder mit möglichen (y) und unmöglichen (n) Zeitslots, sowie ggf. ? bei unleserlichen Zeichen. Diese Angabe entspricht der ersten Zeile der r Zeilen, allerdings mit der korrekten Anordnung der Spalten.

Hier eine Erklärung zu konfetti00.txt, das Beispiel vom Aufgabenblatt zu Teilaufgabe d :

4 4 n
n y n n
y y ? n
y n n y
y n y n

In diesem Beispiel gibt es vier Personen und vier mögliche Zeitslots. Anna weiß ihre eigenen Angaben nicht mehr. Die erste Person hat an drei von vier Zeitslots keine Zeit. Die zweite Person hat an zwei Zeitslots sicher Zeit, eine Angabe ist unleserlich und einmal hat sie keine Zeit. Person drei und vier können jeweils an zwei von vier Zeitslots.

Die hohe Anzahl an Beispielen resultiert aus den Teilaufgaben dieser Aufgabe. Wir erwarten in der Dokumentation folgende Ausgaben bei den Teilaufgaben:
Teilaufgabe a & b: konfetti01.txt - konfetti05.txt
Teilaufgabe c: konfetti06.txt & konfetti07.txt
Teilaufgabe c & d: konfetti08.txt & konfetti12.txt
Teilaufgabe d: konfetti09.txt - konfetti11.txt und konfetti00.txt
Teilaufgabe e: konfetti13.txt und alle bisher “nicht lösbaren” Beispiele.

Ist ein Beispiel lösbar, wird eine zulässige Anordnung als Ausgabe erwartet, ansonsten ein Hinweis auf Unlösbarkeit.