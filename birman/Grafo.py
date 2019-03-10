#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
class Grafo:
	def __init__(self, proceso):
		self.__proceso = proceso
		self.__procesos = np.zeros((proceso,proceso))

	def getProceso(self):
		return self.__proceso

 	def update(self, mensaje):
 		pass


	def __str__(self):
		return self.__procesos

