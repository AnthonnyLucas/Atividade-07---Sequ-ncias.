Projeto: Visualizador Interativo do Mapeamento Logístico

Este projeto oferece uma exploração visual completa da dinâmica do Mapeamento Logístico, uma equação fundamental no estudo da teoria do caos e de sistemas dinâmicos. Foi desenvolvido em Python como parte de uma atividade acadêmica de Cálculo 3.

Conceito
O projeto é centrado na equação recursiva:

Pn+1= k.pn.(1-pn)

Apesar de sua simplicidade, esta fórmula modela como uma população (p_n) evolui ao longo das gerações (n) sob a influência de um fator de crescimento e de limitação ambiental (k). O projeto demonstra como, ao variar o parâmetro k, o sistema transita de um comportamento previsível e ordenado para um estado de caos determinístico.

Funcionalidades Principais
Cálculo da Sequência: O núcleo do projeto é uma função que calcula com precisão a sequência populacional para quaisquer parâmetros k, população inicial e número de gerações.

Visualização Comparativa: Gera múltiplos subplots, permitindo uma comparação direta do comportamento da sequência para diferentes valores de k (2.5, 3.3, 3.5 e 4.0).

Animação Dinâmica: Inclui uma versão com animação que renderiza a formação dos gráficos em tempo real, oferecendo uma visão intuitiva de como a estabilidade, a oscilação e o caos emergem geração após geração.

Código Estruturado e Modular: A versão final do projeto foi reescrita utilizando Programação Orientada a Objetos (POO), encapsulando toda a lógica em uma classe VisualizadorMapeamentoLogistico para maior clareza, organização e reusabilidade do código.

Estilização Customizável: O projeto foi desenvolvido com dois temas visuais distintos:

Tema Escuro: Um design moderno com fundo preto e cores vibrantes.

Tema Claro: Um design profissional e limpo, com fundo branco e uma paleta de cores sóbria.

Tecnologias Utilizadas
Linguagem: Python 

Bibliotecas:

Matplotlib: Para toda a geração de gráficos estáticos e animações.

NumPy: Utilizado para operações numéricas e de array.

Observações e Conclusões
As simulações visuais permitiram observar claramente:

k = 2.5: Convergência para um ponto de equilíbrio estável.

k = 3.3: Bifurcação para um ciclo estável de período 2.

k = 3.5: Nova bifurcação para um ciclo de período 4.

k = 4.0: Ausência de padrão periódico, caracterizando o comportamento caótico.

Este projeto serve como uma demonstração prática e visual da "rota para o caos por duplicação de período", um dos conceitos mais fascinantes dos sistemas não-lineares.
