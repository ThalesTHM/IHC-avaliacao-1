# FitSync — App de Academia de Bairro

> Projeto de tela completo desenvolvido para a disciplina de **Interação Humano-Computador (IHC)** — Avaliação 2.  
> Ferramenta de prototipagem: **Figma**

---

## Contexto

Com base nos dados coletados na pesquisa (N = 50 respondentes) e na persona **Lucas Oliveira Silva**, desenvolvemos o **FitSync**: um aplicativo mobile para academias de bairro que centraliza o acompanhamento de treino, controle de lotação e comunicação com a gestão.

---

## Problema Identificado

Os frequentadores de academia de bairro — representados por Lucas, 25 anos, analista de TI, treino noturno 3×/semana — enfrentam:

| Problema | Impacto |
|---|---|
| Superlotação no horário de pico (18h–20h) | Perde tempo esperando aparelhos |
| Ficha de treino em papel | Não registra histórico de cargas |
| Nenhuma fila virtual para aparelhos disputados | Conflito e desorganização |
| Sem canal direto para reportar problemas | Manutenção atrasada permanece sem solução |
| Sem visualização de progresso | Baixa motivação para permanência |

---

## Solução — FitSync

Aplicativo mobile (Android/iOS) com **5 módulos principais**, cada um mapeado diretamente a uma necessidade da persona:

| # | Módulo | Necessidade da Persona |
|---|---|---|
| 1 | **Ocupação em Tempo Real** | Verificar lotação antes de sair de casa |
| 2 | **Ficha de Treino Digital** | Substituir o papel por sistema interativo com vídeos |
| 3 | **Reserva de Equipamentos** | Fila virtual para aparelhos disputados |
| 4 | **Feedback & Manutenção** | Reportar problemas diretamente à gestão |
| 5 | **Histórico de Evolução** | Visualizar progresso de cargas e frequência |

---

## Estrutura do Projeto de Design

```
app/
├── README.md                        ← este arquivo
├── design-system.md                 ← cores, tipografia e componentes
├── user-flows.md                    ← fluxos de navegação e jornadas do usuário
├── entrega.md                       ← documento de entrega (SIGAA)
└── screens/
    ├── 01-splash-login.md           ← Tela inicial e autenticação
    ├── 02-home-dashboard.md         ← Dashboard principal
    ├── 03-ocupacao-tempo-real.md    ← Monitor de lotação
    ├── 04-ficha-treino.md           ← Ficha de treino digital
    ├── 05-reserva-equipamentos.md   ← Reserva de aparelhos
    ├── 06-feedback-manutencao.md    ← Canal de feedback
    └── 07-historico-evolucao.md     ← Histórico e progresso
```

---

## Princípios de Design

- **Mobile-first:** Lucas usa o smartphone durante o treino, com as mãos suadas e em movimento.
- **Dark Mode como padrão:** Ambiente de academia tem iluminação variável; fundo escuro reduz fadiga visual.
- **Ações em até 2 toques:** Fluxos críticos (verificar lotação, marcar série) devem ser alcançados rapidamente.
- **Feedback visual imediato:** Cada ação deve retornar resposta visual clara (animações leves, toasts).
- **Acessibilidade:** Contraste mínimo WCAG AA; áreas de toque mínimo de 44×44px.

---

## Público-alvo Primário

**Lucas Oliveira Silva** — 25 anos, frequentador noturno, alto letramento digital, foco em hipertrofia, renda média (~R$ 3.200/mês), sensível ao custo-benefício.
