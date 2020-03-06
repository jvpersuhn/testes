from unittest import TestCase
from unittest.mock import Mock, patch

from run import consulta_api_viacep

class TesteConsultaViaCep(TestCase):
    @patch('run.ApiCep.execute')
    @patch('run.input')
    @patch('run.print')
    def test_request_cep(self, mock_retorno_json, mock_valor_cep, mock_api_cep):
        mock_valor_cep.return_value = '89050050'
        mock_api_cep.return_value = 'teste'
        mock_retorno_json.return_value = {'cep': '89050-050', 'logradouro': 'Rua Nicarágua', 'complemento': '',
                             'bairro': 'Ponta Aguda', 'localidade': 'Blumenau', 'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''}

        resultado = consulta_api_viacep()
        self.assertEqual(resultado, 'Cep consultado com sucesso!')

        mock_api_cep.assert_called_once_with('89050050')

        mock_valor_cep.assert_called_once_with("Informe o cep para consulta: ")

        mock_retorno_json.assert_called_once_with('teste')


