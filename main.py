from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pandas.read_csv("topics.csv", sep=",")

for index, row in df.iterrows():
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 21, 200, 21)
        
        # set footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # add writing lines
        ml = 31
        for _ in range(26):
              pdf.line(10, ml, 200, ml)
              ml += 10

        for _ in range(row["Pages"] - 1):
            pdf.add_page()
            
            # set footer
            pdf.ln(277)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

            # add writing lines
            sl = 21
            for _ in range(27):
                pdf.line(10, sl, 200, sl)
                sl += 10

pdf.output("output.pdf")