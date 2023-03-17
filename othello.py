import pyfiglet

ascii_banner = "\n" + "-"*73 + "\n"
ascii_banner += str(pyfiglet.figlet_format("OTHELLO", font= "starwars"))
ascii_banner += "-"*73 + "\n"
ascii_banner += " "*28 + "Alexandre Appolaire" + " "*20 +"\n"
ascii_banner += " "*29 + "Lizzy Barthelemy" + " "*20 +"\n"
ascii_banner += " "*32 + "Aline Cisse" + " "*20 +"\n"
ascii_banner += "-"*73
print(ascii_banner)
