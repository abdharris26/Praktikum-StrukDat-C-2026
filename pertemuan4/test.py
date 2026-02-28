from colorama import Fore, Back, Style, init

init()

print(Fore.RED + "Teks Merah")
print(Fore.GREEN + "Teks Hijau")
print(Fore.BLUE + Back.YELLOW + "teks biru dengan background kuning")
print(Style.RESET_ALL + "kembali normal")