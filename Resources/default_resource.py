from flask_restful import Resource, reqparse

class DefaultResource(Resource):

    def __init__(self):
        self.parser = None

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
        args = self.parser.parse_args()
        return [args[param_name] for param_name in params_name]