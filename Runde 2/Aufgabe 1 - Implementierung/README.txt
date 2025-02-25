Jede Datei enthält eine Botschaft und ist so aufgebaut:

1. Zeile: Anzahl n der verschiedenen Perlenarten.

2. Zeile: Der Durchmesser in mm je Perlenart.

3. Zeile: Die Botschaft.

Hier ein Beispiel:

4
1 2 2 5
Die Sonne. Sie scheint immer für dich.

In diesem Beispiel gibt es 4 verschiedene Perlenarten. Die erste Perlenart hat den Durchmesser 1mm, die zweite und dritte Perlenart haben 2mm Durchmesser und die letzte 5 mm. Für die Botschaft “Die Sonne. Sie scheint immer für dich." muss mit den gegebenen Perlen eine möglichst kurze Codierung gefunden werden.

Die Datei schmuck0.txt entspricht dem Beispiel aus der Aufgabenstellung.

Die Eingabedateien sind UTF-8 codiert ohne BOM am Anfang der Dateien. BOM besteht normalerweise aus drei Bytes, welche die Art der UTF-Codierung spezifizieren.

Jedes Unicode-Symbol gilt als Zeichen, welches codiert werden muss. In der Botschaft wurden Zeilenumbrüche durch Leerzeichen ersetzt, daher sind die Texte teilweise schwer lesbar.

Ein brauchbares Lösungsprogramm hat für zwei Beispieleingaben folgende Werte berechnet:
schmuck5.txt : 3162 mm
schmuck9.txt : 36597 mm