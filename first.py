def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def multiple(a, b):
	return a * b

def div(a, b):
	return a / b

def cal(ex):
	ex = ex.strip()
	i = 0
	while ex[i] >= '0' and ex[i] <= '9' or ex[i] == '.':
		i += 1
	a = float(ex[:i])
	while ex[i].isspace():
		i += 1
	c = ex[i]
	i += 1
	b = float(ex[i:])

	if c == '+':
		return add(a, b)
	elif c == '*':
		return multiple(a, b)
	elif c == '/':
		return div(a, b)
	elif c == '-':
		return sub(a, b)
	else:
		print("Nu este asa operatie")

# daca deschidem python in terminal asata nu este nevoie
ex = raw_input("Dati exercitiul: ")

print(cal(ex))
########