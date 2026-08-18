"""
# Design Pattern: Builder (Creational)

## Intent
Separates the construction of a complex object from its representation, allowing the same construction process to create various representations.

## Use Cases
- Constructing complex SQL queries step-by-step.
- Building HTTP Request objects with headers, query params, body, timeout.
- Configuring complex system components without telescoping constructors.
"""

from typing import Optional, Dict, Any


class HttpRequest:
    """The complex product class."""

    def __init__(self):
        self.method: str = "GET"
        self.url: str = ""
        self.headers: Dict[str, str] = {}
        self.params: Dict[str, str] = {}
        self.body: Optional[str] = None
        self.timeout: int = 30
        self.follow_redirects: bool = True

    def __repr__(self) -> str:
        return (
            f"HttpRequest(method={self.method}, url={self.url}, "
            f"headers={self.headers}, params={self.params}, body={self.body}, "
            f"timeout={self.timeout})"
        )


class HttpRequestBuilder:
    """Fluent Builder for HttpRequest objects."""

    def __init__(self):
        self.reset()

    def reset(self) -> "HttpRequestBuilder":
        self._request = HttpRequest()
        return self

    def set_method(self, method: str) -> "HttpRequestBuilder":
        self._request.method = method.upper()
        return self

    def set_url(self, url: str) -> "HttpRequestBuilder":
        self._request.url = url
        return self

    def add_header(self, key: str, value: str) -> "HttpRequestBuilder":
        self._request.headers[key] = value
        return self

    def add_param(self, key: str, value: str) -> "HttpRequestBuilder":
        self._request.params[key] = value
        return self

    def set_body(self, body: str) -> "HttpRequestBuilder":
        self._request.body = body
        return self

    def set_timeout(self, timeout: int) -> "HttpRequestBuilder":
        self._request.timeout = timeout
        return self

    def build(self) -> HttpRequest:
        if not self._request.url:
            raise ValueError("URL is required to build an HttpRequest")
        request = self._request
        self.reset()  # Reset for subsequent builds
        return request


# Director (Optional helper to build standardized configurations)
class HttpRequestDirector:
    def __init__(self, builder: HttpRequestBuilder):
        self.builder = builder

    def build_json_post(self, url: str, json_body: str) -> HttpRequest:
        return (
            self.builder.reset()
            .set_method("POST")
            .set_url(url)
            .add_header("Content-Type", "application/json")
            .add_header("Accept", "application/json")
            .set_body(json_body)
            .build()
        )


# =====================================================================
# Tests
# =====================================================================
def test_builder():
    builder = HttpRequestBuilder()
    req = (
        builder.set_method("GET")
        .set_url("https://api.example.com/users")
        .add_header("Authorization", "Bearer token123")
        .add_param("page", "1")
        .add_param("limit", "20")
        .set_timeout(10)
        .build()
    )

    assert req.method == "GET"
    assert req.url == "https://api.example.com/users"
    assert req.headers["Authorization"] == "Bearer token123"
    assert req.params["page"] == "1"
    assert req.timeout == 10

    director = HttpRequestDirector(builder)
    post_req = director.build_json_post("https://api.example.com/items", '{"name": "Laptop"}')
    assert post_req.method == "POST"
    assert post_req.headers["Content-Type"] == "application/json"
    assert post_req.body == '{"name": "Laptop"}'


if __name__ == "__main__":
    test_builder()
    print("Builder tests passed successfully! [OK]")
