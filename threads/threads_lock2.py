import threading

# Shared variable
counter = [0,0,0,0,0,0,0,0,0]

# Creating a lock object
lock = threading.Lock()

def increment_counter(id):
    counter
    for _ in range(100000):          
        counter[id] += 1

# Creating threads
thread1 = threading.Thread(target=increment_counter,args=(0,))
thread2 = threading.Thread(target=increment_counter,args=(1,))
thread3 = threading.Thread(target=increment_counter,args=(2,))
thread4 = threading.Thread(target=increment_counter,args=(3,))
thread5 = threading.Thread(target=increment_counter,args=(4,))
thread6 = threading.Thread(target=increment_counter,args=(5,))
thread7 = threading.Thread(target=increment_counter,args=(6,))
thread8 = threading.Thread(target=increment_counter,args=(7,))
thread9 = threading.Thread(target=increment_counter,args=(8,))
# Starting threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()



print(f"Final counter value: {sum(counter)}")
