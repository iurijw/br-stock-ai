> ⚠️ Please note that this code is for study purposes only and will not be maintained.

> 💸 Please note that OpenAI services is not free.


# Brazilian Stock AI (br-stock-ai)
A script that captures financial data of Brazilian stocks from the "StatusInvest" website, including Balance Sheet, Cash Flow and Income Statement, and uses OpenAI's artificial intelligence to generate reports of them.

## Prerequisites
- Python 3.6 or higher, [here](https://www.python.org/downloads/)
- OpenAI API key, [here](https://openai.com/)
- Git 2.40.1 (optional), [here](https://git-scm.com/downloads)

## Windows Tutorial
- Press the Windows key + R to open the Run dialog box.
- Type `cmd` and press Enter.
- Clone the repository by typing `git clone https://github.com/iurijw/br-stock-ai` or download the ZIP file and extract its contents.
- Navigate to the project directory by typing `cd br-stock-ai`.
- Install the required packages by running `pip install -r requirements.txt`.

## Usage of CLI included
> 🧠 This CLI tutorial is just a demonstration of how to use the code. It can be used in many ways, as it extracts the information and returns a dictionary of the data.

The script can be executed from the command line using the following command:

- `python main.py [ticker] [api_key] [--no-txt] [--output OUTPUT]`

  ***[ticker]*** is the stock ticker symbol you want to analyze.

  ***[api_key]*** is your OpenAI API key.

  ***--no-txt*** is an optional argument. If provided, the script will not write results to an output file.

  ***--output OUTPUT*** is also an optional argument. If provided, it will write the results to a file with the specified name. If not provided, the results will be printed to the console.

### Example
Let's say we want to analyze the stock information for CPLE3 (Companhia Paranaense de Energia) using the OpenAI API. We can execute the following command:

    python main.py CPLE3 [open ai api key] --output results.txt
    
This will save the analysis to a file named results.txt. If the file already exists, the results will be appended to the end of the file.

This is the result of an automatic analysis using data collected in 2023:

    A empresa COPEL apresentou uma receita líquida de R$ 21.927,72 milhões nos últimos 12 meses até o 4T2022, o que representa uma queda em relação ao ano anterior (R$ 23.984,29 milhões). Os custos também diminuíram em relação ao ano anterior, passando de R$ 19.119,64 milhões em 2021 para R$ 16.928,41 milhões em 2022. Isso resultou em um lucro bruto de R$ 4.999,31 milhões no último ano.
    As despesas/receitas operacionais foram negativas em R$ 2.083,08 milhões nos últimos 12 meses, o que indica que a empresa teve mais despesas do que receitas nesse período. O EBITDA foi de zero, o que significa que a empresa não gerou lucro antes dos juros, impostos, depreciação e amortização. O EBIT, por outro lado, foi de R$ 2.916,24 milhões, o que indica que a empresa gerou lucro operacional.
    O resultado financeiro foi negativo em R$ 1.966,04 milhões, o que indica que a empresa teve mais despesas financeiras do que receitas financeiras. Os impostos foram de R$ 199,12 milhões, o que indica que a empresa pagou impostos sobre o lucro.
    O lucro líquido atribuído à controladora foi de R$ 1.112,01 milhões, enquanto o lucro líquido atribuído a não controladores foi de R$ 37,31 milhões. A dívida bruta da empresa foi de R$ 12.454,22 milhões, enquanto a dívida líquida não foi informada. Não há informações sobre o CAPEX e o índice dívida líquida/EBITDA nos últimos 12 meses.
    A empresa COPEL apresentou um aumento no Caixa Gerado nas Operações de 82,7% em relação ao ano anterior (2021), e um aumento de 29,3% no Lucro Líquido em relação ao mesmo período. Além disso, houve um aumento no Caixa Líquido das Atividades Operacionais de 15,2% em relação ao ano anterior, indicando uma melhoria na geração de caixa da empresa.
    No entanto, a empresa teve um resultado negativo no Caixa Líquido das Atividades de Investimento, o que pode indicar investimentos em projetos de longo prazo ou aquisições de outras empresas. Já o Fluxo de Caixa Livre apresentou um resultado positivo em 2022, indicando que a empresa gerou caixa suficiente para financiar seus investimentos e pagar dividendos aos acionistas.
    Por fim, a empresa apresentou um saldo final de Caixa e Equivalentes de R$ 2678,46 milhões, indicando uma posição financeira saudável e capaz de enfrentar eventuais desafios financeiros. No geral, os resultados financeiros da COPEL parecem positivos e indicam uma boa performance da empresa.
    A empresa Copel apresenta um crescimento constante em seu Ativo Total nos últimos anos, passando de R$ 35.930,10 em 2018 para R$ 49.537,54 em 2021 e R$ 49.703,70 em 2022. Esse aumento é impulsionado principalmente pelo crescimento do Ativo Não Circulante, que representa a maior parte do Ativo Total da empresa.
    O Ativo Circulante da empresa tem se mantido relativamente estável nos últimos anos, com uma leve queda em 2022 em comparação com o ano anterior. As Aplicações Financeiras tiveram uma queda significativa em 2022, representando apenas R$ 0,25, enquanto em 2021 eram R$ 16,30.
    O Contas a Receber também apresentou uma queda em 2022 em relação ao ano anterior, mas ainda representa uma parcela significativa do Ativo Circulante da empresa. O Caixa e Equivalentes de Caixa, por sua vez, apresenta uma queda constante nos últimos anos.
    No Ativo Não Circulante, o Ativo Realizável a Longo Prazo tem crescido consistentemente nos últimos anos, enquanto os Investimentos e o Imobilizado têm se mantido relativamente estáveis. O Intangível teve um aumento significativo em 2022 em comparação com os anos anteriores.
    No Passivo, a empresa apresenta uma redução no Passivo Circulante em 2022 em comparação com o ano anterior, enquanto o Passivo Não Circulante teve um aumento significativo. Isso pode indicar que a empresa está buscando financiamentos de longo prazo para seus projetos.
    O Patrimônio Líquido Consolidado da empresa tem apresentado um crescimento constante nos últimos anos, impulsionado principalmente pela Reserva Lucros. O Capital Social Realizado se manteve estável nos últimos anos.
    Em geral, a análise do balanço patrimonial da empresa Copel indica que a empresa está em uma posição financeira sólida e com perspectivas de crescimento no longo prazo. No entanto, é importante destacar a queda nas Aplicações Financeiras e no Caixa e Equivalentes de Caixa, o que pode indicar a necessidade de uma gestão mais eficiente do capital de giro da empresa.
