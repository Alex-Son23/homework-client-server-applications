# 5. Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовывает результат из байтовового типа данных в строковый без ошибок
# для любой кодировки операционной системы.
import locale
import platform
import subprocess


def ping_to_service(URL):
    default_encoding = locale.getpreferredencoding()
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '2', URL]
    with subprocess.Popen(args, stdout=subprocess.PIPE) as process:
        for line in process.stdout:
            print(f'encoded in {default_encoding} line - {line}')
            line = line.decode(default_encoding).encode('utf-8')
            print(f"decoded in utf-8 - {line.decode('utf-8')}")


if __name__ == "__main__":
    ping_to_service('yandex.ru')
    ping_to_service('youtube.com')

