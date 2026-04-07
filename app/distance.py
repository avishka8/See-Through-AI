class DistanceEstimator:
    def estimate(self, width):
        if width == 0:
            return 0
        return (0.5 * 700) / width