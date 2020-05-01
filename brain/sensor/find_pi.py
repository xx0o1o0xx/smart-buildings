import requests
import json
import motion_detection


#Iterates through the last octet of IP address (0-255) and returns if a 
#handshake is produced on the desired port
def find_handshake_ip(base_add, port):
    for i in range(0,256):
        req_add = base_add.format(str(i))
        req_string = "http://"+req_add+":"+str(port)
        try:
            x = requests.get(req_string, timeout=0.2)
            if(x.content==b'True'):
                return req_add
        except:
            pass
    return None


def main():
    with open("config.json","r+") as f:
        x = json.load(f)
        # print(x)
    with open("config.json","w") as f:
        x["brain_ip"] = str(find_handshake_ip("192.168.1.{}", x["brain_port"]))
        # x["brain_ip"] = "bassel"
        print(x)
        json.dump(x, f, ensure_ascii=False, indent=4)


def init_config():
    return


def init_data():
    return

if __name__ == "__main__":
    main()
    motion_detection.main()