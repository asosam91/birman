#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
class Mensaje:
	def __init__(self, proceso,procesos):
		self.__mensaje = np.zeros((procesos))
		self.__proceso = proceso

	def setMensaje(self, mensaje):
		for p in range(len(mensaje)):
			if self.__mensaje[p] != mensaje[p]:
				self.__mensaje[p] = mensaje[p] 

	def getMensaje(self):
		return self.__mensaje

	def getProceso(self):
		return self.__proceso

	def enviaMensaje(self):
		pass

	def __str__(self):
		self.__Mensaje= []
		self.__Mensaje.append(self.__proceso)
		self.__Mensaje.append(self.__mensaje)
		return self.__Mensaje
