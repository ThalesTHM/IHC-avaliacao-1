# Tela 02 — Home / Dashboard

> **Módulo:** Central de navegação  
> **Persona — necessidade atendida:** Visão rápida de tudo que Lucas precisa saber antes e durante o treino; acesso em até 2 toques para qualquer funcionalidade.

---

## Layout Geral

```
┌─────────────────────────────┐
│  Boa noite, Lucas!   🔔     │  ← top bar
│  Segunda, 08 jun             │
├─────────────────────────────┤
│                              │
│  ┌──────────────────────┐   │
│  │  🟠 LOTAÇÃO AGORA    │   │  ← card destaque (maior)
│  │  ████████░░  Alta    │   │
│  │  ~38 pessoas • 18h45 │   │
│  │  [ Ver detalhes ]    │   │
│  └──────────────────────┘   │
│                              │
│  PRÓXIMO TREINO              │  ← seção label
│  ┌──────────────────────┐   │
│  │  💪 Treino A          │   │
│  │  Peito + Tríceps      │   │
│  │  8 exercícios         │   │
│  │  [ INICIAR TREINO ]  │   │  ← botão primário
│  └──────────────────────┘   │
│                              │
│  ACESSO RÁPIDO               │  ← seção label
│  ┌────────┐  ┌────────┐     │
│  │📅      │  │⚠️      │     │  ← cards pequenos (2 colunas)
│  │Reservas│  │Reportar│     │
│  └────────┘  └────────┘     │
│  ┌────────┐  ┌────────┐     │
│  │📊      │  │🏆      │     │
│  │Evolução│  │Recordes│     │
│  └────────┘  └────────┘     │
│                              │
│  ÚLTIMA ATIVIDADE            │
│  ┌──────────────────────┐   │
│  │ Treino B — 04 jun    │   │
│  │ Costas + Bíceps      │   │
│  │ 55 min · 6 exercícios│   │
│  └──────────────────────┘   │
│                              │
├─────────────────────────────┤
│  🏠      💪      👥   📅  👤 │  ← bottom nav
└─────────────────────────────┘
```

---

## Especificações por Bloco

### Top Bar
| Elemento | Detalhe |
|---|---|
| Saudação | "Boa noite, Lucas!" — Heading 2, `#FFFFFF` (varia por hora do dia) |
| Data | "Segunda, 08 jun" — Body Small, `#B0B0C0` |
| Ícone sino | Material Symbol `notifications`, 24px, `#B0B0C0` |
| Badge notificação | Círculo `#FF6B35`, 8×8px, posicionado no canto superior direito do sino |
| Background | `#1A1A2E` |
| Altura | 72px |

### Card de Lotação (destaque)
| Elemento | Detalhe |
|---|---|
| Background | Card Base (`#16213E`) |
| Ícone | `groups` — 20px, `#FF6B35` |
| Título | "LOTAÇÃO AGORA" — Caption, `#FF6B35`, peso Medium |
| Barra de progresso | Largura 100%, cor dinâmica (verde/amarelo/vermelho) |
| Status | Badge dinâmico: "Baixa" / "Moderada" / "Alta" |
| Contagem | "~38 pessoas • 18h45" — Body Small, `#B0B0C0` |
| Botão | Botão Secundário (outline) "Ver detalhes" |
| **Regra de cor** | ≤40% capacidade → verde; 41–70% → amarelo; >70% → vermelho |

### Card Próximo Treino
| Elemento | Detalhe |
|---|---|
| Background | `#16213E` com borda esquerda 3px `#FF6B35` |
| Ícone | `fitness_center` — 20px, `#FF6B35` |
| Nome da ficha | Heading 3, `#FFFFFF` |
| Grupos musculares | Body Medium, `#B0B0C0` |
| Contagem exercícios | Body Small, `#555575` |
| Botão CTA | Botão Primário full-width "INICIAR TREINO" |

### Grade de Acesso Rápido (2×2)
| Ação | Ícone | Cor do ícone |
|---|---|---|
| Reservas | `calendar_today` | `#2196F3` |
| Reportar | `report_problem` | `#F44336` |
| Evolução | `bar_chart` | `#4CAF50` |
| Recordes | `emoji_events` | `#FFC107` |

- Cada card: 72×72px, background `#16213E`, border-radius 16px
- Ícone: 28px, centralizado
- Label: Caption, `#B0B0C0`, abaixo do ícone

### Card Última Atividade
| Elemento | Detalhe |
|---|---|
| Background | `#16213E` com opacidade ligeiramente menor |
| Label seção | "ÚLTIMA ATIVIDADE" — Caption, `#555575`, peso Medium |
| Nome treino | Body Large, `#FFFFFF` |
| Data | Body Small, `#B0B0C0` |
| Métricas | "55 min · 6 exercícios" — Body Small, `#B0B0C0` |

---

## Comportamentos Dinâmicos

| Condição | Comportamento da UI |
|---|---|
| Lucas nunca treinou | Card "Próximo Treino" exibe estado vazio com texto "Peça sua ficha ao instrutor" |
| Treino iniciado | Botão "INICIAR TREINO" vira "TREINO EM ANDAMENTO" com spinner |
| Sem conexão | Card de lotação exibe ícone `wifi_off` e texto "Dados offline" |
| Nova notificação | Badge vermelho no sino; ao tocar, expande lista de notificações |
| Dia de descanso detectado | Card "Próximo Treino" exibe "Dia de descanso — bom sono! 😴" |

---

## Personalização por Horário

| Hora | Saudação | Cor de fundo suave |
|---|---|---|
| 05h–11h59 | "Bom dia, Lucas!" | Leve toque azul |
| 12h–17h59 | "Boa tarde, Lucas!" | Neutro |
| 18h–23h59 | "Boa noite, Lucas!" | Leve toque índigo |
