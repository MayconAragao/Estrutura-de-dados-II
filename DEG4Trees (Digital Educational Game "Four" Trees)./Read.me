# README — Game Design Document Briefing (GDD)

## 📌 Visão Geral do Projeto
Este repositório contém a documentação e a especificação técnica do **Game Design Document Briefing (GDD)** desenvolvido para a disciplina de **Estruturas de Dados II**.
O objetivo principal do trabalho é aplicar conceitos de **Engenharia Reversa e Reuso de Modelos Educativos**, analisando as limitações didáticas e técnicas do jogo base **DEG4Trees** (*Digital Educational Game "Four" Trees*) e projetando uma mecânica inovadora baseada em **Árvores Rubro-Negras**.

---

## 👨‍💻 Identificação do Grupo
- **Integrantes:**
  - Maycon Fidelis Aragão
  - Beatriz Alves de Sousa
  - Caio Guilherme Batista Rodrigues
  - Ítalo George da Costa Diniz
- **Curso:** Ciência da Computação
- **Disciplina:** Estruturas de Dados II
- **Data:** 14 / 09 / 2026

---

## 🛠️ Diagnóstico do Modelo Reutilizado (DEG4Trees)

### 🔴 Limitações Identificadas no DEG4Trees Original:
1. **Desconexão Mecânica:** As operações de busca/inserção (minijogo do submarino) e de rotação (minijogo do garçom) ocorrem em cenários separados. O jogador não vivencia a causa e efeito imediata de como uma inserção provoca um desbalanceamento em tempo real.
2. **Defasagem de Conteúdo de ED II:** O jogo base contempla apenas Árvores Binárias de Busca (ABB) e Árvores AVL, ignorando estruturas avançadas essenciais como **Árvores Rubro-Negras** e **Árvores B/B+**.
3. **Ausência de Aprendizagem Ativa de Recoloração:** Ao separar a remoção/inserção das rotações, o aluno não aplica ativamente as regras formais de checagem da **cor do nó tio**, **recoloramento** e manutenção da **altura negra**.
4. **Problemas de Usabilidade e Interface:** A execução visual das rotações no modo AVL apresenta pouca clareza e baixos índices de aceitação de interface pelos usuários (como evidenciado na avaliação do artigo original).

---

## 🚀 Proposta de Upgrade: Esteira Industrial com Árvores Rubro-Negras

O novo game design unifica inserção, verificação e correção em um único *core loop* dinâmico com temática de automação industrial.

### 🎮 Mapeamento de Conceitos em Mecânicas de Gameplay

| Conceito Teórico de ED II | Elemento / Mecânica Correspondente no Jogo |
| :--- | :--- |
| **Nó da Árvore / Chave** | Módulos com valores numéricos que chegam continuamente por uma esteira industrial. |
| **Altura da Árvore ($h$)** | Espaço físico vertical disponível na tela antes que a estrutura atinja o teto do galpão. |
| **Propriedades de Cor (Rubro-Negra)** | **Vermelho (Energizado/Instável):** Todo novo nó inserido nasce vermelho.<br>**Preto (Ancorado/Estável):** Nó estabilizado após validação. |
| **Operação de Correção: Recoloração** | **Pistão Térmico:** Utilizado ativamente quando o **nó tio é Vermelho** (alterna as cores do pai, tio e avô). |
| **Operação de Correção: Rotação** | **Braço Mecânico:** Utilizado quando o **nó tio é Preto** para reestruturar os ponteiros e resolver violações Vermelho-Vermelho (Rotações Simples ou Duplas). |

---

## 🔁 Core Loop e Condições de Jogo

### 🔄 Core Loop do Jogador:
1. **Recebimento:** Um novo pacote com valor numérico (nó vermelho) chega pela esteira industrial.
2. **Inserção ABB:** O jogador insere o pacote na posição correta seguindo as propriedades da Árvore Binária de Busca.
3. **Identificação de Conflito:** O jogador identifica visualmente a violação da regra Rubro-Negra (ex.: dois nós vermelhos consecutivos).
4. **Ação de Correção Ativa:**
   - Se o **tio for Vermelho** $
ightarrow$ Aciona o **Pistão Térmico** (Recolorização).
   - Se o **tio for Preto** $
ightarrow$ Aciona o **Braço Mecânico** (Rotação).

### 🏆 Condição de Vitória:
Organizar com sucesso todas as chaves da rodada mantendo as propriedades fundamentais da Árvore Rubro-Negra:
- Raiz sempre preta.
- Nenhum nó vermelho possui filho vermelho (sem nós vermelhos consecutivos).
- Altura negra ($bh$) uniforme em todos os caminhos da raiz às folhas.

### 💀 Condição de Derrota (Degradação Algorítmica):
A esteira entra em colapso e o cenário entra em pane por **degradação algorítmica**. 
Isso ocorre quando o jogador ignora os conflitos de cor e desbalanceamentos, fazendo com que a árvore se degenere em uma **lista encadeada**. Como resultado, a complexidade de busca atinge o pior caso $\mathcal{O}(n)$, a altura estoura a área útil da tela e o galpão é destruído.

---

## 📚 Referências
- **Jogo Base:** Barbosa, W. A., Nunes, I. F., Inocêncio, A. C. G., Oliveira, T. B., & Parreira Júnior, P. A. (2020). *DEG4Trees: Um Jogo Educacional Digital de Apoio ao Ensino de Estruturas de Dados*.
- **Fundamentação:** Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2002). *Algoritmos: teoria e prática*.
