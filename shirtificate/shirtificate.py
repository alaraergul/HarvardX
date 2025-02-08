from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

def create_shirtificate(name):
    pdf = PDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 40)
    pdf.set_text_color(255, 255, 255)  

    pdf.image("shirtificate.png", x = 10, y = 50, w = 190)

    name_width = pdf.get_string_width(name)
    pdf.text((210 - name_width) / 2, 140, name)

    pdf.output("shirtificate.pdf")

def main():
    name = input("Enter your name: ")
    create_shirtificate(name)

if __name__ == "__main__":
    main()
