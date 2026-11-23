# Atividade N3 - Cadastro de Campeões de League of Legends  

## Sobre o codigo
O codigo foi feito em Python com o objetivo do programa funcionar como um sistema simples de cadastro no terminal, usando como tema os campeões do LoL.

Todas as informações cadastradas ficam guardadas em um arquivo JSON. Assim sempre que o programa é fechado e aberto novamente, os dados continuam salvos e não perdemos, assim como pediu na atividade.

## Arquivos do projeto
- `aula.py`: é o arquivo principal que contém todo o código do programa e o menu de opções.
- `campeoes-lol.json`: é onde ficam guardados os campeões cadastrados.
- `README.md`: é a documentação explicando o funcionamento do trabalho.

## O que o programa faz
Ao iniciar aparece um menu com as seguintes opções e cada execução realiza uma operação, e para escolher outra opção execute o programa novamente.

1. **Incluir campeão:** Permite adicionar um novo campeão informando nome, função, classe e dificuldade. O código vai gera o ID automaticamente e já salva no arquivo JSON.
2. **Alterar campeão:** Pede o ID de um campeão que já está cadastrado e permite atualizar o nome, a função, a classe e a dificuldade dele, salvando as mudanças por cima.
3. **Excluir campeão:** Pede o ID do campeão e remove ele da lista e do arquivo JSON.
4. **Pesquisar por nome ou função:** Aceita parte do nome ou da função e não diferencia letras maiúsculas de minúsculas.
5. **Listar por nome:** Mostra todos os campeões cadastrados organizados em ordem alfabética pelo nome.
6. **Listar por função:** Mostra todos os campeões cadastrados organizados em ordem alfabética pela função.

## Como os dados ficam salvos
Cada campeão salvo no arquivo `campeoes-lol.json` possui 5 informações:

- `id`: Um número usado para identificar cada campeão na hora de alterar ou excluir.
- `nome`: Nome do campeão.
- `funcao`: Posição em que o campeão joga (ex: top, selva, suporte, atirador ou mid).
- `classe`: Tipo do campeão (ex: lutador, assassino, tank).
- `dificuldade`: Nível de dificuldade para jogar com o campeão (fácil, média ou difícil).

## Como executar
Para executar você deve possuir a extensão no VS Code "Code Runner" e clicar na seta de play (você deve estar dentro da pasta "aula.py") que se localiza na parte superior no canto direito e possuir baixado o python ou digitar no terminal `python aula.py`.