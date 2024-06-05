entrada = open("16s_bacteria.fasta").read()
saida = open("16s_bacteria.html","w")

sequence = ["A", "C", "T", "G"]
cont = { i + j : 0 for i in sequence for j in sequence }

entrada = entrada.replace("\n","")

for k in range(len(entrada)-1):
	cont[entrada[k]+entrada[k+1]] += 1

# html

saida.write("<div>")

i = 1
for k in cont:
	transparencia = cont[k]/max(cont.values())
	saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+"')>"+k+"</div>")

	if i%4 == 0:
		saida.write("<div style='clear:both'></div>")

	i+=1

saida.close()
