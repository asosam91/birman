#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
class Grafo:
	def __init__(self, procesos):
		self.__procesos = procesos
		self.__proceso = np.zeros((procesos,procesos))

	def getProcesos(self):
		return self.__procesos

	def setProceso(self, mensaje):
		for p in range(len(mensaje)):
			if self.__proceso[p] < mensaje[p]:
				self.__proceso[p] = mensaje[p]  

	def __str__(self):
		return self.__proceso

	def getProceso(self, num):
		return self.__proceso[num]

