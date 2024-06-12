
# Sobre o projeto

Este programa é um projeto individual e que está em andamento e pode ser utilizado por estudantes ou até mesmo por investidores. Por trás da interface gráfica [(customtkinter)](https://github.com/TomSchimansky/CustomTkinter) existe um algoritmo que é muito simples e prático, escrito na linguagem de programação Python. Ticker6 é o nome do programa, e com ele você poderá consultar a cotação das ações em tempo real e vizualizar o preço teto sem a necessidade de calcular e buscar os dados pela internet e também é possível armazenar os ativos favoritos em uma carteira. Por enquanto, o programa é dependente dos dados fornecidos pela biblioteca [yfinance](https://github.com/ranaroussi/yfinance) (Apache License). Faça o teste você mesmo (a) e Aproveite!

# O código

- O código foi escrito propositalmente em português (sem considerar as palavras reservadas em inglês da própria linguagem).
  
- Há duas variáveis destacadas no início do código, elas são importantes e podem ser alteradas, influenciando no cálculo gerado pelo programa. Por padrão, elas são definidas como: `dy = 0,06 (6%) | anos = 5`
  
- O paradigma de orientação a objeto é utilizado, mesmo não sendo a melhor opção para simplificar casos específicos do código na condição atual - não sendo necessário em algumas partes - mas, é perfeito para a escalabilidade do código.
  
- Sobre a modularização, o código principal executável é `MAIN.py` e faz requisição a uma lista de de ativos validos que está em `VALIDOS.py`.
  
- O código faz a criação de um arquivo `ativos.txt` onde estará registrado todos os ativos permanentes que o usuário definir dentro do programa. 

# Como usar?

Resumindo, você precisará do arquivo `MAIN.py` que será executado e `VALIDOS.py` que é necessário para o funcionamento do programa, e deixe-os na mesma pasta (como no repositório);
depois será necessário a instalação das bibliotecas.

Com tudo pronto, o programa estará livre para ser utilizado 

# Requisitos:
- Python 3.12
- yfinance
- customtkinter
  
---
Você pode fazer o download das bibliotecas dentro do ambiente utilizando o arquivo `requirements.txt` que está no repositório, e com o comando: `pip install -r requirements.txt` você fará a instalação das bibliotecas requisitadas diretamente do arquivo. 

Obviamente, também é possível fazer a instalação de cada uma das bibliotecas utilizando o PIP, visto que são apenas duas bibliotecas.




# O que é o preço teto de uma ação?

O Preço Teto é o valor máximo que um  mples, utiliza-se os dividendos pagos por uma ação e o Dividend Yield desejado.

Aqui, utilizamos o Método [Bazin](https://pt.wikipedia.org/wiki/D%C3%A9cio_Bazin) e consideramos a média de dividendos pagos durante 5 anos e um Dividend Yield esperado de 6%.


	Preço Teto = (Média Dividendos) /  6%
 
Uma vez estabelecido um Preço Teto, se o preço de mercado da ação estiver acima do Preço Teto, podemos considerar a ação **sobrevalorizada** e não recomendada para compra. Se o preço da ação estiver abaixo do Preço Teto, a ação está **subvalorizada** e é recomendada, segundo a estratégia.

É **importante** não confundir o Preço Teto com o _preço justo_ ou o _preço alvo_ de uma ação, pois o Preço Teto é apenas uma margem de segurança que o investidor pode utilizar para comprar uma ação por um valor aceitável, olhando apenas o potencial de remuneração da empresa. 

E não é apenas o indicador de Preço Teto que deve ser considerado na compra de uma ação, e ele pode não significar nada se utilizado de maneira inadequada. É recomendável que o investidor tome suas decisões com cautela e faça uma análise da saúde financeira da empresa e do modelo de negócio, levando em consideração seus objetivos pessoais. 

---
  
	
