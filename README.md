# Modelação Preditiva na Primeira Liga: XGBoost em 2 e 3 classes ⚽📊

Repositório com o código-fonte e *pipeline* de processamento para previsão de resultados da Primeira Liga Portuguesa utilizando XGBoost.

> **Nota:** Para a leitura da metodologia, estudo de ablação e discussão detalhada dos resultados estatísticos, consulta o relatório completo disponível na pasta `documents/`.

---

## 🛠️ Estrutura do Repositório

O projeto está organizado na seguinte estrutura de diretórios e ficheiros:

```text
📦 PrimeiraLiga-Predictor
 ┣ 📂 data
 ┃ ┣ 📂 processed       # Datasets após Feature Engineering
 ┃ ┗ 📂 raw             # Datasets históricos originais em formato CSV
 ┣ 📂 documents         # Documentação do projeto e relatórios
 ┣ 📂 figures
 ┃ ┣ 📂 2classes        # Gráficos do modelo binário (Matrizes, Calibração, etc.)
 ┃ ┗ 📂 3classes        # Gráficos do modelo multiclasse
 ┣ 📂 notebooks         # Jupyter Notebooks com as experiências, EDA e treino do modelo
 ┣ 📂 scripts           # Módulos Python e funções auxiliares consumidas pelo main.py
 ┣ 📜 .env.example      # Template de configuração das variáveis de ambiente (API Key)
 ┣ 📜 .gitignore        # Ficheiros e diretórios ignorados pelo Git
 ┣ 📜 main.py           # Script principal de execução da pipeline
 ┣ 📜 last_matchday.txt # Ficheiro com as probabilidades extraídas da última jornada de 25/26
 ┣ 📜 README.md         # Documentação do repositório
 ┗ 📜 requirements.txt  # Dependências e bibliotecas Python necessárias
```

## ⚙️ Configuração e Instalação

### 1. Clonar o repositório e instalar dependências
Certifica-te de que tens o Python 3.x instalado. No terminal, clona o projeto e instala as bibliotecas necessárias:

```bash
git clone ...
cd ...
pip install -r requirements.txt
```

### 2. Configurar a API Key
Para automatizar a extração das próximas jornadas, o projeto consome a API oficial do [football-data.org](https://www.football-data.org/).

1. Cria uma conta na plataforma para obteres uma chave de acesso gratuita.
2. Na raiz do projeto, configura o teu ficheiro de ambiente. Podes fazê-lo de duas formas:
   * **Interface Gráfica (VS Code / Windows):** Renomeia diretamente o ficheiro `.env.example` para `.env`.
   * **Terminal:** Copia o template executando o comando `cp .env.example .env`.
3. Abre o ficheiro `.env` e insere a tua chave:
   ```env
   FOOTBALL_API_KEY=inserir_aqui_o_token_da_api
   ```

---

## 🏃 Como Executar

### Pipeline Principal
O ponto de entrada de todo o projeto é o ficheiro `main.py`. Este script orquestra as funções de extração (via API), processamento de dados e geração de previsões.

> 💡 **Dica de Execução:** O momento ideal para correr este script é **um dia antes do início de uma nova jornada**. Isto garante que o histórico de resultados da semana anterior está totalmente fechado, permitindo que as métricas de forma das equipas (*rolling windows* e diferenciais de golos) sejam calculadas com a máxima precisão antes de gerar as novas previsões.

Para correr a *pipeline* completa:
```bash
python main.py
```

### Exploração Interativa
Se pretendes analisar o código passo a passo, treinar os modelos individualmente, ou regenerar os gráficos da pasta `figures/`, deves utilizar os ficheiros na pasta `notebooks/`.

Inicia o ambiente Jupyter:
```bash
jupyter notebook
```
De seguida, navega até à pasta `notebooks/` e abre o ficheiro interativo desejado.

---

## 🔄 Manutenção: Transição para Novas Épocas

O projeto está configurado para a época **2025/2026**. Se desejares atualizar o modelo para a época seguinte (ex: 2026/2027), terás de atualizar duas variáveis no script `scripts/update_data.py`:

1. **URL da API:** Altera o ano no URL do *football-data*.
   De: `https://www.football-data.co.uk/mmz4281/2526/P1.csv`
   Para: `https://www.football-data.co.uk/mmz4281/2627/P1.csv`
2. **Caminho Local:** Atualiza o nome do ficheiro para a nova época.
   De: `file_path = Path("data/raw/LigaPortugal25-26.csv")`
   Para: `file_path = Path("data/raw/LigaPortugal26-27.csv")`

Ao executar o script, ele detetará automaticamente que se trata de uma nova época e criará o novo ficheiro base de forma autónoma.