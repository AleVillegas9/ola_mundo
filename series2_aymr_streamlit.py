# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:30:01 2024

@author: Abraxaladro

Descripción: Esta es la parte frontend del programa. 
"""
#Paso 0: Cargar libreria
import streamlit as st


#Paso 1: Datos generales

st.image("judicatura.jpg", use_column_width=True) #Quizá también añadir un logotipo del proyecto. Que lo haga la IA xd. 

st.title('Asistente jurídico Aymr') #Cambiar el nombre cuando se decida uno

st.header("Aymr es un asistente jurídico, impulsado con inteligencia artificial, que te ayudará en la busqueda de normas que sean relevantes para tu caso. Además de que te permitirá interactuar con dichas normas. Su funcionamiento es muy sencillo. Primero debes de seleccionar la categoria en la que se enmarca tu caso en cuestión. Aymr te dará una lista de las normas con una mayor posibilidad de relacionarse con tu caso. Segundo, elije una norma con la que quieras chatear, y hazle preguntas.")  #Mejorar descripción

st.header("Esta herramienta es sólo de apoyo para la labor de los abogados. DE NINGUNA MANERA SUSTITUYE LA LABOR DE INVESTIGACIÓN Y AUTONOMÍA DEL ABOGADO") #Pesar en más advertencias. 

#Paso 2: Selección sobre qué es tu caso. 
categoria_usur = st.selectbox("Elije la categoria que enmarca tu caso: ", ['Acuerdos Organizacionales del CJF', 'Normatividad relevnte para Órganos Jurisdiccioanales', 'Nomatividad relevante para Áreas Administrativas']) #Estas son todas las categorias? Ya me confundí, porque no todas estas son normas, hay proyectos, etc. Además, cuál es la diferencia entre críterios a secas y los otros dos? ESTA RARA LA LISTA, no parecen categorias de normas. Por ejemplo si mi caso es de fraude, cómo lo pongo. A menos, que no sea un repositiorio de solo normas, sino de varios tipos de documentos. 


#Nota 1: Se me ocurren algunas opciones para lograr este paso
    #A) No sé que tan pertinente sea hacerlo multiselección. 
    #B) En teoria se le podría pedir al abogado que ingrese un resumen de no sé 1000 palabras con los puntos más importantes de su caso. 
    #C) Igual en teoría, se podría solicitar que ponga un pdf completo con el caso en cuestion, y la app te diría sobre qué categorias es más probable que se enmarque. 
    #D) Se podrían implementar todas juntas. 
#En lo personal me iría por la opción que puse en la APP, porque 1) Optimiza el proceso, 2) Le da un alto grado de autonomía al abogado. 


st.write(f'haz seleccionado {categoria_usur} El nombre de las normas relevantes para tu caso son: PONER RESPUESTA DEL LLM')

#Nota 2: ¿Cómo se va a saber cuántas normas se van a regresar?
    #A) Poner un top K. Opcion relatiamente fácil porque el mismo codigo de los embedding te dice cuantos resultados quieres que te de. Además, como determinamos el K optimo?
    #B) Todas las normas que rebase cierto rango de probabilidad. Un poco más complicado de programar. como determinar la probabilidad adecuada? Quiza una actualizacion es que el usuario pueda elejir el nivel de probabilidad. 

#Yo me iría por la primera opción. Pondría un K razonablemente grande. Y se compensaria porque el usuario podría utilizar el chat para comprobar que tanto la norma se adapta a su caso. Además, sería más optimo, que agregar otra funciin que calcule probabilidad. 


#Paso 3: Chatea con la norma. 

norma_chat = st.multiselect("Elije la o las normas con la que deseas chatear chatear: ",['2013-3-0-AC_V317', '2013-40-2-AC_V72', '2014-36-0-AC_V18', '2014-56-1-AC_V80', '2014-56-2-AC_V37', '2018-28-2-AC_V03', '2018-45-1-AC_V12', '2019-9-2-AC_V05', '2020-3-1-AC_V02', '2020-12-0-AC_V07', '2021-0-134-DD_V15', '2023-6-2-AC_V01'])
                          


query = "Tu pregunta a la norma"

st.text_area ('La respuesta a tu duda {query} es LO QUE DE EL CHAT')

#Paso 4: Referencias

st.markdown("Enlace al consejo de la judicatura: (https://www.cjf.gob.mx/)") #Poner un enlace
st.markdown("Enlace a la normativa aplicable: (https://apps.cjf.gob.mx/normativa/Index)") #Aqui poner los links al repositorio de normas.

st.markdown("Enlace CIDE: (https://www.cide.edu/)")

#Nota: ¿Qué otros links serían relevantes?
