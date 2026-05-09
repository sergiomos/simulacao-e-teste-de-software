from .task import Status


class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def criar_tarefa(self, task):
        task.validar()
        return self.repository.save(task)

    def listar_todas(self):
        return self.repository.find_all()

    def atualizar_status(self, id, status):
        task = self.repository.find_by_id(id)
        if task is None:
            raise ValueError(f"task {id} nao encontrada")
        if not isinstance(status, Status):
            raise ValueError("status invalido")
        task.status = status
        return task
