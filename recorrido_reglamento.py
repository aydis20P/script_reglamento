import json


# Python3 Program for recursive binary search.
# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
	# Check base case
	if r >= l:
		mid = l + (r - l) // 2
		# If element is present at the middle itself
		if arr[mid]["id"] == x:
			return mid
		# If element is smaller than mid, then it
		# can only be present in left subarray
		elif arr[mid]["id"] > x:
			return binarySearch(arr, l, mid-1, x)
		# Else the element can only be present
		# in right subarray
		else:
			return binarySearch(arr, mid + 1, r, x)
	else:
		# Element is not present in the array
		return -1


t = open("textos.json", "r")
xt = t.read()
yt = json.loads(xt)
textos_list = yt["textos"]

f = open("preguntas.json", "r")
x = f.read()
y = json.loads(x)
preguntas_list = y["preguntas"]
raices_list = []
hijos_list = []

s = open("sanciones.json", "r")
xs = s.read()
ys = json.loads(xs)
sanciones_list = ys["sanciones"]

"""
for sancion in sanciones_list:
    print(sancion["id"])
"""

# Llenar listas de raices e hijos
for pregunta in preguntas_list:
    if pregunta["id_texto"] != "":
        raices_list.append(pregunta)
    else:
        hijos_list.append(pregunta)


str_fin = "Se ha cometido una falta que amerita sanci\u00f3n"
def recorreArbolRec(padre, nivel):
    print("   "*nivel + "-> " + padre["pregunta"] + " (id_pregunta " + str(padre["id"]) + ")")
    
    if padre["pregunta"] == str_fin:
        id_sancion_list = binarySearch(sanciones_list, 0, len(sanciones_list)-1, padre["respuestas"][0]["id_sancion"])
        if padre["respuestas"][0]["aplica_sancion"]:
            if id_sancion_list != -1:
                print("   "*nivel + "sancion_cometida: " + sanciones_list[id_sancion_list]["sancion_cometida"] + " (id_sancion " + str(padre["respuestas"][0]["id_sancion"]) + ")")
            else:
                print("   "*nivel + "no se encontró la sancion_cometida para el id_sancion " + str(padre["respuestas"][0]["id_sancion"]))
        else:
            print("   "*nievl + "----- No aplica sanción -----")

    else:
        for respuesta in padre["respuestas"]:
            print("   "*nivel + respuesta["respuesta"])

            id_pregunta_destino = respuesta["pregunta_destino"]
            result = binarySearch(hijos_list, 0, len(hijos_list)-1, id_pregunta_destino)

            if result != -1:
                recorreArbolRec(hijos_list[result], nivel + 1)
            else:
                if respuesta["aplica_sancion"]:
                    id_sancion_list = binarySearch(sanciones_list, 0, len(sanciones_list)-1, respuesta["id_sancion"])
                    if id_sancion_list != -1:
                        print("   "*nivel + "sancion_cometida: " + sanciones_list[id_sancion_list]["sancion_cometida"] + " (id_sancion " + str(respuesta["id_sancion"]) + ")")
                    else:
                        print("   "*nivel + "no se encontró la sancion_cometida para el id_sancion " + str(respuesta["id_sancion"]))
                else:
                    print("   "*nivel + "----- No aplica sanción -----")



# Caso para un solo padre
#padre = raices_list[55]
#print(json.dumps(padre, indent=2))
#print(binarySearch(hijos_list, 0, len(hijos_list)-1, 19))
#print(json.dumps(hijos_list[5], indent=2))


for padre in raices_list:
    #padre = raices_list[6]
    #print(json.dumps(raices_list[6], indent=1))
    print()
    print()
    id_texto_list = binarySearch(textos_list, 0, len(textos_list)-1, padre["id_texto"])
    if id_texto_list != -1:
        texto = textos_list[id_texto_list]
        print(texto["falta_desc"] + " (id_texto " + str(padre["id_texto"]) + ")")
        print("aplica: ", end="")
        for tipo, val in texto["tipos"].items():
            if val:
                print(tipo + " ", end="")
        print()
    else:
        print("No se encontró el texto asociado al id_texto " + str(padre["id_texto"]))
    recorreArbolRec(padre, 0)


"""
# Buscar pregunta por id en el arreglo
x = 13
result = binarySearch(preguntas_list, 0, len(preguntas_list)-1, x)

if result != -1:
    print(json.dumps(preguntas_list[result], indent=2))
else:
	print("La pregunta con id " + str(x) + " no existe")
"""
