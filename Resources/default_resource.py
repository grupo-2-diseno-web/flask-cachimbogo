from flask_restful import Resource, reqparse


class DefaultResource(Resource):

    def __init__(self):
        self.parser = None
        self.args = None

    def get_paser(self):
        return reqparse.RequestParser()

    def set_params(self, params_name, types, helps):
        self.parser = reqparse.RequestParser()
        i = 0
        length = len(params_name)
        while length > i:
            if types[i] is "int":
                self.parser.add_argument(params_name[i], type=int,
                                         help=helps[i])
            if types[i] is "string":
                self.parser.add_argument(params_name[i], type=str,
                                         help=helps[i])
            i += 1

    def get_params(self, params_name):
        return [self.args[param_name] for param_name in params_name]

    def check_params(self):
        self.args = self.parser.parse_args()
        for arg in self.args.values():
            if arg is None:
                return False
        return True
