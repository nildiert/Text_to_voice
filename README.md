# Voz a texto

----
## Instalación
* Clona este repositorio

```
git clone https://github.com/nildiert/Text_to_voice.git && cd Text_to_voice
```

* Ejecuta el siguiente comando para configurar e instalar los paquetes necesarios:

```
./configure.sh
```

* Dale uso!

----
# Uso

Por ahora deberas ingresar a la carpeta donde hayas clonado el repositorio cada que inicies el computador y ejecutar el archivo `./configure.sh`.

Esto creara el alias `voice`, que te permitirá convertir un archivo de texto a voz.

Para ello, escribe `voice arg1 arg2`.

En donde:

* **`arg1`** es el nombre del archivo de texto
* **`arg2`** es el nombre del archivo mp3 que se creará (No es necesario especificar la terminación .mp3).

>Los archivos .mp3 se crearan en la carpeta `~/voices/`



----
## Changelog
* 7-Abr-2020 Creation

----
## Thanks
* [gTTS](https://pypi.org/project/gTTS/)
