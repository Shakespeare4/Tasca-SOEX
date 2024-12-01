import threading
import multiprocessing
import time


def thread_infinite_loop(stop_event):
    while not stop_event.is_set():  
        print("Hilo corriendo")
        time.sleep(1)  
    print("Hilo detenido.")


def process_infinite_loop(stop_event):
    while not stop_event.value: 
        print("Proceso corriendo")
        time.sleep(1) 
    print("Proceso detenido.")

def main():

    stop_thread_event = threading.Event()


    stop_process_event = multiprocessing.Value('b', False) 


    thread = threading.Thread(target=thread_infinite_loop, args=(stop_thread_event,))
    thread.start()


    process = multiprocessing.Process(target=process_infinite_loop, args=(stop_process_event,))
    process.start()

    print("Hilo corriendo")
    input("Presiona enter para terminar\n")
    
    stop_thread_event.set()
    stop_process_event.value = True
    
    thread.join()
    process.join()

    print("Hilo y proceso terminados")

if __name__ == "__main__":
    main()

