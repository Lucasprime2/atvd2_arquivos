import os
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
aprov_path = os.path.join(script_dir, 'aprovados.txt')
reprov_path = os.path.join(script_dir, 'reprovados.txt')

def le_arquivo(path, default_legend):
    alunos = []
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return alunos

    with open(path, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            lp = linha.lower()
            if lp.startswith('nome') and ('nota' in lp or 'media' in lp or 'observacao' in lp):
                continue
            linha_norm = linha.replace(';', ',')
            partes = [p.strip() for p in linha_norm.split(',')]

            if len(partes) == 0:
                continue

            nome = partes[0]
            ultima = partes[-1]
            tem_legenda = False
            try:
                float(ultima.replace(',', '.'))  
            except ValueError:

                tem_legenda = True
            if tem_legenda:
                legenda = ultima
            else:
                legenda = default_legend

            alunos.append((nome, legenda))
    return alunos

aprovados = le_arquivo(aprov_path, "Aprovado")
reprovados = le_arquivo(reprov_path, "Reprovado")

print("\n=== Lista de Alunos e Situação ===\n")

if aprovados:
    print("Aprovados:")
    for nome, legenda in aprovados:
        print(f" - {nome}  --  {legenda}")
else:
    print("Aprovados: (nenhum aluno registrado)")

print()

if reprovados:
    print("Reprovados:")
    for nome, legenda in reprovados:
        print(f" - {nome}  --  {legenda}")
else:
    print("Reprovados: (nenhum aluno registrado)")
print("\nResumo:")
print(f" - Total aprovados: {len(aprovados)}")
print(f" - Total reprovados: {len(reprovados)}")
print("\nArquivos lidos em:", script_dir)