
# Gerenciar dados de Cliente


-  clone o projeto ``` https://github.com/eltonjncorreia/gerenciar-dados-virtus.git virtus ```
-  entre no diretorio ``` cd virtus ```
-  crie um ambiente virtual da maneira que preferir ``` python -m venv .venv ```
-
-  Instale as dependencias.
-  Estou usando o Pipenv, então use ``` pipenv install Pipfile```
-  depois ative a virtual env ``` pipenv shell``
-  ou  se estiver usando pip, ative o virtual env ``` source .venv/bin/activate ```
-  depois ``` pip install -r requirements.txt ```

-  Configure a instância com o .env  ``` cp contrib/env-sample .env ```
-  rode os testes ``` python manage.py test ```

### Obs:
##### para criar Cliente, Endereços, Pedidos e Itens o usuario tem que estar logado.

-  Crie as migrações com o camando ``` python manage.py migrate ```
-  crie um usuario com o comando ```python manage.py createsuperuser```
-  execute a aplicação ```python manage.py runserver```
-  realize login no menu superior direito.

##### Os endpoints da API são:

-  ``` /v1/pedidos/ ``` Listar todos os pedidos ```http://localhost:8000/v1/pedidos/```
-  ``` /v1/pedidos/2 ``` Recuperar um pedido ```http://localhost:8000/v1/pedidos/2```

-  ``` /v1/itens/ ``` Listar todos os itens ```http://localhost:8000/v1/itens/```
-  ``` /v1/itens/2 ``` Recuperar um item ```http://localhost:8000/v1/itens/2```


### Endereço da aplicação

```http://localhost:8000```


### Requerimentos para rodar o projeto

- Python 3.6 +
- Django 2.0 +
