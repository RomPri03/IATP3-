notes = []
n = int(input("Nombre de notes : "))
for i in range(n):
    note = float(input(f"Note {i+1} : "))
    notes.append(note)
moyenne = sum(notes) / len(notes)
print(f"Moyenne : {moyenne}")