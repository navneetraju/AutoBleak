ar=['abc','bcd','def']  #array of javascript button paths , can be class name or button ids
f=open("autogenscript.js","w+")   #here is the config file
start="https://www.here.com/"     #here is the staring page
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



