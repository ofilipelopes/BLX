from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.config.database import get_db, criar_bd
from infra.sqlalchemy.repositorios.produto import RepositorioProduto


criar_bd()


app = FastAPI()


@app.post('/produtos')
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos():
    return {'msg': 'Listagem de produtos'}
