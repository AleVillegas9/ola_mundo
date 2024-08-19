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

st.subheader ("Instrucciones: A continuación se te presenta ua lista de distintas categorias en las que se clasifican las normas jurídicas. Por favor, selecciona la categoria de la cual te gustaría conocer los textos relacionados")

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


categoria_usur = st.selectbox("Elije la categoria que enmarca tu caso: ", ['Acuerdos Organizacionales del Consejo de la Judicatura Federal', 'Normatividad relevante para Órganos Jurisdiccionales', 'Nomatividad relevante para Áreas Administrativas']) 



#Segundo, construimos una query con esa categoria
query_class = f'¿Qué normativa refiere a la categoria llamada {categoria_usur}?' 

#Entre más especifico lo haga, mejores resultados. 


#Tercero hacemos la query


respuestaprop = retrieverprop.invoke(query_class)


#*-*-*-*-*-*--*-*-*

#Paso 6:  Limpieza

#Primero importamos el llm para chatear

from langchain_openai import ChatOpenAI

#cargamos el modelo
llm = ChatOpenAI(
    openai_api_key= openai_api, 
    model_name='gpt-4o-mini',
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


if st.button("Clasificar"):
    st.markdown('Las normas relevantes para la categoria seleccionada son:')
    st.write (f"""
              {content_value}
              """)

#INTENTA DIVIDIRLO 

#El problema, es que no me lo presenta en forma de texto, y no me dal el texto completo, una opcion podria hacer dos st.wrtie. uno con la primera parte de la categoria usada y el segudo con la respuesta. 

#Hasta aqui funciona 13/08/24

#*-*-**-*-*-*-*-*-*--*-*-


                #Inicia la parte del chat con la norma. 
                
st.header("Chat")
st.subheader("Instrucciones: Primero, ingresa tu nombre. Despuéss selecciona el nombre de las normas con las cuales te gustaría chatear. A continuación, utiliza el espacio indicado para empezar a chatear con el conjunto de normas seleccionadas")

id_session = st.text_input ("Ingresa tu nombre")

#Paso 8: Vectostore chat


indexs2 = pc.Index('indexs2')

vector_store_chat = PineconeVectorStore(index = indexs2, embedding= embeddings, text_key= 'contenido')

#*-*-*-*-*-*-*-*

#Paso 9: Hacemos el cuadro de selecccion sobre que con cuales normas quiere chatear el usuario. 

norma_chat = st.multiselect("Elije la o las normas con la que deseas chatear chatear: ",['2013-3-0-AC_V317', '2013-40-2-AC_V72', '2014-36-0-AC_V18', '2014-56-1-AC_V80', '2014-56-2-AC_V37', '2018-28-2-AC_V03', '2018-45-1-AC_V12', '2019-9-2-AC_V05', '2020-3-1-AC_V02', '2020-12-0-AC_V07', '2021-0-134-DD_V15', '2023-6-2-AC_V01'])
                          
#-*-*-*-*-*-**-*-**-


#Paso 10: Hacemos el rag chain

#Primero cargamos las librerias para hacer el chat, y los system prompts
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

#Segundo definimos el systemprompt
#Nota: Esto cambiará para cuando se de la opcion de elegir las normas con la que quieres chatear

system_prompt1 = f"""
Eres un consultor experto en leyes. Por lo cual, vas a contestar las preguntas que se te hagan, de una manera clara y precisa. Para tu respuesta sólo toma en cuenta las normas que tengan el siguiente nombre {norma_chat}
"""

#Tercero, hacemos el promt template con el system prompt ya definido anteriormente 
prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt1), #lo que va entre " " es como el rol que ese espera que siga la instruccion que va del otro lado e la coma. en este sentido, le digo que el sistema debe adoptar ese systempropmt
     ("human", "{context}"),]) #aqui el papel de humano adoptara lo que sea que le pregunte

#fuente: https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html


#Transformamos el vectorstore en retriever


retriever = vector_store_chat.as_retriever()


#Quinto, creamos el question answer chain y el rag chain

question_answer_chain = create_stuff_documents_chain(llm, prompt) #aqui recupro el promp y el llm que usare

rag_chain1 = create_retrieval_chain(retriever, question_answer_chain) #aqui recupero el rago con la variable retriever

#*-*-*-*-*-*-*-*-*-*-*-*-*-
#Paso 10: memory

from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_community.chat_message_histories import SQLChatMessageHistory


#Recuperamos el system propmt
propmt_memory = ChatPromptTemplate.from_messages(
    [("system", "Eres un consultor experto en leyes. Por lo cual, vas a contestar las preguntas que se te hagan, de una manera clara y precisa."),
       MessagesPlaceholder(variable_name="history"),
       ("human", "{input}")]) #Aqui rescatamos el propmt. Pero le agregamos el message placeholder, para que me diga donde va la memoria, y cual es el input humano. Este input será mi query

#Definimos la session de chat que me dara. En este caso uso la de SQL. aunque hay más opciones. Para un demo, este funciona bien
def get_session_history (session_id):
   return SQLChatMessageHistory(session_id, "sqlite:///memory.db")


#Hacemos el runnable con la memoria. 
runnable_rag_memory =  RunnableWithMessageHistory(rag_chain1, get_session_history,
input_messages_key= "input",
history_messages_key= "history")



#-*-*-*-*-*-*-*-*-*-*-*-*-*

#Paso 11: Ponemos nuestra duda





query = st.text_input('Ingresa tu duda')


#Generamos la respuesta
x = runnable_rag_memory.invoke({'input' : f' Soy un abogado que necesita que me resuelvas la siguiente duda {query}. '},
                             config ={"configurable": {"session_id": f"{id_session}"}},)


#La presentamos

respuesta = x ['answer']


if st.button("chatear"):
    st.write (f'{respuesta}')



#-*-*-*-*-*-*-**-*-**-*-*--*-*-*-*
#Paso 12: Limpiamos la sesion
#Limpiar la sesion

from sqlalchemy import create_engine


if st.button("Presiona aqui al términar de usar el chat"):
    engine = create_engine('sqlite:///memory.db')
    chat_history = SQLChatMessageHistory(session_id= id_session, connection_string= engine)
    chat_history.clear
    
                                    #Extras
                                    

#Paso 4: Referencias

st.header ("Referencias")

st.markdown("Enlace al consejo de la judicatura: https://www.cjf.gob.mx/") #Poner un enlace
st.markdown("Enlace a la normativa aplicable: https://apps.cjf.gob.mx/normativa/Index") #Aqui poner los links al repositorio de normas.

st.markdown("Enlace CIDE: https://www.cide.edu/")

st.markdown("Cualquier duda, sugerencia, o error, por favor comunicarlo a jesus.villegas@alumnos.cide.edu")

st.markdown("Aplicación realizada por: Abraxalandro")

#Nota: ¿Qué otros links serían relevantes?
