


import pikepdf
old_pdf=pikepdf.Pdf.open("fresume.pdf")
no_extr=pikepdf.Permissions(extract=False)
old_pdf.save("pro_new.pdf",encryption=pikepdf.Encryption(user="123cas",owner="Anuja",allow=no_extr))



