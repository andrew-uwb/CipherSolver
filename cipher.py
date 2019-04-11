from collections import OrderedDict
import operator

class cryptogramSolver:

    def __init__(self):

        self.allLetters = list("abcdefghijklmnopqrstuvwxyz")

        self.samplingDictionary = {}

        for letter in self.allLetters:

            self.samplingDictionary[letter] = 0

        self.manuallySet = {}
        self.decodeDict = {}

    def decodeAttempt(self, testString):

        inputLetters = list(testString)
        letterFrequency = list("etaoinsrhdlucmfywgpvbkxqjz")

        for letter in inputLetters:

            if letter in self.samplingDictionary.keys():
                self.samplingDictionary[letter] += 1

        charList = OrderedDict(sorted(self.samplingDictionary.items(), key=operator.itemgetter(1), reverse=True))
        self.decodeDict = {}

        #print(charList)

        for nextLetter in self.manuallySet.keys():
            self.decodeDict[nextLetter] = self.manuallySet[nextLetter]

        for alreadySet in self.decodeDict.values():
            #print("Already set: " + alreadySet)
            if alreadySet in letterFrequency:
                letterFrequency.remove(alreadySet)

        #print(self.decodeDict)

        count = 0
        for nextItem in charList.keys():

            if nextItem not in self.decodeDict.keys():
                self.decodeDict[nextItem] = letterFrequency[count]
                count += 1

        ciphertext = ''.join(inputLetters)
        print(ciphertext.upper())
        for letter in inputLetters:
            if letter not in self.allLetters:
                print(letter, end="")
            else:
                printLetter = self.decodeDict[letter]
                if printLetter in self.manuallySet.values():
                    print(printLetter.upper(), end="")
                else:
                    print(printLetter.lower(), end="")

if __name__ == "__main__":

    solver = cryptogramSolver()
    cryptoString = "RNW GMKOWI EC EGW’P QEPPSOUW CDGRDPSWP SP SGLWIPWUX QIEQEIRSEGDU RE RNW DKEMGR EC EGW’P USVMSF DPPWRP. –PRDGSPUDH UWK"
    #cryptoString = "WCTWYC RTG’L AEX HQOL XTE RT, LQCX AEX HQX XTE RT UL."
    #cryptoString = "DZV KI IUFBVGKQX VGDV FDCBI EUT HZBDVGB RKVG D LKSSBZBQV CKQL US GDOOKQBII. –DQQK DWHBZI"
    #cryptoString = "SE’C DLCW EN ILOD L KPSDFZ. QVLE’C VLPZ EN ILOD SC L CEPLFADP. –LFNFWINJC"
    #cryptoString = "KUBXMJ SA XAM OIAN ZQIQUH MA JBMYJEH BZCYMYAXJ AI MA ETUEYUU OAAS YXMQXMYAXJ."
    #cryptoString = "GFS WMY OG LGDVS MF SFNKYHOSU ESLLMRS, PC WS BFGW POL DMFRQMRS, PL OG CPFU M UPCCSKSFO HDMPFOSXO GC OIS LMES DMFRQMRS DGFR SFGQRI OG CPDD GFS LISSO GK LG, MFU OISF WS NGQFO OIS GNNQKKSFNSL GC SMNI DSOOSK. WS NMDD OIS EGLO CKSJQSFODY GNNQKKPFR DSOOSK OIS 'CPKLO', OIS FSXO EGLO GNNQKKPFR DSOOSK OIS 'LSNGFU' OIS CGDDGWPFR EGLO GNNQKKPFR DSOOSK OIS 'OIPKU', MFU LG GF, QFOPD WS MNNGQFO CGK MDD OIS UPCCSKSFO DSOOSKL PF OIS HDMPFOSXO LMEHDS. OISF WS DGGB MO OIS NPHISK OSXO WS WMFO OG LGDVS MFU WS MDLG NDMLLPCY POL LYEAGDL. WS CPFU OIS EGLO GNNQKKPFR LYEAGD MFU NIMFRS PO OG OIS CGKE GC OIS 'CPKLO' DSOOSK GC OIS HDMPFOSXO LMEHDS, OIS FSXO EGLO NGEEGF LYEAGD PL NIMFRSU OG OIS CGKE GC OIS 'LSNGFU' DSOOSK, MFU OIS CGDDGWPFR EGLO NGEEGF LYEAGD PL NIMFRSU OG OIS CGKE GC OIS 'OIPKU' DSOOSK, MFU LG GF, QFOPD WS MNNGQFO CGK MDD LYEAGDL GC OIS NKYHOGRKME WS WMFO OG LGDVS."
    #cryptoString = "abc dedfcg d hig hdac djg dhk lj d hig mnhok"
    #cryptoString = "wkh sdvvzrug lv vhyhq grqw whoo dqbrqh"
    cryptoString = cryptoString.upper()

    keepGoing = True
    while(keepGoing):

        solver.decodeAttempt(cryptoString.lower())

        print("")
        userInput = str(input(">> "))

        if userInput == "q" or userInput == "quit":
            keepGoing = False
        elif userInput == "s" or userInput == "show":
            if solver.manuallySet:
                displayDict = OrderedDict(sorted(solver.manuallySet.items(), key=operator.itemgetter(1)))
                cryptText = displayDict.keys()
                plainText = displayDict.values()
                print("Ciphertext: ", end="")
                for i in cryptText:
                    print("%s " % str(i).upper(),end="")
                print("\nPlaintext:  ",end="")
                for i in plainText:
                    print("%s " % str(i).upper(),end="")
                print("")
            else:
                print("No values have been set.")
        elif userInput == "r" or userInput == "reset":
            solver.manuallySet = {}
        elif userInput == "help" or userInput == "man":
            print("*********MANUAL***********")
            print("This program guesses cryptograms based on a frequency analysis of the given ciphertext.\n")
            print("To replace all occurrences of 'a' in the ciphertext with 'b' in the plaintext, ")
            print("type 'a=b' and press Enter. Afterward, a will be assigned to b, and the program will assign all ")
            print("other letters based on frequency analysis. To undo a letter, type 'a=' and the letter ")
            print("a will no longer be assigned.\n")
            print("Assigned letters are capitalized in the plaintext. Letters assigned based on frequency analysis are ")
            print("in lowercase.\n")
            print("Valid Commands:\n")
            print("shift x: Replace 'x' with a number to perform a uniform shift in the decryption algorithm.")
            print("   i.e. shift=3 will give a=d,b=e,etc.")
            print("show: Show all assigned letters")
            print("reset: Clear all assigned letters")
            print("quit: Quit the application")
            print("**************************")
        elif userInput[0:6] == "shift ":
            shiftSplit = userInput.split(maxsplit=1)
            shiftAmt = int(shiftSplit[1])
            if shiftAmt > 25 or shiftAmt < -25:
                print("Shift must be between 25 and -25.")
            else:
                solver.manuallySet = {}
                count = 0
                for i in solver.allLetters:
                    location = (count + shiftAmt) % 26
                    solver.manuallySet[i] = solver.allLetters[location]
                    count += 1
        elif len(userInput) == 2 and userInput[1] == "=":
            del solver.manuallySet[str(userInput[0])]
        elif len(userInput) % 2 == 1:
            if len(userInput) // 2 > 0:
                try:
                    wordList = userInput.split(sep="=", maxsplit=1)
                    startLetters = wordList[0]
                    finishLetters = wordList[1]

                    if len(startLetters) != len(finishLetters):
                        print("Invalid Input: Strings on either side of the equals sign must be of equal length.")
                    else:
                        validInput = True
                        for i in startLetters:
                            if i not in solver.allLetters:
                                validInput == False
                                print("You can only assign alphabetic characters.")
                        for i in finishLetters:
                            if i in solver.manuallySet.values():
                                print("The letter %s has already been assigned." % i)
                                validInput = False
                            if i not in solver.allLetters:
                                validInput = False
                                print("You can only assign to alphabetic characters.")
                        
                        if validInput:
                            count = 0
                            for i in startLetters:
                                solver.manuallySet[str(i)] = str(finishLetters[count])
                                count += 1
                except:
                    print("Exception thrown during input parsing.")
            else:
                print("Input appears to be in an invalid format. Type 'help' for more information.")
        else:
            print("Invalid input. Type 'help' for more information.")

