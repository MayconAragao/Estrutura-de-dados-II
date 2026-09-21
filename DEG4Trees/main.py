# Red-Black Tree Industrial Conveyor Game Simulation
# Simulação do Core Loop do jogo DEG4Trees Upgrade

class Node:
    def __init__(self, key):
        self.key = key
        self.color = "VERMELHO"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTreeGameEngine:
    def __init__(self, max_height=5):
        self.NIL = Node(0)
        self.NIL.color = "PRETO"
        self.root = self.NIL
        self.max_height = max_height
        self.score = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent and k.parent.color == "VERMELHO":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "VERMELHO":
                    print("  [PIS] Tio e VERMELHO -> Pistao Termico (Recoloricacao)...")
                    u.color = "PRETO"
                    k.parent.color = "PRETO"
                    k.parent.parent.color = "VERMELHO"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        print("  [BRA] Braco Mecanico -> Rotacao a Direita no pai...")
                        k = k.parent
                        self.right_rotate(k)
                    print("  [BRA] Braco Mecanico -> Rotacao a Esquerda no avo...")
                    k.parent.color = "PRETO"
                    k.parent.parent.color = "VERMELHO"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "VERMELHO":
                    print("  [PIS] Tio e VERMELHO -> Pistao Termico (Recoloricacao)...")
                    u.color = "PRETO"
                    k.parent.color = "PRETO"
                    k.parent.parent.color = "VERMELHO"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        print("  [BRA] Braco Mecanico -> Rotacao a Esquerda no pai...")
                        k = k.parent
                        self.left_rotate(k)
                    print("  [BRA] Braco Mecanico -> Rotacao a Direita no avo...")
                    k.parent.color = "PRETO"
                    k.parent.parent.color = "VERMELHO"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "PRETO"

    def insert(self, key):
        print(f"Novo pacote recebido da esteira: [ {key} ] (Cor: VERMELHO)")
        node = Node(key)
        node.parent = None
        node.left = self.NIL
        node.right = self.NIL
        node.color = "VERMELHO"

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "PRETO"
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)
        self.score += 10

    def get_height(self, node):
        if node == self.NIL or node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def print_tree(self, node, indent="", last=True):
        if node != self.NIL:
            print(indent, end="")
            if last:
                print("└── ", end="")
                indent += "    "
            else:
                print("├── ", end="")
                indent += "│   "
            color_str = "VERMELHO" if node.color == "VERMELHO" else "PRETO"
            print(f"{node.key} ({color_str})")
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

if __name__ == "__main__":
    game = RedBlackTreeGameEngine(max_height=5)
    pacotes_esteira = [10, 20, 30, 15, 25, 5, 1]

    print("==========================================================")
    print("INICIANDO SIMULACAO: DEG4Trees Upgrade (Arvore Rubro-Negra)")
    print("==========================================================
")

    for pkg in pacotes_esteira:
        game.insert(pkg)
        print("
--- Estado Atual da Arvore Industrial ---")
        game.print_tree(game.root)
        current_h = game.get_height(game.root)
        print(f"Altura Atual: {current_h} / Limite da Tela: {game.max_height}")
        
        if current_h > game.max_height:
            print("
DEGRADACAO ALGORITMICA! A estrutura atingiu o teto.")
            print("GAME OVER: O galpão colapsou.")
            break
        print("-" * 50 + "
")

    print(f"Rodada concluida! Pontuacao Total: {game.score} pts")
