# Web Crawler e Strings

O principio do Crawler é procurar dentro do texto html as informações que são relevantes, observando as informações que estão sempre do lado das informações relevantes.
## Funções do programa

1. Dólar
2. Euro
3. Temperatura Máxima
4. Temperatura Mínima

### Exemplo 1
Será utilizado o site [ClimaTempo](https://www.climatempo.com.br/) para temperatura máxima e mínima. Ao inspencionar a páginar e verificar o código html iremos buscar algumas informaçãoes como temperatura máxima.
 
Sempre ao lado desta informação <strong> 29º </strong> estará o texto "temperatura máxima"
O princio de funcionamento crowler é buscar temperatura máxima e pegar o texto, valor que estiver em seguida

### Instruções:

- Importando biblioteca <strong> urllib </strong>
  - `import urllib.request`
    - Desta forma poderemos obter dados da internet
- Utilizando metodos da biblioteca
  - `urllib.request.urlopen(https://www.site.com).read()`
    - Metodo `urlopen` : passando uma url para obter informações
    - Metodo `read()` retorna o conteúdo html do site que passa como parâmetro.
- linha 4, É convertido o resultado da linha anterior para string
  - `content = str(content)`
- linha 5, find: É uma variável que conterar o valor que está próximo da informação relevante, a informação que desejamos.
- linha 6, content.index(str) Retorna para nós o indice que ocorre pela primeira vez a string que passamos como parametro
- ![Manipulação de String](image.jpg)
    - `content.index(str)`
    - `len(str)`
    - content[ posicao : posicao + 4]

## Atualização para o funcionmento em 2022
Fonte: 
1.  [Francisco Calaça](https://youtu.be/IUkvRa0omX4?list=PLVj7t-1tQQnGMIDg5_zpFaDmruEMgbsd1)
2.  [StackoverFlow](https://stackoverflow.com/questions/16627227/problem-http-error-403-in-python-3-web-scraping)
