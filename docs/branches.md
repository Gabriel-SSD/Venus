# Branches

Cada contribuição sai de uma branch nova, criada a partir da `main` atualizada. A `main` não recebe commit direto.

```bash
git checkout main
git pull
git checkout -b feat/ingest-filmes
```

O nome segue `tipo/descricao-curta`. O tipo é o mesmo do commit (`feat`, `fix`, `docs`, `refactor`, `test`, `chore`). A descrição é curta, em minúsculas, com hífen.

```
feat/ingest-filmes
fix/transform-data
docs/guia-de-branch
```

Uma branch, uma mudança. O commit segue [docs/commits.md](commits.md).

Para publicar a branch e abrir o pull request:

```bash
git push -u origin HEAD
```
