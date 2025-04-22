import sys
import argparse

# Командын мөрийн аргументуудыг авах
print(f"Программын нэр: {sys.argv[0]}")
print(f"Аргументууд: {sys.argv[1:]}")

# Жишээ хэрэглээ: python script.py arg1 arg2
if len(sys.argv) > 1:
    print(f"Эхний аргумент: {sys.argv[1]}")
else:
    print("Аргумент өгөөгүй байна")

# Илүү нарийн CLI-д argparse ашиглах

parser = argparse.ArgumentParser(description='Бүхэл тоонуудыг боловсруулах.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='хуримтлуурт зориулсан бүхэл тоо')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='бүхэл тоонуудыг нэмэх (үндсэн: хамгийн их утгыг олох)')

args = parser.parse_args()
print(args.accumulate(args.integers))