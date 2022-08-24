#Rebecca Smith
#Seccion 20

from gl import Renderer, color, V2, V3
from textures import Texture
from obj import Obj
import random

from shaders import flat,unlit, gourad, toon, glow, textureBlend, sabor


w=700
h=700
z=-10

rend= Renderer(w,h)

rend.dirLight = V3(1,0,0)

rend.active_texture = Texture("body.bmp")
rend.active_texture2 = Texture("shades.bmp")
rend.active_shader = sabor


rend.glLoadModel("cookie.obj",
                translate = V3(0, 0, -10),
                scale = V3(1,1,1),
                rotate = V3(0, 65, 90)
                )

rend.active_texture = Texture("body.bmp")
rend.active_texture2 = Texture("shades.bmp")
rend.active_shader = toon

rend.glLoadModel("cookie.obj",
                translate = V3(1, 0, -10),
                scale = V3(1,1,1),
                rotate = V3(0, 65, 90)
                )

rend.active_texture = Texture("body.bmp")
rend.active_texture2 = Texture("shades.bmp")
rend.active_shader = textureBlend

rend.glLoadModel("cookie.obj",
                translate = V3(0.5, 0, -10),
                scale = V3(1,1,1),
                rotate = V3(0, 65, 90)
                )

rend.glFinish("output.bmp")

