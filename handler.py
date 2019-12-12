from flask_restful import Resource, reqparse
import equation_parser
import diagrams_builder
from diagrams_builder.diagram_data import DiagramData


parser = reqparse.RequestParser()
parser.add_argument('equation', type=str, location='json')
parser.add_argument('dataset', type=list, location='json')


class DiagramBuilder(Resource):

    def post(self):
        args = parser.parse_args()
        print(args)

        equation: str = args["equation"]
        dataset: list = args["dataset"]

        if len(equation) == 0:
            return "equation is empty", 400

        if len(dataset) == 0:
            return "dataset is empty", 400

        equation = equation_parser.process_str(equation)

        data: DiagramData = diagrams_builder.build_diagram(equation, dataset)
        return data.to_dict(), 200
