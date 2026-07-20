# Testes E2E

## Ferramenta

Playwright ou equivalente, contra API/banco/Redis/storage de teste reais. Engines musicais podem usar fixtures determinísticas, mas o fluxo HTTP não deve ser inteiramente mockado no gate principal.

## Fluxos Core

### Sucesso MusicXML

```text
abrir /
-> iniciar /transpor
-> enviar fixture suportada
-> escolher Piano e Trompete Bb
-> revisar M2/+2
-> criar job
-> observar queued/running
-> abrir resultado
-> baixar MusicXML
-> conferir nome/tipo e presença no histórico
```

### Oitava

Piano -> Sax tenor deve mostrar nona maior/+14 e produzir fixture semanticamente correta.

### Warning

Job termina `completed_with_warnings`; tela mostra warning antes do download.

### Erros

- XML não MusicXML;
- multiparte/multipauta;
- origem divergente do `<transpose>`;
- rate limit;
- worker falha;
- perda transitória de rede;
- job cancelado;
- artefato expirado.

### Autorização

Dois contextos de navegador: B não acessa URL/IDs de A. Apagar cookies de A torna o histórico local insuficiente para acesso.

### Retenção/deleção

- limpar histórico não apaga servidor;
- apagar servidor bloqueia download;
- relógio avançado expira e depois purga.

## UX/acessibilidade

- viewport mobile, tablet, desktop e wide selecionados;
- PublicShell, StudioShell e UtilityShell corretos;
- fluxo por teclado;
- foco não encoberto por navigation/action bar;
- bottom nav e inspector responsivos;
- reduced motion e forced colors quando suportado;
- conteúdo longo e múltiplos warnings;
- sem violações críticas automatizadas;
- sem erro inesperado de console/rede;
- diff visual revisado nas páginas principais.

## PDF

Nenhum E2E do Core presume PDF. A trilha PDF possui suíte separada e só roda quando a capability está ativa.

## Fluxos avançados condicionais

### Polifônico para monofônico

```text
upload de teclado -> destino flauta
-> Transpor todas bloqueado
-> Extrair melodia
-> revisar duas frases ambíguas
-> confirmar
-> reduzir/transpor
-> resultado com provenance e garantia
```

### Harmonização

```text
melodia confirmada
-> escolher perfil modal/popular
-> gerar variantes
-> comparar
-> escolher uma
-> baixar melodia e proposta harmonizada
```

### Watermark

PDF final mostra token discreto, verificação por hash funciona e edição invalida assinatura.

Esses E2E só entram quando a capability correspondente estiver ativa.
