# Projet Acender um Led 
### Exercicio Grupo de Pesquisa de Internet das Coisas UTFPR TD

Projeto de controle de Led usando flask

### Requisitos Minimos de sistema

* PySerial
* Flask

### Instalação das bibliotecas

$ pip2 install serial flask

### How to use ? 
PS: Abra 2 terminais

 
```shell
terminal-1 $ git clone https://github.com/juanengml/ProjetLed.git
terminal-1 $ cd ProjetLed
terminal-1 $ python app.py 
```


Crie sua conta no https://ngrok.com/
siga os passos para autenticação, depois com seu ngrok autenticado abra o segundo terminal
```shell
terminal-2 $ ./ngrok http 8080 
```
Espere ele gerar seu link simular a esse

![Figure 1-1](https://ngrok.com/static/img/ngrok-demo-static.png "Figure 1-1")

### Como funciona ? 

Seu arduino esta programado para ler 2 valores de entrada, 'l' para ligar e 'd' para desligar, esse comendo é enviado pelo computador que opera como servidor web onde esta armazenado o site que ao receber as entradas dos botões pelo usuario envia para o arduino por uma metodo post. Como o flask cria um server simples temos um numero IP local e uma porta rodando o serviço definida na programação do app.py, o Ngrok faz um tunelamento e nos gera 2 endereços web que, um com ssl e outro apenas http puro.


### Eletronica no Arduino e no Raspberry 
1 - Passo: vc conecta seu modulo rele no arduino 

![Figure 1-2](https://niltonfelipe.files.wordpress.com/2015/02/teste-630x368.png "Figure 1-2")

2 - Passo: conecte seu raspberry na porta usb do arduino

![Figure 1-3](https://www.embarcados.com.br/wp-content/uploads/2015/10/imagem-de-destaque-4-696x418.png "Figure 1-3")

3) Hacking Happy ! 
![Gat hacker](https://media.giphy.com/media/kMfVZAUME15XG/giphy.gif)