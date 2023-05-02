from pydantic import BaseModel
from typing import Optional, List


class Produto(BaseModel):
    id: Optional[str] = None
    # usuario: Usuario
    nome: str
    detalhes: str
    preco: str
    disponivel: bool = False

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[str] = None
    # usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List[Produto]
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]
    