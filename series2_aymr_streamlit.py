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

st.image("judicatura.jpg", use_column_width=True) #Quizá también añadir un logotipo del proyecto. Que lo haga la IA xd. 

st.title('Asistente jurídico Aymr') #Cambiar el nombre cuando se decida uno

st.header("Aymr es un asistente jurídico, impulsado con inteligencia artificial, que te ayudará en la busqueda de normas que sean relevantes para tu caso. Además de que te permitirá interactuar con dichas normas. Su funcionamiento es muy sencillo. Primero debes de seleccionar la categoria en la que se enmarca tu caso en cuestión. Aymr te dará una lista de las normas con una mayor posibilidad de relacionarse con tu caso. Segundo, elije una norma con la que quieras chatear, y hazle preguntas.")  #Mejorar descripción

st.header("Esta herramienta es sólo de apoyo para la labor de los abogados. DE NINGUNA MANERA SUSTITUYE LA LABOR DE INVESTIGACIÓN Y AUTONOMÍA DEL ABOGADO") #Pesar en más advertencias. 

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-

                                #Clasificador
#Paso 2: Cargamos el index de fuentes

#Primero librerias
from pinecone import Pinecone

#Guardamos el secreto
#Nota. Guardar el secreto en streamlit

pinecone_api = st.secrets['pinecone_apikey']

#hacemos la variable
pc = Pinecone(
      api_key=pinecone_api, environment="us-west1-gcp")

# # Iniciamos el index
s2indexfuentes = pc.Index('s2indexfuentes') 

#*-**-*-*-*-*-*-*-*-*-*-*

#Paso 3: Creamos el vecstore para clasificar

#Primero creamos librerias
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

#Segundo, secreteamos la apikey

openai_api = st.secrets['openai_api']


#Primero, creamos el embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key= openai_api)


#Despues Hacemos el vectorstore
vector_store_clasificador = PineconeVectorStore(index = s2indexfuentes, embedding= embeddings, text_key= 'fuente') 


#*-*-*-*-*-*-*-*-

#Paso 4: Convertimos el vectorstore en un retriever para que me de los resultados. 

retrieverprop = vector_store_clasificador.as_retriever(search_type = 'similarity_score_threshold', search_kwargs = {"score_threshold": 0.61}) 

#-**-*-*-*-*-*-*-*-*-*-*-*-*

#Paso 5:Respuesta bruta


#Primero que elija la categoria que quiere
categoria_usur = st.selectbox("Elije la categoria que enmarca tu caso: ", ['Acuerdos Organizacionales del CJF', 'Normatividad relevnte para Órganos Jurisdiccioanales', 'Nomatividad relevante para Áreas Administrativas']) 



#Segundo, construimos una query con esa categoria
query_class = f'¿Qué documentos tratan sobre la categoria {categoria_usur}'


#Tercero hacemos la query
respuestaprop = retrieverprop.invoke(query_class)


#*-*-*-*-*-*--*-*-*

#Paso 6:  Limpieza

#Primero importamos el llm para chatear

from langchain_openai import ChatOpenAI

#cargamos el modelo
llm = ChatOpenAI(
    openai_api_key= openai_api, 
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

#Definimos el system prompt
fake_system_prompt = f"""
Tengo el siguiene texto, el cual contiene una lista de uno o más  textos con nombre, links, y un resumen de los mismos. Por favor, hazme una nueva lista, numerada, en el que vengan esos tres datos por cada texto, pero donde se eliminen los textos repetidos. Deja de enumerar cuando ya no haya más textos nuevos. Entre cada enumaración de cada elemento deja doble espacio. De manera que pueda diferenciar entre cada elemento. El texto es {respuestaprop}
""" 

#Hacemos la limpieza de datos innecesarios

respuesta_limpia = str(llm.invoke(fake_system_prompt))

import re

respuesta_limpia = re.search(r"content='(.*?)'", respuesta_limpia)
if respuesta_limpia:
    content_value = respuesta_limpia.group(1) #Aqui se guarda el string 
    print(content_value)
else:
    print("No se encontró el contenido.")
    
content_value = content_value

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

#Paso 7: Presentamos la respuesta



st.write(f'haz seleccionado {categoria_usur} El nombre de las normas relevantes para tu caso son: {content_value}')





#Paso 3: Chatea con la norma. 

norma_chat = st.multiselect("Elije la o las normas con la que deseas chatear chatear: ",['2013-3-0-AC_V317', '2013-40-2-AC_V72', '2014-36-0-AC_V18', '2014-56-1-AC_V80', '2014-56-2-AC_V37', '2018-28-2-AC_V03', '2018-45-1-AC_V12', '2019-9-2-AC_V05', '2020-3-1-AC_V02', '2020-12-0-AC_V07', '2021-0-134-DD_V15', '2023-6-2-AC_V01'])
                          


query = "Tu pregunta a la norma"

st.text_area ('La respuesta a tu duda {query} es LO QUE DE EL CHAT')

#Paso 4: Referencias

st.markdown("Enlace al consejo de la judicatura: (https://www.cjf.gob.mx/)") #Poner un enlace
st.markdown("Enlace a la normativa aplicable: (https://apps.cjf.gob.mx/normativa/Index)") #Aqui poner los links al repositorio de normas.

st.markdown("Enlace CIDE: (https://www.cide.edu/)")

#Nota: ¿Qué otros links serían relevantes?
