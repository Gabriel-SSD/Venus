# Venus

Pipeline de dados do [TMDB](https://developer.themoviedb.org/reference/getting-started). O código fica em `src/venus/`: `ingest.py` busca a API, `transform.py` trata o resultado, `utils/` é o que os dois compartilham. A saída local vai para `data/`, que não entra no Git.

Python 3.12. O padrão de commit está em [docs/commits.md](docs/commits.md). A branch de trabalho está em [docs/branches.md](docs/branches.md).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
```

Preencha `TMDB_READ_ACCESS_TOKEN` no `.env`. O token é o API Read Access Token da conta no TMDB e entra no header `Authorization: Bearer ...`.

Dependência nova vai em `dependencies` no `pyproject.toml`. Com o ambiente ativo, rode `pip install -e .` de novo.

## Rodar

Com o ambiente ativo:

```bash
python -m venus.ingest
python -m venus.transform
```

Os dois scripts ainda não executam a coleta nem a transformação.
