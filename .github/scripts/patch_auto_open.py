from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

old = '''function openContentView(raw,label="Obsah"){
  const url=normalizeContentUrl(raw);
  if(!url){toast("Odkaz není platná webová adresa");return}
  activeContentUrl=url;
  stopTimer();
  $("contentTitle").textContent=label;
  $("contentUrl").textContent=url;
  $("contentFrame").src=url;
  $("contentOverlay").classList.add("show");
}
'''

new = '''function openContentView(raw,label="Obsah"){
  const url=normalizeContentUrl(raw);
  if(!url){toast("Odkaz není platná webová adresa");return}
  stopTimer();
  const w=window.open(url,"riskuj-content","width=1100,height=800");
  if(w){
    try{w.opener=null}catch(e){}
    try{w.focus()}catch(e){}
  }else{
    window.location.href=url;
  }
}
'''

if 'window.open(url,"riskuj-content","width=1100,height=800")' in s:
    raise SystemExit(0)
if old not in s:
    raise SystemExit("Target openContentView block not found; refusing to patch")

p.write_text(s.replace(old, new, 1), encoding="utf-8")
