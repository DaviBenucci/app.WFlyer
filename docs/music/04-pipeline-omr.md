# Pipeline OMR para PDF

> Status: canônico para a trilha PDF. Capacidade desabilitada no Core.

## Princípio

PDF não contém, em geral, a estrutura musical necessária para transposição. Mesmo um PDF vetorial deve passar por um processo OMR ou por uma fonte simbólica equivalente. “PDF simples” não elimina essa etapa.

## Pipeline

```text
PDF em quarentena
-> inspeção e limites
-> rasterização controlada
-> pré-processamento de página
-> OMR adapter
-> raw_musicxml
-> normalização canônica
-> validação estrutural
-> transposição do Core
-> validação semântica
-> renderização opcional
```

## Adapter

A integração deve implementar uma interface semelhante a:

```python
class OmrAdapter(Protocol):
    def recognize(self, input_pdf: Path, workdir: Path, limits: OmrLimits) -> OmrResult: ...
```

`OmrResult` contém apenas referências internas, versão do engine, métricas internas, warnings e erro categorizado. Rotas e domínio não importam classes específicas do engine.

## Isolamento

Rasterizador e OMR executam:

- como usuário sem privilégios;
- sem acesso de rede;
- com filesystem raiz somente leitura;
- em diretório temporário exclusivo;
- com limites de CPU, memória, PIDs, arquivos e tempo;
- sem `shell=True`;
- com allowlist de extensões de saída;
- com limpeza garantida após sucesso ou falha.

## Qualidade

O sistema deve medir, no mínimo:

- páginas reconhecidas;
- partes e pautas detectadas;
- medidas e eventos;
- erros estruturais;
- confiança agregada do engine;
- símbolos não reconhecidos;
- divergências após normalização;
- duração por etapa;
- versão do engine e configuração.

Métricas brutas ficam internas. O usuário recebe avisos categóricos e a recomendação de revisão.

## Resultados possíveis

- `completed`: sem warnings relevantes no perfil aprovado;
- `completed_with_warnings`: resultado disponível, mas revisão recomendada;
- `failed`: estrutura não confiável ou fora da matriz;
- `cancelled`: cancelamento solicitado;
- `PROCESSING_LIMIT_EXCEEDED`: documento excede limite determinístico;
- `PROCESSING_TIMEOUT`: condição operacional transitória excedeu o prazo.

## Gate de ativação

`pdf_omr` só pode ser ativado quando:

1. engine e licença forem aprovados;
2. sandbox passar na suíte hostil;
3. corpus representativo estiver versionado;
4. limiares quantitativos forem definidos e atingidos;
5. UX de warnings estiver pronta;
6. falhas não produzirem artefato enganoso;
7. custos e capacidade de fila estiverem medidos.

## Candidato de spike

Audiveris pode ser avaliado porque exporta MusicXML e possui editor/diagnósticos de OMR. A escolha de produção depende de qualidade, automação, licença e operação. A exportação OMR para MusicXML pode perder informação; o raw output deve ser preservado para diagnóstico conforme a política de retenção.

## Revisão assistida

Um editor completo não faz parte do Core. Até existir correção interna, resultados com incerteza devem:

- indicar que a leitura pode conter erros;
- apontar página/medida quando possível sem expor dados internos;
- permitir baixar o MusicXML para revisão externa;
- nunca ser apresentados como “verificados” automaticamente.
