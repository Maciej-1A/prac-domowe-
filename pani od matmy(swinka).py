import time

class Pepa:
    def __init__(self, imie, koledzy, zbrodnie_wojenne, event, event1, event2, event3, przedstawienie1, przedstawienie2):
        self.imie = imie
        self.koledzy = koledzy
        self.zbrodnie_wojenne = zbrodnie_wojenne
        self.event = event
        self.event1 = event1
        self.event2 = event2
        self.event3 = event3
        self.przedstawienie1 = przedstawienie1
        self.przedstawienie2 = przedstawienie2

    def przedstawienie(self):
        return f"nazywam sie {self.imie} mam {self.koledzy} kolegów {self.przedstawienie1} {self.zbrodnie_wojenne} {self.przedstawienie2}"

    def lata(self):
        running = True
        szkielet = 21
        czas = 0

        while running:
            print(f"{self.event} {czas}")
            time.sleep(0.001)
            czas += 1

            if czas == 1:
                print(f"{self.imie}{self.event1}")

            if czas == 16:
                print(f"{self.imie}{self.event2}")

            if czas >= szkielet:
                print(f"{self.imie}{self.event3}")
                running = False

swinka = Pepa(imie='Pepa', koledzy=5, zbrodnie_wojenne=10, event='mam lat:', event1=' się właśnie urodziła', event2=' wyszła z więzienia', event3=' umarła :(', przedstawienie1='jest troche nudno bo przez popełnienie',przedstawienie2='zborni wojennych mam wyrok 15 lat w wieńzieniu')
print(swinka.przedstawienie())
swinka.lata()

nauczyciel = Pepa(imie='Kogutowksa', koledzy=0, zbrodnie_wojenne=69, event='jedynki wstawione:', event1=': zaczoł sić dzień czas postawiac 1 :)', event2=': a co sie tu urodziło?', event3=': nareszcie koniec lekcji :D', przedstawienie1='moje hobby to wstawianie 1 i np tez bardzo lubie lamac przawa ucznia wczoraj zlamalam je',przedstawienie2='razy nadal nie wim jak jastem nauczyciel/petagogiem XD')
print(nauczyciel.przedstawienie())
nauczyciel.lata()