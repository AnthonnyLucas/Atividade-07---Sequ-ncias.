import matplotlib.pyplot as plt
import numpy as np

# --- Função de Estilo (vinda do seu segundo código) ---
def estilizar_axes(ax):
    """Aplica um estilo visual escuro a um eixo do matplotlib."""
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    ax.grid(True, color='gray', linestyle='--', alpha=0.3)
    for spine in ax.spines.values():
        spine.set_color('white')

# --- Função de Cálculo (vinda do seu primeiro código) ---
def sequencia_populacional(k, p1, n_geracoes):
    """
    Calcula a sequência recursiva do crescimento populacional.
    """
    populacao = [p1]
    p_n = p1
    for _ in range(1, n_geracoes):
        p_n_mais_1 = k * p_n * (1 - p_n)
        populacao.append(p_n_mais_1)
        p_n = p_n_mais_1
    return populacao

# --- Parâmetros Iniciais ---
p1 = 0.5  # População inicial de 50%
n_geracoes = 100
valores_k = [2.5, 3.3, 3.5, 4.0]
iteracoes = range(1, n_geracoes + 1)

# --- Paleta de Cores (para ficarem bem no fundo escuro) ---
cores_plot = ['#00FFFF', '#FF00FF', '#FFFF00', '#00FF00'] # Ciano, Magenta, Amarelo, Verde Limão

# --- Geração e Plotagem dos Gráficos com o Novo Design ---

# Configura a figura com o fundo escuro
fig, axs = plt.subplots(len(valores_k), 1, figsize=(12, 18), sharex=True)
fig.set_facecolor('#1e1e1e')

# Adiciona o título principal com a cor branca
fig.suptitle(
    'Análise da População de Insetos ($p_{n+1} = k \cdot p_n \cdot (1 - p_n)$)',
    fontsize=18,
    color='white'
)

for i, k in enumerate(valores_k):
    # Seleciona o subplot atual
    ax = axs[i]
    
    # Aplica o estilo escuro ao subplot
    estilizar_axes(ax)
    
    # Calcula a sequência
    p_n = sequencia_populacional(k, p1, n_geracoes)

    # Plota o gráfico usando a cor correspondente da nossa paleta
    ax.plot(iteracoes, p_n, 'o-', markersize=4, label=f'k = {k}', color=cores_plot[i])

    # Define o título do subplot (a cor já foi definida em 'estilizar_axes')
    ax.set_title(f'Comportamento da População para k = {k}', fontsize=14)
    ax.set_ylabel('População ($p_n$)')
    ax.set_ylim(0, 1.05)

    # Configura a legenda com o estilo escuro
    leg = ax.legend(loc='upper right')
    leg.get_frame().set_facecolor('#333333')
    leg.get_frame().set_edgecolor('white')
    for text in leg.get_texts():
        text.set_color('white')

# Ajustes finais do layout
# Adiciona o rótulo do eixo X ao último gráfico
axs[-1].set_xlabel('Geração (n)', fontsize=12)

# Ajusta o espaçamento para evitar sobreposição
fig.tight_layout(pad=3.0, rect=[0, 0, 1, 0.95])

plt.show()