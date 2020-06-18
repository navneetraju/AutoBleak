ar=[]
f=open('queries.txt','r')
exp=f.readline()
exp=exp[:len(exp)-1]
a=f.readline()
a=f.readline()
while(a != ']\n'):
	ar.append(a[3:len(a)-3])
	a=f.readline()
	

f=open("autogenscript.js","w+")   #here is the config file
start=exp     #here is the staring page
f.write("exports.url =\""+start+"\";\n")
f.write("exports.loop = [{\n")

f.write("check: function(){\n")
f.write("	return true;\n")
f.write("},\n")
f.write("next: function() {\n")
f.write("	const first0 = document.querySelector(\""+ar[0]+"\");\n")
f.write("	first0.click();\n")
f.write("}\n}")


for i in range(1,len(ar)):
	f.write(",\n")
	f.write("{\n")
	f.write("check: function(){\n")
	f.write("	return true;\n")
	f.write("},\n")
	f.write("next: function() {\n")
	f.write("	const first"+str(i)+" = document.querySelector(\""+ar[i]+"\");\n")
	f.write("	first"+str(i)+".click();\n")
	f.write("}\n}")
f.write("];")
f.close()



