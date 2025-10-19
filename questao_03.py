import os
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
exame_path = os.path.join(script_dir, 'exame.txt')
aprov_path = os.path.join(script_dir, 'aprovados.txt')
reprov_path = os.path.join(script_dir, 'reprovados.txt')

def ler_nota(msg):
    while True:
        try:
            x = input(msg).strip().replace(',', '.')
            n = float(x)
            if 0 <= n <= 10:
                return n
            print("Nota inválida. Digite um número de 0-10.")
        except ValueError:
            print("Erro: Digite um número de 0-10.")

def cabecalho(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, 'a', encoding='utf-8') as f:
            f.write("nome;media_anterior;nota_exame;media_final;observacao\n")

def append_linha(path, linha):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(linha + "\n")

if not os.path.exists(exame_path):
    print("Arquivo exame.txt não encontrado em:", exame_path)
    raise SystemExit

alunos_exame = []  
with open(exame_path, 'r', encoding='utf-8') as f:
    for linha in f:
        linha = linha.strip()
        if not linha:
            continue
        lp = linha.lower()
      
        if lp.startswith('nome') and ('media' in lp or 'nota' in lp):
            continue

        
        linha_norm = linha.replace(';', ',')
        partes = [p.strip() for p in linha_norm.split(',')]

        if len(partes) < 5:
            print("Linha com erro no formato:", linha)
            continue

        nome = partes[0]
        try:
            media_ant = float(partes[4].replace(',', '.'))
        except ValueError:
            print("Média inválida para", nome, " Linha:", linha)
            continue

        alunos_exame.append((nome, media_ant))

if not alunos_exame:
    print("Não há alunos listados em exame.txt.")
    raise SystemExit

cabecalho(aprov_path)
cabecalho(reprov_path)

cont_aprov = 0
cont_reprov = 0

for nome, media_ant in alunos_exame:
    print("\nAluno:", nome)
    nota_exame = ler_nota("Informe a nota do exame: ")
    media_final = round((media_ant + nota_exame) / 2, 2)

    linha_saida = f"{nome};{media_ant};{nota_exame};{media_final}"

    if media_final >= 5:
        append_linha(aprov_path, linha_saida + ";Aprovado após exame")
        cont_aprov += 1
        print(f"{nome} -> Aprovado após exame (média final {media_final})")
    else:
        append_linha(reprov_path, linha_saida + ";Reprovado após exame")
        cont_reprov += 1
        print(f"{nome} -> Reprovado após exame (média final {media_final})")

print("\nProcedimentos concluídos.")
print(f"Aprovados adicionados: {cont_aprov}")
print(f"Reprovados adicionados: {cont_reprov}")
print("Arquivos atualizados em:", script_dir)