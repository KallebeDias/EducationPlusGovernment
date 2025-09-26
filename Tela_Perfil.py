import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def criar_tela_perfil():
    janela = tk.Tk()
    janela.title("Perfil do Usuário")
    janela.geometry("700x500")
    janela.config(bg="lightgray")

    janela.grid_columnconfigure(0, weight=1)
    janela.grid_columnconfigure(1, weight=1)
    janela.grid_columnconfigure(2, weight=1)

    frame_info = tk.Frame(janela, bg="lightgray")
    frame_info.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    label_titulo = tk.Label(frame_info, text="Informações do Aluno", font=("Arial", 14), bg="lightgray", fg="black")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

    frame_esquerda = tk.Frame(frame_info, bg="lightgray")
    frame_esquerda.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

    frame_direita = tk.Frame(frame_info, bg="lightgray")
    frame_direita.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

    tk.Label(frame_esquerda, text="Nome:", bg="lightgray", fg="black").grid(row=0, column=0, sticky="e", pady=5)
    entry_nome = tk.Entry(frame_esquerda)
    entry_nome.grid(row=0, column=1, pady=5)

    tk.Label(frame_esquerda, text="Matrícula:", bg="lightgray", fg="black").grid(row=1, column=0, sticky="e", pady=5)
    entry_matricula = tk.Entry(frame_esquerda)
    entry_matricula.grid(row=1, column=1, pady=5)

    tk.Label(frame_esquerda, text="Turma:", bg="lightgray", fg="black").grid(row=2, column=0, sticky="e", pady=5)
    entry_turma = tk.Entry(frame_esquerda)
    entry_turma.grid(row=2, column=1, pady=5)

    tk.Label(frame_direita, text="Turno:", bg="lightgray", fg="black").grid(row=0, column=0, sticky="e", pady=5)
    entry_turno = tk.Entry(frame_direita)
    entry_turno.grid(row=0, column=1, pady=5)

    # Área para foto
    frame_foto = tk.Frame(frame_direita, bg="lightgray")
    frame_foto.grid(row=1, column=0, columnspan=2, pady=10)

    label_foto = tk.Label(frame_foto, text="Nenhuma foto", bg="white", width=20, height=10, relief="sunken")
    label_foto.pack()

    # Variável para armazenar a imagem carregada (para evitar garbage collection)
    foto_img = None

    def carregar_foto():
        nonlocal foto_img
        caminho = filedialog.askopenfilename(
            title="Selecione uma foto",
            filetypes=[("Arquivos de imagem", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if caminho:
            try:
                img = Image.open(caminho)
                img.thumbnail((150, 150))
                foto_img = ImageTk.PhotoImage(img)
                label_foto.config(image=foto_img, text="")
                label_foto.image_path = caminho  # Armazena caminho na label
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível carregar a imagem:\n{e}")

    btn_carregar_foto = tk.Button(frame_foto, text="Carregar Foto", command=carregar_foto)
    btn_carregar_foto.pack(pady=5)

    frame_vazio = tk.Frame(janela, bg="lightgray")
    frame_vazio.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

    frame_saida = tk.Frame(janela, bg="white", relief="sunken", borderwidth=1)
    frame_saida.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=10, pady=(0,10))

    janela.grid_rowconfigure(2, weight=1) 

    text_saida = tk.Text(frame_saida, height=8, bg="white", fg="black")
    text_saida.pack(fill="both", expand=True, padx=5, pady=5)

    frame_botoes = tk.Frame(janela, bg="lightgray")
    frame_botoes.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

    frame_botoes.grid_columnconfigure(0, weight=1)
    frame_botoes.grid_columnconfigure(1, weight=1)
    frame_botoes.grid_columnconfigure(2, weight=1)

    alunos = []

    def atualizar_lista():
        text_saida.delete("1.0", tk.END)
        for i, aluno in enumerate(alunos, start=1):
            dados = (
                f"{i}. Nome: {aluno['nome']}\n"
                f"   Matrícula: {aluno['matricula']}\n"
                f"   Turma: {aluno['turma']}\n"
                f"   Turno: {aluno['turno']}\n"
                f"   Foto: {aluno['foto'] if aluno['foto'] else 'Nenhuma'}\n\n"
            )
            text_saida.insert(tk.END, dados)

    def salvar():
        nome = entry_nome.get().strip()
        matricula = entry_matricula.get().strip()
        turma = entry_turma.get().strip()
        turno = entry_turno.get().strip()
        foto = getattr(label_foto, "image_path", None)

        if not nome or not matricula:
            messagebox.showwarning("Aviso", "Nome e Matrícula são obrigatórios!")
            return

        alunos.append({
            "nome": nome,
            "matricula": matricula,
            "turma": turma,
            "turno": turno,
            "foto": foto
        })

        atualizar_lista()
        limpar_campos()

    def editar():
        if not alunos:
            messagebox.showinfo("Info", "Nenhum aluno para editar!")
            return

        aluno = alunos[-1]

        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, aluno["nome"])

        entry_matricula.delete(0, tk.END)
        entry_matricula.insert(0, aluno["matricula"])

        entry_turma.delete(0, tk.END)
        entry_turma.insert(0, aluno["turma"])

        entry_turno.delete(0, tk.END)
        entry_turno.insert(0, aluno["turno"])

        # Carregar foto do aluno
        nonlocal foto_img
        if aluno["foto"]:
            try:
                img = Image.open(aluno["foto"])
                img.thumbnail((150, 150))
                foto_img = ImageTk.PhotoImage(img)
                label_foto.config(image=foto_img, text="")
                label_foto.image_path = aluno["foto"]
            except Exception as e:
                label_foto.config(image="", text="Nenhuma foto")
                label_foto.image_path = None
                messagebox.showerror("Erro", f"Não foi possível carregar a imagem:\n{e}")
        else:
            label_foto.config(image="", text="Nenhuma foto")
            label_foto.image_path = None

        alunos.pop()
        atualizar_lista()
        print("Modo de edição ativado para o último aluno.")

    def excluir():
        if alunos:
            alunos.pop()
            atualizar_lista()
            print("Último aluno excluído!")
        else:
            messagebox.showinfo("Info", "Nenhum aluno para excluir!")

        limpar_campos()

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_matricula.delete(0, tk.END)
        entry_turma.delete(0, tk.END)
        entry_turno.delete(0, tk.END)
        label_foto.config(image="", text="Nenhuma foto")
        label_foto.image_path = None

    btn_salvar = tk.Button(frame_botoes, text="Salvar", font=("Arial", 10), command=salvar,
                           bg="lightblue", fg="black")
    btn_salvar.grid(row=0, column=0, sticky="ew", padx=5)

    btn_editar = tk.Button(frame_botoes, text="Editar", font=("Arial", 10), command=editar,
                           bg="lightyellow", fg="black")
    btn_editar.grid(row=0, column=1, sticky="ew", padx=5)

    btn_excluir = tk.Button(frame_botoes, text="Excluir", font=("Arial", 10), command=excluir,
                            bg="lightcoral", fg="black")
    btn_excluir.grid(row=0, column=2, sticky="ew", padx=5)

    janela.mainloop()

criar_tela_perfil()
