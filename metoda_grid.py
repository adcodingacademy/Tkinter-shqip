# Pozicionimi me sistemin Grid (rrjetë) të Tkinter
# Sistemi grid është një mënyrë më e mirë për të pozicionuar widget në ekran
# Me pack() widget qëndron në një pozicion në mes edhe kur ndryshohen përmasat e dritares
# Sistemi grid(rrjetë) ka kolona dhe rreshta.
# Numërimi i rreshtave dhe kolonave fillon nga 0
# Me grid()  widget nuk ndryshon kur ndryshojnë përmasat e dritares
# kolona është madhësia që zë një widget
# të gjithë elementët në një sistem grid janë të lidhura me njëri tjetrin


from tkinter import *
dritare_kryesore = Tk()
etiketë_teksti1 = Label(dritare_kryesore, text ="Përshëndetje Botë")
etiketë_teksti2 = Label(dritare_kryesore, text ="Programim në Python")
etiketë_teksti3 = Label(dritare_kryesore, text ="GUI me Tkinter.")

etiketë_teksti1.grid(row=0, column=0)
# etiketë_teksti1 do të vendoset në rreshtin e parë dhe kolonën e parë
# brenda kllapave rrethore mund të vendosim arguementet
etiketë_teksti2.grid(row=1, column=1)
# etiketë_teksti2 do të vendoset në rreshtin e dytë dhe kolonën e tretë
etiketë_teksti3.grid(row=1, column=2)

# mund të shkruhet edhe në këtë mënyrë meqënëse është OOL:
etiketë_teksti4 = Label(dritare_kryesore, text ="Ky është sistemi grid").grid(row=1, column=3)
# por është mirë të ndiqet proçesi me dy hapa


dritare_kryesore.mainloop()


