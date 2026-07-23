# Ferramentas

Scripts de apoio à operação da base.

| Arquivo | O que faz |
|---------|-----------|
| [`build_html.py`](build_html.py) | Converte [`../../02-branding/documento-de-marca.md`](../../02-branding/documento-de-marca.md) em HTML com o esquema de cores (verde/vermelho nas tabelas de contraste, destaque nos marcadores ◆/⚠️), para gerar o **Google Doc** do Documento de Marca. Uso: `python3 build_html.py` → HTML → importar no Google Docs convertendo para documento nativo. |

Requer `pip install markdown`. O script evita caracteres fora do BMP (emojis astrais) porque eles corrompem na conversão para Google Docs.
