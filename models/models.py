import os


def reset_file(parameters: list, path):
    with open(path, 'w') as file:
        text = ['\n[NEAT]',
                f'fitness_criterion     = {parameters[0]}',
                f'fitness_threshold     = {parameters[1]}',
                f'pop_size              = {parameters[2]}',
                f'reset_on_extinction   = {parameters[3]}\n',
                '[DefaultGenome]',
                '# node activation options',
                f'activation_default      = {parameters[4]}',
                f'activation_mutate_rate  = {parameters[5]}',
                f'activation_options      = {parameters[6]}\n',
                '# node aggregation options',
                f'aggregation_default     = {parameters[7]}',
                f'aggregation_mutate_rate = {parameters[8]}',
                f'aggregation_options     = {parameters[9]}\n',
                '# node bias options',
                f'bias_init_mean          = {parameters[10]}',
                f'bias_init_stdev         = {parameters[11]}',
                f'bias_max_value          = {parameters[12]}',
                f'bias_min_value          = {parameters[13]}',
                f'bias_mutate_power       = {parameters[14]}',
                f'bias_mutate_rate        = {parameters[15]}',
                f'bias_replace_rate       = {parameters[16]}\n',
                '# genome compatibility options',
                f'compatibility_disjoint_coefficient = {parameters[17]}',
                f'compatibility_weight_coefficient   = {parameters[18]}\n',
                '# connection add/remove rates',
                f'conn_add_prob           = {parameters[19]}',
                f'conn_delete_prob        = {parameters[20]}\n',
                '# connection enable options',
                f'enabled_default         = {parameters[21]}',
                f'enabled_mutate_rate     = {parameters[22]}\n',
                f'feed_forward            = {parameters[23]}',
                f'initial_connection      = {parameters[24]}\n',
                '# node add/remove rates',
                f'node_add_prob           = {parameters[25]}',
                f'node_delete_prob        = {parameters[26]}\n',
                '# network parameters',
                f'num_hidden              = {parameters[27]}',
                f'num_inputs              = {parameters[28]}',
                f'num_outputs             = {parameters[29]}\n',
                '# node response options',
                f'response_init_mean      = {parameters[30]}',
                f'response_init_stdev     = {parameters[31]}',
                f'response_max_value      = {parameters[32]}',
                f'response_min_value      = {parameters[33]}',
                f'response_mutate_power   = {parameters[34]}',
                f'response_mutate_rate    = {parameters[35]}',
                f'response_replace_rate   = {parameters[36]}\n',
                '# connection weight options',
                f'weight_init_mean        = {parameters[37]}',
                f'weight_init_stdev       = {parameters[38]}',
                f'weight_max_value        = {parameters[39]}',
                f'weight_min_value        = {parameters[40]}',
                f'weight_mutate_power     = {parameters[41]}',
                f'weight_mutate_rate      = {parameters[42]}',
                f'weight_replace_rate     = {parameters[43]}\n',
                '[DefaultSpeciesSet]',
                f'compatibility_threshold = {parameters[44]}\n',
                '[DefaultStagnation]',
                f'species_fitness_func = {parameters[45]}',
                f'max_stagnation       = {parameters[46]}',
                f'species_elitism      = {parameters[47]}\n',
                '[DefaultReproduction]',
                f'elitism            = {parameters[48]}',
                f'survival_threshold = {parameters[49]}',
                ]

        text = '\n'.join(text)
        file.write(text)


def count_files(path):
    items = os.listdir(path)
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]
    return len(files)


class File:
    def __init__(self, path=None, parameters=None):
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
            'weight_max_value': float,
            'weight_min_value': float,
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
            'fitness_criterion': 'max',
            'fitness_threshold': 1,
            'pop_size': 1,
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
            'survival_threshold': 20
        }
        self.percentages = [
            'activation_mutate_rate',
            'aggregation_mutate_rate',
            'bias_mutate_power',
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
            'weight_mutate_power',
            'weight_mutate_rate',
            'weight_replace_rate',
            'survival_threshold'
        ]
        self.parameters = [
            'fitness_criterion',
            'fitness_threshold',
            'pop_size',
            'reset_on_extinction',
            'activation_default',
            'activation_mutate_rate',
            'activation_options',
            'aggregation_default',
            'aggregation_mutate_rate',
            'aggregation_options',
            'bias_init_mean',
            'bias_init_stdev',
            'bias_max_value',
            'bias_min_value',
            'bias_mutate_power',
            'bias_mutate_rate',
            'bias_replace_rate',
            'compatibility_disjoint_coefficient',
            'compatibility_weight_coefficient',
            'conn_add_prob',
            'conn_delete_prob',
            'enabled_default',
            'enabled_mutate_rate',
            'feed_forward',
            'initial_connection',
            'node_add_prob',
            'node_delete_prob',
            'num_hidden',
            'num_inputs',
            'num_outputs',
            'response_init_mean',
            'response_init_stdev',
            'response_max_value',
            'response_min_value',
            'response_mutate_power',
            'response_mutate_rate',
            'response_replace_rate',
            'weight_init_mean',
            'weight_init_stdev',
            'weight_max_value',
            'weight_min_value',
            'weight_mutate_power',
            'weight_mutate_rate',
            'weight_replace_rate',
            'compatibility_threshold',
            'species_fitness_func',
            'max_stagnation',
            'species_elitism',
            'elitism',
            'survival_threshold'
        ]
        self.listLines = []
        self.dictLines = {}

        if parameters:
            for i in parameters:
                value = self.types[i](parameters[i])
                if i in self.percentages:
                    value /= 100
                if i == 'on':
                    value = 'True'
                if i == 'off':
                    value = 'False'

                self.dictLines[i] = value
                self.listLines.append(value)

        if path:
            lines_se = []

            with open(path, 'r') as file:
                lines = []
                for line in file:
                    lines.append(line.strip())

            for line in lines:
                if '[' in line:
                    lines.remove(line)

            for line in lines:
                if '#' in line:
                    lines.remove(line)

            for i, line in enumerate(lines):
                if line == '':
                    lines.pop(i)

            for line in lines:
                string_corrigida = ''
                for i in line:
                    if not (' ' == i):
                        string_corrigida += i
                lines_se.append(string_corrigida)

            for line in lines_se:
                line = line.split('=')
                self.dictLines[line[0]] = line[1]
                self.listLines.append(line[1])

    def save(self, path):
        reset_file(self.listLines, path)
