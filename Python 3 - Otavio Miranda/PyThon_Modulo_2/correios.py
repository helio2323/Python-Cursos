import requests
import xml.etree.ElementTree as ET

# Código do serviço.
# 40010 SEDEX
# 41106 PAC
# http://www.correios.com.br/webServices/PDF/SCPP_manual_implementacao_calculo_remoto_de_precos_e_prazos.pdf

params = {
    'nCdEmpresa': '',
    'sDsSenha': '',
    'sCepOrigem': '74380150',
    'sCepDestino': '43810040',
    'nVlPeso': '5',
    'nCdFormato': '1',
    'nVlComprimento': '16',
    'nVlAltura': '5',
    'nVlLargura': '15',
    'nVlDiametro': '0',
    'sCdMaoPropria': 's',
    'nVlValorDeclarado': '200',
    'sCdAvisoRecebimento': 'n',
    'StrRetorno': 'xml',
    'nCdServico': '40010,41106'
}

url = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx'

response = requests.get(url, params=params)
root = ET.fromstring(response.content)

for row in root.findall(".//cServico"):
    print(ET.tostring(row, encoding='unicode', method='xml'))