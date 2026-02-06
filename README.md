# 📝 Bot de Redação Automática

Um bot em Python com interface gráfica que escreve automaticamente textos (redações) em qualquer campo de digitação da tela, utilizando automação de teclado e mouse.

---

## 📌 Descrição

Este projeto permite que o usuário:

- Digite uma redação dentro do aplicativo
- Escolha visualmente o local da tela onde o texto será digitado
- Faça o bot alternar de janela e escrever tudo automaticamente

É útil para automatizar a digitação de textos longos em sites, editores online ou aplicativos.

---

## 🚀 Funcionalidades

- Interface gráfica moderna com CustomTkinter
- Campo de texto para escrever a redação
- Acesso rápido ao ChatGPT e QuillBot
- Seleção visual do local de digitação (mira)
- Escrita automática simulando teclado
- Compatível com qualquer campo de texto da tela

---

## 🛠️ Tecnologias utilizadas

- Python 3
- CustomTkinter
- Tkinter
- PyAutoGUI
- Webbrowser

---

## 📦 Instalação

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

**📖 Como usar**

**1️⃣Abra o aplicativo e digite ou cole o texto no campo de redação.**

**2️⃣ Selecionar o local de digitação**

Clique em "local de digitação"
Uma janela com uma mira vermelha aparecerá
Posicione a mira exatamente sobre o campo onde deseja escrever
Clique em CONFIRMAR

**3️⃣ Escrever automaticamente**

Abra o site ou aplicativo onde o texto será digitado
Clique em "Escrever Redação"

O bot irá:
Alternar de janela (Alt + Tab)
Clicar no local selecionado
Digitar todo o texto automaticamente

**⚠️ Avisos importantes**

Não mexa no mouse ou teclado enquanto o bot estiver escrevendo
Se a resolução da tela mudar, selecione o local novamente
Textos grandes podem levar alguns segundos para concluir
Use com responsabilidade

**🧠 Detalhes técnicos**

A digitação é feita com pyautogui.write()
Intervalo entre teclas configurado em 0.01
Coordenadas capturadas em pixels reais da tela
Interface acompanha o tema do sistema (claro/escuro)

**💡 Possíveis melhorias futuras**

Ajuste manual da velocidade de digitação
Salvamento automático das coordenadas
Conversão para executável (.exe)
Versão mobile / Android
Perfis diferentes de escrita

**📄 Licença**

Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e distribuir.

**❤️ Autor**

Projeto feito com Python, automação e curiosidade.

__Se gostou, deixe uma ⭐ no repositório!__
