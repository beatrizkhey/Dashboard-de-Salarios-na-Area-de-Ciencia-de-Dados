# 📊 Dashboard de Salários na Área de Dados

Este projeto é um **dashboard interativo** construído com [Streamlit](https://streamlit.io/), [Pandas](https://pandas.pydata.org/) e [Plotly](https://plotly.com/python/).  
O objetivo é explorar e visualizar dados salariais da área de dados nos últimos anos.

---

## 🚀 Funcionalidades
- Filtros interativos por **Ano**, **Senioridade**, **Contrato** e **Tamanho da Empresa**.
- KPIs principais (salário médio, máximo, registros totais e cargo mais frequente).
- Gráficos interativos com Plotly (barras, histogramas e pizza).
- Mapa mundial mostrando o salário médio de Cientistas de Dados por país (choropleth).
- Interface amigável e responsiva com Streamlit.

---

## 📦 Pré-requisitos
Certifique-se de ter instalado:
- [Python 3.9+](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/installation/)  

---

## ⚙️ Instalação e execução

1. Clone este repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/seu-usuario/dashboard-salarios.git
   cd dashboard-salarios
   ```

2. Crie um ambiente virtual (venv):
   ```bash 
   python -m venv venv
   ```

3. Ative a venv:
   Windows (PowerShell):
      ```bash 
      venv\Scripts\Activate   
      ```

   Linux/macOS:
   ```bash 
   source venv/bin/activate
   ```

4. Instale as dependências:
   ```bash 
   pip install -r requirements.txt
   ```

5. Execute o dashboard com Streamlit:
   ```bash 
   streamlit run app.py
   ```

6. Abra o navegador no endereço indicado (geralmente):

   http://localhost:8501   

---

📦 Dependências
- pandas
- streamlit
- plotly
- seaborn

👩‍💻 Autor

Desenvolvido por Beatriz Khey ✨