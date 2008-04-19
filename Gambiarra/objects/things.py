# -*- coding: UTF-8 -*-
#
# Copyright (C) 2007 by ULPM: Alexandre Yukio Harano
#                             Fábio Cassarotti Parronchi Navarro
#                             Gabriel Geraldo França Marcondes
#                             Luiz Carlos Irber Júnior
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

# Bowling ball bouncing
# http://freesound.iua.upf.edu/samplesViewSingle.php?id=22744
# Updated at September 12th, 2006.
# Published under Creative Commons Sampling Plus 1.0 License.

# Congratulations
# http://freesound.iua.upf.edu/samplesViewSingle.php?id=25293
# Updated at November 09th, 2006.
# Published under Creative Commons Sampling Plus 1.0 License.

# Penguin bouncing
# http://freesound.iua.upf.edu/samplesViewSingle.php?id=34316
# Updated at May 01st, 2007.
# Published under Creative Commons Sampling Plus 1.0 License.

# Trampoline bouncing
# http://freesound.iua.upf.edu/samplesViewSingle.php?id=19347
# Updated at May 30th, 2006.
# Published under Creative Commons Sampling Plus 1.0 License.

import pygame

class Thing(pygame.sprite.Sprite):

    img = None
    initial_pos = None
    mobility = None
    editable = None
    speed = None
    gravity = None
    snd = None
    elasticity = None # * 1%, from 0 up to 100

    def __init__(self, image, editable, snd, initial_pos=None,
                 elasticity = 70, mobility = False, gravity = 5 ):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image = image
        self.rect = image.get_rect()

        if initial_pos:
            self.initial_pos = initial_pos
            self.rect.topleft = initial_pos[0], initial_pos[1]
        self.elasticity = elasticity
        self.editable = editable
        self.speed = [0,0]
        self.mobility = mobility
        self.gravity = gravity
        self.snd = snd

    def draw(self, screen, pos ):
        # temos a imagem na variavel <img> e
        # o 'zero' (ponto onde deve ser desenhado <pos>
        screen.blit(self.image, (pos[0],pos[1]))

    def play(self):
        if self.snd and pygame.mixer.get_init():
            self.snd.play()

    def collide(self, obj):
        ''' Very basic implementation of elastic collision'''
        #TODO: verify mobility attribute
        hitbox = self.rect.inflate(5,5)
        if hitbox.colliderect(obj.rect):
            if self.rect.left < obj.rect.right:
                self.speed[0], obj.speed[0] = obj.speed[0], self.speed[0]
                self.rect.left = obj.rect.right - 1
            if self.rect.left > obj.rect.right:
                self.speed[0], obj.speed[0] = obj.speed[0], self.speed[0]
                self.rect.right = obj.rect.left - 1
            if self.rect.bottom > obj.rect.top:
                self.speed[1], obj.speed[1] = obj.speed[1], self.speed[1]
                self.rect.bottom = obj.rect.top - 1
            if self.rect.top < obj.rect.bottom:
                self.speed[1], obj.speed[1] = obj.speed[1], self.speed[1]
                self.rect.top = obj.rect.bottom + 1
            return True
        return False

    def update(self):
        if self.mobility:
            newpos = self.rect.move((self.speed[0],self.speed[1]))
            self.rect = newpos
            self.speed[0] *= 0.99
            if self.speed[1] <= self.rect[3]*0.04 and self.speed[1] > 0:
                self.speed[1] = 0
            else:
                self.speed[1] += self.gravity

def check_collision(sprite_list, wall_list):
    new_objects = pygame.sprite.RenderPlain()
    for obj in sprite_list:
        obj.remove(sprite_list)
        obj.add(new_objects)

#        for s in sprite_list:
#            if s.collide(obj)
#                obj.play()
#                s.play()

        for w in wall_list:
            if w.collide(obj):
                obj.play()
                w.play()

    return new_objects

