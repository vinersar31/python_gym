"""
# Design Pattern: Chain of Responsibility (Behavioral)

## Intent
Avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
Chains the receiving objects and passes the request along the chain until an object handles it.

## Use Cases
- HTTP Middleware request pipelines (Auth -> Rate Limiting -> Logging -> Request Handling).
- Support ticketing escalation (Level 1 Support -> Level 2 Engineer -> Lead Architect).
- Input validation workflows.
"""

from abc import ABC, abstractmethod
from typing import Optional


# 1. Request Object
class Request:
    def __init__(self, user: str, role: str, is_authenticated: bool, request_rate: int):
        self.user = user
        self.role = role
        self.is_authenticated = is_authenticated
        self.request_rate = request_rate  # requests per minute


# 2. Handler Interface
class MiddlewareHandler(ABC):
    def __init__(self, next_handler: Optional["MiddlewareHandler"] = None):
        self._next_handler = next_handler

    def set_next(self, handler: "MiddlewareHandler") -> "MiddlewareHandler":
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Request) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


# 3. Concrete Handlers
class AuthenticationMiddleware(MiddlewareHandler):
    def handle(self, request: Request) -> Optional[str]:
        if not request.is_authenticated:
            return "401 Unauthorized: User is not authenticated"
        return super().handle(request)


class RateLimitingMiddleware(MiddlewareHandler):
    def __init__(self, max_rate: int = 100, next_handler: Optional[MiddlewareHandler] = None):
        super().__init__(next_handler)
        self.max_rate = max_rate

    def handle(self, request: Request) -> Optional[str]:
        if request.request_rate > self.max_rate:
            return "429 Too Many Requests: Rate limit exceeded"
        return super().handle(request)


class RoleAuthorizationMiddleware(MiddlewareHandler):
    def __init__(self, required_role: str, next_handler: Optional[MiddlewareHandler] = None):
        super().__init__(next_handler)
        self.required_role = required_role

    def handle(self, request: Request) -> Optional[str]:
        if request.role != self.required_role:
            return f"403 Forbidden: Requires role '{self.required_role}'"
        return super().handle(request)


# =====================================================================
# Tests
# =====================================================================
def test_chain_of_responsibility():
    # Build chain: Auth -> RateLimit (max 50) -> RoleCheck (admin)
    auth = AuthenticationMiddleware()
    rate = RateLimitingMiddleware(max_rate=50)
    role = RoleAuthorizationMiddleware(required_role="admin")
    auth.set_next(rate).set_next(role)

    # 1. Unauthenticated request fails at step 1
    req1 = Request(user="alice", role="admin", is_authenticated=False, request_rate=10)
    assert "401 Unauthorized" in auth.handle(req1)

    # 2. High rate request fails at step 2
    req2 = Request(user="bob", role="admin", is_authenticated=True, request_rate=120)
    assert "429 Too Many Requests" in auth.handle(req2)

    # 3. Wrong role fails at step 3
    req3 = Request(user="charlie", role="viewer", is_authenticated=True, request_rate=20)
    assert "403 Forbidden" in auth.handle(req3)

    # 4. Valid admin passes the entire chain
    req4 = Request(user="david", role="admin", is_authenticated=True, request_rate=20)
    assert auth.handle(req4) is None  # Handled cleanly without errors


if __name__ == "__main__":
    test_chain_of_responsibility()
    print("Chain of Responsibility tests passed successfully! [OK]")
