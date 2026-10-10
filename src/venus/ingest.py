"""Ingestão dos dados públicos do TMDB.

Entra: credenciais da API (variáveis de ambiente) e os parâmetros da
coleta.

Sai: a resposta da API gravada como veio, em ``data/raw``, sem limpeza
nem renomeação de campos.

Não pertence a este script: modelagem, validação de negócio e qualquer
leitura de ``data/curated``. O que for compartilhado com a transformação
mora em ``venus.utils``.
"""


def main() -> None:
    """Busca os dados na API e grava o bruto em ``data/raw``."""
    raise NotImplementedError("A ingestão ainda não está implementada.")


if __name__ == "__main__":
    main()
