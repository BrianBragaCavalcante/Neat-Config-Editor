def redefinir_arquivo(parametros: list, caminho):
    with open(caminho, 'w') as file:
        text = ['\n[NEAT]',
                f'fitness_criterion     = {parametros[0]}',
                f'fitness_threshold     = {parametros[1]}',
                f'pop_size              = {parametros[2]}',
                f'reset_on_extinction   = {parametros[3]}\n',
                '[DefaultGenome]',
                '# node activation options',
                f'activation_default      = {parametros[4]}',
                f'activation_mutate_rate  = {parametros[5]}',
                f'activation_options      = {parametros[6]}\n',
                '# node aggregation options',
                f'aggregation_default     = {parametros[7]}',
                f'aggregation_mutate_rate = {parametros[8]}',
                f'aggregation_options     = {parametros[9]}\n',
                '# node bias options',
                f'bias_init_mean          = {parametros[10]}',
                f'bias_init_stdev         = {parametros[11]}',
                f'bias_max_value          = {parametros[12]}',
                f'bias_min_value          = {parametros[13]}',
                f'bias_mutate_power       = {parametros[14]}',
                f'bias_mutate_rate        = {parametros[15]}',
                f'bias_replace_rate       = {parametros[16]}\n',
                '# genome compatibility options',
                f'compatibility_disjoint_coefficient = {parametros[17]}',
                f'compatibility_weight_coefficient   = {parametros[18]}\n',
                '# connection add/remove rates',
                f'conn_add_prob           = {parametros[19]}',
                f'conn_delete_prob        = {parametros[20]}\n',
                '# connection enable options',
                f'enabled_default         = {parametros[21]}',
                f'enabled_mutate_rate     = {parametros[22]}\n',
                f'feed_forward            = {parametros[23]}',
                f'initial_connection      = {parametros[24]}\n',
                '# node add/remove rates',
                f'node_add_prob           = {parametros[25]}',
                f'node_delete_prob        = {parametros[26]}\n',
                '# network parameters',
                f'num_hidden              = {parametros[27]}',
                f'num_inputs              = {parametros[28]}',
                f'num_outputs             = {parametros[29]}\n',
                '# node response options',
                f'response_init_mean      = {parametros[30]}',
                f'response_init_stdev     = {parametros[31]}',
                f'response_max_value      = {parametros[32]}',
                f'response_min_value      = {parametros[33]}',
                f'response_mutate_power   = {parametros[34]}',
                f'response_mutate_rate    = {parametros[35]}',
                f'response_replace_rate   = {parametros[36]}\n',
                '# connection weight options',
                f'weight_init_mean        = {parametros[37]}',
                f'weight_init_stdev       = {parametros[38]}',
                f'weight_max_value        = {parametros[39]}',
                f'weight_min_value        = {parametros[40]}',
                f'weight_mutate_power     = {parametros[41]}',
                f'weight_mutate_rate      = {parametros[42]}',
                f'weight_replace_rate     = {parametros[43]}\n',
                '[DefaultSpeciesSet]',
                f'compatibility_threshold = {parametros[44]}\n',
                '[DefaultStagnation]',
                f'species_fitness_func = {parametros[45]}',
                f'max_stagnation       = {parametros[46]}',
                f'species_elitism      = {parametros[47]}\n',
                '[DefaultReproduction]',
                f'elitism            = {parametros[48]}',
                f'survival_threshold = {parametros[49]}',
                ]

        text = '\n'.join(text)
        file.write(text)


class File:
    def __init__(self, caminho=None):
        self.types = {
            'fitness_criterion': str,
            'fitness_threshold': int,
            'pop_size': int,
            'reset_on_extinction': bool,
            'activation_default': str,
            'activation_mutate_rate': float,
            'activation_options': str,
            'aggregation_default': str,
            'aggregation_mutate_rate': float,
            'aggregation_options': str,
            'bias_init_mean': float,
            'bias_init_stdev': float,
            'bias_max_value': float,
            'bias_min_value': float,
            'bias_mutate_power': float,
            'bias_mutate_rate': float,
            'bias_replace_rate': float,
            'compatibility_disjoint_coefficient': float,
            'compatibility_weight_coefficient': float,
            'conn_add_prob': float,
            'conn_delete_prob': float,
            'enabled_default': bool,
            'enabled_mutate_rate': float,
            'feed_forward': bool,
            'initial_connection': str,
            'node_add_prob': float,
            'node_delete_prob': float,
            'num_hidden': int,
            'num_inputs': int,
            'num_outputs': int,
            'response_init_mean': float,
            'response_init_stdev': float,
            'response_max_value': float,
            'response_min_value': float,
            'response_mutate_power': float,
            'response_mutate_rate': float,
            'response_replace_rate': float,
            'weight_init_mean': float,
            'weight_init_stdev': float,
            'weight_max_value': int,
            'weight_min_value': int,
            'weight_mutate_power': float,
            'weight_mutate_rate': float,
            'weight_replace_rate': float,
            'compatibility_threshold': float,
            'species_fitness_func': str,
            'max_stagnation': int,
            'species_elitism': int,
            'elitism': int,
            'survival_threshold': float
        }

        self.default = {
            'fitness_criterion': None,
            'fitness_threshold': None,
            'pop_size': None,
            'reset_on_extinction': None,
            'activation_default': 'random',
            'activation_mutate_rate': None,
            'activation_options': 'sigmoid',
            'aggregation_default': 'random',
            'aggregation_mutate_rate': None,
            'aggregation_options': 'sum',
            'bias_init_mean': None,
            'bias_init_stdev': None,
            'bias_max_value': None,
            'bias_min_value': None,
            'bias_mutate_power': None,
            'bias_mutate_rate': None,
            'bias_replace_rate': None,
            'compatibility_disjoint_coefficient': None,
            'compatibility_weight_coefficient': None,
            'conn_add_prob': None,
            'conn_delete_prob': None,
            'enabled_default': None,
            'enabled_mutate_rate': None,
            'feed_forward': None,
            'initial_connection': 'unconnected',
            'node_add_prob': None,
            'node_delete_prob': None,
            'num_hidden': None,
            'num_inputs': None,
            'num_outputs': None,
            'response_init_mean': None,
            'response_init_stdev': None,
            'response_max_value': None,
            'response_min_value': None,
            'response_mutate_power': None,
            'response_mutate_rate': None,
            'response_replace_rate': None,
            'weight_init_mean': None,
            'weight_init_stdev': None,
            'weight_max_value': None,
            'weight_min_value': None,
            'weight_mutate_power': None,
            'weight_mutate_rate': None,
            'weight_replace_rate': None,
            'compatibility_threshold': None,
            'species_fitness_func': 'mean',
            'max_stagnation': 15,
            'species_elitism': 0,
            'elitism': 0,
            'survival_threshold': 0.2
        }

        self.percentages = [
            'activation_mutate_rate',
            'aggregation_mutate_rate',
            'bias_mutate_rate',
            'bias_replace_rate',
            'conn_add_prob',
            'conn_delete_prob',
            'enabled_mutate_rate',
            'node_add_prob',
            'node_delete_prob',
            'response_mutate_power',
            'response_mutate_rate',
            'response_replace_rate',
            'weight_mutate_power'
            'weight_mutate_rate'
            'weight_replace_rate'
            'survival_threshold'
        ]

        if caminho:
            linhas_se = []
            linhas_co = []
            dicionario = {}

            with open(caminho, 'r') as file:
                linhas = []
                for linha in file:
                    linhas.append(linha.strip())

            for linha in linhas:
                if '[' in linha:
                    linhas.remove(linha)

            for linha in linhas:
                if '#' in linha:
                    linhas.remove(linha)

            for i, linha in enumerate(linhas):
                if linha == '':
                    linhas.pop(i)

            for linha in linhas:
                string_corrigida = ''
                for i in linha:
                    if not (' ' == i):
                        string_corrigida += i
                linhas_se.append(string_corrigida)

            for linha in linhas_se:
                linha = linha.split('=')
                dicionario[linha[0]] = linha[1]
                linhas_co.append(linha[1])

            self.llinhas = linhas_co
            self.dlinhas = dicionario

    def __iter__(self):
        return self.llinhas

    def keys(self):
        return self.dlinhas.keys()

    def __getitem__(self, chave):
        return self.dlinhas[chave]


def main():
    opcao = input('Abrir arquivo (A) Criar arquivo (C): ')
    while True:
        if 'A' in opcao.capitalize():
            caminho = input('Caminho do arquivo: ')
            file = File(caminho)
            break
        elif 'C' in opcao.capitalize():
            caminho = input('Caminho do novo arquivo: ')
            parametros = [File().default[i] for i in File().default]
            redefinir_arquivo(parametros=parametros, caminho=caminho)
            file = File(caminho)
            break
        else:
            print('Escolha uma opção válida!')

    parametros = []
    for i in File().types:
        while True:
            try:
                valor = input(f'{i}: ')
                if valor.capitalize() == 'FALSE':
                    valor = False
                elif valor.capitalize() == 'TRUE':
                    valor = True
                else:
                    valor = File().types[i](valor)
                parametros.append(valor)
                break
            except Exception:
                print('Valor não integro')

    redefinir_arquivo(parametros, caminho)


if __name__ == '__main__':
    main()
