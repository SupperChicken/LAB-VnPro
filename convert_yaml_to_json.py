import ruamel.yaml as yaml
import json

if __name__== "__main__":
  print('Làm việc với file yaml')
  with open ("user.yaml","r") as file:
    user_yaml=yaml.safe_load(file)
    print("Print Type of user_yaml")
    print(type(user_yaml))
    for key in user_yaml:
      print(key)

#{key:{key1:value1},}

print("------------------")
print("print value of key 'id'")
print(user_yaml["id"])

print("------------------")
print("print value of key fist_name")
print(user_yaml["first_name"])

print("------------------")
print("print value of key address")
print(user_yaml["address"])

adr1=user_yaml["address"][0]
print("print city 1")
print(adr1['city'])

adr2=user_yaml["address"][1]
print("print city 2")
print(adr2['city'])

print("city 1 ")
print(user_yaml["address"][0]['city'])

print("city 2 ")
print(user_yaml["address"][1]['city'])

print("------------------")
for i in range(0,len(user_yaml["address"])):
  print(user_yaml["address"][i]['city'])

print("------------------")
user_json_10= json.dumps(user_yaml,default=str,indent=10)
print("Structure JSON indient 10")
print(user_json_10)

print("------------------")
user_json_5= json.dumps(user_yaml,default=str,indent=5)
print("Structure JSON indient 5")
print(user_json_5)

print("------------------")
file=open("user5.json","w")
file.write(user_json_5)
print("da chuyen doi xong thanh file json indent 5")
file.close()

print("------------------")
file=open("user10.json","w")
file.write(user_json_10)
print("da chuyen doi xong thanh file json indent 10")
file.close()