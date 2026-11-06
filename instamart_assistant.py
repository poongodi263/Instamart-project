"""A small CLI prototype for an Instamart-inspired grocery assistant.

This starter uses a local sample catalog, so it runs without API keys or
third-party packages. It is not connected to Instamart or an LLM yet.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    category: str
    price: float
    keywords: tuple[str, ...]


PRODUCTS = [
    Product("Organic bananas", "Fruit", 1.99, ("banana", "fruit", "organic", "snack")),
    Product("Red apples (4 pack)", "Fruit", 3.49, ("apple", "fruit", "snack")),
    Product("Whole milk", "Dairy", 2.79, ("milk", "dairy", "breakfast")),
    Product("Oat milk", "Dairy-free", 3.29, ("oat", "milk", "dairy-free", "breakfast")),
    Product("Brown bread", "Bakery", 2.49, ("bread", "bakery", "breakfast", "sandwich")),
    Product("Free-range eggs (6 pack)", "Dairy", 3.99, ("eggs", "protein", "breakfast")),
    Product("Baby spinach", "Vegetables", 2.99, ("spinach", "vegetable", "salad", "healthy")),
    Product("Pasta (500 g)", "Pantry", 1.89, ("pasta", "pantry", "dinner")),
]


def find_products(query: str) -> list[Product]:
    """Return catalog items whose names, categories, or keywords match a query."""
    words = set(query.lower().split())
    if not words:
        return []

    matches = []
    for product in PRODUCTS:
        searchable_text = " ".join(
            (product.name, product.category, *product.keywords)
        ).lower()
        if any(word in searchable_text for word in words):
            matches.append(product)
    return matches


def main() -> None:
    print("Instamart Grocery Assistant — demo")
    print("Try: 'fruit', 'breakfast', 'milk', or 'dinner'. Type 'quit' to exit.\n")

    while True:
        query = input("What are you shopping for? ").strip()
        if query.lower() in {"quit", "exit"}:
            print("Happy shopping!")
            break

        matches = find_products(query)
        if not matches:
            print("I couldn't find a match in the sample catalog. Try another search.\n")
            continue

        print("Here are some options:")
        for product in matches:
            print(f"- {product.name} ({product.category}) — ${product.price:.2f}")
        print()


if __name__ == "__main__":
    main()
