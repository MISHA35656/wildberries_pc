# Wildberries PC
<img src="https://raster.shields.io/badge/version-0.01-green.png">
<img src="https://raster.shields.io/badge/status-maintaining-green.png">
<img align="center" src="https://raw.githubusercontent.com/MISHA35656/wildberries_pc/main/favicon.ico" width="512" height="512">
Wildberries PC это **неофициальная** программа для прямого доступа к Wildberries

## Установка

### Для Windows
Скачайте скомпилированную для Windows версию <a href="https://disk.yandex.ru/d/MDh5y_q0NndYqw">здесь</a>. Её не нужно устанавливать, просто скопируйте в любую папку и введите:
'''batch
/путь/к/файлу/Wildberries PC.exe by
'''
Замените by на нужную страну. ru откроет Wildberries.ru, by - Wildberries.by

### Для Linux
Вам требуется Python 3 и pip. Введите:
'''bash
git clone https://github.com/MISHA35656/wildberries_pc.git
cd wildberries_pc
pip install -r requirements.txt
'''
Вы успешно подготовили Wildberries PC к работе на вашем ПК. Теперь, для запуска вам требуется ввести
'''bash
python3 main.py by
'''
Замените by на нужную страну. ru откроет Wildberries.ru, by - Wildberries.by

#### Компиляция из исходного кода

Данную программу можно компилировать для Windows с помощью pyinstaller. Для этого вам нужно установить pyinstaller ввести в терминал следующее (работает на обоих системах):
'''bash
pyinstaller --noconfirm --onefile --windowed --icon "/home/turbo_mishka/wildberries_pc/favicon.ico"  "/home/turbo_mishka/wildberries_pc/main.py"
'''
Замените /home/turbo_mishka/wildberries_pc/favicon.ico на фавиконку в папке с Wildberries PC. /home/turbo_mishka/wildberries_pc/main.py замените на путь к main.py в папке с Wildberries PC. Если вы хотите отлавливать ошибки, замените --windowed на --console. Аргумент --windowed говорит pyinstallerу чтобы в получившемся .exe не было окна командной строки. Аргумент --console говорит pyinstallerу чтобы в получившемся .exe была командная строка, куда выводятся все printы. Теперь вы имеете файл main.py в папке output вашей домашней папки
