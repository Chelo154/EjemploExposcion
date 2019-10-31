import sys
print("CALCULADORA 1.0")

a = int(sys.argv[1])
b = int(sys.argv[2])
op = str(sys.argv[3])

if(op=="+"):
	c = a+b
	print("Resultado: "+str(c))
if(op=="-"):
	c = a-b
	print("Resultado: "+str(c))
if(op=="*"):
	print("No impplementado todavia")
