# Tela 01 — Splash & Login

> **Módulo:** Autenticação  
> **Persona — necessidade atendida:** Acesso rápido ao app; Lucas não quer perder tempo com login complicado após um dia de trabalho.

---

## Splash Screen

### Layout

```
┌─────────────────────────┐
│                         │
│                         │
│                         │
│       [LOGO]            │
│    ● FitSync            │
│   Academia de Bairro    │
│                         │
│                         │
│   ━━━━━━━━━━━━━━━━      │  ← progress bar loading (laranja)
│                         │
└─────────────────────────┘
Background: gradiente #1A1A2E → #0F3460 (diagonal)
```

### Especificações

| Elemento | Detalhe |
|---|---|
| Logo | Ícone de haltere estilizado em `#FF6B35`, 80×80px |
| Nome app | "FitSync" — Heading 1, Bold, `#FFFFFF` |
| Subtítulo | "Academia de Bairro" — Body Medium, `#B0B0C0` |
| Progress bar | Largura 120px, altura 3px, cor `#FF6B35`, animação 2s linear |
| Background | Gradiente 135° de `#1A1A2E` para `#0F3460` |
| Duração | 2 segundos → transição automática para Login (Fade 300ms) |

---

## Tela de Login

### Layout

```
┌─────────────────────────┐
│  ←                      │
│                         │
│  [LOGO pequeno]         │
│  Bem-vindo de volta     │
│  Entre na sua conta     │
│                         │
│  ┌─────────────────┐   │
│  │ E-mail           │   │
│  └─────────────────┘   │
│                         │
│  ┌─────────────────┐   │
│  │ Senha        👁  │   │
│  └─────────────────┘   │
│                         │
│       Esqueci a senha   │  ← link texto, alinhado à direita
│                         │
│  ┌─────────────────┐   │
│  │    ENTRAR        │   │  ← botão primário laranja
│  └─────────────────┘   │
│                         │
│  ─────── ou ─────────   │
│                         │
│  ┌─────────────────┐   │
│  │  [G] Google      │   │  ← botão outline
│  └─────────────────┘   │
│                         │
│  Não tem conta?         │
│  Cadastre-se            │  ← link texto laranja
│                         │
└─────────────────────────┘
```

### Especificações

| Elemento | Detalhe |
|---|---|
| Background | `#1A1A2E` sólido |
| Top bar | Sem barra; tela full-screen |
| Logo | 40×40px, canto superior esquerdo (ou centralizado) |
| Título | "Bem-vindo de volta" — Heading 2, `#FFFFFF` |
| Subtítulo | "Entre na sua conta" — Body Large, `#B0B0C0` |
| Campo E-mail | Input Field padrão (ver Design System §5.5) |
| Campo Senha | Input Field + ícone olho para revelar senha |
| Ícone olho | Material Symbol `visibility` / `visibility_off` |
| Link "Esqueci" | Body Small, `#FF6B35`, alinhado à direita |
| Botão Entrar | Botão Primário full-width (ver Design System §5.1) |
| Separador "ou" | Linha `#2A2A4A` com texto Body Small `#555575` |
| Botão Google | Botão Outline full-width, ícone Google SVG |
| Link Cadastro | Body Medium, `#B0B0C0` + `#FF6B35` para "Cadastre-se" |

### Estados de Interação

| Estado | Comportamento |
|---|---|
| Loading (após tap Entrar) | Botão exibe spinner branco; texto some |
| Erro de credencial | Campo fica com borda vermelha + mensagem abaixo |
| Sucesso | Transição Slide Up para Home |
| Campo vazio ao tentar entrar | Shake animation + mensagem de erro inline |

### Decisão de Design
Lucas é um usuário frequente — o app deve suportar **biometria (Face ID / impressão digital)** como atalho de login rápido. Um ícone de impressão digital aparece abaixo do botão "Entrar" após o primeiro login bem-sucedido.

---

## Tela de Cadastro (novo aluno)

### Layout resumido

```
┌─────────────────────────┐
│  ←   Criar conta        │
│                         │
│  Nome completo          │
│  ┌───────────────────┐  │
│  └───────────────────┘  │
│  E-mail                 │
│  ┌───────────────────┐  │
│  └───────────────────┘  │
│  Código da academia     │  ← fornecido pela academia
│  ┌───────────────────┐  │
│  └───────────────────┘  │
│  Senha                  │
│  ┌───────────────────┐  │
│  └───────────────────┘  │
│  Confirmar senha        │
│  ┌───────────────────┐  │
│  └───────────────────┘  │
│                         │
│  ┌─────────────────┐    │
│  │  CRIAR CONTA    │    │
│  └─────────────────┘    │
└─────────────────────────┘
```

> **Nota de segurança:** O campo "Código da academia" vincula o aluno à unidade correta e evita cadastros não autorizados. Esse código é fornecido pessoalmente pela recepção.
