# 🔄 Estrutura de Dados: Implementação de Fila (Queue) em C

> Este repositório contém a implementação completa de uma **Fila de Números Inteiros** (estrutura FIFO - *First In, First Out*) em linguagem C, incluindo controle de início/fim e menu interativo.

---

## 📌 Sobre a Atividade

A fila é uma estrutura de dados onde os elementos são inseridos no final (`fim`) e removidos do início (`inicio`). 

O programa controla o limite da fila com base em um tamanho fixo (`TAM = 5`) e disponibiliza as seguintes operações:

1. **Enfileirar (`enfileirar`):** Adiciona um elemento no final da fila.
2. **Desenfileirar (`desenfileirar`):** Remove e retorna o primeiro elemento da fila.
3. **Mostrar Fila (`mostrar`):** Exibe todos os elementos atualmente armazenados.
4. **Esvaziar Fila (`esvaziar`):** Reseta os ponteiros de início e fim, limpando a fila.

---

## 💻 Código Fonte Completo

```c
#include <stdio.h>

#define TAM 5

struct fila {
    int dados[TAM];
    int inicio;
    int fim;
};

struct fila f;

void enfileirar(int elemento) {
    if (f.fim == TAM) {
        printf("Fila cheia!\n");
    } else {
        f.dados[f.fim] = elemento;
        f.fim++;
    }
}

int desenfileirar() {
    int elemento;
    if (f.inicio == f.fim) {
        printf("Fila vazia!\n");
        return -1;
    } else {
        elemento = f.dados[f.inicio];
        f.inicio++;
        return elemento;
    }
}

void mostrar() {
    int i;
    printf("Fila: ");
    for (i = f.inicio; i < f.fim; i++) {
        printf("%d ", f.dados[i]);
    }
    printf("\n");
}

void esvaziar() {
    f.inicio = 0;
    f.fim = 0;
}

int main() {
    int opcao, elemento;
    f.inicio = 0;
    f.fim = 0;

    do {
        printf("\n--- MENU FILA ---\n");
        printf("1. Enfileirar\n");
        printf("2. Desenfileirar\n");
        printf("3. Mostrar Fila\n");
        printf("4. Esvaziar Fila\n");
        printf("5. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite o elemento a ser enfileirado: ");
                scanf("%d", &elemento);
                enfileirar(elemento);
                break;
            case 2:
                elemento = desenfileirar();
                if (elemento != -1) {
                    printf("Elemento desenfileirado: %d\n", elemento);
                }
                break;
            case 3:
                mostrar();
                break;
            case 4:
                esvaziar();
                printf("Fila esvaziada.\n");
                break;
            case 5:
                printf("Saindo...\n");
                break;
            default:
                printf("Opcao invalida!\n");
        }
    } while (opcao != 5);

    return 0;
}
