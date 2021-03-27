import os
from pycotools3 import model


def load_model(k1, k_minus1, k2):
    # create a base directory to work from
    working_directory = os.path.abspath('')
    filename = f'Model_k1={k1}_kminus1={k_minus1}_k2={k2}.cps'

    # create a string to a copasi file on system
    copasi_filename = os.path.join(working_directory, filename)
    antimony_string = f'''
        model negative_feedback()
            // define compartments
            compartment cell = 1.0
            
            //define species
            S in cell
            P in cell
            C in cell
            I in cell
            
            //define initial conditions
            S      = 1
            C      = 1
            I      = 0
            P      = 0
    
            // reaction parameters
            k1             = {k1}
            k_minus1       = {k_minus1}
            k2             = {k2}
    
            //define reactions
            R1:         S + C => I; cell * k1 * S * C
            R_minus1:   I => S + C; cell * k_minus1 * I
            R3:         I => P + C; cell * k2 * I
    
        end
        '''

    return model.loada(antimony_string, copasi_filename)  # load the model


def change_rate_constants(mod, k1=0.1, k2=0.1, k_minus1=0.1):
    dct = {
      'k1': k1,
      'k2': k2,
      'k_minus1': k_minus1
    }

    mod.insert_parameters(parameter_dict=dct, inplace=True)
    return mod
    # params = negative_feedback.get_parameters_as_dict()


def get_data(mod, stop=100, by=1):
    return mod.simulate(start=0, stop=stop, by=by, variables='mg')


def delete_files():
    my_path = r"C:\Users\AnnabelFlook\PycharmProjects\firstdashapp-py36\\"

    for file_name in os.listdir(my_path):
        if file_name.endswith(('.cps', '.sbml')):
            os.remove(my_path + file_name)
