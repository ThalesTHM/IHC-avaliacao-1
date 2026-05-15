import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams["figure.dpi"] = 150
plt.rcParams["font.size"] = 10

idades = [
    18, 18, 19, 19, 20,
    20, 20, 20, 21, 21,
    21, 22, 22, 22, 23,
    23, 23, 24, 24, 25,
    25, 25, 26, 27, 27,
    28, 29, 29, 30, 31,
    32, 33, 34, 35, 36,
    38, 40, 42, 44, 46,
    48, 51, 63, 20, 21,
    22, 23, 27, 29, 34,
]

sexo_nomes = ["Masculino", "Feminino"]
sexo_contagem = [29, 21]

objetivo_nomes = ["Hipertrofia", "Emagrecimento", "Condicionamento", "Saúde geral"]
objetivo_contagem = [18, 13, 8, 11]

freq_dias = [1, 2, 3, 4, 5]
freq_contagem = [1, 9, 20, 12, 8]

tempo_meses = [
    1, 1, 2, 3, 3, 4, 4, 5, 6, 6,
    7, 7, 8, 8, 9, 10, 11, 12, 12, 12,
    14, 16, 16, 18, 18, 20, 20, 24, 24, 24,
    30, 30, 30, 36, 36, 36, 48, 60, 60, 72,
    84, 84, 96, 96, 108, 120, 120, 144, 180, 240,
]

mensalidades = [
    65.0, 70.0, 70.0, 75.0, 75.0, 75.0, 75.0, 80.0, 80.0, 80.0,
    80.0, 80.0, 80.0, 80.0, 80.0, 85.0, 85.0, 85.0, 85.0, 85.0,
    90.0, 90.0, 90.0, 90.0, 90.0, 90.0, 90.0, 90.0, 95.0, 95.0,
    100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 105.0,
    110.0, 110.0, 120.0, 120.0, 120.0, 130.0, 130.0, 140.0, 150.0, 200.0,
]

notas_espaco   = [2] * 6 + [3] * 26 + [4] * 14 + [5] * 4
notas_instrutor = [2] * 1 + [3] * 7 + [4] * 27 + [5] * 15
notas_preco    = [1] * 1 + [2] * 1 + [3] * 20 + [4] * 28

horario_nomes = ["Manhã (6h–9h)", "Tarde (12h–15h)", "Noite (18h–22h)"]
horario_contagem = [18, 8, 24]

rec_nomes = ["Sim", "Não", "Talvez"]
rec_contagem = [40, 5, 5]

rcl_nomes = ["Equipamentos lotados", "Falta de equipamentos", "Preço da mensalidade", "Limpeza insuficiente"]
rcl_contagem = [23, 9, 8, 6]

CORES = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"]
CORES_SAT = ["#d73027", "#fc8d59", "#fee090", "#91bfdb", "#4575b4"]

fig1, axes1 = plt.subplots(1, 3, figsize=(16, 5))
fig1.suptitle("Perfil dos Respondentes — Academia de Musculação", fontsize=13, fontweight="bold")

axes1[0].hist(idades, bins=range(16, 68, 4), color="#4C72B0", edgecolor="white", linewidth=0.8)
axes1[0].axvline(
    np.mean(idades), color="red", linestyle="--", linewidth=1.5,
    label=f"Média: {np.mean(idades):.1f} anos"
)
axes1[0].set_title("Distribuição de Idades")
axes1[0].set_xlabel("Idade")
axes1[0].set_ylabel("Nº de respondentes")
axes1[0].legend()

axes1[1].pie(sexo_contagem, labels=sexo_nomes, autopct="%1.1f%%",
             colors=["#4C72B0", "#DD8452"], startangle=90)
axes1[1].set_title("Distribuição por Sexo")

axes1[2].pie(objetivo_contagem, labels=objetivo_nomes, autopct="%1.1f%%",
             colors=CORES, startangle=90, pctdistance=0.78)
axes1[2].set_title("Objetivo Principal na Academia")

fig1.tight_layout()
fig1.savefig("grafico_perfil.png", bbox_inches="tight")
plt.close(fig1)

fig2, axes2 = plt.subplots(1, 2, figsize=(13, 5))
fig2.suptitle("Padrões de Uso da Academia", fontsize=13, fontweight="bold")

bars_freq = axes2[0].bar(freq_dias, freq_contagem, color="#55A868",
                          edgecolor="white", linewidth=0.8, width=0.6)
for bar, v in zip(bars_freq, freq_contagem):
    axes2[0].text(
        bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.2,
        str(v), ha="center", va="bottom", fontweight="bold"
    )
axes2[0].set_title("Frequência Semanal à Academia")
axes2[0].set_xlabel("Dias por semana")
axes2[0].set_ylabel("Nº de respondentes")
axes2[0].set_xticks(freq_dias)

axes2[1].hist(mensalidades, bins=10, color="#DD8452", edgecolor="white", linewidth=0.8)
axes2[1].axvline(
    np.mean(mensalidades), color="red", linestyle="--", linewidth=1.5,
    label=f"Média: R${np.mean(mensalidades):.2f}"
)
axes2[1].axvline(
    np.median(mensalidades), color="green", linestyle=":", linewidth=1.5,
    label=f"Mediana: R${np.median(mensalidades):.2f}"
)
axes2[1].set_title("Valor da Mensalidade Paga")
axes2[1].set_xlabel("Mensalidade (R$)")
axes2[1].set_ylabel("Nº de respondentes")
axes2[1].legend()

fig2.tight_layout()
fig2.savefig("grafico_uso.png", bbox_inches="tight")
plt.close(fig2)

fig3, axes3 = plt.subplots(1, 2, figsize=(14, 6))
fig3.suptitle("Satisfação dos Frequentadores", fontsize=13, fontweight="bold")

criterios = ["Espaço /\nEquipamentos", "Qualidade do\nInstrutor", "Preço da\nMensalidade"]
todas_notas = [notas_espaco, notas_instrutor, notas_preco]
x = np.arange(len(criterios))
width = 0.15

for i, nota_val in enumerate(range(1, 6)):
    counts = [sum(1 for n in notas if n == nota_val) for notas in todas_notas]
    axes3[0].bar(x + (i - 2) * width, counts, width,
                 label=f"Nota {nota_val}", color=CORES_SAT[i])

axes3[0].set_xticks(x)
axes3[0].set_xticklabels(criterios)
axes3[0].set_ylabel("Nº de respondentes")
axes3[0].set_title("Distribuição das Notas por Critério")
axes3[0].legend(loc="upper right", fontsize=9)
axes3[0].yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

medias = [np.mean(notas_espaco), np.mean(notas_instrutor), np.mean(notas_preco)]
criterios_curtos = ["Espaço", "Instrutor", "Preço"]
bars_med = axes3[1].bar(
    criterios_curtos, medias,
    color=["#4C72B0", "#DD8452", "#55A868"],
    edgecolor="white", linewidth=0.8, width=0.5
)
for bar, v in zip(bars_med, medias):
    axes3[1].text(
        bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
        f"{v:.2f}", ha="center", va="bottom", fontweight="bold"
    )
axes3[1].set_ylim(0, 5.2)
axes3[1].set_ylabel("Nota média (1–5)")
axes3[1].set_title("Nota Média de Satisfação por Critério")
axes3[1].axhline(3.0, color="gray", linestyle="--", linewidth=1, alpha=0.6, label="Neutro (3.0)")
axes3[1].legend(fontsize=9)

fig3.tight_layout()
fig3.savefig("grafico_satisfacao.png", bbox_inches="tight")
plt.close(fig3)

fig4, axes4 = plt.subplots(1, 3, figsize=(16, 5))
fig4.suptitle("Comportamento e Preferências", fontsize=13, fontweight="bold")

axes4[0].pie(horario_contagem, labels=horario_nomes, autopct="%1.1f%%",
             colors=["#55A868", "#DD8452", "#4C72B0"], startangle=90)
axes4[0].set_title("Horário Preferido de Treino")

bar_colors_rec = ["#55A868", "#C44E52", "#DD8452"]
bars_rec = axes4[1].bar(rec_nomes, rec_contagem, color=bar_colors_rec,
                         edgecolor="white", linewidth=0.8, width=0.5)
for bar, v in zip(bars_rec, rec_contagem):
    axes4[1].text(
        bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
        str(v), ha="center", va="bottom", fontweight="bold"
    )
axes4[1].set_title("Recomendaria a Academia?")
axes4[1].set_ylabel("Nº de respondentes")

bars_rcl = axes4[2].barh(rcl_nomes, rcl_contagem, color="#8172B2",
                          edgecolor="white", linewidth=0.8)
for bar, v in zip(bars_rcl, rcl_contagem):
    axes4[2].text(
        v + 0.3, bar.get_y() + bar.get_height() / 2,
        str(v), ha="left", va="center", fontweight="bold"
    )
axes4[2].set_title("Principal Reclamação")
axes4[2].set_xlabel("Nº de respondentes")

fig4.tight_layout()
fig4.savefig("grafico_comportamento.png", bbox_inches="tight")
plt.close(fig4)

print("Gráficos salvos:")
print("  grafico_perfil.png")
print("  grafico_uso.png")
print("  grafico_satisfacao.png")
print("  grafico_comportamento.png")
print()
print(f"N = {len(idades)} respondentes")
print(f"Idade        : média={np.mean(idades):.1f}  mediana={np.median(idades):.0f}  DP={np.std(idades):.1f}")
print(f"Mensalidade  : média=R${np.mean(mensalidades):.2f}  mediana=R${np.median(mensalidades):.2f}  DP=R${np.std(mensalidades):.2f}")
print(f"Sat. espaço  : {np.mean(notas_espaco):.2f}")
print(f"Sat. instrutor: {np.mean(notas_instrutor):.2f}")
print(f"Sat. preço   : {np.mean(notas_preco):.2f}")
print(f"Freq. média  : {np.average(freq_dias, weights=freq_contagem):.2f} dias/semana")
print(f"Recomendaria (Sim): {rec_contagem[0]/sum(rec_contagem)*100:.0f}%")
print(f"Reclamação principal: {rcl_nomes[0]} ({rcl_contagem[0]/sum(rcl_contagem)*100:.0f}%)")
