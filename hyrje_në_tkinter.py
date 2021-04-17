
# Moduli tkinter është modul i integruar me Python.
# Tkiner përdoret për të krijuar GUI e programeve.

import tkinter as tk
# importo modulin tkinter si tk (emri me të cilin do t'i referohemi më vonë)

from tkinter import *
# nga moduli tkinter importo të gjithçka
# mënyra kryesore për të importuar pothujse të gjitha metodat dhe mjetet e këtij moduli

# Në Tkinter gjithçka është një widget - mini-aplikacion
# Gjëja e parë që krijohet është widget kryesor ose dritarja kryesore e GUI (ndëfaqes së përdoruesit)

dritare_kryesore = Tk()

# Për të shfaqur tekst krijojmë një widget Label
# Për të  krijuar gjithçka në Tkinter  është një proçes me dy hapa:
# 1. Në fillim përcaktojmë atë që duam të krijojmë.
# 2. Më pas e vendosim në ekran.


# Hapi i parë: KRIJIMI

etiketë_teksti = Label(dritare_kryesore, text="Përshëndetje botë!")
# emërtimi = lloji i widget (pozicioni, elementët e tjerë të widget)
# Label() është një funksion për paraqitjen e tekstit
# vendosim dritare_kryesore sepse aty ku duam të pozicionojmë widget
# text = " teksti" vendosim tekstin që duam të afishojmë

# Hapi i dytë: VENDOSJA NË EKRAN

# në dritare_kryesore
# me metodën pack() = paketo
# e vendosim në vendin e parë të disponueshëm

etiketë_teksti.pack()
# marrim widgetin tonë dhe e paketojmë në ekran

# Gjëja e fundit që duhet të krijojmë është një unazë eventesh.
# Një unazë eventesh: kur ju keni një GUI ose një program që po ekzekutohet
# është duke looping në mënyrë konstante dhe në këtë mënyrë është në 
# gjendje të zbulojë se çfarë po ndodh. Ndërkohë që po looping ju mund të 
# lëvizni shenjën e kursorit në program dhe do të vërë re pozicionin e tij. # Edhe kur klikoni një buton.
# Kur një program përfundon është momenti kur kjo unazë përfundon.
# Unazat vazhdojnë të punojnë derisa plotësohet një kusht i caktuar.

dritare_kryesore.mainloop()
# unaza kryesore e dritares




