# Caderno do Estudante
# Projeto ConectaUDF: redes sociais com grafos
**Disciplina:** Algoritmos / Matemática Discreta / Ciência de Dados

**Alunos:** Caio Guilherme / Maycon Fidelis / Ítalo Diniz / Beatriz Alves

## 1. O desafio
Você faz parte da equipe que analisa a rede social fictícia **ConectaUDF**. Sua missão é representar as amizades em um grafo, realizar cálculos e usar Python para interpretar a estrutura da rede.

## 2. Conceitos essenciais
- **Vértice (ou nó):** representa um usuário.
- **Aresta:** representa uma amizade entre dois usuários.
- **Grau:** quantidade de conexões diretas de um usuário.
- **Caminho:** sequência de usuários em que cada par consecutivo está conectado.
- **Densidade:** proporção entre as amizades existentes e todas as amizades possíveis.

Neste projeto, a amizade é recíproca. Portanto, usamos um **grafo não direcionado**.

## 3. Conheça os usuários
## 3. Conheça os usuários
| Código | Usuário |
|---|---|
| A | Caio |
| B | Maycon |
| C | Diniz |
| D | Beatriz |
| E | Hugo |
| F | Felipe |
| G | Gabriel |
| H | Hendrick |
| I | Jean |
| J | Jeronimo |
| K | Kelly |
| L | Leandro |
| M | Mônica |
| N | Nando |
| O | Otávio |
| P | Pedro |
| Q | Fred |
| R | Raquel |
| S | Silva |
| T | Tainá |

## Lista de ligações

1. Caio — Diniz
2. Caio — Gabriel
3. Caio — Kelly
4. Caio — Otávio
5. Caio — Tainá
6. Maycon — Beatriz
7. Maycon — Nando
8. Maycon — Silva
9. Maycon — Fred
10. Diniz — Jean
11. Diniz — Kelly
12. Diniz — Leandro
13. Beatriz — Felipe
14. Beatriz — Jeronimo
15. Beatriz — Mônica
16. Beatriz — Raquel
17. Hugo — Gabriel
18. Hugo — Fred
19. Hugo — Otávio
20. Felipe — Mônica
21. Felipe — Pedro
22. Gabriel — Tainá
23. Hendrick — Leandro
24. Hendrick — Nando
25. Jean — Nando
26. Jean — Pedro
27. Jeronimo — Leandro
28. Jeronimo — Pedro
29. Kelly — Silva
30. Mônica — Nando
31. Nando — Silva
32. Raquel — Silva
33. Raquel — Fred
34. Fred — Tainá

---
### Resposta

<img width="730" height="603" alt="Grafo" src="https://github.com/user-attachments/assets/b6d3f5d9-b482-498c-af34-6c01392a4b01" />


---

## 4. Passo a passo: desenhe o grafo
1. Desenhe vinte círculos, um para cada usuário.
2. Escreva o nome de cada pessoa dentro do círculo.
3. Para cada amizade da lista, desenhe uma linha entre os dois usuários.
4. Não desenhe duas linhas para a mesma amizade.
5. Confira se todas as 34 amizades aparecem.

## 5. Passo a passo: calcule o grau
Conte quantas linhas chegam a cada círculo. Registre o resultado.

| Usuário | Amigos diretos | Grau |
|---|---|---|
| Caio | Diniz, Gabriel, Kelly, Otávio, Tainá | 5 |
| Maycon | Beatriz, Nando, Silva, Fred | 4 |
| Diniz | Caio, Jean, Kelly, Leandro | 4 |
| Beatriz | Maycon, Felipe, Jeronimo, Mônica, Raquel | 5 |
| Hugo | Gabriel, Fred, Otávio | 3 |
| Felipe | Beatriz, Mônica, Pedro | 3 |
| Gabriel | Caio, Hugo, Tainá | 3 |
| Hendrick | Leandro, Nando | 2 |
| Jean | Diniz, Nando, Pedro | 3 |
| Jeronimo | Beatriz, Leandro, Pedro | 3 |
| Kelly | Caio, Diniz, Silva | 3 |
| Leandro | Diniz, Hendrick, Jeronimo | 3 |
| Mônica | Beatriz, Felipe, Nando | 3 |
| Nando | Maycon, Hendrick, Jean, Mônica, Silva | 5 |
| Otávio | Caio, Hugo | 2 |
| Pedro | Felipe, Jean, Jeronimo | 3 |
| Fred | Maycon, Hugo, Raquel, Tainá | 4 |
| Raquel | Beatriz, Silva, Fred | 3 |
| Silva | Maycon, Kelly, Nando, Raquel | 4 |
| Tainá | Caio, Gabriel, Fred | 3 |

**Pergunta 1: quem tem mais conexões diretas?**
Resposta: Caio, Beatriz e Nando empatam, cada um com grau 5.

## 6. Passo a passo: calcule o número de amizades
Some todos os graus. Como cada amizade conecta dois usuários, cada aresta é contada duas vezes.

**Fórmula:**
`Número de arestas = soma dos graus ÷ 2`

1. Soma dos graus: 5 + 4 + 4 + 5 + 3 + 3 + 3 + 2 + 3 + 3 + 3 + 3 + 3 + 5 + 2 + 3 + 4 + 3 + 4 + 3 = 68
2. Divida por 2: 68 ÷ 2 = 34
3. Quantas amizades existem no grafo? 34

## 7. Passo a passo: calcule a densidade
A densidade compara as amizades existentes com o total de amizades possíveis.

Para um grafo simples não direcionado:

`D = 2 × E / (V × (V − 1))`

Em que:
- `D` = densidade;
- `E` = número de arestas;
- `V` = número de vértices.

Substitua os valores:
`D = 2 × 34 / (20 × (20 − 1)) = 68 / 380`

Resultado decimal: 0,1789
Resultado percentual: 17,89%

**Interprete:** a rede tem poucas ou muitas das conexões possíveis? Explique com suas palavras.
**Resposta:** Possui poucas conexões possíveis, porque o cálculo mostrou que são apenas cerca de 18% das conexões possíveis. Dos 190 pares de usuários que poderiam ser amigos, só 34 realmente são.

## 8. Passo a passo: represente o grafo em Python
A lista de adjacência registra, para cada usuário, os nomes de seus amigos. Digite o código em Python (por exemplo, no Google Colab ou em outro ambiente disponível).

```python
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
```

Saída esperada nas últimas linhas:

```
Total de usuarios: 20
Total de amizades: 34
Densidade: 17.89%
```

### Entenda o código
1. `rede` guarda os usuários e suas listas de amigos.
2. `len(rede)` conta os usuários.
3. `len(amigos)` calcula o grau de cada usuário.
4. `sum(...)` soma os graus.
5. `// 2` divide a soma por dois para contar cada amizade uma única vez.
6. A fórmula final calcula a densidade.

## 9. Passo a passo: encontre um caminho
Encontre um caminho de Caio até Mônica. Cada passagem por uma linha corresponde a uma aresta.

Exemplo de registro:
`Caio → Diniz → Jean → Nando → Mônica`

- Quantas arestas há no caminho? 4
- Você encontrou outro caminho com a mesma quantidade de arestas? Qual? Sim.
`Caio → Kelly → Silva → Nando → Mônica`

## 10. Perguntas finais

**Duas pessoas ainda não são amigas, mas têm três amigos em comum. Como essa informação poderia ser usada para sugerir uma nova conexão?**
Resposta: A própria rede social tem o sistema de sugestão de amigos em comum. Quanto mais amigos em comum duas pessoas têm, maior a chance de se conhecerem, então a plataforma tende a sugerir uma à outra, formando um novo laço de amizade. No grafo, Maycon e Mônica não são amigos, mas têm Beatriz e Nando em comum, e por isso seriam candidatos a uma sugestão.

**Quais cuidados de privacidade devem ser considerados ao analisar redes sociais?**
Resposta: Os dados de amizades são pessoais, então a plataforma deve usá-los com consentimento e transparência. Também deve evitar que uma sugestão exponha alguém que não quer ser encontrado (como um ex), deixar o usuário controlar quem pode vê-lo e proteger os dados contra vazamentos e uso indevido.

________________________________________________________________

## 10. Desafio em grupo
Amplie a rede social:
1. Adicione pelo menos quatro usuários fictícios.
2. Crie no mínimo cinco novas amizades.
3. Atualize a lista de adjacência no Python.
4. Recalcule os graus, o total de arestas e a densidade.
5. Compare a densidade antes e depois da ampliação.
6. Identifique os usuários com mais conexões.
7. Explique como a rede poderia recomendar uma nova amizade.

## 11. Entrega
Entregue:
- desenho do grafo;
- tabela com os graus;
- cálculos de arestas e densidade;
- código Python executável;
- respostas às perguntas e breve conclusão.

## 12. Pergunta de reflexão
Duas pessoas ainda não são amigas, mas têm três amigos em comum. Como essa informação poderia ser usada para sugerir uma nova conexão? Quais cuidados de privacidade devem ser considerados ao analisar redes sociais?

**Resposta:** A plataforma conta quantos amigos duas pessoas têm em comum, e quanto maior esse número, maior a chance de elas se conhecerem. Com três amigos em comum, é muito provável que o sistema sugira uma à outra, o que pode criar uma nova amizade e deixar a rede mais conectada.Os dados de amizades são pessoais, então a plataforma deve usá-los com consentimento e transparência, deixando claro que usa as conexões para sugerir amigos.
