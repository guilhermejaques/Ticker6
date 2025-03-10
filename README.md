
# Descrição 

Essa automação é um projeto individual em andamento e que pode ser utilizada por estudantes ou investidores. Por trás da interface gráfica [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) existe um algoritmo que é muito simples e eficaz, escrito na linguagem de programação Python. 

Ticker6 é o nome do programa e, com ele, você poderá consultar a cotação atualizada das ações e vizualizar o preço teto sem a necessidade de calcular e buscar os dados em sites. Também é possível armazenar os ativos favoritos em uma carteira. 

O programa depende dos dados fornecidos pela biblioteca [yFinance](https://github.com/ranaroussi/yfinance) (Apache License), e você precisará estar conectado à internet para usá-lo.

Faça o teste, contribua e aproveite!

---
![Carteira](https://github.com/user-attachments/assets/b0bec184-258c-4f52-b5e6-648f306f87da)

![Consulta de Ativo](https://github.com/user-attachments/assets/7006eef4-b2be-4aa2-b5ce-bc5798eb2b70)


---
# O código

- O código foi escrito propositalmente em português (sem considerar as palavras reservadas em inglês da própria linguagem).
  
- Há duas variáveis importantes que estão destacadas no início do código e que podem ser alteradas, influenciando no cálculo do preço teto gerado pelo programa. Por padrão, elas são definidas como `dy = 0,06 (6%) | anos = 5`.
  
- Sobre a modularização, o código principal executável é `main.pyw` e faz requisição a uma lista de ativos válidos que está em `validos.py`.
  
- O código faz a criação de um arquivo `.ativos.txt` (ou .**CSV** na versão atual) onde estará registrado todos os ativos permanentes que o usuário definir dentro do programa. O arquivo simples facilita a manutenção dos ativos na carteira.

- Para as versões mais recentes do programa, existe a pasta `img` que armazena imagens de logomarca das empresas da B3. 

# Requisitos

- Python 3.8 (ou superior) com PIP
  
  **Bibliotecas:**
- yFinance 
- CustomTkinter 
- Pillow (Necessário a partir da versão 0.2.0 do Ticker6)


# Como usar / Instalar


Além da instalação do [Python](https://www.python.org/downloads/) e PIP, você precisará do arquivo `main.pyw` que será executado, e do arquivo `validos.py` que é necessário para o funcionamento do programa. Apenas deixe-os na mesma pasta (como no repositório); por fim, será necessário a instalação das bibliotecas.

---
Você pode fazer o download das bibliotecas através de um terminal utilizando o arquivo `requirements.txt` que está no repositório, e com o comando `pip install -r requirements.txt` você fará a instalação das bibliotecas necessárias diretamente do arquivo. 

E claro! também é possível fazer a instalação utilizando o `pip install` para cada uma das bibliotecas. 

# Executável para windows
Embora o uso do repositório seja mais recomendado, você pode fazer o [download](https://github.com/guilhermejaques/Ticker6/releases/tag/EXE) do executável se assim desejar.

# O que é o preço teto de uma ação?

O Preço Teto é o valor máximo que um investidor está disposto a pagar por uma ação e faz parte de uma estratégia previdenciária que busca um retorno mínimo esperado de dividendos. Esse valor pode ser calculado de diferentes formas, dependendo do perfil do investidor. De maneira simples, utiliza-se os dividendos pagos por uma ação e o Dividend Yield desejado.

Aqui, utilizamos parte do Método [Bazin](https://pt.wikipedia.org/wiki/D%C3%A9cio_Bazin) e consideramos a média de dividendos pagos durante 5 anos e um Dividend Yield esperado de 6%.

	Preço Teto = (Média Dividendos) /  6%
 
Uma vez estabelecido um Preço Teto, se o preço de mercado da ação estiver acima do Preço Teto, podemos considerar a ação **sobrevalorizada** e não recomendada para compra. Se o preço da ação estiver abaixo do Preço Teto, a ação está **subvalorizada** e é recomendada, segundo a estratégia.

	Durante a execução do programa, a cor do valor-cotação das ações é alterado: VERDE caso a cotação for menor ou igual ao preço teto | AVERMELHADO caso a cotação ultrapasse o preço teto calculado.
 	! A alteração na cor ajuda apenas na visualização dos números em relação ao preço teto. Não representa uma recomendação de compra ou venda, muito menos a oscilação do ativo na bolsa de valores.



É **importante** não confundir o Preço Teto com o _preço justo_ ou o _preço alvo_ de uma ação, pois o Preço Teto é apenas uma margem de segurança que o investidor pode utilizar para comprar uma ação por um valor aceitável, olhando apenas o potencial de remuneração da empresa. 

E não é apenas o Preço Teto que deve ser considerado na compra de uma ação, e ele pode não significar nada se utilizado de maneira inadequada. É recomendável que o investidor tome suas decisões com cautela e faça uma análise da saúde financeira da empresa e do modelo de negócio, levando em consideração seus objetivos pessoais. 

---
  
	
