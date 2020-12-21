import  requests
#res = requests.post('http://localhost:5000/app', data={"data":"апишка"})
res = requests.post('http://127.0.0.1:5000/app', json={"data":"вода"})
print(res)
if res.ok:
    print(res.json())