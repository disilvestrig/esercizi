import requests
def accreditamento(nome,cognome):
   res = requests.post("http://192.168.1.231:8080/accreditamento",headers = { "nome": nome+" "+cognome)
   print(res.json())
accreditamento(input(),input())
def consegna(n):
   res = requests.get("http://192.168.1.231:8080/esercizi/"+n,headers = {"x-data" :"true"}
   print(res.json())
   dati = res["data"]
   return dati
dati = consegna(input())
def risposta(ris,n):
   res = requests.get("http://192.168.1.231:8080/esercizi/"+n,json = {"data" : ris}
   print(res.json())
