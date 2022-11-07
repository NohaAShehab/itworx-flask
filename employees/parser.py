from flask_restful import reqparse


employee_parser = reqparse.RequestParser()
employee_parser.add_argument('name', type=str,
                             help='Employee name is required' , required=True)
employee_parser.add_argument('email', type=str, help='Employee email' )
employee_parser.add_argument('age', type=int)
employee_parser.add_argument('salary', type=int)
employee_parser.add_argument('dept_id', type=int)
