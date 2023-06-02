import multiprocessing
from time import sleep, perf_counter


def task(id):
    plik1 = open('t1.txt', 'w')
    plik1.write(str(id))
    sleep(1)


def task2(id):
    plik2 = open('t2.txt', "w")
    plik2.write(str(id))
    sleep(2)


if __name__ == '__main__':
    start_time = perf_counter()

    process1 = multiprocessing.Process(target=task, args=(1,))
    process2 = multiprocessing.Process(target=task2, args=(2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = perf_counter()

    execution_time = end_time - start_time

    print(f"Czas wykonania: {execution_time}")