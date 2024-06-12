input = open("18s_humano.fasta").read()
output = open("18s_humano.html","w")

sequence = ["A", "C", "T", "G"]
count = { i + j : 0 for i in sequence for j in sequence }

input = input.replace("\n","")

for k in range(len(input)-1):
	count[input[k]+input[k+1]] += 1

# html

output.write("<div>")

i = 1
for k in count:
	alpha = count[k]/max(count.values())
	output.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(alpha)+"')>"+k+"</div>")

	if i%4 == 0:
		output.write("<div style='clear:both'></div>")

	i+=1

output.close()
