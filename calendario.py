#Instale primeiro pip install tkcalender


import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from tkcalendar import Calendar  # Requer: pip install tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda com Calendário - Tarefas e Avisos (com Editar/Excluir)")
        self.root.geometry("650x550")
        self.root.configure(bg="#D3D3D3")  # Cinza claro como fundo principal
        
        # Dicionário para armazenar tarefas: {data_str: [lista de tarefas]}
        self.tarefas = {}
        self.data_selecionada = None  # Data atual selecionada no calendário
        self.editando_index = None  # Índice da tarefa sendo editada (None se não editando)
        
        self.criar_interface()
    
    def criar_interface(self):
        # Título
        titulo = tk.Label(self.root, text="Agenda com Calendário", font=("Arial", 16, "bold"),
                          fg="#34495e", bg="#D3D3D3")
        titulo.pack(pady=10)
        
        # Frame para calendário
        frame_calendario = tk.Frame(self.root, bg="#D3D3D3")
        frame_calendario.pack(pady=10, padx=20, fill="x")
        
        tk.Label(frame_calendario, text="Selecione uma data:", fg="#34495e", bg="#D3D3D3", 
                 font=("Arial", 12, "bold")).pack(anchor="w")
        
        # Calendário (fundo branco, bordas #34495e)
        self.cal = Calendar(frame_calendario, selectmode="day", date_pattern="dd/mm/yyyy",
                            background="white", foreground="#34495e", headersbackground="#34495e",
                            headersforeground="white", normalbackground="white", normalforeground="#34495e",
                            weekendbackground="white", weekendforeground="#34495e",
                            selectbackground="#34495e", selectforeground="white",
                            font=("Arial", 10))
        self.cal.pack(pady=5)
        
        # Evento para quando uma data é selecionada
        self.cal.bind("<<CalendarSelected>>", self.on_data_selecionada)
        
        # Frame para entradas (fundo branco)
        frame_entrada = tk.Frame(self.root, bg="white", relief="solid", bd=1)
        frame_entrada.pack(pady=10, padx=20, fill="x")
        
        # Entrada para hora (opcional, formato: HH:MM)
        tk.Label(frame_entrada, text="Hora (HH:MM, opcional):", fg="#34495e", bg="white").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_hora = tk.Entry(frame_entrada, bg="white", fg="#34495e", relief="solid", bd=1)
        self.entry_hora.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Entrada para descrição (tarefa ou aviso)
        tk.Label(frame_entrada, text="Descrição (tarefa ou aviso):", fg="#34495e", bg="white").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_desc = tk.Entry(frame_entrada, bg="white", fg="#34495e", relief="solid", bd=1)
        self.entry_desc.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        frame_entrada.columnconfigure(1, weight=1)
        
        # Frame para botões (para organizar melhor)
        frame_botoes = tk.Frame(frame_entrada, bg="white")
        frame_botoes.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Botão adicionar/atualizar (dinâmico)
        self.btn_adicionar = tk.Button(frame_botoes, text="Adicionar Tarefa/Aviso", command=self.adicionar_ou_atualizar_tarefa,
                                       bg="white", fg="#34495e", relief="raised", bd=2, font=("Arial", 10, "bold"))
        self.btn_adicionar.pack(side="left", padx=5)
        
        # Botão editar
        self.btn_editar = tk.Button(frame_botoes, text="Editar Tarefa", command=self.editar_tarefa_selecionada,
                                    bg="white", fg="#34495e", relief="raised", bd=2, font=("Arial", 10))
        self.btn_editar.pack(side="left", padx=5)
        
        # Botão excluir
        self.btn_excluir = tk.Button(frame_botoes, text="Excluir Tarefa", command=self.excluir_tarefa_selecionada,
                                     bg="white", fg="#34495e", relief="raised", bd=2, font=("Arial", 10))
        self.btn_excluir.pack(side="left", padx=5)
        
        # Botão limpar todas
        self.btn_limpar = tk.Button(frame_botoes, text="Limpar Todas as Tarefas", command=self.limpar_todas_tarefas,
                                    bg="white", fg="#34495e", relief="raised", bd=2, font=("Arial", 10))
        self.btn_limpar.pack(side="left", padx=5)
        
        # Frame para lista de tarefas (fundo cinza claro)
        frame_lista = tk.Frame(self.root, bg="#D3D3D3")
        frame_lista.pack(pady=10, padx=20, fill="both", expand=True)
        
        tk.Label(frame_lista, text="Tarefas/Avisos da Data Selecionada:", fg="#34495e", bg="#D3D3D3", 
                 font=("Arial", 12, "bold")).pack(anchor="w")
        
        # Listbox com scrollbar
        self.listbox = tk.Listbox(frame_lista, bg="#D3D3D3", fg="#34495e", font=("Arial", 10),
                                  relief="solid", bd=1, selectbackground="#34495e", selectforeground="white")
        scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def on_data_selecionada(self, event):
        self.data_selecionada = self.cal.get_date()  # Formato: 'dd/mm/yyyy'
        self.editando_index = None  # Limpa modo de edição ao mudar data
        self.atualizar_interface_normal()  # Volta botões ao normal
        self.atualizar_lista()
        messagebox.showinfo("Data Selecionada", f"Data: {self.data_selecionada}\nAgora adicione ou gerencie tarefas/avisos!")
    
    def adicionar_ou_atualizar_tarefa(self):
        if not self.data_selecionada:
            messagebox.showwarning("Aviso", "Selecione uma data no calendário primeiro!")
            return
        
        hora = self.entry_hora.get().strip()
        desc = self.entry_desc.get().strip()
        
        if not desc:
            messagebox.showwarning("Aviso", "Preencha a descrição da tarefa ou aviso!")
            return
        
        # Validação de hora se fornecida
        if hora:
            try:
                datetime.strptime(hora, "%H:%M")
            except ValueError:
                messagebox.showerror("Erro", "Formato de hora inválido! Use HH:MM (ex: 14:30).")
                return
        
        # Formatar tarefa
        if hora:
            tarefa = f"{hora}: {desc}"
        else:
            tarefa = desc
        
        if self.editando_index is not None:
            # Modo edição: atualiza a tarefa no índice
            if self.data_selecionada in self.tarefas and 0 <= self.editando_index < len(self.tarefas[self.data_selecionada]):
                self.tarefas[self.data_selecionada][self.editando_index] = tarefa
                messagebox.showinfo("Sucesso", "Tarefa/Aviso atualizado!")
            else:
                messagebox.showerror("Erro", "Erro ao atualizar tarefa.")
        else:
            # Modo adicionar: adiciona nova tarefa
            if self.data_selecionada not in self.tarefas:
                self.tarefas[self.data_selecionada] = []
            self.tarefas[self.data_selecionada].append(tarefa)
            messagebox.showinfo("Sucesso", "Tarefa/Aviso adicionado à data selecionada!")
        
        # Atualizar lista e limpar entradas/modo edição
        self.atualizar_lista()
        self.limpar_entradas()
        self.atualizar_interface_normal()
    
    def editar_tarefa_selecionada(self):
        if not self.data_selecionada:
            messagebox.showwarning("Aviso", "Selecione uma data primeiro!")
            return
        
        selecao = self.listbox.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione uma tarefa na lista para editar!")
            return
        
        index = selecao[0]
        if self.data_selecionada not in self.tarefas or index >= len(self.tarefas[self.data_selecionada]):
            messagebox.showerror("Erro", "Tarefa inválida.")
            return
        
        tarefa = self.tarefas[self.data_selecionada][index]
        
        # Separar hora e desc se houver hora
        if ": " in tarefa and len(tarefa.split(": ", 1)[0].split(":")) == 2:
            hora, desc = tarefa.split(": ", 1)
            self.entry_hora.delete(0, tk.END)
            self.entry_hora.insert(0, hora)
            self.entry_desc.delete(0, tk.END)
            self.entry_desc.insert(0, desc)
        else:
            self.entry_hora.delete(0, tk.END)
            self.entry_desc.delete(0, tk.END)
            self.entry_desc.insert(0, tarefa)
        
        self.editando_index = index
        self.btn_adicionar.config(text="Atualizar Tarefa/Aviso")
        messagebox.showinfo("Modo Edição", "Edite os campos e clique em 'Atualizar Tarefa/Aviso'.")
    
    def excluir_tarefa_selecionada(self):
        if not self.data_selecionada:
            messagebox.showwarning("Aviso", "Selecione uma data primeiro!")
            return
        
        selecao = self.listbox.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione uma tarefa na lista para excluir!")
            return
        
        index = selecao[0]
        if self.data_selecionada not in self.tarefas or index >= len(self.tarefas[self.data_selecionada]):
            messagebox.showerror("Erro", "Tarefa inválida.")
            return
        
        tarefa = self.tarefas[self.data_selecionada][index]
        if messagebox.askyesno("Confirmar Exclusão", f"Excluir a tarefa '{tarefa}'?"):
            del self.tarefas[self.data_selecionada][index]
            if not self.tarefas[self.data_selecionada]:  # Se lista vazia, remove a chave
                del self.tarefas[self.data_selecionada]
            self.atualizar_lista()
            self.limpar_entradas()
            messagebox.showinfo("Sucesso", "Tarefa/Aviso excluído!")
    
    def limpar_todas_tarefas(self):
        if self.data_selecionada and self.data_selecionada in self.tarefas:
            if messagebox.askyesno("Confirmar Limpeza", "Limpar todas as tarefas desta data?"):
                del self.tarefas[self.data_selecionada]
                self.editando_index = None
                self.atualizar_interface_normal()
                self.atualizar_lista()
                messagebox.showinfo("Limpo", "Todas as tarefas/avisos da data selecionada foram removidos!")
        else:
            messagebox.showinfo("Info", "Nenhuma tarefa para limpar.")
    
    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        if self.data_selecionada and self.data_selecionada in self.tarefas:
            for tarefa in self.tarefas[self.data_selecionada]:
                self.listbox.insert(tk.END, tarefa)
        else:
            self.listbox.insert(tk.END, "Nenhuma tarefa/aviso para esta data.")
    
    def limpar_entradas(self):
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)
    
    def atualizar_interface_normal(self):
        self.editando_index = None
        self.btn_adicionar.config(text="Adicionar Tarefa/Aviso")
        self.limpar_entradas()
    
    def on_closing(self):
        if messagebox.askokcancel("Sair", "Deseja sair da agenda?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
