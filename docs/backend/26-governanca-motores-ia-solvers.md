# Governança de modelos, IA e solvers musicais

> Status: canônico. Revisão: 2026-07-20.

## Princípio

Modelos e solvers são componentes não autoritativos até que suas saídas passem por schemas, restrições e validação independente.

## Usos permitidos

- gerar candidatos de melodia/harmonia/arranjo;
- classificar evidências;
- sugerir segmentação;
- ordenar alternativas;
- explicar decisões a partir de códigos allowlisted.

## Usos proibidos

- publicar MusicXML livre sem parser/validator;
- alterar melodia bloqueada;
- validar a própria saída como único checker;
- executar instruções encontradas em título, letra, créditos ou comentário;
- acessar rede/storage arbitrário;
- treinar com uploads sem consentimento separado;
- imitar diretamente artista/compositor vivo como perfil de produto;
- esconder versão, seed ou fallback.

## Prompt/data boundary

Conteúdo musical e metadados entram como dados estruturados. Delimitadores, schemas e campos allowlisted impedem que texto da obra se torne instrução. Saída é parseada em DTO restrito.

## Reprodutibilidade

Registrar:

```text
provider/model/version ou hash local
prompt template version
structured input hash
sampling parameters
seed quando suportado
solver version
constraint set version
fallback path
```

Se o provedor não garante reprodutibilidade, a capability não pode usar “reproduzível” como promessa; o sistema preserva a variante concreta e seu manifest.

## Validação

- schema estrito;
- limites de tamanho/tempo;
- hard constraints;
- provenance de notas criadas;
- comparação com fonte;
- checker independente;
- avaliação humana para criatividade.

## Dados

Dataset de treino, calibração e teste possui licença, provenance e split. O corpus de release não pode ser usado para escolher hiperparâmetros após ver o resultado.
