import random

class ClassRoom:

   def __init__(self, rozmiar):
      self.rozmiar = rozmiar
      self.tablica=[random.randint(1,1000) for _ in range(rozmiar)]

   def wszystkie_elementy(self):
      for indeks,wartosc in enumerate(self.tablica):
         print(f"{indeks}: {wartosc}")

   def szukaj(self,szukana_wartosc):
      index=[]
      for indeks,wartosc in enumerate(self.tablica):
         if(szukana_wartosc == wartosc):
            index.append(indeks)

      return index if len(index)>1 else -1
   
   def nieparzyste(self):
      liczby_nparzyste=[wartosc for wartosc in self.tablica if wartosc % 2 != 0]
      print(f"liczby nieparzyste: {liczby_nparzyste}")
      return len(liczby_nparzyste)
   
   def oblicz_sr(self):
      return sum(self.tablica)/self.rozmiar if self.rozmiar>0 else 0
   
if __name__=="__main__":

   rozmiar=30
   tablica=ClassRoom(rozmiar)

   print("wszystkie lementy tablicy: ")
   tablica.wszystkie_elementy()

   szukana_wartosc=30
   indeks=tablica.szukaj(szukana_wartosc)

   if indeks!=-1:
      print(f"Wartość szukana - {szukana_wartosc} znajduje się na indeksie {indeks}")
   else:
      print(f"Wartość {szukana_wartosc} nie została znaleziona w tablicy")

   liczba_nieparzystych=tablica.nieparzyste()
   print(f"Liczba liczb nieprzarzystych w tablicy to: {liczba_nieparzystych}")
   
   srednia=tablica.oblicz_sr()
   print(f"srednia wartosci w tablicy to: {srednia}")