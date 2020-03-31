#!/usr/bin/env python3
# coding: utf8
import pyxel, os
class App:
    def __init__(self):
        self.window = Window()
        Resource()
        self.pc = PlayerCharacter()
        pyxel.run(self.update, self.draw)
    def update(self):
        self.pc.update()
    def draw(self):
        self.window.draw()
        self.pc.draw()

class Resource:
    def __init__(self):
        pyxel.load(self.ResourcePath)
    def __this_dir(self): return os.path.dirname(__file__)
    def __parent_dir(self, path): return os.path.dirname(path)
    @property
    def RootDir(self): return self.__parent_dir(self.__this_dir())
    @property
    def ResourcePath(self): return os.path.join(self.RootDir, 'res/python.pyxres')

class Window:
    def __init__(self, width=128, height=96, border_width=0):
        pyxel.init(width, height, border_width=border_width)
    def draw(self): pyxel.cls(0)

class PlayerCharacter:
    def __init__(self, x=0, y=0, width=8, height=8, img=0, u=0, v=0, colkey=0):
        self.w = width
        self.h = height
        self.x = (pyxel.width / 2) - (self.w / 2)
        self.y = (pyxel.height/ 2) - (self.h / 2)
        self.img = img
        self.u = u
        self.v = v
        self.colkey = colkey
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0: self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < pyxel.width - self.w: self.x += 1
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0: self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < pyxel.height - self.h: self.y += 1
    def draw(self):
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.w, self.h, self.colkey)

App()
