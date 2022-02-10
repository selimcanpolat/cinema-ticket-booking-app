from fpdf import FPDF


class Ticket:
    def __init__(self, id, user, price, seat):
        self.seat = seat
        self.price = price
        self.user = user
        self.id = id

    def to_pdf(self, path):
        self.path = path

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt=" Your Digital Ticket", border=1, align="C", ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=25, txt="Name:", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=150, h=40, txt=self.user, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Price", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Seat Number:", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.seat), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.output(f"digital_ticket{self.id}.pdf","F")