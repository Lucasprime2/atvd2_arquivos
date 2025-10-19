import os
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
notas_path = os.path.join(script_dir, 'notas.txt')

def ler_nota(msg):
    while True:
        try:
            x = input(msg).strip().replace(',', '.')
            n = float(x)
            if 0 <= n <= 10:
                return n
            print("Nota inválida")
        except ValueError:
            print("Nota inválida. Digite um número de 0-10.")

def escolher_continuar():
    while True:
        r = input("Deseja continuar? (S/N): ").strip().upper()
        if not r:
            print("Resposta inválida. Digite sim ou não")
            continue
        if r[0] == 'S':
            return True
        if r[0] == 'N':
            return False
        print("Resposta inválida. Digite sim ou não.")

print("As informações serão gravados em:", notas_path)
while True:
    nome = input("Informe o nome: ").strip()
    if not nome:
        print("Nome não pode ficar vazio.")
        continue

    n1 = ler_nota("Digite a nota 1: ")
    n2 = ler_nota("Digite a nota 2: ")
    n3 = ler_nota("Digite a nota 3: ")

    with open(notas_path, 'a', encoding='utf-8') as f:
        f.write(f"{nome};{n1};{n2};{n3}\n")

    print(f"{nome} salvo em notas.txt.")
    if not escolher_continuar():
        print("Encerrando a entrada de notas.")
        break