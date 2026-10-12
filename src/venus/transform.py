"""Transformação do bruto em dado curado.

Entra: os arquivos gravados por ``venus.ingest`` em ``data/raw``.

Sai: dados limpos e modelados em ``data/curated``.

Não pertence a este script: chamada à API do TMDB e autenticação.
O que for compartilhado com a ingestão mora em ``venus.utils``.
"""


def main() -> None:
    """Lê ``data/raw``, limpa e modela, e grava em ``data/curated``."""
    raise NotImplementedError("A transformação ainda não está implementada.")


if __name__ == "__main__":
    main()
