# Exercício Python 21
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
# from pygame import mixer

pygame.mixer.init()
pygame.mixer.music.load('C:/Users/natan/OneDrive/Documentos/Curso de Python/Curso em Video/Exercicios/arquivos_auxiliares/high _hopes.mp3')
pygame.mixer.music.play()
input()

