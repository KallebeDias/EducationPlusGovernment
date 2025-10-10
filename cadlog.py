import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import hashlib
from main import Application
from databasepi import verificar_login, cadastrar_usuario

# Configurações de cores (mantendo o tema anterior)
COR_FUNDO = "#f0f0f0"  # Cinza claro
COR_TEXTO = "#34495e"  # Cor escura
COR_BRANCO = "#ffffff"  # Branco
COR_BORDA = "#271b1b"  # Cinza para bordas
COR_HOVER = "#e8e8e8"  # Hover


# Classe principal para a interface
class AppLoginCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login e Cadastro")
        self.root.geometry("400x500")
        self.root.configure(bg=COR_FUNDO)
        
        # Frame principal
        self.frame_principal = tk.Frame(root, bg=COR_FUNDO)
        self.frame_principal.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Título
        self.titulo = tk.Label(
            self.frame_principal,
            text="Bem-vindo!",
            font=("Arial", 20, "bold"),
            fg=COR_TEXTO,
            bg=COR_FUNDO
        )
        self.titulo.pack(pady=20)
        
        # Botão para alternar para Login
        self.btn_login = tk.Button(
            self.frame_principal,
            text="Login",
            font=("Arial", 12, "bold"),
            fg=COR_BRANCO,
            bg=COR_TEXTO,
            relief=tk.FLAT,
            padx=20,
            pady=10,
            command=self.mostrar_login
        )
        self.btn_login.pack(pady=10)
        
        # Botão para alternar para Cadastro
        self.btn_cadastro = tk.Button(
            self.frame_principal,
            text="Cadastro",
            font=("Arial", 12, "bold"),
            fg=COR_BRANCO,
            bg=COR_TEXTO,
            relief=tk.FLAT,
            padx=20,
            pady=10,
            command=self.mostrar_cadastro
        )
        self.btn_cadastro.pack(pady=10)
        
        # Inicialmente mostrar tela de login
        self.mostrar_login()
    
    def limpar_frame(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()
            widget.quit()
        
    
    def mostrar_login(self):
        self.limpar_frame()
        
        # Frame para campos de login
        frame_login = tk.Frame(self.frame_principal, bg=COR_FUNDO)
        frame_login.pack(expand=True, fill=tk.BOTH)
        
        # Label de instrução
        instruc = tk.Label(
            frame_login,
            text="Faça login com suas credenciais:",
            font=("Arial", 12),
            fg=COR_TEXTO,
            bg=COR_FUNDO
        )
        instruc.pack(pady=10)
        
        # Username
        tk.Label(frame_login, text="Usuário:", font=("Arial", 10), fg=COR_TEXTO, bg=COR_FUNDO).pack(pady=5)
        self.entry_username_login = tk.Entry(frame_login, font=("Arial", 10), relief=tk.FLAT, bd=2, highlightbackground=COR_BORDA)
        self.entry_username_login.pack(pady=5, padx=20, fill=tk.X)
        
        # Senha
        tk.Label(frame_login, text="Senha:", font=("Arial", 10), fg=COR_TEXTO, bg=COR_FUNDO).pack(pady=5)
        self.entry_senha_login = tk.Entry(frame_login, font=("Arial", 10), show="*", relief=tk.FLAT, bd=2, highlightbackground=COR_BORDA)
        self.entry_senha_login.pack(pady=5, padx=20, fill=tk.X)
        
        # Botão de login
        btn_login = tk.Button(
            frame_login,
            text="Entrar",
            font=("Arial", 12, "bold"),
            fg=COR_BRANCO,
            bg=COR_TEXTO,
            relief=tk.FLAT,
            padx=20,
            pady=10,
            command=self.fazer_login
        )
        btn_login.pack(pady=20)
    
    def fazer_login(self):
        username = self.entry_username_login.get().strip()
        senha = self.entry_senha_login.get().strip()
        
        if not username or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if verificar_login(username, senha):
            self.app = Application()
            self.limpar_frame()
            self.app.root.mainloop()
            
            # Aqui você pode abrir a tela principal do app (ex: atividades)
            #self.root.quit()  # Fecha a janela por enquanto; substitua por navegação real
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
    
    def mostrar_cadastro(self):
        self.limpar_frame()
        
        # Frame para campos de cadastro
        frame_cadastro = tk.Frame(self.frame_principal, bg=COR_FUNDO)
        frame_cadastro.pack(expand=True, fill=tk.BOTH)
        
        # Label de instrução
        instruc = tk.Label(
            frame_cadastro,
            text="Crie uma nova conta:",
            font=("Arial", 12),
            fg=COR_TEXTO,
            bg=COR_FUNDO
        )
        instruc.pack(pady=10)
        
        # Username
        tk.Label(frame_cadastro, text="Usuário:", font=("Arial", 10), fg=COR_TEXTO, bg=COR_FUNDO).pack(pady=5)
        self.entry_username_cadastro = tk.Entry(frame_cadastro, font=("Arial", 10), relief=tk.FLAT, bd=2, highlightbackground=COR_BORDA)
        self.entry_username_cadastro.pack(pady=5, padx=20, fill=tk.X)
        
        # Senha
        tk.Label(frame_cadastro, text="Senha:", font=("Arial", 10), fg=COR_TEXTO, bg=COR_FUNDO).pack(pady=5)
        self.entry_senha_cadastro = tk.Entry(frame_cadastro, font=("Arial", 10), show="*", relief=tk.FLAT, bd=2, highlightbackground=COR_BORDA)
        self.entry_senha_cadastro.pack(pady=5, padx=20, fill=tk.X)
        
        # Confirmar senha
        tk.Label(frame_cadastro, text="Confirmar Senha:", font=("Arial", 10), fg=COR_TEXTO, bg=COR_FUNDO).pack(pady=5)
        self.entry_confirmar_senha = tk.Entry(frame_cadastro, font=("Arial", 10), show="*", relief=tk.FLAT, bd=2, highlightbackground=COR_BORDA)
        self.entry_confirmar_senha.pack(pady=5, padx=20, fill=tk.X)
        
        # Botão de cadastro
        btn_cadastro = tk.Button(
            frame_cadastro,
            text="Cadastrar",
            font=("Arial", 12, "bold"),
            fg=COR_BRANCO,
            bg=COR_TEXTO,
            relief=tk.FLAT,
            padx=20,
            pady=10,
            command=self.fazer_cadastro
        )
        btn_cadastro.pack(pady=20)
    
    def fazer_cadastro(self):
        username = self.entry_username_cadastro.get().strip()
        senha = self.entry_senha_cadastro.get().strip()
        confirmar = self.entry_confirmar_senha.get().strip()
        
        if not username or not senha or not confirmar:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if senha != confirmar:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return
        
        if len(senha) < 6:
            messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres!")
            return
        
        if cadastrar_usuario(username, senha):
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso! Agora faça login.")
            self.mostrar_login()  # Volta para login
        else:
            messagebox.showerror("Erro", "Usuário já existe! Escolha outro nome.")

# Executar o programa
if __name__ == "__main__":
    root = tk.Tk()
    app = AppLoginCadastro(root)
    root.mainloop()
