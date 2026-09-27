from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

marker = "  @media(max-width:900px){.editor-category-title{grid-template-columns:1fr}.editor-q-grid{grid-template-columns:1fr;overflow:visible}.editor-q{min-width:0}.editor-modal{padding:12px}.editor-head{top:-12px}}\n"
css = r'''

  /* Hlavní herní obrazovka se vždy vejde do viewportu */
  html,body{height:100%;overflow:hidden}
  .app{height:100dvh;min-height:0;overflow:hidden}
  .topbar{position:relative;flex:0 0 auto;padding:8px 12px;gap:8px;min-height:0}
  .brand{flex:0 0 auto;gap:8px}
  .brand-mark{width:34px;height:34px;border-radius:10px;font-size:19px}
  .brand h1{font-size:18px}.brand small{font-size:10px}
  .actions{flex:1 1 auto;flex-wrap:nowrap;overflow-x:auto;gap:5px;justify-content:flex-end;scrollbar-width:thin}
  .actions .btn{flex:0 0 auto;white-space:nowrap;padding:7px 9px;font-size:12px;border-radius:9px}
  .main{width:100%;max-width:1500px;height:0;min-height:0;overflow:hidden;padding:8px 10px;gap:7px}
  .game-title{flex:0 0 auto;font-size:clamp(18px,2.2vw,30px);line-height:1.05;margin:0}
  .board-wrap{flex:1 1 auto;min-height:0;overflow:hidden;padding:5px;border-radius:14px}
  .board{height:100%;min-height:0;min-width:0!important;gap:4px}
  .category{min-height:0;padding:4px 5px;border-radius:8px;font-size:clamp(10px,1.15vw,18px);line-height:1.08;letter-spacing:.2px}
  .cell{min-height:0;border-radius:8px;font-size:clamp(18px,3.2vh,36px)}
  .cell.used::after{font-size:clamp(20px,3vh,30px)}
  .scoreboard{flex:0 0 auto;display:flex;overflow-x:auto;gap:6px;padding:0;scrollbar-width:thin}
  .team{flex:1 0 145px;min-width:0;border-radius:10px;padding:5px 7px;gap:2px 6px}
  .team-name{font-size:13px}.team-score{font-size:21px}
  .team-tools{gap:4px}.mini{padding:3px 6px;border-radius:7px;font-size:10px}
  .footer-actions{flex:0 0 auto;margin:0}
  .footer-actions .btn{padding:5px 8px;font-size:11px}
  .hint{display:none}
  @media(max-height:650px){
    .topbar{padding:5px 8px}.brand-mark{width:30px;height:30px;font-size:17px}.brand h1{font-size:16px}.brand small{display:none}
    .actions .btn{padding:5px 7px;font-size:11px}.main{padding:5px 7px;gap:4px}.game-title{font-size:17px}
    .board-wrap{padding:3px}.board{gap:3px}.category{font-size:10px;padding:2px 3px}.cell{font-size:clamp(16px,3vh,28px)}
    .team{padding:3px 5px}.team-name{font-size:11px}.team-score{font-size:18px}.mini{padding:2px 5px;font-size:9px}
  }
'''

if "Hlavní herní obrazovka se vždy vejde do viewportu" not in s:
    if marker not in s:
        raise SystemExit("CSS marker not found")
    s = s.replace(marker, marker + css, 1)

old = '''  b.style.gridTemplateColumns=`repeat(${cols},minmax(150px,1fr))`;
  b.style.minWidth=Math.max(720,cols*165)+"px";'''
new = '''  b.style.gridTemplateColumns=`repeat(${cols},minmax(0,1fr))`;
  b.style.minWidth="0";'''
if old in s:
    s = s.replace(old, new, 1)
elif "repeat(${cols},minmax(0,1fr))" not in s:
    raise SystemExit("board columns snippet not found")

old_rows = "  const rows=boardRows();\n"
new_rows = "  const rows=boardRows();\n  b.style.gridTemplateRows=`minmax(38px,.72fr) repeat(${rows},minmax(0,1fr))`;\n"
if "b.style.gridTemplateRows=" not in s:
    if old_rows not in s:
        raise SystemExit("rows snippet not found")
    s = s.replace(old_rows, new_rows, 1)

p.write_text(s, encoding="utf-8")
