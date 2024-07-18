import threading

# Shared variable
counter = 0

def increment_counter():
    global counter
    for _ in range(1000000):          
        counter += 1


# Creating threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)
thread3 = threading.Thread(target=increment_counter)
thread4 = threading.Thread(target=increment_counter)
thread5 = threading.Thread(target=increment_counter)
thread6 = threading.Thread(target=increment_counter)
thread7 = threading.Thread(target=increment_counter)
thread8 = threading.Thread(target=increment_counter)
thread9 = threading.Thread(target=increment_counter)
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


print(f"Final counter value: {counter}")
