"""Bundle the review build into one offline HTML file. Run after INCLUDE_DRAFTS=true npm run build."""
from pathlib import Path
import re, json, base64, sys
root=Path(__file__).resolve().parent.parent/'dist'
pages={}
for p in root.rglob('*.html'):
    route='/' + str(p.relative_to(root)).removesuffix('index.html')
    html=p.read_text()
    body=re.search(r'<body[^>]*>(.*)</body>',html,re.S).group(1)
    pages[route]={'body':body,'title':re.search(r'<title>(.*?)</title>',html).group(1)}
css='\n'.join(p.read_text() for p in (root/'_astro').glob('*.css'))
def embed(m):
    name=m.group(1).strip('"\'')
    path=root/name.lstrip('/')
    if path.is_file():return 'url(data:font/woff2;base64,'+base64.b64encode(path.read_bytes()).decode()+')'
    raise ValueError(f'Unresolved asset: {name}')
css=re.sub(r'url\(([^)]+)\)',embed,css)
feed='data:application/rss+xml;base64,'+base64.b64encode((root/'rss.xml').read_bytes()).decode()
favicon='data:image/svg+xml;base64,'+base64.b64encode((root/'favicon.svg').read_bytes()).decode()
js='''const pages=PAGES;function render(){const route=location.hash.slice(1)||'/';const page=pages[route]||pages['/404.html'];document.body.innerHTML=page.body;document.title=page.title;document.querySelectorAll('a[href^="/"]').forEach(a=>{const href=a.getAttribute('href');if(href==='/rss.xml'){a.href=FEED;a.download='rss.xml';}else a.href='#'+href;});document.querySelectorAll('a[href="#top"]').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();window.scrollTo(0,0)}));document.querySelector('.skip')?.addEventListener('click',e=>{e.preventDefault();const main=document.querySelector('main');main.setAttribute('tabindex','-1');main.focus();});window.scrollTo(0,0);}window.addEventListener('hashchange',render);render();'''.replace('PAGES',json.dumps(pages).replace('</','<\\/')).replace('FEED',json.dumps(feed))
output=Path(sys.argv[1])
output.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Mateo Echeverri — design preview</title><link rel="icon" href="'+favicon+'"><style>'+css+'</style></head><body id="top">'+pages['/']['body']+'<script>'+js+'</script></body></html>')
print(f'Exported {len(pages)} pages to {output}, {output.stat().st_size} bytes')
# Check every internal link against the generated site.
for page in root.rglob('*.html'):
    for href in re.findall(r'href="(/[^"]*)"',page.read_text()):
        target=root/href.lstrip('/')
        if href.endswith('/'):target=target/'index.html'
        assert target.exists(),f'Broken link: {page} -> {href}'

print('Internal links resolve.')
