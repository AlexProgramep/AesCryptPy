import click
import pyAesCrypt
import os


@click.group()
def mycommands():
    pass


@click.command()
@click.option("--file", prompt="Введіть назву файлу або шлях до нього", help="Назва файлу, який шифруватиметься.")
@click.option("--password", prompt="Введіть пароль", help="Шифрує файл на цей пароль.")
def encrypt(file, password):
    size = 512 * 1024

    try:
        pyAesCrypt.encryptFile(
            str(file),
            str(file) + ".crp",
            password,
            size
        )
        click.echo(f"""{str(file)} зашифрований у формат .crp
Пароль: {password}""")
    except Exception:
        click.echo("Введено неправильну назву/шлях файлу.")


@click.command()
@click.option("--file", prompt="Введіть назву файлу або шлях до нього", help="Назва файлу, який дешифруватиметься.")
@click.option("--password", prompt="Введіть пароль", help="Дешифрує файл на цей пароль..")
def decrypt(file, password):
    size = 512 * 1024

    try:
        pyAesCrypt.decryptFile(
            str(file),
            str(os.path.splitext(file)[0]),
            password,
            size
        )

        click.echo(str(file) + " дешифрований")
    except Exception:
        click.echo("Введено неправильний пароль або назву/шлях файлу.")



mycommands.add_command(decrypt)
mycommands.add_command(encrypt)

if __name__ == "__main__":
    mycommands()
