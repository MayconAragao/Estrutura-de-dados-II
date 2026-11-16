🌳 Estrutura de Dados II — Árvores
📚 Introdução

Árvores são estruturas de dados não lineares utilizadas para organizar e armazenar informações de maneira hierárquica. Diferentemente das estruturas lineares, como listas, filas e pilhas, nas árvores os elementos são organizados em níveis, estabelecendo relações entre pais e filhos.

As árvores são muito utilizadas em sistemas de arquivos, bancos de dados, mecanismos de busca, compiladores e algoritmos de ordenação.

🌱 1. Conceitos fundamentais

Uma árvore é formada por elementos chamados nós (nodes), que estão conectados por arestas.

Principais conceitos:

Raiz (Root): primeiro nó da árvore.
Nó: elemento que armazena uma informação.
Aresta: conexão entre dois nós.
Pai: nó que possui um ou mais filhos.
Filho: nó conectado abaixo de outro nó.
Folha: nó que não possui filhos.
Subárvore: parte de uma árvore que possui sua própria raiz.
Altura: maior distância, em arestas, entre a raiz e uma folha.
Profundidade: distância da raiz até determinado nó.
Grau: quantidade de filhos de um nó.
Exemplo de uma árvore
text
          A
        /   \
       B     C
      / \     \
     D   E     F


Nesse exemplo:

A é a raiz.
B e C são filhos de A.
D, E e F são folhas.
A possui grau 2.
B e C estão no nível 1.
🌳 2. Árvore Binária

Uma árvore binária é uma estrutura em que cada nó pode possuir, no máximo, dois filhos:

Filho à esquerda.
Filho à direita.

Exemplo:

text
          10
         /  \
        5    15
       / \     \
      3   7     20

Características
Cada nó possui no máximo dois filhos.
Os nós podem possuir zero, um ou dois filhos.
Permite organizar dados de maneira hierárquica.
É utilizada em pesquisas e ordenação de dados.
🌿 3. Árvore Binária de Busca (ABB)

A Árvore Binária de Busca é um tipo especial de árvore binária que segue uma regra de organização:

Valores menores que o nó atual ficam à esquerda.
Valores maiores que o nó atual ficam à direita.

Exemplo:

text
          50
         /  \
        30   70
       / \   / \
      20 40 60 80


Essa organização permite realizar operações de busca, inserção e remoção.

Operações principais

Inserção: adiciona um novo elemento respeitando as regras da árvore.

Busca: procura um valor percorrendo os nós da árvore.

Remoção: exclui um elemento, reorganizando a árvore quando necessário.

💻 4. Implementação de uma Árvore Binária em C

Exemplo de estrutura de um nó:

c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *esquerda;
    struct No *direita;
} No;

Criando um novo nó
c
No* criarNo(int valor) {
    No *novo = malloc(sizeof(No));

    if (novo == NULL) {
        return NULL;
    }

    novo->valor = valor;
    novo->esquerda = NULL;
    novo->direita = NULL;

    return novo;
}

Inserindo elementos na árvore
c
No* inserir(No *raiz, int valor) {

    if (raiz == NULL) {
        return criarNo(valor);
    }

    if (valor < raiz->valor) {
        raiz->esquerda =
            inserir(raiz->esquerda, valor);
    }
    else if (valor > raiz->valor) {
        raiz->direita =
            inserir(raiz->direita, valor);
    }

    return raiz;
}

🔄 5. Percursos em Árvores

Os percursos são maneiras de visitar todos os nós de uma árvore.

Existem três principais tipos de percurso em profundidade:

Pré-ordem (Preorder)

Ordem de visita:

Raiz.
Subárvore esquerda.
Subárvore direita.
c
void preOrdem(No *raiz) {
    if (raiz != NULL) {
        printf("%d ", raiz->valor);
        preOrdem(raiz->esquerda);
        preOrdem(raiz->direita);
    }
}

Em ordem (Inorder)

Ordem de visita:

Subárvore esquerda.
Raiz.
Subárvore direita.
c
void emOrdem(No *raiz) {
    if (raiz != NULL) {
        emOrdem(raiz->esquerda);
        printf("%d ", raiz->valor);
        emOrdem(raiz->direita);
    }
}


Em uma árvore binária de busca, esse percurso apresenta os valores em ordem crescente.

Pós-ordem (Postorder)

Ordem de visita:

Subárvore esquerda.
Subárvore direita.
Raiz.
c
void posOrdem(No *raiz) {
    if (raiz != NULL) {
        posOrdem(raiz->esquerda);
        posOrdem(raiz->direita);
        printf("%d ", raiz->valor);
    }
}

⚖️ 6. Árvores Balanceadas

Uma árvore balanceada é aquela que mantém uma distribuição relativamente equilibrada entre seus nós, evitando que a estrutura fique muito inclinada para um dos lados.

O balanceamento é importante porque pode melhorar o desempenho das operações de busca, inserção e remoção.

Árvore AVL

A árvore AVL é uma árvore binária de busca que mantém seu balanceamento automaticamente.

Ela utiliza rotações para corrigir desequilíbrios:

Rotação simples à esquerda.
Rotação simples à direita.
Rotação dupla esquerda-direita.
Rotação dupla direita-esquerda.
Árvore Rubro-Negra

É uma árvore binária de busca balanceada que utiliza regras de cores (vermelho e preto) para controlar sua altura e manter operações eficientes.

⏱️ 7. Complexidade das operações

A complexidade representa o custo computacional de uma operação.

Operação	Árvore balanceada	Pior caso em ABB
Busca	O(log n)	O(n)
Inserção	O(log n)	O(n)
Remoção	O(log n)	O(n)

O pior caso acontece quando uma árvore binária de busca fica muito desbalanceada, funcionando de maneira semelhante a uma lista encadeada.

🌲 8. Aplicações das Árvores

As árvores são utilizadas em diversas áreas da computação:

Sistemas de arquivos e diretórios.
Bancos de dados.
Inteligência artificial.
Compiladores.
Algoritmos de busca.
Organização de informações.
Árvores de decisão.
📝 9. Conclusão

As árvores são estruturas fundamentais em Estrutura de Dados II, pois permitem organizar informações de forma hierárquica e realizar operações de maneira eficiente.

Compreender conceitos como árvores binárias, árvores binárias de busca, percursos e balanceamento é essencial para desenvolver algoritmos mais eficientes e entender estruturas utilizadas em sistemas computacionais reais.

📖 10. Referências
CORMEN, Thomas H. et al. Algoritmos: Teoria e Prática.
ZIVIANI, Nivio. Projeto de Algoritmos.
Material didático da disciplina de Estrutura de Dados II.

Disciplina: Estrutura de Dados II
Tema: Árvores
Linguagem de programação utilizada nos exemplos: C
