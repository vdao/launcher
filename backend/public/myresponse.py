class RecommendationResponse:
    def __init__(self, offers, view_id, request_id):
        self.offers = offers
        self.view_id = view_id
        self.request_id = request_id