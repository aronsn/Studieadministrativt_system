def registrer():
    #Åpne student.txt og skriver inn opplysninger
    studentfil = open("Student.txt","a")

    studentfil.write(studnr + "\n")
    studentfil.write(fornavn + "\n")
    studentfil.write(etternavn + "\n")
    studentfil.write(studium + "\n")

    studentfil.close()
    print()
    print("Opplysningene som er blitt skrevet inn og er nå lagret på Student.txt")
    print()
    
#Menysystem for å navigere til de ulike funskjonene i programmet
studiesystem=True
while studiesystem:
    print(">- - - - - - - - - Meny - - - - - - - - - - -<")
    print("1 for å registrere opplysninger om en student")
    print("2 for å slette en student")
    print("3 for å skrive ut karakterliste for en student")
    print("0 for å avslutte programmet")
    
    systemvalg=int(input("Skriv inn din handling: "))
    if systemvalg < 0 or systemvalg > 3:
        
        print()
        print("Handlingen er ugyldig, prøv igjen...")
        print()
        
    elif systemvalg == 0:
        studiesystem=False
        print("Programmet er avsluttet...")
        
    else:
        studiesystem=False

    #Løkke får å registrere opplysningene til en student
    while systemvalg == 1:
        print()
        print("Du har valgt å registrere student.")
        print()
        
        studnr=input("Skriv inn studentnummeret: ")

        #Søker om opplysningene finnes fra før i Student.txt
        funnet=False
        studsøk=studnr
        studentfil=open("Student.txt", "r")
        søkstudnr=studentfil.readline()

        while søkstudnr != "":
            
            søkfornavn=studentfil.readline()
            søketternavn=studentfil.readline()
            søkstudium=studentfil.readline()

            søkstudnr=søkstudnr.rstrip("\n")
            søkfornavn=søkfornavn.rstrip("\n")
            søketternavn=søketternavn.rstrip("\n")

            if søkstudnr == studsøk:
                print("Dette studentnummeret eksisterer.")
                print()
                print(søkstudnr)
                print(søkfornavn)
                print(søketternavn)
                print(søkstudium)

                funnet = True

            søkstudnr=studentfil.readline()

        studentfil.close()
        #Fortsetter registreringen om ikke studenten finnes
        if not funnet:
            fornavn=input("Skriv inn Fornavn: ")
            etternavn=input("Skriv inn Etternavn: ")
            studium=input("Skriv inn Studium: ")

            registrer()

            systemvalg = False
            
        #Undermeny (1) Kan føre bruker tilbake til hovedmeny
        #Eller registrere ny student
        print()
        print("1 for å registrere en ny student")
        print("2 for å gå tilbake til hovedmeny'en")
        print("0 for å avslutte programmet")
        
        undermeny=int(input("Skriv inn din handling: "))
        print()

        if undermeny == 1:
            studiesystem=False
            systemvalg=True
            
        elif undermeny == 2:
            systemvalg=False
            studiesystem=True

        elif undermeny == 0:
            systemvalg=False
            studiesystem=False
            print("Programmet er avsluttet...")
            
    #Løkke for å kunne slette student
    while systemvalg == 2:
        print()
        print("Du har valgt å slette en student")
        print()

        studnr=input("Skriv inn studentnummeret: ")
        
        #Søker om opplysningene finnes fra før i Eksamensresultat.txt
        funnet=False
        studsøk=studnr
        studentfil=open("Eksamensresultat.txt", "r")
        søkemnekode=studentfil.readline()

        while søkemnekode != "":
            
            søkstudnr=studentfil.readline()
            søkkarakter=studentfil.readline()

            søkemnekode=søkemnekode.rstrip("\n")
            søkstudnr=søkstudnr.rstrip("\n")
          

            if søkstudnr == studsøk:
                print()
                funnet = True

            søkemnekode=studentfil.readline()

        studentfil.close()
        if funnet:
            print("Dette studentnummeret har eksamensresultat.")
            print("Kan ikke slettes...")
            print()
            
        #Kan slette student, om studenten ikke har noen eksamensresultat
        if not funnet:
            print()
            print("Denne studenten har ikke noen eksamensresultat")
            
            import os
            funnet2=False
            #Åpner filen der data'en er lagret
            studentfil=open("Student.txt", "r")
            #Åpner en midlertidig fil der data'en skal overføres
            midlertidigfil=open("midlertidig.txt", "w")
            
            #Skriver inn data'en som ikke skal slettes og overfører det til 'midlertidig.txt'
            søkstudnr=studentfil.readline()      
            while søkstudnr != "":
                søkstudnr=søkstudnr.rstrip("\n")

                if søkstudnr != studnr:
                    midlertidigfil.write(søkstudnr + "\n")
                else:
                    funnet2=True
                    søkstudnr=studentfil.readline()
                    søkstudnr=studentfil.readline()
                    søkstudnr=studentfil.readline()
                   
                søkstudnr=studentfil.readline()
            studentfil.close()
            midlertidigfil.close()
            #Sletter 'Student.txt' og endrer 'midlertidig.txt' til nye 'Student.txt'
            os.remove("Student.txt")
            os.rename("midlertidig.txt", "Student.txt")

            if funnet2:
                print()
                print("Filen har blitt oppdatert")
                print()
            else:
                print()
                print("Denne studenten har ikke noen opplysninger i 'Student.txt' ")
                print()

        #Undermeny (2) Kan føre bruker tilbake til hovedmeny
        #Eller slette en ny student
        print("1 for å slette en ny student")
        print("2 for å gå tilbake til hovedmeny'en")
        print("0 for å avslutte programmet")
        
        undermeny2=int(input("Skriv inn din handling: "))
        print()

        if undermeny2 == 1:
            systemvalg=2
        
        elif undermeny2 == 2:
            systemvalg=False
            studiesystem=True

        elif undermeny2 == 0:
            systemvalg=False
            studiesystem=False
            print("Programmet er avsluttet...")
            
    #Løkke for å skrive ut karakterliste for student
    while systemvalg == 3:
        print()
        print("Du har valgt å registrere student.")
        print()
        
        studnr=input("Skriv inn studentnummeret: ")
        print()
        funnet=False
        #Tester om studenten finnes i 'student.txt' før den gjennomfører søk i 'eksamensresultater.txt' og 'emne.txt'
        studentfil=open("Student.txt", "r")
        studnrsøk=studentfil.readline()

        while studnrsøk != "":
            studnrsøk=studnrsøk.rstrip("\n")
            
            if studnrsøk == studnr:
                studnrlag = studnrsøk
                
                fornavnlag = studentfil.readline()
                etternavnlag = studentfil.readline()
                studiumlag = studentfil.readline()
                funnet=True
                
            studnrsøk=studentfil.readline()
        studentfil.close()

        #Utskrift av hentet data fra 'student.txt', hvis studenten finnes
        if funnet:
            fornavnlag=fornavnlag.rstrip("\n")
            etternavnlag=etternavnlag.rstrip("\n")
            studiumlag=studiumlag.rstrip("\n")
            
            print("Studentnummer:", studnrlag)
            print("Fornavn:", fornavnlag)
            print("Etternavn:", etternavnlag)
            print("Studium:", studiumlag)
            print()
            #Søker 'eksamensresultat.txt' for å se studentens karakterer
            exfil=open("Eksamensresultat.txt", "r")
            
            søkkarakter=exfil.readline()
            
            while søkkarakter != "":
                søkkarakter=søkkarakter.rstrip("\n")
                
                if søkkarakter == studnrlag:
                    exresultat=exfil.readline()
                    
                    søkemnekode = søkemnekode.rstrip("\n")
                    exresultat=exresultat.rstrip("\n")
                    

                    #Tar med dataen fra 'eksamensresultat.txt' og søker i 'Emne.txt'
                    emfil=open("Emne.txt", "r")
                    søkemnenavn=emfil.readline()
                    
                    while søkemnenavn != "":
                        søkemnenavn=søkemnenavn.rstrip("\n")
                        
                        if søkemnenavn == søkemnekode:
                            søkemnenavn2=emfil.readline()
                            søkemnenavn2=søkemnenavn2.rstrip("\n")
                        søkemnenavn=emfil.readline()
                        
                    emfil.close()
                    
                    print("Emnekode:", søkemnekode)
                    print("Emnenavn:", søkemnenavn2)
                    print("Karakter:", exresultat)
                    print()
                    
                   
                søkemnekode = søkkarakter
                søkkarakter=exfil.readline()
                
            exfil.close
         
        else:
            print("Dette studentnummeret finnes ikke")
            print()
            
        #Undermeny (3) Kan føre bruker tilbake til hovedmeny
        #Eller skrive ut en ny karakterliste
        print("1 for å skrive ut en ny karakterliste")
        print("2 for å gå tilbake til hovedmeny'en")
        print("0 for å avslutte programmet")
        
        undermeny3=int(input("Skriv inn din handling: "))
        print()

        if undermeny3 == 1:
            systemvalg=3
        
        elif undermeny3 == 2:
            systemvalg=False
            studiesystem=True

        elif undermeny3 == 0:
            systemvalg=False
            studiesystem=False
            print("Programmet er avsluttet...")

           

                        

                    
                    
                    
                    
            
                


                

                

                
                    

                
                


                



            
            
