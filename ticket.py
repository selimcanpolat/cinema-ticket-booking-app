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
        pdf.cell(w=0, h=80, txt="Ticket", border=0, align="C", ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=self.user, border=0, ln=1)