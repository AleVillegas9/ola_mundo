# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:42:08 2024

@author: javal
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:30:01 2024

@author: Abraxaladro

Descripción: Esta es la parte frontend del programa. 
"""
#Paso 0: Cargar libreria basica
import streamlit as st

#*-*-*-**-*-*-*-**-*-*-*-
                                #Datos generales

#Paso 1: Datos generales


st.title('Asistente jurídico Aymr') #Cambiar el nombre cuando se decida uno

st.image("judicatura.jpg", use_column_width=True) #Quizá también añadir un logotipo del proyecto. Que lo haga la IA xd. 


st.subheader("Aymr es un asistente jurídico, impulsado con inteligencia artificial, que te ayudará en la busqueda de normas que sean relevantes para tu caso. Además de que te permitirá interactuar con dichas normas. Su funcionamiento es muy sencillo. Primero debes de seleccionar la categoria en la que se enmarca tu caso en cuestión. Aymr te dará una lista de las normas con una mayor posibilidad de relacionarse con tu caso. Segundo, elije una norma con la que quieras chatear, y hazle preguntas")


st.subheader(" ADVERTENCIA: Esta herramienta es sólo de apoyo para la labor de los abogados. DE NINGUNA MANERA SUSTITUYE LA LABOR DE INVESTIGACIÓN Y AUTONOMÍA DEL ABOGADO")


st.header("Clasificador")

st.subheader ("Instrucciones: A continuación se te presenta una lista de distintas categorias en las que se clasifican las normas jurídicas. Por favor, selecciona la categoria de la cual te gustaría conocer los textos relacionados")