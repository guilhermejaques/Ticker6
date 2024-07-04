
# Descrição 

Esta automação é um projeto individual em andamento e que pode ser utilizada por estudantes ou investidores. Por trás da interface gráfica [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) existe um algoritmo que é muito simples e eficaz, escrito na linguagem de programação Python. 

Ticker6 é o nome do programa e, com ele, você poderá consultar a cotação atualizada das ações e vizualizar o preço teto sem a necessidade de calcular e buscar os dados em sites. Também é possível armazenar os ativos favoritos em uma carteira. 

O programa depende dos dados fornecidos pela biblioteca [yFinance](https://github.com/ranaroussi/yfinance) (Apache License), e você precisará estar conectado à internet para usá-lo.

Faça o teste, contribua e aproveite!

---
![Janela Consulta - Ticker6](https://private-user-images.githubusercontent.com/159738624/345963867-2f3c672a-8535-4fa5-80f9-e409608b6af3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjAxMzY2MTEsIm5iZiI6MTcyMDEzNjMxMSwicGF0aCI6Ii8xNTk3Mzg2MjQvMzQ1OTYzODY3LTJmM2M2NzJhLTg1MzUtNGZhNS04MGY5LWU0MDk2MDhiNmFmMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDcwNFQyMzM4MzFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MzMyOGQwY2E2ZTBlNzVkMjRmZDg0MGMwZDk0MzM5MWNjMDQ1ZWUwMGNjOGRlN2U1NzAwNWNiMTMwY2E2NmNlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Ycaa-8PQx39pGcmCEyWmG2RLNK1o3HzZOvFTFb3V1-g)

![Janela Carteira - Ticker6](https://private-user-images.githubusercontent.com/159738624/345963857-bf99e384-f990-4119-b27f-a1d76b22b9c3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjAxMzY2MTEsIm5iZiI6MTcyMDEzNjMxMSwicGF0aCI6Ii8xNTk3Mzg2MjQvMzQ1OTYzODU3LWJmOTllMzg0LWY5OTAtNDExOS1iMjdmLWExZDc2YjIyYjljMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDcwNFQyMzM4MzFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yYWNiZjRiMzZhYjNiZWI3Zjg0ODM3Mzg5NjQ2NTk1M2FhMGU4ZmI1OTcwZjU2MDc5OWQ0YWU5ZThmODgwZWI4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.7OWn-sfKdzuMajbcQ-twE1qOCnGMT_KzBHq0JmJTrqo)


# Executável para windows
[Clique Aqui](https://github.com/guilhermejaques/Ticker6/releases/tag/v0.1.0) para ter acesso ao DOWNLOAD do arquivo executável.

---
# O código

- O código foi escrito propositalmente em português (sem considerar as palavras reservadas em inglês da própria linguagem).
  
- Há duas variáveis importantes que estão destacadas no início do código e que podem ser alteradas, influenciando no cálculo do preço teto gerado pelo programa. Por padrão, elas são definidas como `dy = 0,06 (6%) | anos = 5`.
  
- Sobre a modularização, o código principal executável é `main.py` e faz requisição a uma lista de ativos válidos que está em `validos.py`.
  
- O código faz a criação de um arquivo `.ativos.txt` onde estará registrado todos os ativos permanentes que o usuário definir dentro do programa. 


# Como usar 

Além da instalação do Python, você precisará do arquivo `main.py` que será executado, e do arquivo `validos.py` que é necessário para o funcionamento do programa. Apenas deixe-os na mesma pasta (como no repositório); por fim, será necessário a instalação das bibliotecas.

Como em qualquer outro repositório, ao fazer o download ou clonagem, os arquivos já estarão na estrutura ideal para uso. E contanto que o usuário mantenha os arquivos citados acima no mesmo diretório, não haverá problemas para iniciar.



# Requisitos

- Python 3.8 +
- yFinance 0.2.40
- CustomTkinter 5.2.2

---
Você pode fazer o download das bibliotecas dentro do ambiente desejado utilizando o arquivo `requirements.txt` que está no repositório, e com o comando `pip install -r requirements.txt` você fará a instalação das bibliotecas necessárias diretamente do arquivo.

E claro! também é possível fazer a instalação utilizando o `pip install` para cada uma das bibliotecas.


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
  
	
