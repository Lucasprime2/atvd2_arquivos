import os
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
notas_path = os.path.join(script_dir, 'notas.txt')
aprov_path = os.path.join(script_dir, 'aprovados.txt')
exame_path = os.path.join(script_dir, 'exame.txt')
reprov_path = os.path.join(script_dir, 'reprovados.txt')

if not os.path.exists(notas_path):
    print("Arquivo notas.txt não encontrado em:", notas_path)
    raise SystemExit

aprovados = []
exame = []
reprovados = []

with open(notas_path, 'r', encoding='utf-8') as f:
    for linha in f:
        linha = linha.strip()
        if not linha:
            continue
        linha_norm = linha.replace(';', ',')
        partes = linha_norm.split(',')
        if len(partes) < 4:
            print("Linha ignorada (formato errado):", linha)
            continue

        nome = partes[0].strip()
        try:
            n1 = float(partes[1].strip().replace(',', '.'))
            n2 = float(partes[2].strip().replace(',', '.'))
            n3 = float(partes[3].strip().replace(',', '.'))
        except ValueError:
            print("Notas inválidas para", nome)
            continue

        media = round((n1 + n2 + n3) / 3, 2)
        linha_saida = f"{nome};{n1};{n2};{n3};{media}"

        if media >= 7:
            aprovados.append(linha_saida)
        elif media >= 5:
            exame.append(linha_saida)
        else:
            reprovados.append(linha_saida)

def gravar_arquivo(path, lista):
    with open(path, 'w', encoding='utf-8') as f:
        if lista:
            f.write("nome;nota1;nota2;nota3;media\n")
            for l in lista:
                f.write(l + "\n")
        else:
            pass

gravar_arquivo(aprov_path, aprovados)
gravar_arquivo(exame_path, exame)
gravar_arquivo(reprov_path, reprovados)

print("Processamento concluído. Arquivos gerados em:", script_dir)
print("- aprovados:", os.path.basename(aprov_path), "| registros:", len(aprovados))
print("- exame:   ", os.path.basename(exame_path), "| registros:", len(exame))
print("- reprovados:", os.path.basename(reprov_path), "| registros:", len(reprovados))