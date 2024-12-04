#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyhanko import stamp
from pyhanko.pdf_utils import text, images
from pyhanko.pdf_utils.font import opentype
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import fields, signers

def firma_pdf():
    path = 'input/documento.pdf'
    path_cert = 'p12/certificate.p12'
    signer = signers.SimpleSigner.load_pkcs12(pfx_file=path_cert)
    with open(path, 'rb') as inf:
        w = IncrementalPdfFileWriter(inf)
        fields.append_signature_field(w, sig_field_spec=fields.SigFieldSpec('Signature', box=(20, 20, 220, 80)))

        meta = signers.PdfSignatureMetadata(field_name='Signature')
        pdf_signer = signers.PdfSigner(
            meta, signer=signer, stamp_style=stamp.TextStampStyle(
                # the 'signer' and 'ts' parameters will be interpolated by pyHanko, if present
                stamp_text='Prueba Firma PDF\nFirmado por: %(signer)s\nTime: %(ts)s',
                text_box_style=text.TextBoxStyle(
                    font=opentype.GlyphAccumulatorFactory('NotoSans-Regular.ttf')
                ),
                background=images.PdfImage('logomr1.png')
            ),
        )
        with open('/output/documento-firmado.pdf', 'wb') as outf:
            pdf_signer.sign_pdf(w, output=outf)