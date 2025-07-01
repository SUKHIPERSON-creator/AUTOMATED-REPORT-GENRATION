from fpdf import FPDF
import pandas as pop
#pandas library is use for read data from excel/csv file.
import matplotlib.pyplot as mr
#matplotlib library is use for plot a graph between x,y-axis.
data=pop.read_excel("C:/Users/PUNJAB TELECOM/Desktop/1.xlsx")
#__.read_excel("name/address (where file is store)")
x=data["Name of subjects"]
y=data['Aakash']
mr.bar(x,y)
mr.title("REPORT OF AAKASH")
mr.savefig("student report card.png")
mr.close()
#mr.show()



pdf=FPDF()
#pdf=FPDF.FPDF("SUKHI.pdf",bottomup=0)
pdf.add_page()

pdf.set_font("Times",size=12)
pdf.cell(200,10,txt="AUTOMATED PDF GENERATION WITH PYTHON",ln=True,align="C")
pdf.cell(200,10,txt="Student marks report card",ln=True,align="C")
#pdf.add_page()
pdf.cell(200,10,txt="Name is aakash",ln=True,align="C")
#pdf.add_page()
pdf.cell(200,10,txt="class is 12th",ln=True,align="C")
pdf.cell(200,10,txt="task complete ",ln=True,align="C")

pdf.ln(10)
pdf.image("student report card.png",x=30,w=170)
pdf.output("aakash final report.pdf")
