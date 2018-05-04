

class UrlTool:

    @staticmethod
    def url_params_from_dict(parameters: dict, **keywords):
        # if parameters:
        #     parameters = {}
        paras: list = []
        for k, v in parameters.items():
            paras.append('{}={}'.format(k, v))
        url: str = ''
        if 'baseUrl' in keywords.keys():
            url += keywords['baseUrl']
        if 'subUrl' in keywords.keys():
            url += keywords['subUrl']

        if len(paras) > 0:
            url += '?' + '&'.join(paras)
        return url
