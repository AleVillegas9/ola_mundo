# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:56:19 2024

@author: Abraxalandro
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

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-



#Paso 2: Ponemos el select box. 

categoria_usur = st.selectbox("Elije la categoria que enmarca tu caso: ", ['Acuerdos Organizacionales del Consejo de la Judicatura Federal', 'Normatividad Relevante para Órganos Jurisdiccionales', 'Nomatividad Relevante para Áreas Administrativas']) 

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                #Clasificador
#Nota importante: El proceso de clasificación se llevó  cabo en un paso previo (Ver archivo de clasifiación). Por cuestiones de optimización, así solamente se recuperan los resultados de ese proceso, y se liga cada categoria con el resulado arrojado previamente.  (Ver paso 12 de series2_aymr_clasificador) o lo corro, desde la v2. 


#Paso 3: Aplicamos la clasificacion

if st.button ('Clasificar'):
    st.markdown ('Las normas relevantes para la categoria seleccionada son:')
    if categoria_usur == 'Acuerdos Organizacionales del Consejo de la Judicatura Federal':
        st.write('1. Nombre de la Norma: 2014-56-1-AC_V80\n Link: https://apps.cjf.gob.mx/normativa/Recursos/2014-56-1-AC_V80.PDF\n Resumen: El Consejo de la Judicatura Federal emitió un acuerdo integral que describe las disposiciones administrativas para sus actividades, enfatizando la independencia, simplificando los procesos regulatorios y abordando diversos aspectos como los recursos humanos, la presupuestación, procedimientos de adquisición y gobernanza digital. El acuerdo contempla normas para el uso de firmas electrónicas, herramientas digitales y el manejo de archivos personales para servidores públicos, así como lineamientos para el uso de códigos QR, reserva fondos y procesos de adquisición. También detalla los procedimientos para administrar los fondos de ahorro, proporcionar servicios de cuidado infantil y apoyo de vivienda para los funcionarios públicos, al tiempo que enfatiza el cumplimiento de las leyes, regulaciones y el bienestar de los niños y servidores públicos. Además, el documento describe los procedimientos para arrendar, adquirir, administrar y enajenar propiedades inmobiliarias, la gestión financiera y los requisitos de presentación de informes dentro del Consejo de la Judicatura Federal. También discute acuerdos relacionados con la protección civil, los nombramientos judiciales y la reestructuración organizativa, con un enfoque en mejorar la transparencia, la rendición de cuentas y la eficiencia dentro del Consejo.\n\n2. Nombre de la Norma: 2013-40-2-AC_V72\n Link: https://apps.cjf.gob.mx/normativa/Recursos/2013-40-2-AC_V72.PDF\n Resumen: El documento emitido por el Consejo de la Judicatura Federal en 2013 describe la organización, funciones y reformas dentro de la Judicatura Federal de México. Se centra en modernizar las normas institucionales, aclarar los procedimientos y garantizar la eficiencia y seguridad jurídica. El documento detalla las responsabilidades y funciones de varios departamentos dentro del Poder Judicial, incluida la supervisión de asuntos judiciales, la prestación de apoyo legal, la administración de finanzas, la implementación de políticas anticorrupción y coordinar los esfuerzos de comunicación. También describe los acuerdos realizados por el Consejo entre 2013 y 2023, abordando reformas y modificaciones en diversos aspectos de la organización y el funcionamiento del Consejo.\n\n3. Nombre de la Norma: 2018-45-1-AC_V12\n Link: https://apps.cjf.gob.mx/normativa/Recursos/2018-45-1-AC_V12.PDF\n Resumen: El Acuerdo General del Pleno del Consejo de la Judicatura Federal establece disposiciones para las responsabilidades administrativas, el control financiero y la rendición de cuentas dentro del poder judicial. Describe la autoridad del Consejo para supervisar la judicial, emitir acuerdos generales, regular investigaciones y sanciones por responsabilidades administrativas, y enfatizar principios como la legalidad, la presunción de inocencia y el respeto a los derechos humanos. El documento detalla los procedimientos para investigar y sancionar las responsabilidades administrativas, incluida la creación de una Unidad de Investigación de Responsabilidades Administrativas, declaración de bienes e intereses, responsabilidades de los servidores públicos, imposición de sanciones, notificaciones, medidas cautelares, reembolso de ingresos perdidos, sanciones económicas, monitoreo de declaraciones de activos y manejo de procedimientos de responsabilidad administrativa. También enfatiza la transparencia, la rendición de cuentas y la importancia de incorporar la perspectiva de género en los casos de conducta sexual inapropiada o violencia de género. Además, el documento describe los procedimientos y regulaciones para la responsabilidad administrativa, incluida la presentación de apelaciones, reconsideraciones, quejas contra decisiones, violaciones, medidas para restablecer el status quo, aplicación de sanciones, sistema de justicia en línea, evaluaciones financieras de servidores públicos, inspección de órganos judiciales, entrega y recepción de materiales administrativos, conciliación de saldos bancarios, lineamientos para investigaciones administrativas, acuerdos relacionados con la Reforma Laboral de Justicia, creación de Juzgados Federales de Trabajo e incorporación de perspectiva de género en los procesos disciplinarios judiciales.')
    elif categoria_usur == 'Normatividad relevante para Órganos Jurisdiccionales':
        st.write('1. 1.	Nombre de la Norma: 2014-56-1-AC_V80\n Link: https://apps.cjf.gob.mx/normativa/Recursos/2014-56-1-AC_V80.PDF\n Resumen: El Consejo de la Judicatura Federal emitió un acuerdo integral que describe las disposiciones administrativas para sus actividades, enfatizando la independencia, simplificando los procesos regulatorios y abordando diversos aspectos como los recursos humanos, la presupuestación, procedimientos de adquisición y gobernanza digital. El acuerdo contempla normas para el uso de firmas electrónicas, herramientas digitales y el manejo de archivos personales para servidores públicos, así como lineamientos para el uso de códigos QR, reserva fondos y procesos de adquisición. También detalla los procedimientos para administrar los fondos de ahorro, proporcionar servicios de cuidado infantil y apoyo de vivienda para los funcionarios públicos, al tiempo que enfatiza el cumplimiento de las leyes, regulaciones y el bienestar de los niños y servidores públicos. Además, el documento describe los procedimientos para arrendar, adquirir, administrar y enajenar propiedades inmobiliarias, la gestión financiera y los requisitos de presentación de informes dentro del Consejo de la Judicatura Federal. También discute acuerdos relacionados con la protección civil, los nombramientos judiciales y la reestructuración organizativa, con un enfoque en mejorar la transparencia, la rendición de cuentas y la eficiencia dentro del Consejo.\n\n2. Nombre de la Norma: 2020-12-0-AC_V07\n Link: https://apps.cjf.gob.mx/normativa/Recursos/2020-12-0-AC_V07.PDF\n Resumen: El Acuerdo General 12/2020 del Pleno del Consejo de la Judicatura Federal en México se centra en regular el uso de archivos electrónicos y videoconferencias en materia judicial para mejorar el acceso a la justicia, particularmente durante la COVID-19 pandemia. Permite el uso de medios electrónicos en los procedimientos judiciales, describe las pautas para las notificaciones electrónicas, las firmas digitales y las videoconferencias, y enfatiza la importancia de mantener la integridad y la seguridad de archivos electrónicos. El documento tiene como objetivo modernizar y agilizar el proceso legal a través de medios digitales al tiempo que garantiza la seguridad y validez de los documentos electrónicos. También detalla los esfuerzos de modernización del Consejo de la Judicatura Federal, incluida la implementación de la tecnología de videoconferencia, y enfatiza la importancia de la seguridad, el cifrado y el respeto de los derechos de todas las partes involucradas en los procedimientos legales.\n\n3. Nombre de la Norma: 2018-28-2-AC_V03\n Link: https://apps.cjf.gob.mx/normativa/Recursos/2018-28-2-AC_V03.PDF\n Resumen: El Consejo de la Judicatura Federal emitió un acuerdo general sobre la protección de datos personales, que describe los procedimientos para manejar las solicitudes y garantizar el cumplimiento de las leyes de protección de datos. Discute los principios para proteger los datos personales, el consentimiento para el procesamiento de datos y medidas para la seguridad de los datos. El documento también establece responsabilidades para los servidores públicos en el manejo de datos personales y describe los procedimientos para ejercer los derechos ARCO. Adicionalmente, detalla la implementación de la mano de obra reformas de justicia, incluida la creación de Tribunales Federales de Trabajo en varios estados de México.')
    else:
        '1. Nombre de la Norma: 2014-56-1-AC_V80\n Link: https://apps.cjf.gob.mx/normativa/Recursos/2014-56-1-AC_V80.PDF\n Resumen: El Consejo de la Judicatura Federal emitió un acuerdo integral que describe las disposiciones administrativas para sus actividades, enfatizando la independencia, simplificando los procesos regulatorios y abordando diversos aspectos como los recursos humanos, la presupuestación, procedimientos de adquisición y gobernanza digital. El acuerdo contempla normas para el uso de firmas electrónicas, herramientas digitales y el manejo de archivos personales para servidores públicos, así como lineamientos para el uso de códigos QR, reserva fondos y procesos de adquisición. También detalla los procedimientos para administrar los fondos de ahorro, proporcionar servicios de cuidado infantil y apoyo de vivienda para los funcionarios públicos, al tiempo que enfatiza el cumplimiento de las leyes, regulaciones y el bienestar de los niños y servidores públicos. Además, el documento describe los procedimientos para arrendar, adquirir, administrar y enajenar propiedades inmobiliarias, la gestión financiera y los requisitos de presentación de informes dentro del Consejo de la Judicatura Federal. También discute acuerdos relacionados con la protección civil, los nombramientos judiciales y la reestructuración organizativa, con un enfoque en mejorar la transparencia, la rendición de cuentas y la eficiencia dentro del Consejo.\n\n2. Nombre de la Norma: 2018-45-1-AC_V12\n Link: https://apps.cjf.gob.mx/normativa/Recursos/2018-45-1-AC_V12.PDF\n Resumen: El Acuerdo General del Pleno del Consejo de la Judicatura Federal establece disposiciones para las responsabilidades administrativas, el control financiero y la rendición de cuentas dentro del poder judicial. Describe la autoridad del Consejo para supervisar la judicial, emitir acuerdos generales, regular investigaciones y sanciones por responsabilidades administrativas, y enfatizar principios como la legalidad, la presunción de inocencia y el respeto a los derechos humanos. El documento detalla los procedimientos para investigar y sancionar las responsabilidades administrativas, incluida la creación de una Unidad de Investigación de Responsabilidades Administrativas, declaración de bienes e intereses, responsabilidades de los servidores públicos, imposición de sanciones, notificaciones, medidas cautelares, reembolso de ingresos perdidos, sanciones económicas, monitoreo de declaraciones de activos y manejo de procedimientos de responsabilidad administrativa. También enfatiza la transparencia, la rendición de cuentas y la importancia de incorporar la perspectiva de género en los casos de conducta sexual inapropiada o violencia de género.\n\n3. Nombre de la Norma: 2013-40-2-AC_V72\n Link: https://apps.cjf.gob.mx/normativa/Recursos/2013-40-2-AC_V72.PDF\n Resumen: El documento emitido por el Consejo de la Judicatura Federal en 2013 describe la organización, funciones y reformas dentro de la Judicatura Federal de México. Se centra en modernizar las normas institucionales, aclarar los procedimientos y garantizar la eficiencia y seguridad jurídica. El documento detalla las responsabilidades y funciones de varios departamentos dentro del Poder Judicial, incluida la supervisión de asuntos judiciales, la prestación de apoyo legal, la administración de finanzas, la implementación de políticas anticorrupción y coordinar los esfuerzos de comunicación. También describe los acuerdos realizados por el Consejo entre 2013 y 2023, abordando reformas y modificaciones en diversos aspectos de la organización y el funcionamiento del Consejo. '

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*

#                               Chat

#Paso 4: Headersm, instucciones y selección de normas del chat

st.header("Chat")
st.subheader("Instrucciones")

st.write("""
         1. Selecciona el nombre de la o las normas con las que deseas chatear
         \n\n\n2. Utiliza el espacio de texto realizar una consulta. La consulta puede ser una pregunta, o alguna instrucción, como por ejemplo, detallar un aspecto de las normas seleccionadas.
         \n\n\n3. Pulsa chatear
         \n\n\n4. Ingresa las consultas que deseees
         \n\n\n5. Cuando termines de usar el chat, por favor "limpia la sessión presionando el botón correspondiente"
         """)

normas_chat = st.multiselect("Elije la o las normas con la que deseas chatear chatear: ",['2013-3-0-AC_V317', '2013-40-2-AC_V72', '2014-36-0-AC_V18', '2014-56-1-AC_V80', '2014-56-2-AC_V37', '2018-28-2-AC_V03', '2018-45-1-AC_V12', '2019-9-2-AC_V05', '2020-3-1-AC_V02', '2020-12-0-AC_V07', '2021-0-134-DD_V15', '2023-6-2-AC_V01'])

#-*-*-*-*-*-*-*-*-*-*-*
#Paso 5: iniciamos una sesión


#Creamos una sesion para almacenar los mensajes en una sesion
if "messages" not in st.session_state: #session_state hace un diccionario
    st.session_state.messages = [] #crea una lista vacia para guadar tanto los mensajes mios como los del bot
    

#Posible mejora: Que se ejecute cuando se refresque la página. 
#Posible mejora 2: Que el usuario ponga su nombre. Aunque aqui el problema sería eliminar todas las sesiones. 

#-*-*-*-**-*-*-*--*-*-

#Paso 6:Iniciamos el index de pinecone

from pinecone import Pinecone

#Guardamos el secreto
#Nota. Guardar el secreto en streamlit

pinecone_api = st.secrets['pinecone_api'] #waaaa

#hacemos la variable
pc = Pinecone(
      api_key=pinecone_api, environment="us-west1-gcp")
    
    
#Iniciamos el index
indexs2 = pc.Index('indexs2') #esto se puede verificar desde mi cuenta en pinecone.com

#-*-*-*-*-*-*-*-*-*-*-**-*-*

#Paso 7: Iniciamos el index como vectostore

from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

#Agarramos el secreto de la apikey
openai_api = st.secrets['openai_api']


#Creamos el embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key= openai_api)

#Hacemos el vectostore
vector_store_chat = PineconeVectorStore(index = indexs2, embedding= embeddings, text_key= 'contenido')

#-*-*-**-*-*-*-*-*-*-*

#Paso 8: Hacemos el rag chain

#Primero cargamos las librerias para hacer el chat, y los system prompts
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

#Segundo definimos el systemprompt
#Nota//punto de mejora: Esto cambiará para cuando se de la opcion de elegir las normas con la que quieres chatear. Esto también seria un punto de mejora, pues la idea es que, en tanto más específico sea el systempropmt mejores respuestas dara. Ideas 1) El mismo systemprompt podría ser un rag chain. 2) expertos. 

system_prompt1 = (f"Eres un consultor experto en leyes. Por lo cual, vas a contestar las preguntas que se te hagan, de una manera clara y precisa. Para responder, te basarás sólo en los documentos que tengan el siguiente nombre {normas_chat}. Además, por favor consteta a los usuarios de manera amigable. Porbablemente te digan sus nombres. Su edad, a que se dedican. Datos por el estilo. ")

#Tercero, hacemos el promt template con el system prompt ya definido anteriormente 
prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt1), #lo que va entre " " es como el rol que ese espera que siga la instruccion que va del otro lado e la coma. en este sentido, le digo que el sistema debe adoptar ese systempropmt
     ("human", "{context}"),]) #aqui el papel de humano adoptara lo que sea que le pregunte

#fuente: https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html


#Cuarto, cargamos el llm y el retriever

from langchain_openai import ChatOpenAI


#cargamos el modelo
llm = ChatOpenAI(
    openai_api_key= openai_api , 
    model_name='gpt-4o-mini', #recuerda que tambien esta disponible chat gto 4o
    temperature=0.0
)

#Transformamos el vectorstore en retriever


retriever = vector_store_chat.as_retriever()


#Quinto, creamos el question answer chain y el rag chain

question_answer_chain = create_stuff_documents_chain(llm, prompt) #aqui recupro el promp y el llm que usare

rag_chain1 = create_retrieval_chain(retriever, question_answer_chain) #aqui recupero el rag con la variable retriever

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

#Paso 9: Hacemos una función para obtener la respuesta


def get_robot_response (user_message):
    response = rag_chain1.invoke({"input": user_message})
    return response ['answer']

#*-*-*-*-*-*-**-*

#Paso 10: Hacemos la función para enviar mensajes



def send_message():
    user_message = st.session_state.user_input #toma el texto del usuario y lo guarda en una variable user_message
    if user_message:
        bot_response = get_robot_response(user_message) #genera la respuesta
        st.session_state.messages.append({"user":user_message, "bot": bot_response}) #recupera la respuesra del usuario, y da la respuesta del bot
        st.session_state.user_input = "" #vacia el campo para que el usuario ponga más cosas

#*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

#Paso 11: Lo implementamos


#Entrada de texto para el usuario

st.text_input ("Tu mensaje", key = "user_input", on_change=send_message) #key = nombre del ussairoo, que está en st.session_state.  on_change = me dice con que funcion de mensaje se va a usar el input


#Mostrar el chat

for message in st.session_state.messages: #itera sobre todos los mensajes guardados. Esto es lo que permite que se tenga memoria. 
    with st.chat_message("user"):
        st.markdown(message["user"])
    with st.chat_message("bot"):
        st.markdown (message["bot"])
        
#-**-*-*-*-*-*-*-*-*-*-*-*

#Paso 12: cerrar sesión


if st.button("Limpiar chat// reiniciar aplicación"):
    st.session_state.messages = []


#-**-**-*-*-*-**- 
#Psso X: Referencias

st.header ("Referencias")

st.markdown("Enlace al consejo de la judicatura: https://www.cjf.gob.mx/") #Poner un enlace
st.markdown("Enlace a la normativa aplicable: https://apps.cjf.gob.mx/normativa/Index") #Aqui poner los links al repositorio de normas.

st.markdown("Enlace CIDE: https://www.cide.edu/")

st.markdown("Cualquier duda, sugerencia, o error, por favor comunicarlo a jesus.villegas@alumnos.cide.edu")

st.markdown("Aplicación realizada por: Abraxalandro")

#Nota: ¿Qué otros links serían relevantes?