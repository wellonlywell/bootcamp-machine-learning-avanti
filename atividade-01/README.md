# Atividade 01 — Conceitos básicos de Machine Learning

## Curso

Básico em Machine Learning — Atlântico Avanti

## Participante

Well Sousa

## Tipo de atividade

Atividade diagnóstica individual.

## Respostas

### 1. Explique, com suas palavras, o que é machine learning?

Machine learning, ou aprendizado de máquina, é uma área da computação que permite que sistemas encontrem padrões em dados e utilizem esses padrões para realizar previsões, classificações ou tomar decisões.

Diferente de um programa em que todas as regras são escritas manualmente, em machine learning fornecemos exemplos para que o modelo aprenda relações existentes nos dados. Por exemplo, um sistema pode analisar várias mensagens já classificadas como spam ou não spam e, a partir delas, aprender a identificar novas mensagens suspeitas.

Isso não significa que a máquina pensa como uma pessoa. Ela realiza cálculos e identifica padrões com base nos dados que recebeu.

### 2. Explique o conceito de conjunto de treinamento, conjunto de validação e conjunto de teste em machine learning.

O conjunto de treinamento é a parte dos dados utilizada para o modelo aprender os padrões. É nessa etapa que o algoritmo observa os exemplos e ajusta seus parâmetros.

O conjunto de validação é utilizado durante o desenvolvimento para verificar o desempenho do modelo e ajudar na escolha de configurações. Ele permite perceber se o modelo precisa de ajustes antes da avaliação final.

Já o conjunto de teste é utilizado no final para avaliar como o modelo se comporta com dados que não foram usados no treinamento nem nos ajustes.

Eu comparo esse processo com estudar para uma prova: o conjunto de treinamento seria o conteúdo e os exercícios usados para aprender, a validação seria um simulado usado para descobrir o que ainda precisa ser melhorado e o teste seria a prova final, com questões novas.

### 3. Explique como você lidaria com dados ausentes em um conjunto de dados de treinamento.

Primeiro, eu verificaria a quantidade de dados ausentes e tentaria entender por que eles não foram preenchidos. Eu não removeria ou substituiria os valores automaticamente, porque a ausência de uma informação também pode ter algum significado.

Quando existissem poucos registros incompletos e eles não fossem importantes para a análise, poderia ser possível removê-los. Em outros casos, valores numéricos poderiam ser preenchidos utilizando a média ou a mediana, enquanto dados categóricos poderiam ser preenchidos com a categoria mais frequente.

A decisão dependeria do contexto e da importância da informação. Em dados de saúde, por exemplo, preencher um valor sem cuidado poderia gerar uma interpretação errada. Por isso, eu também registraria quais alterações foram realizadas no conjunto de dados.

### 4. O que é uma matriz de confusão e como ela é usada para avaliar o desempenho de um modelo preditivo?

A matriz de confusão é uma tabela que compara as previsões feitas pelo modelo com os resultados verdadeiros. Ela ajuda a identificar não apenas quantos acertos o modelo teve, mas também quais tipos de erro ele cometeu.

Em uma classificação com duas possibilidades, a matriz apresenta quatro resultados:

- Verdadeiro positivo: o modelo prevê positivo e a resposta verdadeira também é positiva;
- Verdadeiro negativo: o modelo prevê negativo e a resposta verdadeira também é negativa;
- Falso positivo: o modelo prevê positivo, mas a resposta verdadeira é negativa;
- Falso negativo: o modelo prevê negativo, mas a resposta verdadeira é positiva.

Por exemplo, em um sistema de apoio à identificação de uma doença, um falso negativo acontece quando a pessoa possui a doença, mas o modelo informa que não possui. Esse erro pode ser mais grave do que um falso positivo, dependendo da situação.

A matriz de confusão também permite calcular métricas como acurácia, precisão e revocação, ajudando a avaliar o desempenho do modelo de forma mais completa.

### 5. Em quais áreas você acha mais interessante aplicar algoritmos de machine learning?

As áreas que considero mais interessantes para aplicar machine learning são saúde, educação, acessibilidade e serviços públicos.

Na saúde, algoritmos podem ajudar a identificar padrões em exames, prever demandas de atendimento e apoiar profissionais na análise de informações. Porém, acredito que esses sistemas devem funcionar como apoio e não substituir completamente a decisão humana.

Na educação, machine learning pode ajudar a identificar dificuldades de aprendizagem e recomendar atividades de acordo com o ritmo e as necessidades de cada estudante.

Também considero importante a aplicação na acessibilidade, como em sistemas de legendas automáticas, reconhecimento de voz, descrição de imagens e adaptação de conteúdos.

Apesar das possibilidades, é necessário ter cuidado com a privacidade, a qualidade dos dados e os preconceitos que podem ser reproduzidos pelos algoritmos, principalmente quando as decisões afetam diretamente a vida das pessoas.
