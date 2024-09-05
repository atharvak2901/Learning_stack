
import threading
import time

class a(threading.Thread):
    def run(self):  #Run method is by default a component of Thread class so is required
        # print("1")
        print("{} started!".format(self.getName()))
        time.sleep(1)
        print("{} finished!".format(self.getName()))
        
def Main():
    for x in range(3):
        ob1 = a(name = "A", daemon=True) #daemon is a background tasks running thread
                                        #which is optional

        ob1.start()
        time.sleep(1)

if __name__ == "__main__":
    Main()