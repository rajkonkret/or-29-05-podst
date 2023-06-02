from threading import Thread
from time import sleep, perf_counter


def task(id):
    plik1 = open('t1.txt', 'w')
    plik1.write(str(id))
    sleep(1)


def task2(id):
    plik2 = open('t2.txt', "w")
    plik2.write(str(id))
    sleep(1)


# task1
start_time = perf_counter()

t1 = Thread(target=task, args=(1,))
t2 = Thread(target=task2, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()

print(f'Zajęło to {end_time - start_time} sek')  # Zajęło to 1.1322512999759056 sek
