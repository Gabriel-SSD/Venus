# Venus 🟠
![Badge Status](https://img.shields.io/badge/Status-Refinement-blue)

Projeto desenvolvido para praticar aprendizados do curso **Data Lake - Design, Projeto e Integração** da Data Science Academy.

## Descrição do Projeto:
### Contexto
Você foi contratado como Engenheiro de Dados na Solar System Airlines, uma companhia aérea centrada em dados. Sua responsabilidade é criar um Data Lake eficiente e seguro para armazenar os ativos de dados da empresa. Além disso, você será encarregado de fornecer dados confiáveis e bem organizados para equipes de Business Intelligence (BI) e Machine Learning (ML), impulsionando a tomada de decisões informadas.
### Projeto Venus
Venus é um projeto de design, implementação e integração de um Data Lake. Este projeto abrangente envolve a extração de dados de múltiplos tipos (não-estruturados, semi-estruturados e estruturados) e de diversas origens. A coleta de dados será realizada tanto em lotes (batch) quanto em tempo real (streaming). Uma vez coletados, os dados serão depositados no Data Lake, onde passarão por processos de organização e rotulação, visando facilitar a recuperação e uso futuro.

Após essa etapa, os usuários terão a capacidade de consumir os dados do Data Lake, aplicando as transformações necessárias para suas análises e tarefas específicas. Esses dados serão fundamentais para múltiplos propósitos, incluindo visualização direta, alimentação de um Data Warehouse e, especialmente, para o treinamento de modelos de Machine Learning.

A principal fonte de dados para esse projeto são diversos endpoints de uma API, que serão extraídos por meio do uso do Apache Airflow, uma ferramenta robusta e flexível de automação de fluxos de trabalho. O Projeto Venus visa estabelecer uma base sólida para a utilização inteligente dos dados da Solar System Airlines, capacitando as equipes de toda a organização a tomar decisões mais informadas e estratégicas.
## Tecnologias e Ferramentas utilizadas:

- Storage: [HDFS](https://hadoop.apache.org/)
- Compute: [Spark](https://spark.apache.org/)
- Data Management: [Atlas](https://atlas.apache.org/)
- Analytics: [Metabase](https://www.metabase.com/)
- ELT: [Apache Airflow](https://airflow.apache.org/)
- Database (DW): [PostgreSQL](https://www.postgresql.org/)
- Infra: [Docker](https://www.docker.com/)

## Esquema
![venus_schema](https://github.com/Gabriel-SSD/Venus/assets/110556455/96ff67bd-ae29-4302-8ef3-4e6667428acb)

