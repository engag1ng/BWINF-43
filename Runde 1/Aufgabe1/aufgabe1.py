import tkinter as tk
def is_hopsitext(text):
    """
    Überprüft ob ein eingegebener Text ein Hopsitext ist.

    text                 -- Der zu überprüfende Text
    player1              -- Speichert den aktuellen Index auf dem sich Spieler1 befindet
    player2              -- Speichert den aktuellen Index auf dem sich Spieler2 befindet
    kein_hopsitext       -- Boolean Wert der angibt ob der Text ein Hopsitext ist 
                            (False) oder nicht (True)
    kein_hopsitext_index -- Integer welcher angibt bei welchem Index im Text 
                            kein_hopsitext True wird.
    """
    player1 = 0
    player2 = 1
    for index, item in enumerate(list(text)):
        if player1 != player2:
            alert_label.config(text="")
            kein_hopsitext = False

        if player1 == player2:
            if kein_hopsitext == False:
                kein_hopsitext_index = index
            kein_hopsitext = True
            alert_label.config(text=f"ALARM: Kein Hopsitext bei Index '{kein_hopsitext_index}'")

        if item not in letter_dict:
            player1 += 1    
            player2 += 1

        if index == player1:
            player1 += letter_dict.get(item)
        if index == player2:
            player2 += letter_dict.get(item)

    return not kein_hopsitext

def text_ändern(event):
    """
    Speichert den eingegeben Text, die aktuelle Textlänge und evaluierte Textlänge. 
    Ändert außerdem den das index_label basierend auf der aktuellen Textlänge. 
    Löst wenn nötig die is_hopsitext Funktion aus.

    text_eingabe         -- Enthält den Text aus dem Textfeld
    aktuelle_textlänge   -- Ist die aktuelle Textlänge in Zeichen
    evaluierte_textlänge -- Ist die Textlänge die schon auf einen 
                            Hopsitext überprüft wurde
    """
    global evaluierte_textlänge
    text_eingabe = text_feld.get("1.0", tk.END)
    aktuelle_textlänge = len(list(text_eingabe))
    index_label.config(text=str(aktuelle_textlänge-1)) # von der aktuellen_textlänge wird 1 subtriert, da Textlänge bei 1 und Index bei 0 startet.

    if aktuelle_textlänge > evaluierte_textlänge: # Wenn neuer Text hinzugefügt wurde
        is_hopsitext(text_eingabe)
    evaluierte_textlänge = aktuelle_textlänge


evaluierte_textlänge = 0
kein_hopsitext = False
letter_dict = { #Speichert alle Buchstaben und ihre zugehörigen Sprungweiten
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
    'Ä': 27, 'ä': 27, 'Ö': 28, 'ö': 28, 'Ü': 29, 'ü': 29, 'ß': 30, 
}

# Definiert das Tkinter Fenster
fenster = tk.Tk()
fenster.title("Hopsitexte")
fenster.resizable(False, False)

# Definiert den Mainframe
frame = tk.Frame(fenster)
frame.pack(pady=10)

# Definiertdas Eingabefeld
text_feld = tk.Text(frame)
text_feld.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Ermöglichst das scrollen bei langen Texten
scrollbar = tk.Scrollbar(frame, command=text_feld.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_feld.config(yscrollcommand=scrollbar.set)

# Löst die Funktion text_ändern aus sobald der Text im Eingabefeld geändert wird
text_feld.bind("<KeyRelease>", text_ändern)

# Platzhalter Label für die Länge des Textes
index_label = tk.Label(fenster, text="", height=2)
index_label.pack(pady=5)
# Plathalter Label für den "Kein Hopsitext" Alarm
alert_label = tk.Label(fenster, text="", height=2, fg="red")
alert_label.pack(pady=5)

fenster.mainloop()