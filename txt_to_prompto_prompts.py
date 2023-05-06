import os
import openai
import requests
import json
import shutil

# Recuperar la clave de la API de OpenAI desde localhost:9000
url = "http://localhost:9000/get_open_ai_key"
response = requests.get(url)
response_json = response.json()

if 'message' in response_json:
    api_key = response_json['message'].split(': ')[1]
    openai.api_key = api_key
else:
    print("Error: No se pudo obtener la clave de la API de OpenAI.")
    exit()

# Crear la carpeta txt_to_proc si no existe
if not os.path.exists("txt_to_proc"):
    os.makedirs("txt_to_proc")

# Crear la carpeta txt_processed si no existe
if not os.path.exists("txt_processed"):
    os.makedirs("txt_processed")

# Crear la carpeta prompts_from_csv si no existe
if not os.path.exists("prompts_from_txt"):
    os.makedirs("prompts_from_txt")

# Procesar cada archivo de texto en la carpeta txt_to_proc
for archivo_txt in os.listdir("txt_to_proc"):
    if archivo_txt.endswith(".txt"):
        with open(os.path.join("txt_to_proc", archivo_txt), encoding='utf-8') as txtfile:
            for linea in txtfile:
                prompt_a_procesar = linea.strip()

                try:
                    texto = f"""Dado este ejemplo dónde de esta función: 
                    Generame 10 ideas combinando {{mundo 1}}  y  {{mundo 2}} .
                    Generamos este contendio para archivo json: {{
                        "Título": [
                          "Ideas entre dos mundos"
                        ],
                        "Descripción": [
                          "El objetivo de esta función es el de generar 10 ideas mezclando 2 mundos o cosas "
                        ],
                        "Inputs": [
                          "mundo 1", "mundo 2"
                        ],
                        "Prompt": [
                          "Generame 10 ideas combinando +input_1+  y  +input_2+ . "
                        ],
                        "Actúa como": [
                          "Actúa como un recursos creativo."
                        ]
                    }} ----> Genera el contenido de json para esta función, teniendo en cuenta que los inputs en el prompt tienen este formato +input_1+, +input_2+, etc..: 
                    {prompt_a_procesar}."""

                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=texto,
                        temperature=0.7,
                        max_tokens=1557,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )

                    respuesta = response.choices[0].text.strip()
                    json_respuesta = json.loads(respuesta)

                    nombre_archivo = json_respuesta['Título'][0] + '.json'
                    with open(os.path.join("prompts_from_txt", nombre_archivo), 'w', encoding='utf-8') as outfile:
                        json.dump(json_respuesta, outfile, ensure_ascii=False, indent=4)

                    print(f"Archivo {nombre_archivo} creado.")

                except json.decoder.JSONDecodeError as e:
                    print(f"Error: No se pudo procesar la línea '{prompt_a_procesar}'. Mensaje de error: {str(e)}")
                    continue

        # Mover el archivo de texto procesado a la carpeta txt_processed y eliminar de la carpeta txt_to_proc
        shutil.move(os.path.join("txt_to_proc", archivo_txt), os.path.join("txt_processed", archivo_txt))
        print(f"Archivo {archivo_txt} movido a la carpeta txt_processed.")