from base.modelo import Modelo

class Cliente(Modelo):
    Tabela = "cliente"

    def __init__(self, id=None):
        super().__init__(self.Tabela);
        self.id = id;
        if id:
            dado = self.obter_por_id(id)

            if dado:
                
                self.cpf = dado["cpf"];
                self.nome = dado["nome"];
                self.cidade = dado["cidade"];
                self.telefone = dado["telefone"];
                self.profissao = dado["profissao"];

            else:

                self.id = None;
                self.cpf = None;
                self.nome = None;
                self.cidade = None;
                self.telefone = None;
                self.profissao = None;

        else:

            self.cpf = None;
            self.nome = None;
            self.cidade = None;
            self.telefone = None;
            self.profissao = None;

    def excluir(self):

        if self.id:

            self.excluir_por_id(self.id)

            return True
        else:
            print(f"Impossibilidade na exclusão. {self.id}")
            return False
    
    def salvar(self):

        try:
            if self.id:

                instrucao = "UPDATE {tabela} SET nome=%s,cpf=%s,cidade=%s,telefone=%s,profissao=%s WHERE id=%s".format(tabela =self.Tabela)
                self.obter_cursor().execute(instrucao, [self.nome,self.cpf,self.cidade,self.telefone,self.profissao,self.id])

            else:
                instrucao = "INSERT INTO {tabela} (nome,cpf,cidade,telefone,profissao) VALUES (%s, %s, %s,%s,%s)".format(tabela =self.Tabela)
                self.obter_cursor().execute(instrucao, [self.nome,self.cpf,self.cidade,self.telefone,self.profissao])
                self.id = self.obter_cursor().lastrowid

            return True

        except:
            print("Houve um erro ao executar!", self.obter_cursor()._last_executed)
            return False

    

    def obter_dados(self, id):

        try:

            instrucao = "SELECT * FROM {tabela} WHERE id=%s".format(tabela = self.Tabela)
            self.obter_cursor().execute(instrucao, id)
            resultado = self.obter_cursor().fetchone()

            return resultado
        except:
            print("Houve um erro ao executar!.", self.__cursor._last_executed)
            
            return None
