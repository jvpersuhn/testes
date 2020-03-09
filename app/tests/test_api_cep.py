from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from app.api_cep import _get_somente_numeros, ApiCep

class TesteApiCep(TestCase):
    @patch('app.api_cep.re.sub')
    def test_get_somente_numeros(self, mock_re):
        parametro = '91dadas=*123-987'
        mock_re.return_value = '91123987'

        resultado = _get_somente_numeros(parametro)

        self.assertEqual('91123987', resultado)

        mock_re.assert_called_once_with('[^0-9]', '' ,'91dadas=*123-987')

    @patch('app.api_cep.requests.get')
    @patch('app.api_cep._get_somente_numeros')
    def test_ApiCep_execute(self, mock_get_somente_numeros, mock_request_get):
        apiCep = ApiCep()

        mock_get_somente_numeros.return_value = '89050050'
        mock_request_get.return_value.json.return_value = {'teste' : 'teste'}

        mock_request_get.return_value.json = Mock(return_value={'teste' : 'teste'})

        resultado = apiCep.execute('89050-050')

        self.assertEqual({'teste' : 'teste'},resultado)

        mock_request_get.return_value.json.assert_called_once()

        mock_get_somente_numeros.assert_called_once_with('89050-050')
        mock_request_get.assert_called_once_with('http://www.viacep.com.br/ws/89050050/json/')

