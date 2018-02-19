# Desarrollo en Python - Requisitos

Necesitaremos tener varias herramientas instaladas en nuestro ordenador:

- Python 2
- Python 3
- Virtualenv
- Visual Studio Code (o cualquier otro editor o entorno de desarrollo)

A continuación encontraréis instrucciones específicas para cada sistema operativo (OS X y Windows).

## 1. Instalación de Python 
### 1.1. Instalación de Python en OS X

Para instalar Python usaremos [Homebrew](https://brew.sh), un conocido gestor de paquetes para OS X. Lo primero que haremos es comprobar si lo tenemos instalado. Para ello debemos abrir una ventana con Terminal (o iTerm2) y teclear:

``` sh
brew --version
```
Si Homebrew está instalado veremos algo parecido a esto:

``` sh
$ brew --version
Homebrew 1.5.2
Homebrew/homebrew-core (git revision 1d5b; last commit 2018-01-24)
$
``` 
En ese caso nos limitaremos a asegurar que tanto el gestor de paquetes como el repositorio de paquetes disponible están actualizados lanzando este comando:

``` sh
brew update
```
Si Homebrew no estuviese en nuestro sistema deberemos instalarlo. Es tan simple como ejecutar el siguiente comando:

``` sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

La instalación de algunos paquetes requiere disponer de un compilador. Para ello, lo más fácil es instalar las XCode's Command Line Tools con este comando:

``` sh
xcode-select --install
```

En principio ya está todo listo para instalar Python 2 y Python 3 con Homebrew tecleando:

``` sh
brew install python2 python3 
```
Una vez finalizada la instalación podemos comprobar que ha ido bien:

``` sh
$ python --version
Python 2.7.10
$ python2 --version
Python 2.7.14
$ python3 --version
Python 3.6.4
``` 

Lógicamente, si los números de versiones son distintos deberían ser mayores.

OS X viene con una instalación de Python 2 que es utilizada y actualizada por el propio sistema operativo. Se recomienda utilizar otra instalación de Python 2 para uso general y, de esta manera, no interferir con la que usa el sistema operativo. Por ello vemos que hay 3 versiones instaladas.

Cuando instalamos Python se instala también una herramienta, Pip, para instalar paquetes/bibliotecas/librerias en Python. En consecuencia, podemos comprobar también que tenemos 3 versiones instaladas:

``` sh
$ pip --version
pip 1.5.4 from /Library/Python/2.7/site-packages (python 2.7)
$ pip2 --version
pip 9.0.1 from /usr/local/lib/python2.7/site-packages (python 2.7)
$ pip3 --version
pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)
``` 

El siguiente paso es instalar Virtualenv.

### 1.2. Instalación de Python en Windows

Para instalar Python hay que bajarse sitio web oficial de [Python](https://www.python.org/downloads/windows/) el instalador específico para el sistema que tengamos (32 bits o 64 bits). Lo haremos para ambas versiones, Python 2 y Python 3.

Durante la instalación es necesario marcar siempre la opción "Add Python X.X to PATH". Además, en el caso de Python 3 dejaremos marcada la opción "Install launcher for all users (recommended)".

Una vez finalizadas las instalaciones podemos comprobar que ha ido bien utilizando Python Launcher desde una ventana de comandos. Así, para entrar en Python 2 ejecutaremos:

``` sh
py -2 
```

Para salir del interprete deberemos teclear:

``` python
exit()
``` 

Y para entrar en Python 3 ejecutaremos:

``` sh
py -3
```

Otra vez, para salir del interprete deberemos teclear:

``` python
exit()
``` 

También podemos comprobar que se han instalado las versiones del gestor de paquetes en Python Pip correspondientes a cada versión de Python:

``` sh
> pip --version
pip 9.0.1 from  c:\python27\lib\site-packages (Python 2.7.13)
> pip3 --version
pip 9.0.1 from c:\users\[USERNAME]\appdata\local\programs\python\python36-32\lib\site-packages (python 3.6)
``` 

El siguiente paso es instalar Virtualenv.

## 2. Instalación de Virtualenv

[virtualenv](https://virtualenv.pypa.io/en/stable/) es una utilidad para crear entornos Python aislados.

### 2.1. Instalación en OS X

Para instalar virtualenv en OS X utilizaremos la versión de pip instalada con Python 3:

``` sh
pip3 install --upgrade virtualenv 
```

### 2.2. Instalación en Windows

Para instalar virtualenv en Windows utilizaremos pip:

``` sh
pip install --upgrade virtualenv 
```

## 3. Instalación de Visual Studio Code

Podemos utilizar cualquier editor para escribir código. Os recomendamos [Visual Studio Code](https://code.visualstudio.com). Otras alternativas son:

- [Atom](https://atom.io)
- [PyCharm](https://www.jetbrains.com/pycharm/) 

Para instalar Visual Studio Code es necesario bajarse el instalador apropiado a nuestro sistema operativo (OS X o Windows 32 bits o Windows 64 bits) y lanzarlo.




## Anexo 1. Como desinstalar en OS X una versión de Python no instalada con Homebrew

En una instalación hecha con Homebrew el intérprete de Python está en ```/usr/local/bin/python3```. Podemos comprobarlo:

``` shell
$ which python3
/usr/local/bin/python3
$ which python2
/usr/local/bin/python2
```

Imaginemos que ya tenemos la versión 3.4 instalada (no con Homebrew):

``` shell
$ which python3
/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
```

Para proceder a su desintalación debemos lanzar los siguientes comandos desde un terminal:

``` shell
sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.4/
sudo rm -rf /Applications/Python\ 3.4/
ls -l /usr/local/bin | grep '../Library/Frameworks/Python.framework/Versions/3.4'  | awk '{print $9}' | tr -d @ | xargs rm
```

Es probable que la variable de entorno PATH incluya el directorio ```/Library/Frameworks/Python.framework/Versions/3.4/bin```:

``` shell
$ echo $PATH
/Library/Frameworks/Python.framework/Versions/3.4/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/VMware Fusion.app/Contents/Public:/opt/X11/bin:/usr/local/bin/jamf
``` 

Podemos editar el fichero ```~/.bash_profile``` para quitarlo con este comando:

``` shell
open -a textedit ~/.bash_profile
```

Una vez en el editor hay que borrar las líneas:

```
PATH="/Library/Frameworks/Python.framework/Versions/3.4/bin:$PATH"
export PATH
```

Con esto debería estar completamente desinstalada la versión 3.4. Obviamente, si la versión es otra el proceso es el mismo cambiando el número de versión.

Si hubiesemos instalado python3 -para seguir con el ejemplo- con Homebrew antes de desinstalar el Python 3 previamente instalado sin Homebrew deberemos completar la instalación lanzando:

``` shell
brew unlink python3
brew link python3
```

Si no lo hubiesemos instalado, lo haremos tal como se describe en las instrucciones iniciales mediante este comando:

``` shell
brew install python3
```



## Anexo 2. Como usar virtualenv

### Prólogo

Python, como muchos otros lenguajes de programación, dispone de un repositorio público donde es posible encontrar "paquetes" -también llamados blibliotecas o librerías- que facilitan la implementación de una determinada funcionalidad. Estos paquetes no son nada más que módulos Python, es decir ficheros con código. Podemos encontrar desde paquetes que simplifican el tratamiento de datos en un formato determinado, por ejemplo leer una hoja de cálculo, hasta paquetes que permiten interactuar con otros sistemas, como una plataforma de colaboración.

pip es el sistema de gestión de paquetes que usaremos para instalar, actualizar y desinstalar modulos de Python en nuestro sistema.

Al instalar estos paquetes en nuestro sistema estarán disponibles para usarlos en cualquier programa Python que desarrollemos. El principal beneficio que aporta esta aproximación es que no hace falta descargar/copiar los módulos cada vez que los queramos usar en un programa.

Sin embargo, esta aproximación crea un problema al introducir dependencias. Podemos tener un programa que requiere un paquete en una versión determinada y otro que requiere el mismo paquete en una versión distinta, que implementa un cambio de funcionalidad. pip solo mantiene instalada una versión del paquete por lo que si al cabo de un tiempo de instalar un paquete como dependencia de un programa que estemos usando lo volvemos a instalar, por ejemplo como dependencia de un nuevo programa que queremos probar, es posible que el primer programa deje de funcionar. 

Además, es habitual que un paquete incluya dependencias a otros paquetes con lo cual el problema se hace cada vez mayor.

virtualenv nos ayuda a gestionar este problema de dependecias creando copias del entorno Python, intérprete y paquetes, por aplicación. De esta forma podemos mantener entornos aislados inmunes a cambios en otros entornos. 

### Uso en virtualenv

Para crear un entorno virtual persistente lo primero que debemos hacer es crear un directorio para nuestra aplicación, situarnos en él y ejecutar virtualenv:

``` shell
mkdir myapp
cd myapp
virtualenv --python python3 env
```

Podemos indicar una versión específica de Python, de entre las que tengamos instaladas, por medio del flag ```--python```. También deberemos indicar el nombre del directorio donde se clonará la instalación de Python y, por lo tanto, donde se instalarán todas la dependencias. Es habitual usar ```env``` para este fin.

A partir de entonces, cada vez que necesitemos activar este entorno deberemos, desde el directorio de la aplicación, lanzar este comando:

- Para OS X:

``` shell
source env/bin/activate
```

- Para Windows:

``` shell
./env/bin/activate
```

Si ya no necesitamos este entorno podemos desactivarlo lanzando este comando:

``` shell
deactivate
```

## Anexo 3. Atajos de teclado para Visual Studio Code

Para ser más rápidos con Visual Studio Code:

- [Keyboard shortcuts for macOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
- [Keyboard shortcuts for Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
