from pydantic import BaseModel

class TareaCrear(BaseModel):
    titulo: str
    descripcion: str | None = None

class TareaLeer(BaseModel):
    id: int
    titulo: str
    completada: bool
    descripcion: str | None