#!/usr/bin/bash


echo "Instalando pip ..."
echo ""
sudo apt install python3-pip -y

echo "Instalando gTTS ..."
echo ""
pip3 install gTTS

cp voice.py ~/

echo "Creando ~/voices"
mkdir ~/voices

echo ""
echo "Listo, se supone que todo quedo instalado. :)"
