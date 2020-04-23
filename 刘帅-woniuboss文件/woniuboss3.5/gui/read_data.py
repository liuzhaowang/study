class ReadData:
    def read_data(self):
        with open('./login_data','r') as file:
            results = file.readlines()
            for result in results:
                result = result.strip().split(',')
                username = result[0]
                password = result[1]
                verifycode = result[2]
                # print(username,password,verifycode)
        return username,password,verifycode

# if __name__ == '__main__':
#     read_data()