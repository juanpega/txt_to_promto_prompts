Este script permite convertir un archivo de texto con prompts en el formato adecuado para usarlos con PROMTO, una herramienta de PROMPTING. PROMTO es un software desarrollado por Innocreatividad, una empresa dedicada a la innovación y la creatividad. Puedes encontrar más información sobre PROMTO y sus características en: https://innocreatividad.com/producto/promto-ai/

Donde `input.txt` es el nombre del archivo de texto con los prompts y `output.json` es el nombre del archivo de salida con el formato de PROMTO. El archivo de texto debe tener un prompt por línea, separado por un salto de línea. El script generará un archivo JSON con un array de objetos, donde cada objeto tiene un atributo `prompt` con el texto del prompt.

This script allows you to convert a text file with prompts into the appropriate format to use them with PROMTO, a prompting tool. PROMTO is a software developed by Innocreatividad, a company dedicated to innovation and creativity. You can find more information about PROMTO and its features at: https://innocreatividad.com/producto/promto-ai/
Where `input.txt` is the name of the text file with the prompts and `output.json` is the name of the output file with the PROMTO format. The text file must have one prompt per line, separated by a line break. The script will generate a JSON file with an array of objects, where each object has an attribute `prompt` with the text of the prompt.

## Example

If you have a text file called `prompts.txt` with the following content:

```
Write a story about time travel.
Write a poem about spring.
Write a love letter to your partner.
```

And you will get a JSON file called `prompts.json`.

These prompts are ready to be used with PROMTO and enjoy its creative potential.
