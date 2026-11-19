# Post IG (carrusel 4:5) + stories (9:16): reseñas de Goodreads y petición de «Quiero leerlo» / reseña en Amazon.
# Uso: python3 gen.py && node render.js   (salida en ../instagram y ../stories)
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">'
CSS = '''
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000}
section.slide{position:relative;overflow:hidden;background:#0b1220;color:#e7f4fe;font-family:Lora,serif}
.feed{width:1080px;height:1350px}.story{width:1080px;height:1920px}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.velo{position:absolute;inset:0}
.c{position:absolute;left:0;right:0;text-align:center;display:flex;flex-direction:column;align-items:center}
.ante{font:600 32px/1.3 Cinzel,serif;letter-spacing:.22em;text-transform:uppercase;color:#cfe3f3}
.est{font:400 76px/1 "Cormorant Garamond",serif;letter-spacing:.14em;color:#5fa8d3;text-shadow:0 0 36px rgba(95,168,211,.55)}
.tit{font:700 96px/1.04 "Cormorant Garamond",serif;color:#f3f8fd;text-shadow:0 4px 24px rgba(0,0,0,.6)}
.tit em{font-style:italic;font-weight:600;color:#5fa8d3}
.cita{font:italic 600 66px/1.18 "Cormorant Garamond",serif;color:#f3f8fd;text-shadow:0 4px 24px rgba(0,0,0,.6)}
.firma{font:600 30px/1.3 Cinzel,serif;letter-spacing:.16em;text-transform:uppercase;color:#cfe3f3}
.gr{font:500 30px/1.3 Lora,serif;color:#8fa0b8}
.cuerpo{font:400 38px/1.45 Lora,serif;color:#e7f4fe}
.tenue{color:#8fa0b8}
.sep{display:block;opacity:.8}
.boton{display:inline-block;font:600 34px/1 Cinzel,serif;letter-spacing:.14em;text-transform:uppercase;color:#0b1220;background:#e7f4fe;padding:22px 34px;border-radius:10px}
.sello{display:inline-block;font:600 30px/1 Cinzel,serif;letter-spacing:.18em;text-transform:uppercase;color:#f3f8fd;background:#b3364f;padding:20px 36px;border-radius:999px}
.paso{display:flex;gap:26px;align-items:flex-start;text-align:left;width:860px}
.paso .n{flex:none;width:84px;height:84px;border:2px solid #5fa8d3;border-radius:50%;font:700 44px/80px "Cormorant Garamond",serif;color:#5fa8d3;text-align:center}
.paso .t{font:400 36px/1.4 Lora,serif}
.paso .t b{font:600 30px/1.3 Cinzel,serif;letter-spacing:.14em;text-transform:uppercase;color:#cfe3f3;display:block;margin-bottom:6px}
.tarjeta{width:860px;border:1.5px solid #2e4470;background:rgba(11,18,32,.72);border-radius:14px;padding:24px 40px 22px}
.tarjeta .e{font:400 34px/1 "Cormorant Garamond",serif;letter-spacing:.12em;color:#5fa8d3}
.tarjeta .q{font:italic 600 38px/1.18 "Cormorant Garamond",serif;color:#f3f8fd;margin-top:14px}
.tarjeta .f{font:600 24px/1.3 Cinzel,serif;letter-spacing:.16em;text-transform:uppercase;color:#8fa0b8;margin-top:14px}
.esq{position:absolute;width:170px;opacity:.7}
.scene{position:absolute;perspective:2400px}
.book{position:relative;transform-style:preserve-3d;transform:rotateY(-32deg) rotateX(2deg)}
.book .front{position:absolute;inset:0;background-size:cover;background-position:center;border-radius:2px 4px 4px 2px;
  box-shadow:inset 3px 0 6px rgba(255,255,255,.18), inset -2px 0 3px rgba(0,0,0,.4)}
.book .front::after{content:"";position:absolute;inset:0;background:linear-gradient(100deg,rgba(255,255,255,0) 0%,rgba(255,255,255,.10) 38%,rgba(255,255,255,0) 60%),linear-gradient(90deg,rgba(0,0,0,.35) 0,rgba(0,0,0,0) 2.2%,rgba(255,255,255,.12) 3%,rgba(0,0,0,0) 4.5%)}
.book .pages{position:absolute;top:1.2%;height:97.6%;transform-origin:left center;
  background:repeating-linear-gradient(90deg,#f1ead9 0,#f1ead9 2px,#d9d0bb 2px,#d9d0bb 3px),#efe7d4;box-shadow:inset 0 0 18px rgba(0,0,0,.35)}
.book .back{position:absolute;inset:0;background:#0d1730}
.shadow{position:absolute;border-radius:50%;background:radial-gradient(ellipse at center,rgba(0,0,0,.75) 0%,rgba(0,0,0,0) 70%);filter:blur(6px)}
'''

import sys
NOMBRE4 = sys.argv[1] if len(sys.argv) > 1 else "NOMBRE"
RESENAS = [
    ("Marta", "No suelo leer libros de fantasía, pero este libro me ha mantenido enganchada todo el rato."),
    ("Itziar", "Sin duda un libro de fantasía oscura que no te dejará indiferente."),
    ("Sergio", "Lo recomiendo si te gusta la fantasía y, sobre todo, si te gustan las brujas."),
    (NOMBRE4, "Una versión de las brujas y la hechicería muy original. Es fácil leer varios capítulos de una sentada."),
    ("Laura Ferrer · editora", "Tanto los personajes como la ambientación hicieron que no quisiera dejar el libro."),
    ("Maria", "Es una historia que te atrapa desde la primera página y que no te deja indiferente."),
]


def book(x, y, w, thick):
    h = round(w * 2936 / 2036)
    return f'''<div class="shadow" style="left:{x-w*0.05}px;top:{y+h-30}px;width:{w*1.25}px;height:80px"></div>
<div class="scene" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="book" style="width:{w}px;height:{h}px">
<div class="back" style="transform:translateZ(-{thick}px)"></div><div class="pages" style="left:{w-2}px;width:{thick}px;transform:rotateY(90deg)"></div>
<div class="front" style="background-image:url(img/portada.jpg)"></div></div></div>'''


def fondo(oscuro=.72):
    return f'''<img class="bg" src="img/damask-noche.png">
<div class="velo" style="background:radial-gradient(ellipse 70% 60% at 50% 48%,rgba(6,10,20,{oscuro}),rgba(6,10,20,{oscuro-0.35}) 85%)"></div>'''


def esquinas(top, bottom):
    return (f'<img class="esq" style="left:48px;top:{top}px" src="img/esquina-sol-lunas-sup-izq-plata-lunar.png">'
            f'<img class="esq" style="right:48px;top:{top}px" src="img/esquina-sol-lunas-sup-der-plata-lunar.png">'
            f'<img class="esq" style="left:48px;bottom:{bottom}px" src="img/esquina-sol-lunas-inf-izq-plata-lunar.png">'
            f'<img class="esq" style="right:48px;bottom:{bottom}px" src="img/esquina-sol-lunas-inf-der-plata-lunar.png">')


LOGO = '<img src="img/logo-blanco.png" style="position:absolute;left:478px;bottom:56px;width:124px;opacity:.9">'

# ---------- CARRUSEL 4:5 ----------
def feed1():
    return f'''<section class="slide feed" id="resenas-01">{fondo(.55)}
<div class="velo" style="background:radial-gradient(ellipse 55% 40% at 50% 70%,rgba(95,168,211,.16),rgba(0,0,0,0) 70%)"></div>
<div class="c" style="top:96px"><p class="ante">Primeras reseñas en Goodreads</p>
<p class="est" style="margin-top:34px">★★★★★</p>
<p class="tit" style="margin-top:26px">Ya hay quien ha<br>cruzado a <em>Aerthea</em></p></div>
{book(355,570,370,64)}
</section>'''


def feed_resena(i, nombre, texto):
    return f'''<section class="slide feed" id="resenas-0{i+2}">{fondo(.78)}{esquinas(60, 60)}
<div class="c" style="top:0;bottom:0;justify-content:center;padding:0 130px">
<p class="est">★★★★★</p>
<p class="cita" style="margin-top:46px">«{texto}»</p>
<img class="sep" src="img/separador-filigrana-plata-lunar.png" style="width:300px;margin:46px 0 34px">
<p class="firma">{nombre}</p><p class="gr" style="margin-top:8px">en Goodreads</p></div>
</section>'''


def feed5():
    return f'''<section class="slide feed" id="resenas-08">{fondo(.8)}
<div class="c" style="top:150px"><p class="ante">Ya a la venta</p>
<p class="tit" style="margin-top:24px;font-size:90px">¿Te animas a<br><em>entrar en Aerthea</em>?</p>
<img class="sep" src="img/separador-sol-lunas-plata-lunar.png" style="width:420px;margin:40px 0 52px"></div>
<div class="c" style="top:640px;gap:46px">
<div class="paso"><div class="n">1</div><div class="t"><b>Brujas de Aerthea · El secreto de Violet</b>Ya disponible. El enlace está en mi perfil.</div></div>
</div>
</section>'''


# ---------- STORIES 9:16 (zonas seguras: 250 arriba, 420 abajo) ----------
def story1():
    tarjetas = ''.join(f'<div class="tarjeta"><p class="e">★★★★★</p><p class="q">«{t}»</p><p class="f">{n} · Goodreads</p></div>' for n, t in RESENAS)
    return f'''<section class="slide story" id="story-resenas-1">{fondo(.75)}
<div class="c" style="top:265px"><p class="ante">Ya han llegado</p>
<p class="tit" style="margin-top:18px;font-size:84px">Las primeras <em>reseñas</em></p></div>
<div class="c" style="top:470px;gap:22px">{tarjetas}</div>
</section>'''


def story2():
    return f'''<section class="slide story" id="story-resenas-2">{fondo(.6)}
<div class="velo" style="background:radial-gradient(ellipse 60% 30% at 50% 30%,rgba(95,168,211,.18),rgba(0,0,0,0) 70%)"></div>
{book(385,290,310,54)}
<div class="c" style="top:800px"><p class="ante">¿Aún no lo tienes guardado?</p>
<p class="tit" style="margin-top:18px;font-size:80px">Márcalo en <em>Goodreads</em></p>
<p class="cuerpo" style="margin-top:24px">Toca el enlace y pulsa</p>
<p class="boton" style="margin-top:24px">Quiero leerlo</p>
<p class="cuerpo tenue" style="margin-top:24px;font-size:32px">Diez segundos para ti, muchísimo para mí</p></div>
<!-- hueco para el sticker de enlace: y≈1330-1480 -->
</section>'''


def story3():
    return f'''<section class="slide story" id="story-resenas-3">{fondo(.78)}{esquinas(262, 430)}
<div class="c" style="top:420px;padding:0 140px"><p class="ante">Ya a la venta en Amazon</p>
<p class="est" style="margin-top:36px">☆☆☆☆☆</p>
<p class="tit" style="margin-top:28px;font-size:80px">Cuando lo leas,<br>déjame tu <em>reseña</em><br>en Amazon</p>
<img class="sep" src="img/separador-sol-lunas-plata-lunar.png" style="width:420px;margin:38px 0 32px">
<p class="cuerpo">Unas líneas valen más<br>que cualquier anuncio.</p>
<p class="cuerpo tenue" style="margin-top:24px;font-size:32px">Enlace en la bio ↓</p></div>
<!-- hueco para el sticker de enlace a Amazon: y≈1250-1480 -->
</section>'''


def page(body):
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{body}</body></html>'


open('feed.html', 'w').write(page(feed1() + ''.join(feed_resena(i, n, t) for i, (n, t) in enumerate(RESENAS)) + feed5()))
open('stories.html', 'w').write(page(story1() + story2() + story3()))
