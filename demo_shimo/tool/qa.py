class qa():
    def data_handle(self, input_data, file_name):
        datas = [data.split("=>") for data in input_data]
        data_str = ""
        for data in datas:
            my_data = '<p>[{}]{}</p>\t{}\n'.format(file_name, data[0], data[1])
            data_str += my_data
        return data_str

