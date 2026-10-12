# Commits

Cada commit descreve uma única mudança lógica, no formato do
[Conventional Commits](https://www.conventionalcommits.org/):

```
tipo(escopo): descrição
```

A descrição fica no infinitivo, em minúsculas, sem ponto final, e a
linha inteira cabe em cerca de 72 caracteres.

```
feat(ingest): buscar filmes públicos da API
```

O escopo é opcional quando a mudança não cabe num script:

```
chore: atualizar dependências
```

## Tipos

| Tipo | Quando usar |
| --- | --- |
| `feat` | Funcionalidade nova |
| `fix` | Correção de bug |
| `docs` | Só documentação |
| `style` | Formatação, sem mudança de comportamento |
| `refactor` | Reorganização interna, sem feature nem bugfix |
| `test` | Testes |
| `chore` | Manutenção que não entra nos tipos acima |
| `ci` | Pipeline de integração contínua |
| `build` | Dependências e empacotamento |
| `perf` | Melhoria de desempenho |

## Escopos

Use o nome do script ou da área tocada:

- `ingest`
- `transform`
- `utils`
- `docs`

## Corpo e rodapé

Separe o corpo do título com uma linha em branco. O corpo explica o
porquê, não a lista do que o diff já mostra.

Uma mudança incompatível leva `!` depois do tipo ou do escopo, e um
rodapé `BREAKING CHANGE:`:

```
feat(transform)!: trocar o formato dos arquivos curados

Os consumidores de data/curated passam a ler Parquet.

BREAKING CHANGE: os arquivos em data/curated deixam de ser JSON.
```

## Uma mudança por commit

Um commit faz uma coisa. Se a ingestão e a transformação mudam por
motivos diferentes, são dois commits.

Válidos:

```
feat(ingest): buscar filmes públicos da API
fix(transform): tratar campo de data ausente
docs: descrever o padrão de commit
refactor(utils): reunir a leitura do ambiente
```

Inválidos:

```
Added ingest client.
feat: Adiciona o cliente.
feat(ingest): adicionar o cliente e corrigir a transformação.
update stuff
```
