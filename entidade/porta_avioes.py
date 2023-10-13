from entidade.embarcacao import Embarcacao


class PortaAviao(Embarcacao):
    def __init__(self):
        super().__init__(4, 1)