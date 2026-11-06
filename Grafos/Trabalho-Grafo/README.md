# Grafo de Conexões — Comunidade UDF no Instagram

Grafo de relacionamentos entre perfis da comunidade acadêmica do **UDF Centro Universitário** no Instagram, construído no [draw.io](https://app.diagrams.net) (diagrams.net).

O ponto de partida foi o perfil **techudfoficial** e os perfis que o seguem e, ao mesmo tempo, seguem o autor. A partir daí, o grafo foi expandido com os seguidores de quatro desses perfis.

## Objetivo

Visualizar como diferentes perfis se conectam entre si: quem aparece em mais de uma lista, quais perfis funcionam como "pontes" entre comunidades e como os grupos se sobrepõem.

## Como o grafo foi construído

1. **Coleta:** a partir de capturas de tela das listas de seguidores de quatro perfis (os *hubs*).
2. **Hubs:** cada perfil analisado vira um nó central, com seus seguidores ao redor.
3. **Nós compartilhados:** perfis que aparecem em mais de uma lista ficam entre os hubs, ligados a todos em que aparecem.
4. **Ligações entre hubs:** quando um hub aparece na lista de outro, os dois são ligados por uma linha mais grossa.

## Legenda

| Cor / forma | Significado |
|---|---|
| 🟦 Elipse azul | Perfil de origem da análise (`techudfoficial`) |
| 🟩 Elipse verde | Autor do trabalho |
| 🟨 Elipse amarela | Hub: perfil cujos seguidores foram mapeados |
| 🟧 Retângulo laranja | Perfil presente em mais de uma lista |
| ⬜ Retângulo cinza | Perfil presente em apenas uma lista |
| Linha amarela grossa | Conexão entre dois hubs |

## Números

- **30 nós:** 4 hubs, 1 autor, 1 perfil de origem, 4 compartilhados e 20 exclusivos de um hub
- **40 ligações**

## Estrutura do repositório

```
.
├── grafo-seguidores-techudf-v2.drawio   # arquivo editável do grafo
└── README.md
```

## Como abrir e editar

1. Acesse [app.diagrams.net](https://app.diagrams.net).
2. Vá em **File → Open from → Device**.
3. Selecione `grafo-seguidores-techudf-v2.drawio`.

Para exportar como imagem: **File → Export as → PNG / SVG / PDF**.

## Limitações

- Os dados vêm de capturas de tela, então refletem apenas o que estava visível no momento da coleta.
- Algumas listas estavam cortadas e podem ter mais perfis do que os mapeados.
- As relações são de seguir/ser seguido no Instagram e não indicam proximidade real entre as pessoas.

## Privacidade

O grafo usa nomes de usuário reais de perfis do Instagram. Se este repositório for público, considere pedir autorização das pessoas citadas ou trocar os nomes por identificadores anônimos (por exemplo, `Perfil 01`) antes de publicar o arquivo `.drawio`.

## Ferramentas

- [draw.io / diagrams.net](https://app.diagrams.net)

## Autor

**Maycon** — Ciência da Computação, UDF
