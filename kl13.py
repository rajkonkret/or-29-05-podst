from dataclasses import dataclass
import pickle


@dataclass  # oznacza klase danych, automatycznie dodaje getery,setery, __str__, konstruktor
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f"Witam, jestem {self.first_name} {self.last_name}, Id to {self.id}")


# kod w bloku __name___ wykona sie tylko, gdy plik jest bezpośrednio uruchamiany
if __name__ == '__main__':
    # [Person(first_name='Jacek', last_name='Kowalski', id=1), Person(first_name='Mateusz', last_name='Zegar', id=2)]
    people = [
        Person("Jacek", "Kowalski", 1),
        Person("Mateusz", "Zegar", 2)
    ]

    print(people)
    print(people[0])

    with open('data.pickle', 'wb') as stream:
        pickle.dump(people, stream)
