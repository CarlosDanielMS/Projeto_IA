# Treinamento do Agente SARSA no Ambiente Taxi-v3

Este repositório contém a implementação do algoritmo SARSA para treinar um agente no ambiente **Taxi-v3** do OpenAI Gymnasium. O agente aprende a navegar e a realizar ações no ambiente utilizando o algoritmo SARSA (State-Action-Reward-State-Action), com o objetivo de otimizar a recompensa obtida durante o processo de aprendizado.

## Funcionalidades

- **Treinamento SARSA:** O agente é treinado utilizando o algoritmo SARSA para aprender a tomar ações com base no ambiente.
- **Visualização do Treinamento:** Durante o treinamento, o agente realiza ações no ambiente, que são visualizadas em um GIF animado.
- **Métricas de Desempenho:** O desempenho do agente é avaliado durante o treinamento, com gráficos que mostram as recompensas e o número de passos por episódio.

Link Colab: https://colab.research.google.com/drive/1pzJUex68u-_YT7OjJwEhNnshkN-gVnbc?usp=sharing

Como Usar

    Configuração do Ambiente: O código cria automaticamente o ambiente Taxi-v3 do Gymnasium. Você pode customizar o ambiente conforme necessário.

    Treinamento do Agente: O treinamento do agente é feito no ambiente Taxi-v3 utilizando o algoritmo SARSA. O código treina o agente por 20.000 episódios, mas você pode ajustar o número de episódios conforme necessário.

    Visualização do Agente: Durante o treinamento, o agente realiza ações que podem ser visualizadas como um GIF animado. O processo de aprendizado pode ser visualizado em vários episódios de treinamento.

    Métricas: O código gera dois gráficos:
        Recompensas por Episódio: Exibe a recompensa total que o agente obteve durante cada episódio.
        Passos por Episódio: Mostra o número de passos que o agente levou para completar um episódio.

    GIF de Treinamento: O código cria um GIF mostrando como o agente está aprendendo e evoluindo ao longo do tempo. O GIF é salvo na pasta images.

Estrutura do Código
Funções Principais

    create_environment(): Cria o ambiente Taxi-v3 com o modo de renderização rgb_array.
    initialize_q_table(): Inicializa a tabela Q para o algoritmo SARSA, que armazena as ações do agente.
    epsilon_greedy(): Implementa a política epsilon-greedy para selecionar ações com base na tabela Q.
    sarsa_update(): Atualiza a tabela Q de acordo com o algoritmo SARSA.
    train_sarsa(): Treina o agente utilizando o algoritmo SARSA.
    visualize_training(): Executa episódios do agente e captura os frames para gerar uma visualização do treinamento.
    create_gif(): Cria um GIF a partir dos frames coletados durante o treinamento.
    plot_metrics(): Plota gráficos de recompensas e passos por episódio.

Resultados

Após o treinamento, você verá os seguintes resultados:

    Gráficos: O código gera gráficos que mostram o progresso do agente durante o treinamento.
    GIF: O código cria um GIF que mostra o agente realizando as ações no ambiente Taxi-v3 ao longo dos episódios.

Testado no Google Colab

Este código foi testado com sucesso no Google Colab. Para rodar no Colab, basta fazer upload dos arquivos do repositório e seguir as instruções acima para instalar as dependências.
