"""
Makes it easy to create all desired combinations of specified variables. 

All functionality is accessed via the ConditionCollector class.
Focus is on ease-of-use, not on efficiency!
"""
import copy

class CombinationCollector:
    """
    Container class that allows users to register variables with any number of values, which will than be combined to produce all possible combinations.
    """
    def __init__(self):
        """
        Initialize the ConditionCollector class, creating the variable dictionary and an ordered list for variable names. 
        """
        self.val_dict = {}
        self.var_name_list = [] # To preserver ordering 
        self.exception_list = []        
 
    def register_var(self, var_name):
        """
        Register a new variable to be used in combinations. 

        This must be done prior to giving values for that variable.
        Registration order of variables is preserved. 
        First variable registered changes least often as we iterate through all combinations.
        
        Arguments:
        var_name - Name of the variable to register.
        """
        if var_name in self.val_dict.keys():
            print('Error! Variable "' + var_name + '" already registered!')
            exit(-1)
        self.val_dict[var_name] = []
        self.var_name_list.append(var_name)

    def add_val(self, var_name, val):
        """ 
        Add values for the specified variable.
    
        Variable must first be registered via register_var().
        
        Arguments: 
        var_name - The name of the variable to add values for
        val - The value to add to this variable. Supports single values as well as tuples and lists (which will add each value to the variable). 
        """
        if not var_name in self.val_dict.keys():
            print('Error! Variable "' + var_name + '" not registered.')
            print('You must register variables before adding values for them!')
        if type(val) in (list, tuple):
            self.val_dict[var_name] += val
        else:
            self.val_dict[var_name].append(val)

    def get_vals(self, var_name):
        """ 
        Get all values of the specified variable.
        
        Arguments: 
        var_name: Name of the variable to fetch values for.
        """
        return self.val_dict[var_name]  

    def get_combos(self):
        """ 
        Return the all possible combinations of registered variables and their values.
        """
        list_cur = [{}]
        # Iterate through variable in order they were registered
        for var_name in self.var_name_list:
            list_next = []
            for dict_old in list_cur:
                for val in self.val_dict[var_name]:
                    dict_new = copy.deepcopy(dict_old)
                    dict_new[var_name] = val
                    is_exception = False
                    for exception_dict in self.exception_list:
                        is_exception = True
                        for var_name_ex in exception_dict.keys():
                            if var_name_ex not in dict_new.keys():
                                is_exception = False
                                break
                            if dict_new[var_name_ex] != exception_dict[var_name_ex]:
                                is_exception = False
                                break
                        if is_exception:    
                            break
                    if not is_exception:
                        list_next.append(dict_new) 
            list_cur = list_next
        return list_cur
    
    def add_exception(self, exception_dict):
        """
        Add a combination of variables such that any combination that contains this subset will not be included in all combinations.
        
        Arguments: 
        exception_dict - Dictionary of the form {var_name : val, var_name_2 : val_2, ...} where var_name elements are registered variables, and val is a sinlge value or a list/tuple (which all elements of the collection will be used.
        """
        tmp_collect = CombinationCollector() 
        for var_name in exception_dict.keys():
            tmp_collect.register_var(var_name)
            tmp_collect.add_val(var_name, exception_dict[var_name])
        self.exception_list += tmp_collect.get_combos()
 
    def get_str(self, D, sep_in = '_', sep_between = '__'):
        """
        Takes a single entry as a dictionary, and returns it as a string with all info encoded.
        
        Arguments:
        D - Dictionary to turn into a string
        sep_in - separating character/string between variable name and value, _ in VAR_VAL.
        sep_between - separating character/string between two variables, -- in VAR1_VAL--VAR2_VAL.
        """
        s = ''
        for key_idx in range(len(self.var_name_list)):
            key = self.var_name_list[key_idx]
            if type(D[key]) in (tuple, list):
                print('Error! dict_to_str cannot handle values that are lists are tuples!')
                exit(-1)
            if key_idx != 0:
                s += sep_between
            s += key + sep_in + str(D[key])
        return s 

    def get_dict(self, s, sep_in = '_', sep_between = '__'):
        """
        Takes a string and returns it as a dictionary for one combination of variables
        
        Arguments:
        s - String to create a dictionary from.
        sep_in - separating character/string between variable name and value, _ in VAR_VAL.
        sep_between - separating character/string between two variables, -- in VAR1_VAL--VAR2_VAL.
        """
        D = {}
        str_parts = s.split(sep_between)
        for str_part in str_parts:
            var_name, val = str_part.split(sep_in) 
            D[var_name] = val
        return D 
        
 
if __name__ == '__main__':
    combos = CombinationCollector()
    #combos.register_var('test')
    #combos.add_val('test', 127)
    #combos.add_val('test', [67, 56, 234])
    #print(combos.get_vals('test'))
    #combos.register_var('foo')
    #combos.add_val('foo', ['a', 'b', 'c'])
    for letter in ['a', 'b', 'c', 'd']:
        combos.register_var(letter)
        combos.add_val(letter, list(range(0, 10)))
    combos.add_exception({'a' : [1,2,3,4,5,6,8,9]})
    combos.add_exception({'b' : [1,3,5,7,9]})
    combos.add_exception({'c' : [0,2,4,6,8]})
    res = combos.get_combos()
    for x in res:
        print(x)
        #print(combos.get_str(x))
        #print(str_to_dict(dict_to_str(x)))
