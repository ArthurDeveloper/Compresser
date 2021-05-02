file = input("Diretório do arquivo para comprimir")

try:
	fileContent = open(file, "rt")
except:
	print("Arquivo não encontrado. Tente novamente.")
	exit()

def comprimir(file):
	content = file.read()
	content = content.replace('\n', '')
	return content
	
comprimido = comprimir(fileContent)
	
print("Comprimido: ", comprimido)

open(file, 'wt').write(comprimido)

print("Compressão salva")