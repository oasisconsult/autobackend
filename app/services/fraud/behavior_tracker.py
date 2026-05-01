import time
import redis
from app.core.config import settings


r = redis.Redis.from_url(settings.REDIS_URL)


class BehaviorTracker:

    def record_request(self, user_id: str):

        now = int(time.time())

        r.lpush(f"req:{user_id}", now)
        r.ltrim(f"req:{user_id}", 0, 100)

    def get_requests_last_minute(self, user_id: str):

        now = int(time.time())
        timestamps = r.lrange(f"req:{user_id}", 0, -1)

        return sum(
            1 for t in timestamps
            if now - int(t) < 60
        )