from datetime import datetime
from enum import Enum, IntEnum


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


class Task:
    def __init__(self, id, titulo, descricao, prioridade, prazo, status=Status.PENDENTE):
        if not isinstance(status, Status):
            raise ValueError("status deve ser um valor de Status")
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self._status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo):
        if not isinstance(novo, Status):
            raise ValueError("status deve ser um valor de Status")
        self._status = novo

    def validar(self):
        if not isinstance(self.titulo, str) or len(self.titulo) < 3:
            raise ValueError("titulo deve ter ao menos 3 caracteres")
        if not isinstance(self.prazo, datetime):
            raise ValueError("prazo deve ser datetime")
        if self.prazo < datetime.now():
            raise ValueError("prazo nao pode estar no passado")
