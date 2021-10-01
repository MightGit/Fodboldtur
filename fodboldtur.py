import pickle

filename = 'betalinger.pk'

fodboldtur ={}

def afslut(): #for at af slutte programmet
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste(): #def for printliste funktion
    for item in fodboldtur.items():
        print(item)
    menu()

def menu(): #defination for menuen
    print("MENU")
    print("1: Print liste")
    print("2: Afslut program")
    print("3 Skift beløb")
    print("4 Tilføj navne")
    #printer valg eller decisions for vore code

    valg = input("Indtast dit valg:")
    if (valg == '1'):
        printliste()
    if (valg == '2'):
        afslut()
    if (valg == '3'): #If state for at tjekke input
        print('Hvem skal beløbet blive skiftet ved?')
        printliste()
        name = input("Skriv navn") # vi skal bruge name til at bruge den til at finde navne i files, plus det bruges til at skifte det fra en input
        if name in fodboldtur: #If statement igen for at tjekke i listen
            pris = int(input("Hvor meget skal skiftes?"))  #int statement for at ændre beløb
            if pris == 0: # 0 for at tjek om det rigtig, ellers error
                valg = input("Forkert beløb, prøv igen tak") #Hvis 0 bliver skrevet slukker programmet med forkert beløb
            else:
                fodboldtur[name] += pris #Hvis gjort rigtigt gemmer den navn og pris
                menu()

            menu()

    if (valg == '4'):
        name = input("Skriv navn du vil add")
        fodboldtur[name] = 0 #Giver pris til ny person som bliver added
        printliste() #printer listen for at vise navne der allerede er der
        menu()

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()
