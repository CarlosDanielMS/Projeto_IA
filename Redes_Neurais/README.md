# Deep Q-Learning no Ambiente Taxi-v3

Este projeto implementa um agente de **Reinforcement Learning** utilizando a abordagem **Deep Q-Learning (DQN)** no ambiente **Taxi-v3** do Gymnasium. O código foi desenvolvido e testado no **Google Colab**, aproveitando os recursos da plataforma para realizar simulações e visualizações de forma eficiente.

---

## 📖 **Descrição do Projeto**

O objetivo do agente é aprender a realizar a tarefa de transporte de passageiros no ambiente **Taxi-v3** de maneira otimizada. Para isso, ele utiliza o algoritmo **Deep Q-Learning**, que combina:

- **Rede Neural Profunda (DQN)**: Para aproximar os valores-Q.
- **Replay Buffer**: Para armazenar e reutilizar transições da experiência passada.
- **Target Network**: Para estabilidade no treinamento.

### **Principais Funcionalidades**
- Treinamento do agente em um ambiente discreto com estados representados por *one-hot encoding*.
- Visualização do desempenho do agente por meio de gráficos.
- Criação de um GIF animado mostrando as ações do agente no ambiente após o treinamento.

---

## 🛠️ **Desenvolvimento no Google Colab**

O código foi inteiramente testado no ambiente **Google Colab**, que oferece uma configuração rápida e prática para projetos em Python. O Colab permite:

- Instalação de dependências como `gymnasium`, `pygame` e `moviepy`.
- Renderização de frames e geração de animações para visualização do aprendizado do agente.
- Visualização de gráficos e métricas durante o treinamento.

### **Passos Realizados**
1. **Configuração Inicial**:
   - Instalação de pacotes necessários:
     ```bash
     !apt-get install -y python-opengl ffmpeg > /dev/null
     !pip install gymnasium moviepy pygame > /dev/null
     ```
   - Preparação do ambiente **Taxi-v3** no Gymnasium.

2. **Treinamento**:
   - O agente foi treinado por 500 episódios, ajustando sua política para maximizar as recompensas.
   - Utilizou-se uma rede neural simples com duas camadas ocultas para aproximar os Q-values.

3. **Visualização**:
   - Quadros renderizados foram coletados e transformados em GIF para acompanhar o comportamento do agente.
   - Um gráfico de desempenho (recompensa por episódio) foi gerado.

---

## 📊 **Resultados Obtidos**

1. **Gráfico de Recompensas**:
   - Mostra a evolução do desempenho do agente ao longo dos episódios de treinamento.
   - O agente aprendeu a maximizar a recompensa acumulada com o tempo.

2. **GIF Animado**:
   - O GIF gerado (`images/dqn_training_visualization.gif`) demonstra as decisões tomadas pelo agente em um ambiente visível.

---

## 🚀 **Como Executar no Colab**

1. Copie o código fornecido em um notebook do Google Colab.
2. Certifique-se de instalar todas as dependências.
3. Execute o treinamento e visualize os resultados diretamente na plataforma.
4. link colab: https://colab.research.google.com/drive/1pzJUex68u-_YT7OjJwEhNnshkN-gVnbc?authuser=1#scrollTo=hs7ZjW_dZD2T

---

