import tkinter as tk
from tkinter import messagebox

# Configurações de cores
COR_FUNDO = "#f0f0f0"  # Cinza claro (gravite claro)
COR_TEXTO = "#34495e"  # Cor escura especificada
COR_BRANCO = "#ffffff"  # Branco
COR_BORDA = "#d0d0d0"  # Cinza claro para bordas
COR_HOVER = "#e8e8e8"  # Cinza mais claro para hover

# Função para criar a tela de atividades com quadrados
def criartelaatividades():
    # Criar a janela principal
    root = tk.Tk()
    root.title("Tela de Atividades")
    root.geometry("800x600")
    root.configure(bg=COR_FUNDO)
    
    # Título principal
    titulo = tk.Label(
        root,
        text="Atividades Diárias",
        font=("Arial", 20, "bold"),
        fg=COR_TEXTO,
        bg=COR_FUNDO
    )
    titulo.pack(pady=30)
    
    # Frame principal para organizar os quadrados
    frame_principal = tk.Frame(root, bg=COR_FUNDO)
    frame_principal.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)
    
    # Lista de atividades de exemplo
    atividades = [
        {
            "titulo": "Leitura",
            "descricao": "Ler um livro por 30 minutos",
            "icone": "📚"
        },
        {
            "titulo": "Exercícios",
            "descricao": "Fazer exercícios físicos",
            "icone": "💪"
        },
        {
            "titulo": "Estudo",
            "descricao": "Estudar uma nova habilidade",
            "icone": "🎯"
        },
        {
            "titulo": "Organização",
            "descricao": "Organizar o ambiente",
            "icone": "🧹"
        },
        {
            "titulo": "Meditação",
            "descricao": "Praticar meditação",
            "icone": "🧘"
        },
        {
            "titulo": "Criatividade",
            "descricao": "Fazer algo criativo",
            "icone": "🎨"
        }
    ]
    
    # Função para criar efeito hover
    def on_enter(event, button):
        button.configure(bg=COR_HOVER)
        
    def on_leave(event, button):
        button.configure(bg=COR_BRANCO)
    
    # Função para mostrar conclusão
    def mostrar_concluida(atividade):
        messagebox.showinfo("Atividade Concluída", f"Você concluiu: {atividade['titulo']}")
    
    # Criar grid 2x3 para os quadrados
    for i, atividade in enumerate(atividades):
        row = i // 3  # 3 colunas
        col = i % 3   # 3 colunas
        
        # Frame quadrado para cada atividade
        frame_quadrado = tk.Frame(
            frame_principal,
            bg=COR_BRANCO,
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=20
        )
        frame_quadrado.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
        frame_quadrado.configure(highlightbackground=COR_BORDA)
        
        # Configurar peso das linhas e colunas para expandir
        frame_principal.grid_rowconfigure(row, weight=1)
        frame_principal.grid_columnconfigure(col, weight=1)
        
        # Ícone da atividade
        label_icone = tk.Label(
            frame_quadrado,
            text=atividade["icone"],
            font=("Arial", 24),
            bg=COR_BRANCO,
            fg=COR_TEXTO
        )
        label_icone.pack(pady=(10, 5))
        
        # Título da atividade
        label_titulo = tk.Label(
            frame_quadrado,
            text=atividade["titulo"],
            font=("Arial", 12, "bold"),
            bg=COR_BRANCO,
            fg=COR_TEXTO,
            wraplength=150
        )
        label_titulo.pack(pady=(0, 5))
        
        # Descrição da atividade
        label_descricao = tk.Label(
            frame_quadrado,
            text=atividade["descricao"],
            font=("Arial", 9),
            bg=COR_BRANCO,
            fg=COR_TEXTO,
            wraplength=150,
            justify=tk.CENTER
        )
        label_descricao.pack(pady=(0, 10))
        
        # Botão de concluir
        btn_concluir = tk.Button(
            frame_quadrado,
            text="Concluir",
            font=("Arial", 10),
            fg=COR_BRANCO,
            bg=COR_TEXTO,
            relief=tk.FLAT,
            padx=15,
            pady=5,
            command=lambda a=atividade: mostrar_concluida(a)
        )
        btn_concluir.pack(pady=5)
        
        # Configurar eventos de hover para o frame inteiro
        frame_quadrado.bind("<Enter>", lambda e, b=frame_quadrado: on_enter(e, b))
        frame_quadrado.bind("<Leave>", lambda e, b=frame_quadrado: on_leave(e, b))
        
        # Tornar o frame clicável
        frame_quadrado.bind("<Button-1>", lambda e, a=atividade: mostrar_concluida(a))
        
        # Tornar os labels clicáveis também
        for widget in [label_icone, label_titulo, label_descricao]:
            widget.bind("<Button-1>", lambda e, a=atividade: mostrar_concluida(a))
            widget.configure(cursor="hand2")
    
    # Rodapé com instruções
    rodape = tk.Label(
        root,
        text="Clique em qualquer área do quadrado para marcar a atividade como concluída.",
        font=("Arial", 9),
        fg=COR_TEXTO,
        bg=COR_FUNDO
    )
    rodape.pack(side=tk.BOTTOM, pady=20)
    
    # Iniciar o loop principal
    root.mainloop()

# Executar o programa
if __name__ == "__main__":
    criartelaatividades()
