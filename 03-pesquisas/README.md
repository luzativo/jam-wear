# 03 · Pesquisas

Arquivo **integral** das pesquisas externas do projeto. O objetivo é poder, no futuro: consultar a pesquisa completa, comparar com novas rodadas, entender a origem de cada decisão e apresentar dados e fontes ao cliente.

## Método

Seis frentes de pesquisa (P1–P6) foram rodadas com **os mesmos prompts em dois motores** — **Perplexity** e **Gemini** — e depois **trianguladas** (o que os dois concordam vira base sólida; onde divergem, apresenta-se a leitura reconciliada; o que é frágil pede pesquisa primária).

| Frente | Tema |
|--------|------|
| **P1** | Mercado, preço e concorrentes |
| **P2** | Percepção e comportamento (regata masculina) |
| **P3** | Tecidos e materiais |
| **P4** | Comunicação (execução) |
| **P5** | Pointer / identidade e símbolos animais |
| **P6** | Posicionamento social e gestão de risco |

## Estrutura

| Subpasta / arquivo | Conteúdo |
|--------------------|----------|
| [`prompts/`](prompts/) | Os prompts usados nas pesquisas (mesmos prompts nos dois motores) + as frentes que foram descartadas e por quê. |
| [`resultados-perplexity/`](resultados-perplexity/) | Resultados brutos do Perplexity, por frente. |
| [`resultados-gemini/`](resultados-gemini/) | Resultados brutos do Gemini, por frente. |
| [`consolidacao-triangulacao.md`](consolidacao-triangulacao.md) | **A leitura consolidada** — cruzamento Perplexity × Gemini das 6 frentes, com status por achado (✅ confirmado / ⚖️ divergente resolvido / 🌫️ frágil). É o documento que a estratégia consome. |

## Como isso conecta com o resto

Os achados triangulados foram incorporados ao [Documento de Marca v4.0](../02-branding/documento-de-marca.md) marcados como **◆ propostas a validar**, e as pendências correspondentes estão em [`../00-gestao/pendencias-e-validacoes.md`](../00-gestao/pendencias-e-validacoes.md).

## Onde inserir no futuro

- Nova rodada de pesquisa → novo par de arquivos em `resultados-*/` + atualização da consolidação, preservando a rodada anterior.
- Sempre datar e nomear a fonte (motor, data).
