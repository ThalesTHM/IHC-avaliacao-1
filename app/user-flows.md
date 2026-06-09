# Fluxos de Usuário — FitSync

> Mapeamento das jornadas do usuário (User Flows) e navegação entre telas.  
> Persona base: **Lucas Oliveira Silva**, 25 anos, treino noturno, foco em hipertrofia.

---

## 1. Arquitetura de Informação

```
FitSync
├── Autenticação
│   ├── Splash Screen
│   ├── Login
│   └── Cadastro (novo aluno)
│
├── Home (Dashboard)              ← ponto central pós-login
│
├── Módulo 1 — Ocupação
│   ├── Visualização em tempo real
│   └── Histórico de lotação por horário
│
├── Módulo 2 — Ficha de Treino
│   ├── Lista de fichas
│   ├── Ficha ativa (séries e cargas)
│   └── Detalhe do exercício (vídeo + instruções)
│
├── Módulo 3 — Reservas
│   ├── Lista de equipamentos disponíveis
│   ├── Fila virtual de equipamento
│   └── Confirmação de reserva
│
├── Módulo 4 — Feedback
│   ├── Lista de reportes abertos
│   ├── Criar novo reporte
│   └── Status do reporte
│
└── Módulo 5 — Histórico & Perfil
    ├── Perfil do usuário
    ├── Histórico de evolução de cargas
    └── Frequência e metas
```

---

## 2. Navegação Principal

### Bottom Navigation Bar (5 itens)

```
[  Home  ]  [ Treino ]  [ Lotação ]  [ Reservas ]  [ Perfil ]
  🏠           💪          👥           📅            👤
```

A barra de navegação inferior está **sempre visível** após o login, exceto em:
- Tela de splash/login
- Modal de detalhe de exercício (foco total)
- Fluxo de criação de reporte (tela cheia)

---

## 3. Fluxos Principais

### Fluxo A — Primeiro Acesso (Onboarding)

```
[Splash]
    ↓ (2s autoplay)
[Login / Cadastro]
    ↓ (credenciais válidas)
[Onboarding 1] → "Verifique a lotação antes de sair"
    ↓ swipe
[Onboarding 2] → "Sua ficha de treino no bolso"
    ↓ swipe
[Onboarding 3] → "Reserve aparelhos com antecedência"
    ↓ tap "Começar"
[Home Dashboard]
```

---

### Fluxo B — Verificar Lotação (Uso mais frequente de Lucas)

**Gatilho:** Lucas está em casa às 17h30 e quer saber se vale ir agora ou esperar.

```
[Home]
    ↓ tap no card "Lotação Atual" ou ícone na Bottom Nav
[Ocupação — Tempo Real]
    ↓ vê lotação ALTA (vermelho) → decide esperar
    ↓ tap em "Ver horários menos cheios"
[Histórico de Lotação por Horário]
    ↓ identifica que 20h30 é mais tranquilo
    ↓ tap "Definir lembrete para 20h00"
[Toast: "Lembrete definido para 20:00 ✓"]
    ↓ volta para Home (botão voltar ou nav)
[Home]
```

---

### Fluxo C — Treino Ativo (Uso diário de Lucas)

**Gatilho:** Lucas chegou na academia e vai iniciar o treino.

```
[Home]
    ↓ tap em "Iniciar Treino" (CTA principal)
[Ficha de Treino — Lista]
    ↓ tap na ficha "Treino A — Peito/Tríceps"
[Ficha Ativa]
    ↓ vê exercício 1: "Supino Reto — 4x10 — 60kg"
    ↓ tap em "▶ Ver execução"
[Modal: Vídeo do Exercício]
    ↓ assiste 30s, tap "X" fechar
[Ficha Ativa]
    ↓ registra série 1: tap nos círculos de série
    ↓ registra carga: tap no campo "60 kg" → edita
    ↓ repete para séries 2, 3, 4
    ↓ tap "Próximo exercício ›"
    ... (repete para todos os exercícios)
    ↓ tap "Finalizar Treino"
[Modal: "Treino concluído! Duração: 55min" + confete]
    ↓ tap "Ver resumo"
[Histórico — Resumo do Treino]
    ↓ tap "Voltar para Home"
[Home]
```

---

### Fluxo D — Reservar Equipamento

**Gatilho:** Lucas quer garantir o Leg Press sem esperar na fila.

```
[Home] ou [Bottom Nav → Reservas]
    ↓
[Lista de Equipamentos]
    ↓ vê "Leg Press — 3 na fila" (badge laranja)
    ↓ tap em "Leg Press"
[Detalhe do Equipamento + Fila]
    ↓ vê posição atual na fila e tempo estimado
    ↓ tap "Entrar na Fila"
[Toast: "Você é o #4 na fila. Tempo estimado: 18 min"]
    ↓ notificação push quando chegar a vez dele
[Notificação: "Sua vez no Leg Press! Você tem 3 min"]
    ↓ tap na notificação
[Confirmação: "Confirmar uso?"]
    ↓ tap "Confirmar"
[Toast: "Leg Press reservado por 20 min ✓"]
```

---

### Fluxo E — Reportar Problema

**Gatilho:** Lucas percebe que o estofado do banco do supino está rasgado.

```
[Home] ou [qualquer tela → ícone de alerta no canto]
    ↓
[Feedback & Manutenção — Lista de reportes]
    ↓ tap "Novo Reporte" (FAB laranja)
[Criar Reporte]
    ↓ seleciona categoria: "Equipamento danificado"
    ↓ seleciona equipamento: "Banco de Supino Reto"
    ↓ preenche descrição: "Estofado rasgado no encosto"
    ↓ (opcional) tira foto com câmera
    ↓ tap "Enviar Reporte"
[Toast: "Reporte enviado! Protocolo #1247"]
    ↓ redireciona para lista com novo item "Em análise"
[Feedback — Lista]
```

---

### Fluxo F — Ver Evolução de Cargas

**Gatilho:** Lucas quer saber se está evoluindo no Supino ao longo do mês.

```
[Bottom Nav → Perfil]
    ↓
[Perfil do Usuário]
    ↓ tap em "Ver Histórico Completo"
[Histórico de Evolução]
    ↓ tab "Cargas" ativo por padrão
    ↓ seleciona exercício: "Supino Reto"
[Gráfico de evolução de carga — linha temporal]
    ↓ tap em ponto do gráfico → tooltip com data e valor
    ↓ swipe para tab "Frequência"
[Gráfico de frequência semanal — barras]
    ↓ swipe para tab "Recordes"
[Lista de PRs (Personal Records)]
```

---

## 4. Mapa de Transições

| De | Para | Gatilho | Tipo de Transição |
|---|---|---|---|
| Splash | Login | Auto (2s) | Fade |
| Login | Home | Submit válido | Slide up |
| Home | Ocupação | Tap card / bottom nav | Slide right |
| Home | Ficha Ativa | Tap "Iniciar Treino" | Slide right |
| Home | Reservas | Bottom nav | Slide right |
| Home | Perfil | Bottom nav | Slide right |
| Ficha Lista | Ficha Ativa | Tap ficha | Slide right |
| Ficha Ativa | Modal Vídeo | Tap "Ver execução" | Slide up (sheet) |
| Qualquer | Novo Reporte | FAB / ícone alerta | Slide up (full) |
| Ficha Ativa | Resumo | Tap "Finalizar" | Slide up |

---

## 5. Estados de Erro e Casos Extremos

| Situação | Comportamento |
|---|---|
| Sem internet ao abrir o app | Banner "Sem conexão — dados podem estar desatualizados" |
| Lotação indisponível | Card cinza com "Dados não disponíveis agora" |
| Treino sem exercícios na ficha | Estado vazio com CTA "Pedir nova ficha ao instrutor" |
| Fila cheia (>10 na fila) | Botão "Entrar na fila" desabilitado + sugestão de horário alternativo |
| Reporte com foto > 10MB | Toast de erro + instrução para tirar foto menor |
