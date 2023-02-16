from lambda_local.main import call
import lambda_function
import json
from lambda_local.context import Context

def main():
    with open("./sample_event/sample-event.json") as data:
        event = json.load(data)
        context = Context(30)
        call(lambda_function.lambda_handler, event,context)

if __name__ == '__main__':
    main() 