import tkinter as tk
from tkinter import scrolledtext, messagebox

def criar_janela_principal():
    # Cria a janela principal
    root = tk.Tk()
    root.title("Configurações")
    root.geometry("600x400") 
    root.config(bg="#34495e")

    # Label de boas-vindas
    label = tk.Label(root, text="Configurações",  font=("Arial", 16, "bold"), fg="white", bg="#34495e")
    label.pack(pady=20)
   
    # Botão para mostrar termos de uso
    botao_termos = tk.Button(root, text="TERMOS DE USO", command=mostrar_termos_uso,
                             font=("Arial", 12), bg="#34495e",fg="white", width=25)
    botao_termos.pack(pady=10)
   
    botao_termos = tk.Button(root, text="TERMOS DE PRIVACIDADE", command=mostrar_termos_privacidade,
                             font=("Arial", 12), bg="#34495e",fg="white", width=25)
    botao_termos.pack(pady=10)

    botao_termos = tk.Button(root, text="OUVIDORIA", command=mostrar_ouvidoria,
                             font=("Arial", 12), bg="#34495e",fg="white", width=25)
    botao_termos.pack(pady=10)


    # Inicia o loop da interface
    root.mainloop()

# Função que é chamada ao clicar no botão
def mostrar_termos_uso():
    # Texto dos termos de uso (edite aqui com o conteúdo real do seu app)
    termos_texto = """
    TERMOS DE USO DO SISTEMA


    1. Introdução
    Ao usar este aplicativo, você concorda com estes termos. Leia atentamente.


    2. Uso Permitido
    Você pode usar o app para fins educacionais, mas não para atividades ilegais ou que possa compremeter com a imagem da escola.


    3. Privacidade
    Coletamos dados apenas para melhorar o serviço. Veja nossa política de privacidade.


    4. Responsabilidades
    O desenvolvedor não se responsabiliza por danos causados pelo uso indevido ou ações que o usuário compremeteu ao fazer ações ilicitas.


    5. Alterações
    Estes termos podem ser atualizados a qualquer momento.


    """
   
    # Cria uma nova janela (popup) para os termos
    janela_termos = tk.Toplevel()  # Janela filha da principal
    janela_termos.title("Termos de Uso")
    janela_termos.geometry("600x400")
    janela_termos.config(bg="#34495e")  # Cor de fundo da janela corrigida
   
    # Label no topo
    label_titulo = tk.Label(janela_termos, text="Termos de Uso", font=("Arial", 16, "bold"), fg="white", bg="#34495e")
    label_titulo.pack(pady=10)
   
    texto_area = scrolledtext.ScrolledText(janela_termos, wrap=tk.WORD, width=60, height=20,
                                           font=("Arial", 10), fg="black", bg="lightgray")  # Área de texto rolável para exibir os termos
    texto_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
    texto_area.insert(tk.END, termos_texto)  # Insere o texto
    texto_area.config(state=tk.DISABLED)  # Torna o texto só-leitura
   
    # Centraliza a janela na tela (opcional)
    janela_termos.transient(tk._default_root if tk._default_root else None)
    janela_termos.grab_set()  # Modal: bloqueia interação com a janela principal até fechar

def mostrar_ouvidoria():
    # Texto da ouvidoria (edite aqui com o conteúdo real do seu app)
    termos_texto = """
   OUVIDORIA DO SISTEMA 

   NÚMERO DA OUVIDORIA 61 9999-9999

   EMAIL DA OUVIDORIA educamaisescola@edu.com.br

   Após o contato com a ouvidoria ou número, o usuário pode receber uma atualização imediata ou receberá uma resposta em ATÉ 3 dias úteis.


    """

    # Cria uma nova janela (popup) para os termos
    janela_termos = tk.Toplevel()  # Janela filha da principal
    janela_termos.title("OUVIDORIA")
    janela_termos.geometry("600x400")  # Tamanho maior para texto
    janela_termos.config(bg="#34495e")  # Adicionado cor de fundo para consistência
   
    # Label no topo
    label_titulo = tk.Label(janela_termos, text="OUVIDORIA", font=("Arial", 16, "bold"), fg="white", bg="#34495e")
    label_titulo.pack(pady=10)
   
    texto_area = scrolledtext.ScrolledText(janela_termos, wrap=tk.WORD, width=60, height=20,
                                           font=("Arial", 10), fg="black", bg="lightgray")   # Área de texto rolável para exibir os termos
    texto_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
    texto_area.insert(tk.END, termos_texto)  # Insere o texto
    texto_area.config(state=tk.DISABLED)  # Torna o texto só-leitura
   
    # Centraliza a janela na tela (opcional)
    janela_termos.transient(tk._default_root if tk._default_root else None)
    janela_termos.grab_set()  # Modal: bloqueia interação com a janela principal até fechar

def mostrar_termos_privacidade():
    # Texto dO termos de privacidade (edite aqui com o conteúdo real do seu app)
    termos_texto = """
    1. Coleta de Dados Pessoais:

    Coletamos informações pessoais, como nome, e-mail e dados acadêmicos, apenas para fins específicos relacionados ao uso do aplicativo escolar. Esses dados não serão compartilhados com terceiros sem o consentimento expresso dos usuários.

    2. Uso de Cookies:

    Utilizamos cookies e tecnologias semelhantes para melhorar a experiência do usuário, personalizar conteúdo e analisar o tráfego do aplicativo. Os usuários podem ajustar as configurações de cookies em seu dispositivo a qualquer momento.

    3. Segurança dos Dados:

    Implementamos medidas de segurança para proteger os dados pessoais dos usuários contra acessos não autorizados, perda ou alteração. No entanto, não podemos garantir a segurança absoluta dos dados transmitidos via internet.

    4. Compartilhamento de Informações:

    Não compartilhamos informações pessoais com terceiros, exceto quando exigido por lei ou com o consentimento explícito dos usuários. O compartilhamento de dados é restrito ao uso interno e à melhoria contínua do aplicativo.

    5. Direitos dos Usuários:

    Os usuários têm o direito de acessar, corrigir ou excluir seus dados pessoais a qualquer momento, entrando em contato conosco através da seção de configurações do aplicativo. Caso o usuário deseje, pode solicitar a exclusão de sua conta.
    """

    # Cria uma nova janela (popup) para os termos
    janela_termos = tk.Toplevel()  # Janela filha da principal
    janela_termos.title("TERMOS DE PRIVACIDADE")
    janela_termos.geometry("600x400")  # Tamanho maior para texto
    janela_termos.config(bg="#34495e")  # Adicionado cor de fundo para consistência
   
    # Label no topo
    label_titulo = tk.Label(janela_termos, text="TERMOS DE PRIVACIDADE", font=("Arial", 16, "bold"), fg="white", bg="#34495e")
    label_titulo.pack(pady=10)
   
    texto_area = scrolledtext.ScrolledText(janela_termos, wrap=tk.WORD, width=60, height=20,
                                           font=("Arial", 10), fg="black", bg="lightgray")   # Área de texto rolável para exibir os termos
    texto_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
    texto_area.insert(tk.END, termos_texto)  # Insere o texto
    texto_area.config(state=tk.DISABLED)  # Torna o texto só-leitura
   
    # Centraliza a janela na tela (opcional)
    janela_termos.transient(tk._default_root if tk._default_root else None)
    janela_termos.grab_set()  # Modal: bloqueia interação com a janela principal até fechar

# Executa o programa
if __name__ == "__main__":
    criar_janela_principal()
