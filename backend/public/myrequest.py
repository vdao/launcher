class RecommendationsRequest:
    def __init__(self, viewed, accepted, tags, max_results):
        self.viewed = viewed
        self.accepted = accepted
        self.tags = tags
        self.max_results = max_results
