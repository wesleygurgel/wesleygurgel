"""Gera assets/terminal.svg, o terminal do README. Rode: python3 assets/gerar_terminal.py"""
from html import escape

W, LH, X0, X1 = 900, 23, 36, 170
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'DejaVu Sans Mono',monospace"
P = "wesley@dev"
# (tipo, ...) : prompt(cmd) | t(texto,classe) | row(rotulo,valor) | gap | head
L = [
 ("head",),
 ("gap",),
 ("prompt", "whoami"),
 ("t", "Wesley Gurgel · engenheiro de software", "b"),
 ("t", "No mundo do desenvolvimento desde 2018 · UFRN, Bacharelado em TI (Eng. de Software)", ""),
 ("t", "Transformo problemas de negócio em software que roda em produção,", ""),
 ("t", "trabalhando em dupla com IA do desenho da solução ao deploy.", ""),
 ("gap",),
 ("prompt", "cat como-trabalho.md"),
 ("n", "1.", "Eu decido, a IA acelera.", " Defino o problema, a arquitetura e o critério de pronto."),
 ("n", "2.", "Contexto antes de código.", " Specs, regras do projeto e exemplos para a IA."),
 ("n", "3.", "Nada vai sem revisão.", " Leio o diff, rodo os testes e valido o comportamento."),
 ("n", "4.", "Pequeno e verificável.", " Entregas curtas, com testes, para errar barato."),
 ("gap",),
 ("prompt", "cat fundamentos.md"),
 ("t", "# Linguagem e framework mudam. Estes fundamentos ficam.", "d"),
 ("row", "arquitetura", "monólito modular · hexagonal · DDD · event-driven · ADRs"),
 ("row", "padrões", "design patterns · SOLID · clean code · refatoração segura"),
 ("row", "dados", "modelagem relacional · consultas e índices · migrações sem downtime"),
 ("row", "sistemas", "APIs e contratos · concorrência e assíncrono · filas · observabilidade"),
 ("row", "qualidade", "testes automatizados · revisão de código · CI/CD"),
 ("gap",),
 ("prompt", "ls ferramentas/"),
 ("t", "# o que uso para aplicar os fundamentos acima, e que troco quando o problema pede", "d"),
 ("t", "Python  TypeScript  JavaScript  PHP  SQL", ""),
 ("t", "FastAPI  Django  SQLAlchemy  Laravel  Angular  React", ""),
 ("t", "Claude Code  agentes  MCP  Selenium", ""),
 ("gap",),
 ("prompt", "contato --listar"),
 ("ok", "email", "wesleygurgel27@gmail.com"),
 ("ok", "telegram", "t.me/wesleygurgel"),
 ("cursor",),
]
out, y = [], 0
def T(x, y, s, c):
    out.append(f'<text x="{x}" y="{y}" class="{c}">{escape(s)}</text>')

y = 52  # abaixo da barra de título
for it in L:
    k = it[0]
    if k == "head":
        out.append(f'<text x="{X0}" y="{y+22}" class="logo">WESLEY GURGEL</text>')
        y += 30
    elif k == "gap":
        y += LH // 2
    elif k == "prompt":
        y += LH
        T(X0, y, P, "a"); T(X0 + 85, y, ":", "d"); T(X0 + 93, y, "~", "d"); T(X0 + 107, y, "$", "d"); T(X0 + 125, y, it[1], "")
    elif k == "t":
        y += LH; T(X0, y, it[1], it[2])
    elif k == "n":
        y += LH; T(X0, y, it[1], "a")
        out.append(f'<text x="{X0+26}" y="{y}" class=""><tspan class="a">{escape(it[2])}</tspan><tspan>{escape(it[3])}</tspan></text>')
    elif k == "row":
        y += LH; T(X0, y, it[1], "a"); T(X1, y, it[2], "")
    elif k == "ok":
        y += LH; T(X0, y, "✓", "g"); T(X0 + 24, y, it[1], "a"); T(X1, y, it[2], "")
    elif k == "cursor":
        y += LH
        T(X0, y, P, "a"); T(X0 + 85, y, ":", "d"); T(X0 + 93, y, "~", "d"); T(X0 + 107, y, "$", "d")
        out.append(f'<rect x="{X0+125}" y="{y-14}" width="9" height="17" fill="#e8a23a"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite"/></rect>')
H = y + 30
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">Terminal de Wesley Gurgel</title>
<desc id="d">Engenheiro de software desde 2018, trabalha em dupla com IA. Princípios de trabalho, fundamentos (arquitetura, padrões, dados, sistemas, qualidade), ferramentas e contato.</desc>
<style>
text{{font-family:{FONT};font-size:14px;fill:#e9e1d3;white-space:pre}}
.a{{fill:#e8a23a}}.d{{fill:#8c8272}}.g{{fill:#8fbf7a}}.b{{font-weight:700}}
.logo{{font-size:32px;font-weight:800;fill:#e8a23a;letter-spacing:5px}}
</style>
<rect width="{W}" height="{H}" rx="12" fill="#14110f"/>
<rect width="{W}" height="36" rx="12" fill="#1d1915"/><rect y="24" width="{W}" height="12" fill="#1d1915"/>
<circle cx="22" cy="18" r="6" fill="#e8a23a"/><circle cx="42" cy="18" r="6" fill="#4a4237"/><circle cx="62" cy="18" r="6" fill="#4a4237"/>
<text x="{W//2}" y="23" text-anchor="middle" class="d" style="font-size:12px">wesleygurgel — zsh</text>
{chr(10).join(out)}
</svg>'''
open("assets/terminal.svg", "w", encoding="utf-8").write(svg)
print(W, H)
