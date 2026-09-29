# Revisão de Estruturas de Árvores — Estrutura de Dados II

**Instituição:** UDF — Centro Universitário  
**Disciplina:** Estrutura de Dados II  
**Professora:** Profa. Kadidja Valéria  
**Modalidade:** Atividade individual remota  

---

## 📌 Apresentação

Este repositório contém a resolução da atividade prática de revisão sobre **Estruturas de Árvores**, cobrindo desde conceitos fundamentais até estruturas avançadas como AVL, Rubro-Negra, Árvore B e B+.

---

## 🎯 Objetivos

* Retomar conceitos fundamentais: nó, raiz, pai, filho, folha, altura e percurso.
* Analisar e comparar as regras, propriedades e aplicações dos principais tipos de árvores.
* Relacionar analogias do cotidiano às propriedades técnicas e limitações das estruturas de dados.

---

## ✍️ Etapa 1 — Revisão Bibliográfica

### 1. Conceitos Básicos

* **Árvore:** Estrutura de dados não linear e hierárquica formada por um conjunto de nós conectados por arestas.
* **Raiz:** O nó principal no topo da hierarquia, que não possui nó pai.
* **Pai e Filho:** Um nó é "pai" dos nós imediatamente abaixo dele, que são seus "filhos".
* **Folha:** Nó terminal que não possui nenhum filho.
* **Altura:** O comprimento do caminho mais longo da raiz até uma folha.
* **Percurso:** A ordem de visitação dos nós (ex.: pré-ordem, em-ordem, pós-ordem e em largura).

### 2. Estruturas Analisadas

* **Árvore Geral:** Estrutura hierárquica sem limite fixo de ramificações por nó. Os dados são organizados com ponteiros/listas para filhos. Utilizada em sistemas de arquivos e documentos estruturados (XML/HTML).
* **Árvore Binária:** Estrutura em que cada nó possui no máximo dois filhos (esquerdo e direito). Não possui balanceamento automático. Utilizada em árvores de expressão e decisão.
* **Árvore Binária de Busca (ABB):** Mantém a propriedade de ordenação em que a subárvore esquerda de um nó contém apenas chaves menores que ele, e a direita apenas maiores. Utilizada para dicionários dinâmicos e tabelas de símbolos na memória principal.
* **Árvore AVL:** ABB autobalanceada onde a diferença de altura entre as subárvores esquerda e direita de qualquer nó (fator de balanceamento) é de no máximo 1. Ajustada via rotações simples ou duplas. Utilizada em sistemas com alto volume de consultas na memória.
* **Árvore Rubro-Negra (Red-Black):** ABB autobalanceada onde cada nó possui um atributo de cor (vermelho ou preto). O balanceamento é garantido por regras de coloração, mantendo a altura controlada por meio de recolorações e rotações. Utilizada em bibliotecas padrão de linguagens (`std::map` em C++, `TreeMap` em Java).
* **Árvore B:** Estrutura $m$-ária autobalanceada otimizada para armazenamento em memória secundária (disco). Todos os nós folhas estão no mesmo nível. Quando um nó enche, ocorre o *split* (cisão). Utilizada em sistemas de arquivos e índices de SGBDs.
* **Árvore B+:** Variação da Árvore B onde todos os registros residem exclusivamente nas folhas, enquanto os nós internos contêm apenas chaves de índice. As folhas são ligadas em lista encadeada, favorecendo consultas por intervalo (*range queries*).

---

## 📊 Etapa 2 — Quadro Comparativo

| Estrutura | Organização dos dados | Regra ou propriedade | Operação ou ajuste | Aplicação | Referência |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Árvore Geral** | Nós encadeados com $N$ ramificações arbitrárias. | Relação hierárquica sem limite fixo para a quantidade de nós filhos. | Percurso e inserção direta como filho; não requer rebalanceamento. | Sistemas de arquivos e documentos XML/HTML. | DROZDEK, A. (2018); CELES, W. & CERQUEIRA, R. (2004) |
| **Árvore Binária** | Estrutura hierárquica em que cada nó possui no máximo 2 filhos. | Grau de cada nó é no máximo 2. | Percursos (pré-ordem, em-ordem, pós-ordem) e inserção na primeira folha disponível. | Árvores de expressão aritmética e decisão. | DROZDEK, A. (2018); VETORAZZO, A. S. et al. (2018) |
| **ABB** | Nós encadeados ordenados com subárvores esquerda e direita. | Subárvore esquerda com chaves menores; subárvore direita com maiores. | Busca binária; remoção exige substituição pelo antecessor ou sucessor em-ordem. | Tabelas de símbolos e dicionários dinâmicos. | DROZDEK, A. (2018); VETORAZZO, A. S. et al. (2018) |
| **AVL** | Árvore binária de busca autobalanceada. | O fator de balanceamento $FB = |h_{dir} - h_{esq}|$ de todo nó deve ser $\le 1$. | Rotações simples (LL, RR) ou duplas (LR, RL) após alterações. | Sistemas com alto volume de consultas em memória. | DROZDEK, A. (2018); CELES, W. & CERQUEIRA, R. (2004) |
| **Rubro-negra** | ABB autobalanceada com bit de cor (vermelho/preto) em cada nó. | Raiz e folhas (NIL) são pretas; nó vermelho não tem filho vermelho; número de nós pretos constante em todos os caminhos. | Recolorações de nós e rotações para manter a altura controlada. | Estruturas de dados nativas (`std::map`, `TreeMap`). | DROZDEK, A. (2018) |
| **Heap** | Árvore binária quase completa mapeada em vetor/array. | Propriedade de Heap: no *Max-Heap*, a chave do pai é $\ge$ à dos filhos. | Operações *Heapify* (subir/descer nó no vetor após alterações). | Filas de prioridade e algoritmo Heapsort. | DROZDEK, A. (2018); ASCENCIO, A. F. G. & CAMPOS, E. A. V. (2007) |
| **Trie** | Árvore de prefixos onde as arestas/nós representam caracteres. | Caminho da raiz ao nó representa a sequência do prefixo compartilhado. | Inserção e busca caractere por caractere ao longo da palavra. | Autocompletar e verificação ortográfica. | DROZDEK, A. (2018) |
| **Árvore B** | Árvore de busca $m$-ária otimizada para bloco de memória secundária. | Múltiplas chaves por nó; todas as folhas no mesmo nível. | *Split* (cisão) em transbordo; *Merge* (fusão) em subfluxo de chaves. | Sistemas de arquivos (NTFS, ext4) e índices primários em SGBDs. | DROZDEK, A. (2018); VETORAZZO, A. S. et al. (2018) |
| **Árvore B+** | Variante da Árvore B com dados agrupados estritamente nas folhas. | Nós internos guardam apenas chaves de índice; folhas interligadas por lista encadeada. | Cisão e fusão de nós com atualização dos ponteiros da lista de folhas. | Índices secundários em SGBDs e consultas por intervalo. | DROZDEK, A. (2018) |

---

## 💡 Etapa 3 — Identificação por Analogias

1. **Estante reorganizada por rotações ao pender para um lado:**  
   Trata-se da **Árvore AVL**. A regra técnica principal dessa estrutura é o autobalanceamento, onde a diferença de altura entre a subárvore esquerda e a direita de qualquer nó (o chamado fator de balanceamento) nunca pode ser maior que 1; quando uma inserção ou remoção quebra esse limite, a árvore executa rotações simples ou duplas para reestabelecer o equilíbrio. O limite da analogia com a estante é que, no mundo físico, reorganizar livros envolve força, peso e espaço tridimensional real, enquanto na AVL o reajuste é puramente lógico, feito apenas trocando os ponteiros de memória entre os nós de forma instantânea.

2. **Catálogo que guarda várias chaves por página e se divide quando cheio:**  
   Trata-se da **Árvore B**. Ela é uma estrutura de busca multidirecional projetada para memória secundária, onde cada nó funciona como uma página que guarda múltiplos elementos e ponteiros; quando uma página atinge seu limite máximo de chaves, ocorre o processo de divisão conhecido como *split*, que reparte as chaves e promove a mediana para o nó pai para manter a árvore balanceada. O limite da analogia é que dividir uma página de papel em um fichário ou catálogo físico exige rasgar a folha ou encadernar novos papéis manualmente, enquanto na Árvore B o *split* aloca um novo nó em disco ou RAM e reorganiza os índices e ponteiros de forma totalmente automatizada.

3. **Fila que mantém a tarefa de maior prioridade no topo:**  
   Trata-se do **Heap Binário (Max-Heap)**, muito usado para implementar filas de prioridade. Essa estrutura satisfaz a propriedade de Heap, onde o valor de qualquer nó pai é sempre maior ou igual ao de seus filhos, o que garante que o elemento de maior prioridade fique isolado logo no topo, na raiz, permitindo remoção em tempo constante $O(1)$ e reajuste rápido por *heapify*. O limite dessa comparação é que em uma fila humana ou de tarefas comum as pessoas ficam paradas em uma linha reta física, enquanto no Heap os dados ficam dispostos em uma hierarquia de árvore (geralmente mapeada num vetor) onde apenas a raiz tem ordenação absoluta em relação aos descendentes diretos.

4. **Índice que percorre letras sucessivas e compartilha prefixos:**  
   Trata-se da **Trie** (ou Árvore de Prefixos). Sua propriedade técnica marcante é organizar os dados caractere por caractere ao longo do caminho da árvore, fazendo com que palavras que começam com as mesmas letras compartilhem exatamente os mesmos nós iniciais (os prefixos) até o ponto em que se diferenciam. O limite da analogia é que um índice impresso tradicional precisa escrever a palavra inteira repetidas vezes no papel, gerando redundância, enquanto a Trie economiza memória ao quebrar a palavra em letras e reutilizar os nós de prefixos já existentes sem precisar duplicar o texto.

5. **Estrutura que usa cores, recolorações e rotações para manter a altura:**  
   Trata-se da **Árvore Rubro-Negra (Red-Black Tree)**. A propriedade que a define é o uso de cores (cada nó é marcado como vermelho ou preto) combinadas a regras rígidas — como a raiz ser sempre preta, nós vermelhos não poderem ter filhos vermelhos e todos os caminhos até as folhas nulas terem a mesma quantidade de nós pretos —, utilizando recolorações e rotações para manter a altura controlada em tempo logarítmico. O limite da analogia é que a palavra "cor" aqui é apenas uma metáfora para um bit de controle (0 ou 1) que o algoritmo lê na memória para tomar decisões, não existindo qualquer aspecto visual ou estético no processador.

6. **Índice que conduz às folhas interligadas para consultas por intervalo:**  
   Trata-se da **Árvore B+**. Sua grande propriedade técnica é que todos os dados e registros reais ficam guardados exclusivamente nos nós folha, enquanto os nós superiores servem apenas como um índice de navegação; além disso, todas as folhas são interligadas diretamente por uma lista encadeada, o que torna buscas por intervalo extremamente rápidas. O limite da analogia é que um índice remete o leitor para páginas soltas do livro e exige que ele volte ao índice para procurar o próximo item, ao passo que na B+ as próprias páginas finais estão "grampeadas" em sequência, permitindo navegar de uma folha para a outra sem precisar subir de volta para os nós principais.

7. **Coleção onde cada nó direciona menores para a esquerda e maiores para a direita:**  
   Trata-se da **Árvore Binária de Busca (ABB ou BST)**. A propriedade técnica fundamental dessa estrutura dita que, para qualquer nó escolhido, todos os valores armazenados na sua subárvore esquerda devem ser estritamente menores que ele, e todos os valores na sua subárvore direita devem ser maiores. O limite da analogia é que organizar objetos físicos maiores e menores em caixas ou prateleiras requer mover e empurrar objetos de lugar no espaço real, enquanto na Árvore Binária de Busca os elementos permanecem nos seus endereços de memória e a ordenação é feita exclusivamente apontando as referências para os nós da esquerda ou da direita.

---

## 📚 Referências Bibliográficas

* **ASCENCIO, Ana Fernanda Gomes; CAMPOS, Edilene Aparecida Veneruchi de.** *Fundamentos da programação de computadores: algoritmos, pascal, C/C++ e java*. 2. ed. São Paulo: Pearson, 2007.
* **CELES, W.; CERQUEIRA, R.** *Introdução a estrutura de dados*. São Paulo: Campus, 2004.
* **DEITEL, H.; DEITEL, P.** *C: Como programar*. 6. ed. São Paulo: Prentice-Hall, 2011.
* **DROZDEK, Adam.** *Estrutura de Dados e Algoritmos em C++*. Tradução da 4ª edição. São Paulo: Cengage Learning Brasil, 2018.
* **FORBELLONE, André Luiz Villar; EBERSPÄCHER, Henri Frederico.** *Lógica de programação: a construção de algoritmos e estrutura de dados*. 2. ed. rev. e ampl. São Paulo: Makron Books, 2000.
* **NETTO, Paulo Oswaldo B.; JURKIEWICZ, Samuel.** *Grafos: introdução e prática*. Editora Blucher, 2017.
* **PEREIRA, A. W.** *Linguagem e Lógica de Programação*. Editora Saraiva, 2014.
* **VETORAZZO, Adriana de Souza et al.** *Estrutura de dados*. Porto Alegre: SAGAH, 2018.