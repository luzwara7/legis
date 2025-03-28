from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_cv(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Encabezado
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "Currículum Vitae")
    
    # Información personal
    c.setFont("Helvetica", 14)
    c.drawString(50, height - 100, "Nombre: Juan Pérez")
    c.drawString(50, height - 120, "Correo: juan.perez@email.com")
    c.drawString(50, height - 140, "Teléfono: +123456789")
    c.drawString(50, height - 160, "Ubicación: Ciudad, País")
    
    # Experiencia laboral
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 200, "Experiencia Laboral")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 220, "- Desarrollador Web en Empresa XYZ (2020 - Presente)")
    c.drawString(50, height - 240, "  * Desarrollo de aplicaciones web con Python y Django")
    c.drawString(50, height - 260, "  * Optimización de bases de datos SQL")
    
    c.drawString(50, height - 280, "- Analista de Datos en Empresa ABC (2018 - 2020)")
    c.drawString(50, height - 300, "  * Análisis de datos con Pandas y NumPy")
    c.drawString(50, height - 320, "  * Creación de reportes automatizados")
    
    # Educación
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 360, "Educación")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 380, "- Licenciatura en Ingeniería de Sistemas, Universidad ABC (2014 - 2018)")
    
    # Habilidades
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 420, "Habilidades")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 440, "- Python, Django, Flask")
    c.drawString(50, height - 460, "- SQL, PostgreSQL, MySQL")
    c.drawString(50, height - 480, "- JavaScript, React, HTML, CSS")
    c.drawString(50, height - 500, "- Análisis de datos, Machine Learning")
    
    c.save()
    print(f"Currículum generado: {filename}")

# Generar el PDF
generate_cv("curriculum.pdf")
