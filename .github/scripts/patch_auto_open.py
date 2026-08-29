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

new = '''function canEmbedContent(url){
  try{
    const host=new URL(url).hostname.toLowerCase().replace(/^www\\./,"");
    return host==="wikipedia.org" || host.endsWith(".wikipedia.org") ||
           host==="wikimedia.org" || host.endsWith(".wikimedia.org") ||
           host==="youtube-nocookie.com" || host.endsWith(".youtube-nocookie.com");
  }catch(e){return false}
}
function openExternalContent(url){
  const w=window.open(url,"_blank","noopener,noreferrer");
  if(!w) window.location.href=url;
}
function openContentView(raw,label="Obsah"){
  const url=normalizeContentUrl(raw);
  if(!url){toast("Odkaz není platná webová adresa");return}
  stopTimer();
  if(!canEmbedContent(url)){
    openExternalContent(url);
    return;
  }
  activeContentUrl=url;
  $("contentTitle").textContent=label;
  $("contentUrl").textContent=url;
  $("contentFrame").src=url;
  $("contentOverlay").classList.add("show");
}
'''

if "function canEmbedContent(url)" in s:
    raise SystemExit(0)
if old not in s:
    raise SystemExit("Target openContentView block not found; refusing to patch")

p.write_text(s.replace(old, new, 1), encoding="utf-8")
