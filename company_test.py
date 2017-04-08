class colume(object):

    def __init__(self):
        self.col_name = ""
        self.values = []
        self.input_type = ""
        self.default_value = ""
        self.sort_flag = 0

    def set_type(self, date_type):
        types = ["string", "int", "long", "float", "boolean"]
        date_type = str(date_type).lower()
        if date_type not in types:
            return False
        self.input_type = date_type

    def set_col_name(self, col_name):
        self.col_name = col_name

    def add(self, value):
        self.values.append(value)

    def set_sort_flag(self, sort_flag):
        sort_flag = int(sort_flag)
        if int(sort_flag) in [0,1]:
           self.sort_flag = sort_flag

    def set_default_value(self, value):
        self.default_value = value

    def check_value(self,value):
        return True

    def get_deal_columes(self):
        deal_cols = []
        if self.sort_flag == 0:
            cols = list(set(self.values))
            cols.sort()
            for col in cols:
                cols_value = []
                name = "Flag"+ col
                cols_value.append(name)
                for value in self.values:
                    if value == col:
                        cols_value.append("True")
                    else:
                        cols_value.append("False")
                deal_cols.append(cols_value)
        else:
            value_index = list(set(self.values))
            counts_values = {index: self.values.count(index) for index in value_index}
            counts_values = sorted(counts_values.iteritems(),key=lambda asd:asd[1])








