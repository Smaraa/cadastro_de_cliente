from modelos.prof import Profissao

class ControladorProf ():

    def cadastrar_prof(self, nome_da_profissao):

        if nome_da_profissao is None:
            print ("Preencha com o nome da profissão! ")
            return False

    novo_prof = Profissao()
        novo_prof.nome_da_profissao = nome_da_profissao
        novo_prof.salvar()
        pass

    def excluir_prof(self, id):

        excluir_prof = Profissao(id)
        excluir_prof.excluir()
        pass

    def atualizar_alterar_prof(self, id, nome_da_profissao)

        atualizar_alterar_prof = Profissao(id)
        atualizar_alterar_prof.nome_da_profissao = nome_da_profissao
        atualizar_alterar_prof.salvar()
        pass
