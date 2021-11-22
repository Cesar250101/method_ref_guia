# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class NotaVenta(models.Model):
    _inherit = 'sale.order'


    @api.multi
    def _prepare_invoice(self):
        vals = super(NotaVenta, self)._prepare_invoice()
        guias=self.env['stock.picking'].search([('sale_id','=',self.id),('use_documents','=',True),('state','=','done')])
        if guias:
            tipo_docto=self.env['sii.document_class'].search([('sii_code','=',52)],limit=1).id
            vals["referencias"] = []
            for ref in guias:
                vals["referencias"].append(
                    (
                        0,
                        0,
                        {
                            "origen": ref.name,
                            "sii_referencia_TpoDocRef": tipo_docto,
                            "fecha_documento": str(ref.date),
                        },
                    )
                )
        return vals        

    
