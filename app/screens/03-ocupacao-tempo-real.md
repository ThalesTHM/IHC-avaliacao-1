# Tela 03 — Ocupação em Tempo Real

> **Módulo:** Monitor de Lotação  
> **Persona — necessidade atendida:** Lucas quer verificar a lotação da academia antes de sair de casa, evitando perder 30 minutos esperando aparelhos no horário de pico (18h–20h).

---

## Layout Principal

```
┌─────────────────────────────┐
│  ←   Lotação da Academia    │  ← top bar
│                             🔔 │
├─────────────────────────────┤
│                              │
│  AGORA — 18h45               │
│  ┌──────────────────────┐   │
│  │                      │   │
│  │       🔴  ALTA       │   │  ← indicador central
│  │    ~38 / 50 pessoas  │   │
│  │   ████████████░░░    │   │  ← barra de ocupação
│  │      76% da capacidade│   │
│  │                      │   │
│  │ Tempo médio de espera │   │
│  │   por aparelho: 8min  │   │
│  └──────────────────────┘   │
│                              │
│  [ 🔔 Me avise quando baixar ]│  ← botão outline
│                              │
│  ──────────────────────────  │
│                              │
│  PREVISÃO PARA HOJE          │
│                              │
│  ┌──────────────────────┐   │
│  │ Gráfico de barras    │   │  ← gráfico horário × lotação
│  │                      │   │
│  │  6h  9h  12h 15h 18h 21h│
│  │  ██  ░   ░    ░  ████ ██│
│  └──────────────────────┘   │
│                              │
│  MELHOR HORÁRIO HOJE         │
│  ┌────────┐ ┌────────┐      │
│  │ 💚 9h  │ │ 💚 21h │      │  ← cards de sugestão
│  │ Baixa  │ │ Baixa  │      │
│  └────────┘ └────────┘      │
│                              │
│  HISTÓRICO SEMANAL           │
│  ← Seg Ter Qua Qui Sex →    │  ← tabs de dia da semana
│  [gráfico de barras do dia]  │
│                              │
└─────────────────────────────┘
```

---

## Especificações

### Card Principal — Indicador Central

| Elemento | Detalhe |
|---|---|
| Background | `#16213E`, border-radius 20px |
| Timestamp | "AGORA — 18h45" — Caption, `#FF6B35` |
| Ícone indicador | Círculo 60×60px colorido dinamicamente |
| Estado texto | "BAIXA" / "MODERADA" / "ALTA" — Heading 2, Bold |
| Contagem | "~38 / 50 pessoas" — Body Large, `#FFFFFF` |
| Barra de progresso | Altura 12px, border-radius 6px, cor dinâmica |
| Porcentagem | Body Medium, `#B0B0C0` |
| Subtexto | "Tempo médio de espera por aparelho: 8min" — Body Small, `#555575` |

### Mapeamento de Cores por Ocupação

| Faixa | % | Cor | Status |
|---|---|---|---|
| Baixa | 0–40% | `#4CAF50` (verde) | "BAIXA" |
| Moderada | 41–70% | `#FFC107` (amarelo) | "MODERADA" |
| Alta | 71–100% | `#F44336` (vermelho) | "ALTA" |

### Botão "Me avise quando baixar"
| Estado | Visual |
|---|---|
| Disponível (lotação Alta/Moderada) | Botão Outline ativo, ícone `notifications_active` |
| Lembrete já ativo | Botão com fundo `rgba(255,107,53,0.2)`, ícone preenchido, texto "Lembrete ativo" |
| Lotação já baixa | Botão escondido ou desabilitado com tooltip "Já está tranquilo!" |

---

### Gráfico de Previsão para Hoje

| Elemento | Detalhe |
|---|---|
| Tipo | Gráfico de barras vertical |
| Eixo X | Horários: 6h, 9h, 12h, 15h, 18h, 21h |
| Eixo Y | 0–100% (sem label numérico, apenas visual) |
| Cor barras | Gradiente conforme faixa de ocupação |
| Barra atual | Marcada com outline `#FF6B35` e seta apontando |
| Fonte dos dados | Médias históricas do mesmo dia da semana (últimas 4 semanas) |
| Interação | Tap em uma barra → tooltip com valor percentual estimado |

---

### Cards de Sugestão "Melhor Horário"

| Elemento | Detalhe |
|---|---|
| Layout | Row com 2–3 cards lado a lado |
| Tamanho | ~100×64px cada |
| Background | `rgba(76,175,80,0.1)` — verde translúcido |
| Borda | 1px `#4CAF50` |
| Ícone | `schedule` verde, 18px |
| Horário | Heading 3, `#4CAF50` |
| Label | "Baixa" ou "Moderada" — Caption, `#4CAF50` |

---

### Histórico Semanal (seção expansível)

| Elemento | Detalhe |
|---|---|
| Tabs | Seg / Ter / Qua / Qui / Sex / Sáb — 7 chips, pill |
| Tab ativo | Background `#FF6B35`, texto branco |
| Tab inativo | Background transparente, borda `#2A2A4A`, texto `#B0B0C0` |
| Gráfico | Barras por horário do dia selecionado |
| Dados | Histograma de frequência de horário dos últimos 30 dias |
| Sem dados | Estado vazio "Dados insuficientes para este dia" |

---

## Atualização em Tempo Real

| Aspecto | Especificação |
|---|---|
| Frequência de atualização | A cada 60 segundos (polling ou WebSocket) |
| Indicador de atualização | Círculo pulsante pequeno `#FF6B35` no canto do card |
| Última atualização | "Atualizado há 23s" — Caption, `#555575`, abaixo do card principal |
| Fallback offline | Banner amarelo no topo: "Sem conexão — dados de 10 min atrás" |

---

## Notificação Push — "Avise-me"

```
┌────────────────────────────────┐
│ 🏋️ FitSync                     │
│ A academia está tranquila!     │
│ Lotação atual: 28% • 20h15     │
│ [Abrir FitSync]                │
└────────────────────────────────┘
```

Ao receber a notificação e tocar nela, o app abre diretamente nesta tela com dados atualizados.
