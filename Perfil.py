import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def criartelaperfil():
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

    # Campos de entrada organizados na mesma coluna à esquerda
    tk.Label(frame_esquerda, text="Nome:", bg="lightgray", fg="black").grid(row=0, column=0, sticky="e", pady=5)
    entry_nome = tk.Entry(frame_esquerda)
    entry_nome.grid(row=0, column=1, pady=5, padx=(5, 0))

    tk.Label(frame_esquerda, text="Matrícula:", bg="lightgray", fg="black").grid(row=1, column=0, sticky="e", pady=5)
    entry_matricula = tk.Entry(frame_esquerda)
    entry_matricula.grid(row=1, column=1, pady=5, padx=(5, 0))

    tk.Label(frame_esquerda, text="Turma:", bg="lightgray", fg="black").grid(row=2, column=0, sticky="e", pady=5)
    entry_turma = tk.Entry(frame_esquerda)
    entry_turma.grid(row=2, column=1, pady=5, padx=(5, 0))

    tk.Label(frame_esquerda, text="Turno:", bg="lightgray", fg="black").grid(row=3, column=0, sticky="e", pady=5)
    entry_turno = tk.Entry(frame_esquerda)
    entry_turno.grid(row=3, column=1, pady=5, padx=(5, 0))

    # Área para foto (direita)
    frame_foto = tk.Frame(frame_direita, bg="lightgray")
    frame_foto.grid(row=1, column=0, columnspan=2, pady=10)

    label_foto = tk.Label(frame_foto, text="Nenhuma foto", bg="white", width=20, height=10, relief="sunken")
    label_foto.pack()

    # Variável para armazenar a imagem carregada (para evitar garbage collection)
    foto_img = None

    def carregarfoto():
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

    btn_carregar_foto = tk.Button(frame_foto, text="Carregar Foto", command=carregarfoto)
    btn_carregar_foto.pack(pady=5)

    frame_vazio = tk.Frame(janela, bg="lightgray")
    frame_vazio.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

    frame_saida = tk.Frame(janela, bg="#34495e", relief="sunken", borderwidth=1)
    frame_saida.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=10, pady=(0,10))

    janela.grid_rowconfigure(2, weight=1) 

    # Usar Listbox para seleção de alunos
    lista_alunos = tk.Listbox(frame_saida, height=8, bg="#34495e", fg="white", selectbackground="#5a9bd4", selectforeground="white")
    lista_alunos.pack(fill="both", expand=True, padx=5, pady=5)

    frame_botoes = tk.Frame(janela, bg="lightgray")
    frame_botoes.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

    frame_botoes.grid_columnconfigure(0, weight=1)
    frame_botoes.grid_columnconfigure(1, weight=1)
    frame_botoes.grid_columnconfigure(2, weight=1)

    alunos = []
    modo_edicao = False
    indice_edicao = None
    aluno_temp = None

    def atualizarlista():
        lista_alunos.delete(0, tk.END)
        for i, aluno in enumerate(alunos, start=1):
            item = f"{i}. {aluno['nome']} - Matrícula: {aluno['matricula']} (Turma: {aluno['turma']}, Turno: {aluno['turno']})"
            if aluno['foto']:
                item += " [Foto]"
            lista_alunos.insert(tk.END, item)

    def salvar():
        nonlocal modo_edicao, indice_edicao, aluno_temp  # Usar nonlocal em vez de global, pois estamos em função aninhada
        nome = entry_nome.get().strip()
        matricula = entry_matricula.get().strip()
        turma = entry_turma.get().strip()
        turno = entry_turno.get().strip()
        foto = getattr(label_foto, "image_path", None)

        if not nome or not matricula:
            messagebox.showwarning("Aviso", "Nome e Matrícula são obrigatórios!")
            return

        # Validação para matrícula (apenas números) - permite digitar letras, mas mostra erro no salvar
        if not matricula.isdigit():
            messagebox.showwarning("Aviso", "Matrícula deve conter apenas números!")
            return

        # Validação para turno (deve ser 'Matutino' ou 'Vespertino')
        if turno not in ["Matutino", "Vespertino"]:
            messagebox.showwarning("Aviso", "Turno deve ser 'Matutino' ou 'Vespertino'!")
            return

        novo_aluno = {
            "nome": nome,
            "matricula": matricula,
            "turma": turma,
            "turno": turno,
            "foto": foto
        }

        if modo_edicao and indice_edicao is not None and aluno_temp is not None:
            # Modo edição: inserir no índice original
            alunos.insert(indice_edicao, novo_aluno)
            modo_edicao = False
            indice_edicao = None
            aluno_temp = None
            messagebox.showinfo("Sucesso", "Aluno editado com sucesso!")
        else:
            # Modo normal: adicionar no final
            alunos.append(novo_aluno)
            messagebox.showinfo("Sucesso", "Aluno salvo com sucesso!")

        atualizarlista()
        limpar_campos()

    def editar():
        nonlocal modo_edicao, indice_edicao, aluno_temp
        selecao = lista_alunos.curselection()
        if not selecao:
            messagebox.showinfo("Info", "Selecione um aluno na lista para editar!")
            return

        indice = selecao[0]
        aluno_temp = alunos[indice].copy()  # Copia para evitar referência
        del alunos[indice]
        modo_edicao = True
        indice_edicao = indice

        # Carregar dados nos campos
        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, aluno_temp["nome"])

        entry_matricula.delete(0, tk.END)
        entry_matricula.insert(0, aluno_temp["matricula"])

        entry_turma.delete(0, tk.END)
        entry_turma.insert(0, aluno_temp["turma"])

        entry_turno.delete(0, tk.END)
        entry_turno.insert(0, aluno_temp["turno"])

        # Carregar foto do aluno
        nonlocal foto_img
        if aluno_temp["foto"]:
            try:
                img = Image.open(aluno_temp["foto"])
                img.thumbnail((150, 150))
                foto_img = ImageTk.PhotoImage(img)
                label_foto.config(image=foto_img, text="")
                label_foto.image_path = aluno_temp["foto"]
            except Exception as e:
                label_foto.config(image="", text="Nenhuma foto")
                label_foto.image_path = None
                messagebox.showerror("Erro", f"Não foi possível carregar a imagem:\n{e}")
        else:
            label_foto.config(image="", text="Nenhuma foto")
            label_foto.image_path = None

        atualizarlista()
        print(f"Modo de edição ativado para o aluno selecionado (índice original: {indice}).")

    def excluir():
        selecao = lista_alunos.curselection()
        if not selecao:
            messagebox.showinfo("Info", "Selecione um aluno na lista para excluir!")
            return

        indice = selecao[0]
        del alunos[indice]
        atualizarlista()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")
        print("Aluno selecionado excluído!")

    def limpar_campos():
        nonlocal modo_edicao, indice_edicao, aluno_temp
        entry_nome.delete(0, tk.END)
        entry_matricula.delete(0, tk.END)
        entry_turma.delete(0, tk.END)
        entry_turno.delete(0, tk.END)
        label_foto.config(image="", text="Nenhuma foto")
        label_foto.image_path = None
        # Se estava em modo edição e limpa, cancelar edição restaurando o aluno original
        if modo_edicao and aluno_temp is not None:
            alunos.insert(indice_edicao, aluno_temp)
            atualizarlista()
            modo_edicao = False
            indice_edicao = None
            aluno_temp = None
            messagebox.showinfo("Info", "Edição cancelada. Campos limpos.")

    btn_salvar = tk.Button(frame_botoes, text="Salvar", font=("Arial", 10), command=salvar,
                           bg="white",)
    btn_salvar.grid(row=0, column=0, sticky="ew", padx=5)  # Corrigido: era btn_salver

    btn_editar = tk.Button(frame_botoes, text="Editar", font=("Arial", 10), command=editar,
                           bg="white", )
    btn_editar.grid(row=0, column=1, sticky="ew", padx=5)

    btn_excluir = tk.Button(frame_botoes, text="Excluir", font=("Arial", 10), command=excluir,
                            bg="white",)
    btn_excluir.grid(row=0, column=2, sticky="ew", padx=5)

    janela.mainloop()

criartelaperfil()
