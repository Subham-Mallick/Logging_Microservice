import requests
import string
import random, time
  
def randomString():
    N = 25
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k = N))
    return str(res)

if __name__ == "__main__":
    for i in range(0,1000):
        time.sleep(1)
        if random.randint(0, 1):
            response = requests.post('http://127.0.0.1:9999/insert', data = {'key':'randomString'})
        else:
            response = requests.get('http://127.0.0.1:9999/')
        print(response)
