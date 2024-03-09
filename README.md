# ExperimentoMVC

O Flask desempenha o papel de controlador frontal, gerenciando todas as solicitações HTTP na aplicação web. Quando um usuário acessa a rota '/', o Flask direciona a solicitação para a função index(). Essa função é responsável por renderizar o template HTML index.html e exibir a lista de usuários disponíveis.

Ao adicionar um novo usuário através do formulário, a rota '/add' é ativada por meio do método POST. Nesse momento, o Flask invoca a função add_user(), que extrai o nome do usuário do formulário. Em seguida, a função chama o método add_user() do controlador para efetivamente adicionar o novo usuário ao sistema. Após a conclusão desse processo, o Flask redireciona o usuário de volta para a página principal, pronta para exibir as atualizações mais recentes.
