from django.shortcuts import render, redirect
from django.http import FileResponse
from django.utils.translation import gettext as _
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from user.models import Client
from shoppingCart.models import CartProduct

def generar_pdf(request):
    user = request.user
    response = FileResponse(generate_file(user), as_attachment=True, filename=_('factura.pdf'))
    return response

def generate_file(user):
    from io import BytesIO
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    
    p.setFont("Helvetica-Bold", 20)
    p.setFillColor(colors.HexColor("#1f77b4"))
    p.drawString(50, height - 80, _('Factura de Compra'))

    p.setFont("Helvetica-Bold", 14)
    p.setFillColor(colors.black)
    p.drawString(50, height - 120, _('Nombre del Cliente: {first_name} {last_name}').format(first_name=user.first_name, last_name=user.last_name))
    p.drawString(50, height - 140, _('Email: {email}').format(email=user.email))

    p.setStrokeColor(colors.HexColor("#1f77b4"))
    p.setLineWidth(1.5)
    p.line(50, height - 160, width - 50, height - 160)

    
    y = height - 200
    cart = CartProduct.objects.filter(client=Client.objects.get(user=user))
    total_price = sum(item.product.price * item.quantity for item in cart)

    data = [[_('Producto'), _('Cantidad'), _('Precio Unitario'), _('Precio Total')]]
    for item in cart:
        data.append([
            item.product.name,
            str(item.quantity),
            f"${item.product.price:.2f}",
            f"${item.product.price * item.quantity:.2f}"
        ])
    
    data.append([_('Total'), '', '', f"${total_price:.2f}"])

    table = Table(data, colWidths=[200, 100, 100, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1f77b4")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.whitesmoke]),
    ]))

    table.wrapOn(p, width, height)
    table.drawOn(p, 50, y - len(data) * 25)

    p.setFont("Helvetica-Oblique", 10)
    p.setFillColor(colors.HexColor("#555555"))
    p.drawString(50, 50, _('Gracias por su compra. Si tiene alguna pregunta, no dude en ponerse en contacto con nosotros.'))

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
