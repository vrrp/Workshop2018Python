# Python para Geociencias

# Contenido

## Módulo 1

* [01 Introduction](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/01_Introduction.ipynb)
* [02_Estructura y contros de datos](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/02_NatureOfWaves.ipynb)
* [03_Control de flujos](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/03_FourierTransform.ipynb)
* [04. Entrada y salida de datos](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/04_WaveDeconvolution.ipynb)
* [05_Funciones](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/05_RotationWithE.ipynb)
* [06_Módulos y Paquetes](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/06_FFTInPython.ipynb)
* [07_Programación Orientada a Objetos (POO)](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/07_SeeingSound.ipynb)
* [08_Bibliotecas estándar de Python](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/08_STFT.ipynb)

# Módulo 2


Módulos de Python necesarios:

* numpy
* scipy
* matplotlib
* ipython
* scikits.audiolab


# Módulo 3

Módulos de Python necesarios:

* numpy
* scipy
* matplotlib
* ipython
* scikits.audiolab

---

To record audio on your laptop, you can use [sox](http://sox.sourceforge.net/) (note that `rec` is a commnad installed with `sox`).  Here are 2 useful sox commands

* `rec -r 44100 -c 2 -b 16 A4.wav`
    - records at 44100 samples per sec, 2 channels, and 16 bits per sample
* `sox audio_2channels.wav audio_1channel.wav channels 1`
    - converts from 2 channels to 1 channel


