# Design System — FitSync

> Guia de identidade visual e componentes reutilizáveis do app FitSync.  
> Todas as telas devem referenciar este documento para consistência visual.

---

## 1. Paleta de Cores

### Cores Primárias

| Nome | HEX | Uso |
|---|---|---|
| **Brand Orange** | `#FF6B35` | CTAs principais, destaque, ícones ativos |
| **Brand Dark** | `#1A1A2E` | Background principal (dark mode) |
| **Surface Dark** | `#16213E` | Cards e superfícies elevadas |
| **Surface Mid** | `#0F3460` | Bordas, separadores, elementos secundários |

### Cores Neutras

| Nome | HEX | Uso |
|---|---|---|
| **Text Primary** | `#FFFFFF` | Textos principais |
| **Text Secondary** | `#B0B0C0` | Textos secundários, labels, placeholders |
| **Text Disabled** | `#555575` | Estados desabilitados |
| **Divider** | `#2A2A4A` | Linhas divisórias |

### Cores Semânticas

| Nome | HEX | Uso |
|---|---|---|
| **Success Green** | `#4CAF50` | Confirmações, ocupação baixa, check |
| **Warning Yellow** | `#FFC107` | Ocupação média, alertas moderados |
| **Error Red** | `#F44336` | Erros, ocupação alta, problemas críticos |
| **Info Blue** | `#2196F3` | Informações neutras, dicas |

---

## 2. Tipografia

**Fonte principal:** `Inter` (Google Fonts — licença open source)  
**Fonte alternativa:** `Roboto`

| Estilo | Tamanho | Peso | Uso |
|---|---|---|---|
| **Heading 1** | 28sp | Bold (700) | Títulos de tela |
| **Heading 2** | 22sp | SemiBold (600) | Títulos de seção |
| **Heading 3** | 18sp | SemiBold (600) | Subtítulos, card headers |
| **Body Large** | 16sp | Regular (400) | Texto de corpo principal |
| **Body Medium** | 14sp | Regular (400) | Listas, descrições |
| **Body Small** | 12sp | Regular (400) | Labels, captions |
| **Caption** | 10sp | Medium (500) | Timestamps, badges |
| **Button** | 14sp | Bold (700) | Rótulos de botões |

---

## 3. Espaçamento (Grid)

- **Grid base:** 8px
- **Margem lateral da tela:** 16px
- **Gutter entre cards:** 12px
- **Padding interno de card:** 16px
- **Padding interno de botão:** 12px vertical / 24px horizontal

| Token | Valor |
|---|---|
| `space-xs` | 4px |
| `space-sm` | 8px |
| `space-md` | 16px |
| `space-lg` | 24px |
| `space-xl` | 32px |
| `space-2xl` | 48px |

---

## 4. Bordas e Sombras

| Elemento | Border-radius | Sombra |
|---|---|---|
| Cards principais | 16px | `0 4px 20px rgba(0,0,0,0.4)` |
| Cards secundários | 12px | `0 2px 10px rgba(0,0,0,0.3)` |
| Botões primários | 12px | `0 4px 15px rgba(255,107,53,0.4)` |
| Botões secundários | 12px | nenhuma |
| Chips / Tags | 20px (pill) | nenhuma |
| Bottom Nav | 0px (top) / 0px | `0 -2px 10px rgba(0,0,0,0.3)` |

---

## 5. Componentes

### 5.1 Botão Primário (CTA)
- Background: `#FF6B35`
- Texto: `#FFFFFF`, peso Bold
- Border-radius: 12px
- Altura: 52px
- Largura: 100% (full-width) ou mínimo 160px
- Estado hover/pressed: `#E55A2B` (10% mais escuro)
- Estado disabled: `#555575` background, `#333350` texto

### 5.2 Botão Secundário (Outline)
- Background: transparente
- Borda: 1.5px sólida `#FF6B35`
- Texto: `#FF6B35`
- Demais parâmetros idênticos ao primário

### 5.3 Botão Ghost (Texto)
- Background: transparente
- Texto: `#B0B0C0`
- Sem borda

### 5.4 Card Base
```
Background:     #16213E
Border-radius:  16px
Padding:        16px
Shadow:         0 4px 20px rgba(0,0,0,0.4)
```

### 5.5 Input Field
- Background: `#0F3460`
- Borda: 1px `#2A2A4A` (idle) / `#FF6B35` (focus)
- Border-radius: 10px
- Padding: 14px 16px
- Texto: `#FFFFFF`
- Placeholder: `#555575`
- Label acima do campo: `#B0B0C0`, 12sp

### 5.6 Barra de Progresso
- Background track: `#2A2A4A`
- Fill: gradiente `#FF6B35` → `#FF8C5A`
- Altura: 8px
- Border-radius: 4px

### 5.7 Badge / Chip
- Variante Success: background `rgba(76,175,80,0.2)`, texto `#4CAF50`
- Variante Warning: background `rgba(255,193,7,0.2)`, texto `#FFC107`
- Variante Error: background `rgba(244,67,54,0.2)`, texto `#F44336`
- Border-radius: 20px (pill)
- Padding: 4px 12px

### 5.8 Bottom Navigation Bar
- Background: `#16213E`
- Shadow: `0 -2px 10px rgba(0,0,0,0.3)`
- Ícone ativo: `#FF6B35` + label colorida
- Ícone inativo: `#555575`
- Altura: 64px
- 5 itens: Home · Treino · Lotação · Reservas · Perfil

### 5.9 Top App Bar
- Background: `#1A1A2E` (transparente com blur em algumas telas)
- Altura: 56px
- Título: Heading 3, centralizado
- Ação esquerda: ícone voltar ou menu
- Ação direita: ícone contextual (notificação, ajuda etc.)

### 5.10 Toast / Snackbar
- Background: `#2A2A4A`
- Texto: `#FFFFFF`, Body Medium
- Border-radius: 10px
- Posição: bottom center, 16px acima da bottom nav
- Ícone opcional à esquerda (semântico)
- Duração: 3 segundos

---

## 6. Iconografia

- **Biblioteca:** Material Symbols (Google) — variante Rounded, peso 400
- **Tamanho padrão:** 24px
- **Cor ativa:** `#FF6B35`
- **Cor inativa:** `#555575`

### Ícones por módulo

| Módulo | Ícone Material |
|---|---|
| Home | `home` |
| Ficha de Treino | `fitness_center` |
| Ocupação | `groups` |
| Reservas | `calendar_today` |
| Perfil | `person` |
| Histórico | `bar_chart` |
| Feedback | `report_problem` |
| Notificação | `notifications` |
| Check / Concluído | `check_circle` |
| Adicionar | `add_circle` |
| Vídeo | `play_circle` |
| Cadeado | `lock` |

---

## 7. Motion & Animações

| Tipo | Duração | Easing | Uso |
|---|---|---|---|
| Transição de tela | 300ms | ease-in-out | Push entre telas |
| Fade de modal | 200ms | ease-out | Bottom sheets, diálogos |
| Tap ripple | 150ms | ease-out | Feedback de toque |
| Loading spinner | loop | linear | Estados de carregamento |
| Progress bar fill | 600ms | ease-out | Carregamento de dados |
| Toast aparece | 250ms | spring | Animação de entrada |

---

## 8. Acessibilidade

- **Contraste mínimo:** 4.5:1 (WCAG AA) para texto normal; 3:1 para texto grande
- **Área de toque mínima:** 44×44px para todos os elementos interativos
- **Rótulos de acessibilidade:** todos os ícones devem ter `contentDescription`
- **Modo de alto contraste:** suportado via trocas de cor
- **Tamanho de fonte:** respeitar configurações de acessibilidade do sistema operacional
