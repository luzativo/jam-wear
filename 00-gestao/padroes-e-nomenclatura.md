# Padrões — nomenclatura, versionamento e status

Regras para manter a base organizada, rastreável e fácil de consultar. Valem para todos que contribuírem no repositório.

---

## 1. Nomenclatura de arquivos e pastas

- **`kebab-case`**, tudo minúsculo, sem acentos, sem espaços nos nomes de arquivo. (Acentos são livres **dentro** do conteúdo — só não no nome do arquivo.)
  - ✅ `documento-de-marca.md` · `benchmark-concorrentes.md`
  - ❌ `Documento de Marca.md` · `Pesquisa Têxtil (final).md`
- **Nomes descritivos**, nunca genéricos. Evitar `final`, `novo`, `v2 (2)`, `sem título`.
- **Datas** no formato ISO **`AAAA-MM-DD`** quando o arquivo for datado (reuniões, relatórios, exports):
  - `reuniao-2026-06-19-roteiro.md` · `analise-desempenho-2026-08.md`
- Pastas de topo são **numeradas** (`00-`, `01-`, …) para ordenar por fluxo de trabalho.

## 2. Versionamento

- Entregas evolutivas usam **`vMAJOR.MINOR`** (ex.: Documento de Marca `v3.2` → `v4.0`). MAJOR = reescrita/virada estrutural; MINOR = ajustes e incrementos.
- **A versão vigente vive no caminho canônico, sem sufixo de versão no nome do arquivo.** Há sempre um só arquivo "atual" de cada entrega (ex.: `02-branding/documento-de-marca.md`). A versão é declarada **no cabeçalho do arquivo**, não no nome.
- Ao criar uma nova versão, a anterior vai para **[`99-arquivo/`](../99-arquivo/)** com sufixo de versão e data:
  - `99-arquivo/branding-versoes-anteriores/documento-de-marca-v3.2-2026-07-23.md`
- O histórico fino (linha a linha) fica no **git**; o `99-arquivo/` guarda apenas marcos que valem consulta rápida.

## 3. Cabeçalho de metadados

Todo documento de trabalho começa com um bloco curto de metadados, para dar contexto sem depender de quem criou:

```
> **Status:** ✅ Validado · **Versão:** 4.0 · **Atualizado:** 2026-07-23
> **Fonte:** produção Luzativo / insumo do cliente / pesquisa externa (motor)
> **Relacionado:** links para documentos conexos
```

## 4. Status — legenda única da base

| Marcador | Significado |
|----------|-------------|
| ✅ **Validado** | Decidido/confirmado (pelo cliente ou por dado sólido). Pode orientar ações. |
| ◆ **Proposta** | Direção sustentada (pesquisa/análise), **a confirmar** com o cliente. |
| ⚠️ **Pendente** | Depende de decisão do cliente ou de dado que ainda não temos. |
| 🚧 **Em construção** | Sendo produzido; ainda não é entregável. |
| 🗄️ **Arquivado** | Superado. Mantido só como histórico em `99-arquivo/`. |

> Regra de ouro do projeto: **nunca tratar hipótese como decisão validada.** Tudo que ainda não foi confirmado com o cliente entra como ◆ ou ⚠️, jamais como ✅.

## 5. Fontes externas e binários

- Materiais de **texto** (pesquisas, docs de trabalho) são espelhados **em markdown** dentro da base — versionáveis, buscáveis e comparáveis.
- **Originais binários** do cliente e documentos assinados (PDF, DOCX, PSD, imagens) permanecem canônicos no **Google Drive**; a base guarda a extração de texto quando útil e sempre um **índice com link, ID e status** em [`00-gestao/fontes-e-materiais-externos.md`](fontes-e-materiais-externos.md). Assim nada se perde e as fontes podem ser apresentadas ao cliente.

## 6. Prioridade de fontes (em caso de conflito)

Ordem de validade quando materiais divergirem:
1. O **documento mais recente** validado nesta base (ex.: Documento de Marca vigente).
2. As **definições construídas e validadas** ao longo do projeto (registro de decisões).
3. As **reuniões anteriores**, apenas quando não conflitarem com 1 e 2.

Contradições relevantes que a hierarquia não resolva devem ser **sinalizadas** (em Pendências) antes de incorporadas — nunca resolvidas por inércia.
