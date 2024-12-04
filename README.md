# firmapdf

 python3 -m venv enviroment

 source enviroment/bin/activate.fish (para fish)

 pip install -r requeriments.txt

 python firmapdf.py

 deactivate

 donde:
  input/documento.pdf -> pdf a firmar
  p12/certificate.p12 -> certificado p12
  output/documento-firmado.pdf -> pdf firmado


crear certificado de test

 mkdir openssl
 cd openssl
 openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
 openssl x509 -text -noout -in certificate.pem
 openssl pkcs12 -inkey key.pem -in certificate.pem -export -out certificate.p12
 openssl pkcs12 -in certificate.p12 -noout -info