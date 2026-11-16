rede = {
    "Caio": ["Diniz", "Gabriel", "Kelly", "Otávio", "Tainá"],
    "Maycon": ["Beatriz", "Nando", "Silva", "Fred"],
    "Diniz": ["Caio", "Jean", "Kelly", "Leandro"],
    "Beatriz": ["Maycon", "Felipe", "Jeronimo", "Mônica", "Raquel"],
    "Hugo": ["Gabriel", "Fred", "Otávio"],
    "Felipe": ["Beatriz", "Mônica", "Pedro"],
    "Gabriel": ["Caio", "Hugo", "Tainá"],
    "Hendrick": ["Leandro", "Nando"],
    "Jean": ["Diniz", "Nando", "Pedro"],
    "Jeronimo": ["Beatriz", "Leandro", "Pedro"],
    "Kelly": ["Caio", "Diniz", "Silva"],
    "Leandro": ["Diniz", "Hendrick", "Jeronimo"],
    "Mônica": ["Beatriz", "Felipe", "Nando"],
    "Nando": ["Maycon", "Hendrick", "Jean", "Mônica", "Silva"],
    "Otávio": ["Caio", "Hugo"],
    "Pedro": ["Felipe", "Jean", "Jeronimo"],
    "Fred": ["Maycon", "Hugo", "Raquel", "Tainá"],
    "Raquel": ["Beatriz", "Silva", "Fred"],
    "Silva": ["Maycon", "Kelly", "Nando", "Raquel"],
    "Tainá": ["Caio", "Gabriel", "Fred"]
}

# Quantidade de usuarios
n = len(rede)

# Calcule o grau de cada usuario
for usuario, amigos in rede.items():
    print(usuario, "tem", len(amigos), "conexoes")

# A soma dos graus conta cada amizade duas vezes
soma_graus = sum(len(amigos) for amigos in rede.values())
arestas = soma_graus // 2

print("Total de usuarios:", n)
print("Total de amizades:", arestas)

# Densidade do grafo
densidade = (2 * arestas) / (n * (n - 1))
print(f"Densidade: {densidade:.2%}")
