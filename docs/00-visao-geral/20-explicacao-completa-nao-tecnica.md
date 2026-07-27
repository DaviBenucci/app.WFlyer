# W_Flyer explicado para quem não é programador

> Status: referência. Revisão: 2026-07-27.  
> Público: músicos, professores, maestros, gestores, parceiros, clientes e demais pessoas que desejam compreender a aplicação sem precisar conhecer programação.

## 1. O que é o W_Flyer

O W_Flyer será uma aplicação web criada para ajudar músicos a preparar partituras para instrumentos diferentes com mais segurança, clareza e controle.

Em sua primeira versão, o foco será a **transposição de partituras**. Transpor significa reescrever uma música para outro instrumento ou outra afinação, preservando o som musical correto.

Um exemplo simples:

- uma partitura foi escrita para piano, que é um instrumento em Dó;
- o músico deseja tocá-la em um trompete em Si bemol;
- o W_Flyer recebe a partitura, identifica sua estrutura musical e cria uma nova versão escrita corretamente para o trompete;
- mesmo que as notas escritas sejam diferentes, a música deve soar na altura esperada quando cada instrumento tocar sua própria parte.

A proposta não é apenas “mover notas para cima ou para baixo”. O sistema deverá preservar elementos importantes da obra, verificar o resultado e explicar o que foi alterado.

## 2. Qual problema a aplicação pretende resolver

A transposição manual pode exigir tempo, conhecimento de teoria musical e muita atenção. Um erro pequeno pode alterar:

- a nota que será tocada;
- a tonalidade da música;
- a oitava;
- a armadura de clave;
- um acidente musical;
- a relação entre a parte escrita e o som real do instrumento.

Esses erros podem passar despercebidos até o ensaio ou a apresentação.

O W_Flyer pretende reduzir esse trabalho repetitivo e oferecer uma forma mais segura de preparar material para:

- estudantes;
- professores de música;
- instrumentistas;
- bandas;
- igrejas;
- escolas;
- grupos de sopros;
- pequenos conjuntos;
- arranjadores;
- maestros.

O valor principal da aplicação será a **confiança no processo**, e não apenas a velocidade.

## 3. O que a primeira versão fará

A primeira versão funcional será chamada de **MVP Core MusicXML**.

Ela aceitará uma partitura digital estruturada no formato MusicXML. Esse formato não é apenas uma imagem da partitura: ele contém informações musicais organizadas, como notas, compassos, vozes, tonalidades e durações.

O fluxo inicial será:

```text
Enviar uma partitura MusicXML
→ escolher o instrumento de origem
→ escolher o instrumento de destino
→ confirmar a operação
→ aguardar o processamento
→ receber o resultado verificado
→ baixar a nova partitura em MusicXML
```

A primeira versão deverá trabalhar com um perfil controlado:

- uma parte instrumental por arquivo;
- uma pauta;
- instrumentos com notas definidas;
- sistema musical tradicional de doze semitons;
- notas, pausas, acordes escritos, vozes, ligaduras e quiálteras dentro do perfil suportado;
- mudanças de clave, compasso e tonalidade dentro da mesma parte.

Esse limite inicial existe para que o núcleo seja construído e testado com seriedade antes de aceitar partituras mais complexas.

## 4. O que não estará disponível no primeiro lançamento

Algumas funções já estão planejadas, mas não serão ativadas apenas porque aparecem na documentação.

No primeiro núcleo, não estarão disponíveis:

- leitura automática de PDF ou fotografia da partitura;
- reconhecimento de partitura manuscrita;
- escolha automática da melodia principal em uma partitura de piano complexa;
- harmonização automática;
- criação de arranjos completos;
- geração de partes para uma banda inteira;
- reprodução de áudio comparativa;
- modo de ensaio;
- marca d'água em PDF;
- colaboração entre vários usuários;
- pagamentos ou planos comerciais.

Essas funções serão adicionadas em etapas posteriores, somente depois de testes próprios e aprovação dos critérios de confiabilidade de cada uma.

## 5. Como uma pessoa usará a aplicação

### 5.1 Entrada na aplicação

Ao abrir o W_Flyer, o usuário verá uma interface com identidade musical, mas sem excesso de efeitos ou aparência de painel administrativo genérico.

A página deverá explicar de maneira direta:

- o que pode ser enviado;
- o que a aplicação fará;
- quais são os limites atuais;
- como o resultado será verificado.

Uma animação curta poderá apresentar a ideia de transposição: a “tinta” das notas se deslocará de uma partitura de origem para uma partitura de destino. Essa animação será decorativa e explicativa; ela não poderá atrasar o acesso ao conteúdo nem dificultar o uso da página.

### 5.2 Envio do arquivo

O usuário escolherá um arquivo MusicXML válido.

Antes de aceitar o arquivo, o W_Flyer verificará:

- se o arquivo não está vazio;
- se o tamanho está dentro do limite;
- se o formato declarado corresponde ao conteúdo real;
- se a estrutura musical pertence ao perfil que a versão atual suporta;
- se o arquivo apresenta sinais de conteúdo perigoso ou inválido.

Se houver um problema, a aplicação deverá explicar claramente o motivo. Ela não deverá responder apenas com uma mensagem vaga como “algo deu errado”.

### 5.3 Escolha dos instrumentos

O usuário informará:

- para qual instrumento a partitura atual foi escrita;
- para qual instrumento deseja gerar a nova versão.

A aplicação mostrará o caminho da transformação, por exemplo:

```text
Piano em Dó
→ segunda maior acima
→ Trompete em Si bemol
```

O usuário não precisará calcular o intervalo. O próprio sistema fará isso com base no catálogo de instrumentos.

### 5.4 Confirmação

Antes de iniciar, a aplicação apresentará um resumo:

- arquivo selecionado;
- instrumento de origem;
- instrumento de destino;
- tipo de operação;
- formato de saída;
- possíveis limitações encontradas.

O usuário poderá revisar essas informações antes de continuar.

### 5.5 Processamento

O processamento ocorrerá em etapas. A tela poderá indicar estados reais, como:

```text
Validando o arquivo
Normalizando a estrutura musical
Calculando a transposição
Verificando o resultado
Preparando o arquivo de saída
```

Essas mensagens deverão representar o que o sistema realmente está fazendo. Não serão usadas barras de progresso falsas apenas para produzir uma sensação de atividade.

### 5.6 Resultado

Quando a operação terminar, o usuário verá:

- se a transposição foi concluída;
- qual nível de verificação foi alcançado;
- avisos que precisam ser conhecidos;
- o arquivo disponível para download;
- a data de expiração do resultado.

No futuro, uma tela de comparação poderá destacar nota por nota o que mudou entre a origem e o resultado.

## 6. O que acontece por trás da tela

Embora o usuário veja um processo simples, o W_Flyer executará várias verificações.

De forma não técnica, o funcionamento será semelhante a este:

```text
1. Receber o arquivo em uma área protegida.
2. Conferir se ele é válido e seguro.
3. Ler sua estrutura musical.
4. Organizar as informações em um modelo interno.
5. Calcular como a escrita deve mudar entre os instrumentos.
6. Reescrever as notas, tonalidades e acidentes necessários.
7. Conferir o resultado com um verificador separado.
8. Salvar o arquivo final somente se os controles forem aprovados.
9. Liberar o download para a mesma sessão que enviou o arquivo.
```

O componente que transforma a partitura não será o único responsável por dizer que ela está correta. Um segundo componente verificará o resultado de forma independente.

## 7. O significado de “resultado verificado”

O W_Flyer não deverá usar a palavra “verificado” como um termo de marketing.

Um resultado somente receberá essa indicação quando tiver passado pelos testes previstos para aquela operação.

Na transposição exata, o sistema deverá verificar, entre outros pontos:

- se a altura de concerto foi preservada;
- se nenhuma nota desapareceu sem motivo;
- se a duração das notas e pausas permaneceu coerente;
- se os compassos foram preservados;
- se a nova grafia musical corresponde ao intervalo correto;
- se a armadura de clave foi tratada corretamente;
- se as informações do instrumento de destino foram registradas;
- se o arquivo de saída pode ser lido novamente sem erro.

Se o sistema não conseguir provar uma decisão importante, ele não deverá escolher uma alternativa silenciosamente.

O comportamento correto será um destes:

- pedir confirmação ao usuário;
- apresentar alternativas;
- interromper o processamento;
- informar que aquela partitura ainda não é suportada.

## 8. A aplicação não promete acertar tudo automaticamente

Nenhuma aplicação de leitura ou transformação musical consegue garantir que qualquer arquivo, de qualquer origem e complexidade, será entendido sem erro.

Por isso, a promessa do W_Flyer será cuidadosa:

> Todo resultado que o sistema apresentar como verificado deverá ter passado pelos controles definidos para aquela operação.

Isso não significa que todos os arquivos serão aceitos. Em alguns casos, a decisão mais segura será recusar a operação ou pedir revisão humana.

Essa postura é mais útil do que entregar rapidamente uma partitura possivelmente incorreta.

## 9. Diferença entre transpor, extrair melodia, harmonizar e arranjar

Essas funções são diferentes e não poderão ser misturadas.

### 9.1 Transpor

Transpor significa reescrever as mesmas informações musicais para outra afinação.

A aplicação não cria uma nova música e não escolhe qual voz é mais importante. Ela preserva as notas e muda sua escrita de acordo com o instrumento.

### 9.2 Extrair a melodia

Uma partitura de piano ou teclado pode ter várias notas ao mesmo tempo. Para transformar esse material em uma parte de flauta, por exemplo, não basta transpor tudo, porque a flauta normalmente toca uma nota por vez.

Nesse caso, uma função futura deverá descobrir qual linha representa a melodia principal.

A melodia nem sempre é:

- a nota mais aguda;
- a mão direita;
- a clave de Sol;
- a voz com maior volume.

Ela pode passar de uma pauta para outra, aparecer em uma voz interna ou ser dividida entre frases diferentes.

Por isso, o sistema apresentará candidatos e solicitará ajuda do músico quando houver dúvida.

### 9.3 Harmonizar

Harmonizar significa acrescentar acordes ou outras vozes a uma melodia.

Essa função cria material novo. Portanto, uma harmonização não poderá receber o mesmo tipo de garantia de uma transposição exata.

O usuário poderá escolher parâmetros como:

- linguagem tonal, popular, modal ou jazz leve;
- densidade da harmonia;
- nível de tensão;
- ritmo das trocas de acordes;
- grau de fidelidade à obra original.

A aplicação deverá preservar a melodia escolhida e apresentar diferentes versões para comparação.

### 9.4 Adaptar ou arranjar para um instrumento

Uma música pode estar correta em termos de notas e ainda ser desconfortável ou pouco natural para determinado instrumento.

Uma adaptação futura poderá observar:

- extensão confortável;
- necessidade de respiração;
- abertura de acordes;
- dedilhado;
- resistência do músico;
- articulação;
- velocidade;
- registro e projeção sonora.

Essa função deverá sugerir alternativas, e não alterar a obra sem autorização.

## 10. Como o W_Flyer tratará partituras complexas

Partituras complexas exigem decisões que nem sempre têm uma única resposta correta.

Exemplos:

- piano com várias vozes;
- melodia escondida no meio dos acordes;
- contracanto que se torna melodia em outra seção;
- acordes impossíveis no instrumento de destino;
- mudança de instrumento no meio da partitura;
- várias partes no mesmo arquivo;
- escrita microtonal;
- percussão sem altura definida;
- notação contemporânea ou experimental.

O W_Flyer deverá identificar a complexidade antes de prometer um resultado.

As capacidades serão ativadas por etapas. Cada expansão exigirá:

- exemplos musicais de teste;
- casos válidos e inválidos;
- revisão por músicos;
- critérios claros de aprovação;
- possibilidade de desativação rápida caso seja encontrado um problema grave.

## 11. Experiência visual da aplicação

A interface será inspirada em um **estúdio de preparação musical**, não em um painel empresarial comum.

A direção visual prevê:

- superfícies claras e levemente quentes, próximas ao papel;
- texto com aparência de tinta, evitando preto excessivamente duro;
- violeta e azul usados com moderação;
- espaço amplo para a partitura;
- painel lateral para as escolhas da operação;
- elementos visuais que representem origem, intervalo e destino;
- divisores que lembrem barras de compasso;
- animações curtas ligadas a ações reais do usuário.

A aplicação evitará:

- excesso de cards iguais;
- títulos genéricos em gradiente;
- efeitos brilhantes sem função;
- notas flutuando continuamente;
- textos exagerados sobre “revolucionar a música com IA”;
- números ou depoimentos inventados;
- aparência padrão de um modelo pronto.

A identidade deverá vir das tarefas musicais reais: partitura, instrumentos, comparação, revisão, tocabilidade e ensaio.

## 12. Animações e respostas às ações do usuário

As animações deverão ajudar a explicar mudanças e confirmar ações.

Exemplos:

- instrumento selecionado reagindo de forma sutil;
- linha visual mostrando a passagem da origem para o destino;
- etapas do processamento sendo atualizadas;
- notas de origem e resultado sendo destacadas em uma comparação;
- animação “Ink Transfer”, na qual a tinta se desloca entre duas pautas.

As animações não poderão:

- esconder informações importantes;
- impedir o uso por teclado;
- causar desconforto em pessoas sensíveis a movimento;
- ser obrigatórias para compreender a página;
- manter o computador ocupado sem necessidade.

Quem utiliza a opção de redução de movimento receberá uma versão estática ou mais discreta.

## 13. Privacidade e proteção dos arquivos

As partituras enviadas serão tratadas como arquivos privados.

A aplicação deverá:

- armazenar os arquivos em área não pública;
- permitir o acesso apenas à sessão que os enviou;
- usar links de download controlados;
- remover os arquivos depois do período de retenção;
- evitar colocar nomes, e-mails ou segredos nos registros técnicos;
- impedir que arquivos de um usuário sejam acessados por outro;
- não usar partituras para treinar modelos sem autorização clara.

Na primeira versão, o usuário poderá usar uma sessão anônima. Isso significa que não será necessário criar uma conta para executar o fluxo básico, mas a sessão ainda terá um identificador privado no navegador.

## 14. Marca d'água e rastreabilidade futura

Quando a geração de PDF for ativada, a aplicação poderá aplicar uma marca d'água discreta.

A marca deverá:

- não atrapalhar a leitura da pauta;
- não cobrir notas, acidentes, letras ou dinâmicas;
- usar um código de rastreabilidade, sem expor dados pessoais;
- aparecer em posições planejadas para dificultar uma remoção simples;
- ser combinada com informações de integridade do arquivo.

Nenhuma marca visual é impossível de remover. Por isso, a proteção será formada por várias camadas:

- marca visível;
- código do documento;
- registro do arquivo gerado;
- verificação de integridade;
- assinatura digital quando a tecnologia estiver habilitada.

A marca do W_Flyer não poderá afirmar que a aplicação é dona da composição ou apagar créditos do autor, arranjador ou editor.

## 15. Histórico e duração dos resultados

Os arquivos não ficarão armazenados para sempre por padrão.

Cada resultado terá uma data de expiração. Antes dela, o usuário poderá baixar os arquivos gerados. Depois da expiração, o W_Flyer deverá informar que o resultado foi removido.

Um histórico local poderá ajudar o navegador a lembrar operações recentes, mas não deverá fingir que um arquivo expirado ainda existe no servidor.

Contas permanentes, bibliotecas em nuvem e colaboração são funções futuras e dependerão de regras adicionais de acesso e privacidade.

## 16. Diferenciais planejados

Depois que o núcleo estiver confiável, o W_Flyer poderá oferecer recursos de maior valor musical.

### 16.1 Comparação musical

O usuário poderá clicar em uma nota do resultado e descobrir:

- de qual nota original ela veio;
- qual intervalo foi aplicado;
- se houve mudança de oitava;
- por que a grafia foi escolhida;
- qual regra ou versão do motor produziu a mudança.

### 16.2 Verificador de tocabilidade

A aplicação poderá apontar:

- notas fora da extensão;
- regiões desconfortáveis;
- frases longas para instrumentos de sopro;
- acordes difíceis ou impossíveis;
- saltos e mudanças de registro exigentes.

### 16.3 Audição comparativa

O músico poderá ouvir:

- a versão original;
- a versão transformada;
- uma comparação alternada;
- uma frase em repetição;
- melodia e harmonia separadamente.

### 16.4 Modo de ensaio

Poderá incluir:

- cursor acompanhando a partitura;
- contagem de entrada;
- metrônomo;
- alteração de velocidade sem mudar a altura;
- repetição por compasso ou frase;
- anotações;
- passagem de página;
- tela simplificada para performance.

### 16.5 Pacote para grupos

Uma versão futura poderá receber uma música e produzir:

- partitura do maestro;
- partes para cada instrumento;
- transposição individual correta;
- avisos de tocabilidade;
- áudio de referência;
- pacote organizado para ensaio.

## 17. Como a qualidade será testada

A aplicação será testada em vários níveis.

Em linguagem simples:

- pequenas regras serão testadas isoladamente;
- partes diferentes do sistema serão testadas juntas;
- bancos de dados e filas reais serão usados em testes controlados;
- o fluxo completo do usuário será repetido automaticamente;
- partituras de referência terão resultados conhecidos;
- casos extremos serão gerados para procurar falhas difíceis;
- alterações visuais serão comparadas com exemplos aprovados;
- músicos avaliarão funções inferenciais ou criativas;
- todo erro real encontrado deverá virar um teste para não reaparecer.

A porcentagem de cobertura de testes não será suficiente sozinha. O objetivo é provar os comportamentos importantes.

## 18. Como a inteligência artificial será usada no desenvolvimento

Ferramentas de inteligência artificial ajudarão a desenvolver o W_Flyer, mas deverão seguir regras.

A IA terá que:

- consultar a documentação antes de alterar o projeto;
- planejar cada mudança;
- identificar módulos afetados;
- usar exemplos visuais internos;
- executar testes;
- registrar o que foi feito;
- atualizar o mapa do projeto;
- parar quando uma decisão ainda não foi aprovada.

Ela não poderá:

- inventar funções não autorizadas;
- esconder limitações;
- declarar uma fase concluída sem testes;
- colocar regras musicais apenas na tela;
- copiar a identidade de outro produto;
- alterar silenciosamente a intenção musical da obra.

## 19. Etapas de desenvolvimento

O projeto será construído em fases que dependem umas das outras.

### Fase 0 — preparação

Concluída documentalmente. Foram organizadas regras, ferramentas de navegação para IA, riscos, exemplos visuais e critérios de qualidade.

### Fase 1 — fundação executável

Será criada a base real da aplicação:

- site;
- servidor;
- banco de dados;
- fila de processamento;
- armazenamento;
- ambiente de testes;
- controles básicos de segurança.

### Fase 2 — modelo musical

Serão implementados o catálogo de instrumentos e a forma interna de representar notas e intervalos.

### Fase 3 — motor MusicXML

Serão implementados:

- leitura;
- normalização;
- transposição;
- verificação independente;
- testes musicais.

### Fases seguintes — produto completo do Core

Depois, o núcleo será conectado ao envio de arquivos, processamento, interface final, segurança, operação e aceite.

### Trilhas avançadas

Somente depois do Core:

- PDF e reconhecimento musical;
- extração de melodia;
- adaptação instrumental;
- harmonização;
- áudio;
- ensaio;
- score, partes e conjuntos;
- colaboração.

Uma fase não será iniciada automaticamente ao terminar a anterior. Haverá revisão e aprovação.

## 20. Situação atual do projeto

Na data desta revisão:

- a Fase 0 está concluída e arquivada;
- a documentação está organizada;
- as ferramentas que orientarão a IA foram preparadas;
- a estrutura futura do projeto foi planejada;
- o código funcional do produto ainda não foi iniciado;
- o frontend, a API, o banco, o worker e o motor musical ainda não existem.

Isso não representa atraso. É uma decisão para reduzir improvisações antes de iniciar o código.

A próxima etapa prevista é a criação da **fundação executável da Fase 1**.

## 21. Empresa, site e lançamento

A empresa W_Flyer ainda não está aberta. A abertura é planejada para o final de agosto de 2026. Antes disso, o projeto pode preparar o site, a identidade, as demonstrações e toda a documentação, mas não deve se apresentar como pessoa jurídica já regularizada.

O plano é:

```text
wflyer.com.br
→ site da futura empresa, serviços de programação e apresentação do produto

app.wflyer.com.br
→ aplicação musical quando estiver pronta

sites de clientes
→ hospedagens e domínios separados da aplicação
```

O site institucional será criado primeiro para apresentar serviços de criação de sites, aplicações e integrações. O pagamento do SaaS ficará para depois que o produto estiver praticamente completo, com custos, impostos, suporte e emissão de NFS-e validados.

Stripe e Mercado Pago serão testados. Stripe é o candidato inicial, mas a decisão só será final depois de testes em ambiente de sandbox e da abertura da empresa.

A aplicação deverá ser hospedada em infraestrutura própria e resiliente, planejada para AWS, sem depender da mesma hospedagem usada pelo site institucional ou por clientes. Backups, restauração, filas, proteção do banco e resposta a falhas já estão previstos na documentação.

## 22. O que o W_Flyer não deve se tornar

O W_Flyer não deverá ser:

- apenas um conversor de arquivos sem explicação;
- uma interface bonita sobre um resultado não verificável;
- um sistema que chama qualquer mudança de “transposição”;
- uma ferramenta que esconde incerteza atrás da palavra IA;
- um editor que modifica a obra sem permitir revisão;
- um produto que promete perfeição para qualquer partitura;
- uma cópia visual de outra aplicação musical;
- um repositório com muitas funções parcialmente prontas e nenhuma confiável.

## 23. Resumo em uma frase

> O W_Flyer será um estúdio digital que transforma material musical, mostra o que mudou, verifica o que pode ser provado e mantém o músico responsável pelas decisões que dependem de interpretação ou criatividade.

## 24. Glossário simples

| Termo | Significado simples |
|---|---|
| Partitura | Representação escrita de uma música. |
| MusicXML | Arquivo que guarda informações musicais estruturadas, e não apenas uma imagem. |
| Transposição | Reescrita da música para outra altura ou afinação instrumental. |
| Instrumento transpositor | Instrumento cuja nota escrita pode soar em outra altura, como trompete em Si bemol. |
| Altura de concerto | Som real que deve ser ouvido, independentemente de como cada instrumento lê a nota. |
| Armadura de clave | Sustenidos ou bemóis colocados no início da pauta para indicar a tonalidade. |
| Acidente | Sustenido, bemol ou bequadro aplicado a uma nota. |
| Oitava | Região mais grave ou mais aguda da mesma nota. |
| OMR | Leitura automática de símbolos musicais em PDF ou imagem. |
| Extração de melodia | Seleção da linha melódica principal em uma textura com várias notas. |
| Harmonização | Criação de acordes ou vozes para acompanhar uma melodia. |
| Adaptação idiomática | Ajuste para tornar a escrita mais natural e executável em um instrumento. |
| Verificação independente | Conferência feita por uma parte separada do sistema. |
| Fail-closed | Em caso de dúvida importante, o sistema interrompe em vez de publicar um resultado arriscado. |
| Sessão anônima | Uso sem conta permanente, mas com um identificador privado temporário. |
| Retenção | Período durante o qual o arquivo permanece disponível. |
| Capability | Função que pode estar preparada, mas só é ativada após aprovação. |

## Como preços, créditos e políticas serão decididos

Os preços não foram escolhidos antecipadamente. A equipe primeiro medirá quanto cada operação realmente custa e preencherá os campos reservados na documentação. O sistema de créditos mostrará o custo antes de iniciar, reservará o saldo durante o processamento e devolverá a reserva quando uma falha interna impedir a entrega.

O site e a aplicação terão uma Central de Políticas pública com termos, privacidade, cookies, pagamentos, cancelamento, direitos autorais, uso aceitável, retenção, suporte e segurança. Enquanto a empresa não estiver formalizada e os textos não forem revisados, essas políticas permanecem como rascunhos internos.



## 25. Como as decisões futuras serão tomadas

Nem toda escolha pode ser feita antes de existir uma versão funcional. Por exemplo, ainda não é possível afirmar qual serviço de leitura de PDF será melhor, quanto cada operação custará ou qual tamanho de servidor será suficiente sem executar testes reais.

Para evitar improvisação, o W_Flyer mantém um registro de decisões. Cada assunto passa pela mesma sequência:

```text
pergunta clara
→ informações e testes necessários
→ resultados registrados
→ comparação entre alternativas
→ aprovação da pessoa responsável
→ implementação
→ nova verificação depois de pronto
```

Isso significa que:

- a inteligência artificial pode pesquisar, organizar testes e explicar resultados;
- ela não pode escolher sozinha um fornecedor, preço, regra fiscal, limite técnico ou decisão musical;
- resultados ruins também são guardados, para que o mesmo erro não seja repetido;
- uma função futura permanece desligada enquanto as provas necessárias não existirem;
- uma decisão pode ser revista se custos, leis, tecnologia, repertório ou necessidades mudarem.

Exemplos:

- o leitor de PDF só será escolhido depois de comparar precisão, segurança, licença, custo e tempo de processamento;
- Stripe e Mercado Pago executarão os mesmos cenários de teste antes da escolha;
- preços e créditos só serão preenchidos depois de medir custos reais e validar impostos;
- a hospedagem só será dimensionada depois de testes de carga, backup, restauração e simulação de falhas;
- a logo só será aprovada depois de revisar aplicações, versões SVG, legibilidade, direitos e uso em animações.

Portanto, “pendente” não significa “esquecido”. Significa que a documentação já informa **o que precisa ser feito para chegar a uma decisão confiável**.
