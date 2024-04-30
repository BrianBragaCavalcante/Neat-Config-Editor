class File:
    def __init__(self, caminho=None):
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

    def redefinir_arquivo(self, parametros: list, caminho):
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


file = File()

file.redefinir_arquivo(parametros=[], caminho='teste.txt')
