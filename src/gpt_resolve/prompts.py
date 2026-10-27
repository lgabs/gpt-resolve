"""Prompts and output schemas for the extractor, solver and judge agents."""

EXTRACT_SYSTEM = (
    "Você é um assistente que organiza provas de vestibular. Leia a prova com a ferramenta Read "
    "(para PDFs use o parâmetro `pages`, no máximo 20 páginas por chamada) e liste as questões."
)

EXTRACT_PROMPT = """A prova está em: {sources}

Liste todas as questões da prova. Para cada questão informe:
- number: o número da questão como aparece na prova;
- pages: as páginas do PDF (contando a partir de 1) onde estão o enunciado e as figuras dela (vazio se a prova for em imagens);
- statement: a transcrição fiel do enunciado, com fórmulas em LaTeX e uma descrição das figuras.

Em `instructions`, transcreva as instruções gerais, notações e constantes da prova que valem para todas as questões (ou deixe vazio)."""

EXTRACT_SCHEMA = {
    "type": "object",
    "properties": {
        "instructions": {"type": "string"},
        "questions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "number": {"type": "integer"},
                    "pages": {"type": "array", "items": {"type": "integer"}},
                    "statement": {"type": "string"},
                },
                "required": ["number", "pages", "statement"],
            },
        },
    },
    "required": ["instructions", "questions"],
}

SOLVER_SYSTEM = (
    "Você é um professor especialista em vestibulares militares (IME, ITA) e resolve questões "
    "discursivas como uma resolução modelo de cursinho: correta, completa, rigorosa e didática. "
    "Você pode usar a ferramenta Read para ver a prova original (figuras inclusive) e Bash com python3 "
    "para conferir contas, mas a resolução final deve se sustentar sozinha, sem depender de código."
)

SOLVER_PROMPT = """Resolva a questão {number} da prova.

Prova original: {sources}{pages_hint}
Instruções gerais da prova:
{instructions}

Transcrição do enunciado (confira com o original, que prevalece):
{statement}

Requisitos da resolução:
- Explique o raciocínio passo a passo, justificando cada passo (hipóteses, leis/teoremas usados, condições de validade), de forma objetiva como numa prova, cabendo em cerca de uma página.
- Responda todos os itens pedidos e confira unidades, sinais, casos particulares e ordens de grandeza.
- Use LaTeX válido: uma única seção começando com \\section*{{Solução}}. Não aninhe `align*` dentro de `\\[ \\]`. Não use pacotes além de amsmath, amssymb, amsfonts, graphicx, tikz e pgfplots.
- Use vírgula como separador decimal e não use ponto para milhar.
- Termine com uma linha 'ANSWER:' seguida do resultado final.
{revision}
Devolva `solution_latex` (a seção LaTeX completa) e `final_answer` (resumo curto da resposta)."""

REVISION_BLOCK = """
Esta é uma revisão. Sua tentativa anterior recebeu nota {score}/10 de um avaliador rigoroso. Não confie cegamente nele: verifique cada crítica, corrija o que estiver certo e mantenha o que estiver correto.

Tentativa anterior:
{previous}

Parecer do avaliador:
{feedback}
"""

SOLVER_SCHEMA = {
    "type": "object",
    "properties": {
        "solution_latex": {"type": "string"},
        "final_answer": {"type": "string"},
    },
    "required": ["solution_latex", "final_answer"],
}

JUDGE_SYSTEM = (
    "Você é um corretor adversarial de provas discursivas do IME/ITA. Seu trabalho é encontrar falhas "
    "na resolução: erros de conta, de física/matemática, hipóteses não justificadas, casos esquecidos, "
    "itens não respondidos, saltos lógicos, unidades e notação. Resolva a questão você mesmo de forma "
    "independente antes de julgar. Você pode usar Read para ver a prova original e Bash com python3 para "
    "conferir contas. Seja exigente: nota 9 ou mais significa uma resolução que um professor publicaria "
    "como gabarito comentado."
)

JUDGE_PROMPT = """Avalie a resolução da questão {number}.

Prova original: {sources}{pages_hint}
Instruções gerais da prova:
{instructions}

Transcrição do enunciado (confira com o original, que prevalece):
{statement}

Resolução a avaliar:
{solution}

Dê uma nota de 0 a 10 para a qualidade da resolução como um todo (correção, completude, rigor, clareza), não apenas para a resposta final. Uma resposta final certa com justificativa fraca não passa de 7. Liste cada problema encontrado com sua gravidade (critical, major, minor) e o que deveria ser feito."""

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "score": {"type": "number", "minimum": 0, "maximum": 10},
        "answer_correct": {"type": "boolean"},
        "issues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "severity": {"type": "string", "enum": ["critical", "major", "minor"]},
                    "description": {"type": "string"},
                },
                "required": ["severity", "description"],
            },
        },
        "summary": {"type": "string"},
    },
    "required": ["score", "answer_correct", "issues", "summary"],
}
