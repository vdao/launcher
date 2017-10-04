from logging import info

from flask import Flask
from flask import jsonify
from flask import request

from public.engine import pick_recommendations
from public.myrequest import RecommendationsRequest
from public.myresponse import RecommendationResponse

app = Flask(__name__)

@app.route('/')
def recommendations():
    request_id = request.args.get('request_id', '')
    view_id = request.args.get('view_id', '')
    user_id = request.args.get('user_id', '')
    recently_viewed = parse_int_list(request.args.get('recently_viewed', ''))
    accepted = parse_int_list(request.args.get('accepted', ''))
    tags = parse_list(request.args.get('tags', ''))
    max_results = request.args.get('max_results', '50')

    info('recommendations(): request_id=%s, view_id=%s, user_id=%s, recently_viewed=%s,accepted=%s, tags=%s, max_results=%s',
        request_id, view_id, user_id, recently_viewed, accepted, tags, max_results)

    request_object = RecommendationsRequest(recently_viewed, accepted, tags, max_results)
    response_object = RecommendationResponse(pick_recommendations(request_object), view_id, request_id)

    response = jsonify(response_object.__dict__)
    info('response=%s', response)
    return response


def parse_int_list(str):
    return [e for e in str.split(",") if (len(e) > 0) & e.isnumeric()]


def parse_list(str):
    return [e for e in str.split(",") if (len(e) > 0)]
