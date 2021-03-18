from reverso_api.context import ReversoContextAPI
from flask import jsonify


def hello_world(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    request_args = request.args
    requested_parameters = ['source_lang', 'target_lang', 'text']

    if request_args and all([x in request_args for x in requested_parameters]):
        api = ReversoContextAPI(
            request_args['text'],
            '',
            request_args['source_lang'],
            request_args['target_lang'],
        )
        rep = []
        for _, translation, frequency, part_of_speech, _ \
                in api.get_translations():
            elt = {
                'translation': translation,
                'frequency': frequency,
                'part_of_speech': part_of_speech,
            }
            rep.append(elt)
        return jsonify(rep)
    else:
        return ("Request should provide the following get parameters : %s"
                % ", ".join(requested_parameters)), 400
