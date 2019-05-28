Wystarczy napisać tutaj skrypt pythonowy. Nawet nie musibyć to klasa chociaż miłoby było, nawet jeżeli nie macie pojęcia jak to zrobić i chcecie zrobić zwykłą przejebaną jak chuj funkcje na 600 linijek to polecam zrobić np coś takeigo:

```
class BestFirst:

@staticmethod
  def search(edges, edge):
    I lecimy z kodzikiem
```
Wówczas moge w kodzie zrobić coś takiego

```
from modules.PathFinder.best-first-search import BestFirst
BestFirst.search(edges, edge)
```

Zachowujemy wtedy "obiektowość", a ty nie musisz umieć obiektowość. Generalnie win-win
Aczkolwiek nie jest to konieczne możesz zrobić kilka klas, albo jedną funkcje nie powinno nam to stworzc większych problemów

Gdy algorytm zostanie zaimplementowany należy w klasie modules.PathFinder.PathFinder dodać metode:

```
from modules.PathFinder.best-first-search import PotrzebnaKlasa

...

  def getPathToByBestSearch(self,x,y):
    return PotrzebnaKlasa.search(x,y)
```

Przykładowa implementacja nie traktować dosłownie.

Zwracać ma ona listę kroków, jaką postać ma pokonać by dostać się do pukty x,y.
Pamiętaj o tym, że punkt (0,0) to lewy górny róg.

Gdy skończycie implementacje by sprawdzić czy działa w mainie wystarczy zamienić 

```
steps = PathFinder.getPathToByDfs(board, 3, 6)
```

na np.

```
steps = PathFinder.getPathToByBestSearch(board, 3, 6)
```

W module dfs dodam readme z krótkim wytłumaczeniem tego co ja zrobiłem możecie się tym sugerować jak nie będziecie mieli lepszego pomysłu, aczkolwiek moja implementacja również jest daleka od ideału i musze tam kilka rzeczy zmienić.
