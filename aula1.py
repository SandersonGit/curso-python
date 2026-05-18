# Como Fazer um Print no Output e Como Fazer Comentários no Código
# Para mostrar qualquer informação na tela, nós usamos a função print(). Dentro dos parênteses, você coloca o tex
# Para se fazer comentários devemos usar o # e tudo o que vier após isso na linha será ignorado pelo sistema. É perfeito para deixar explicações no seu código!
# Isto é um comentário e não será executado print("Isto vai aparecer na tela!") # Também dá para comentar no fim da linha
print(1 + 1)
print("Hello World")

# Uma docstring (documentation string) é uma string literal usada em Python para documentar o que um módulo, função, classe ou método faz.
# Ela é escrita logo na primeira linha do bloco de código, delimitada por três aspas duplas (""") ou três aspas simples (''').

def somar(a, b):
    """Soma dois números e retorna o resultado. 🐍"""
    return a + b

# A grande diferença para um comentário comum (#) é que a docstring pode ser acessada em tempo de execução usando o atributo especial __doc__ (ex: somar.__doc__) ou a função help(somar), servindo como uma documentação oficial e automatizada do seu código.

