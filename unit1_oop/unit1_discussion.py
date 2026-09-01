"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    platform = "Read Write X Studio"

    def __init__(self, title, author):
        """Create a content asset with the information shared by every asset type."""
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author} on {self.platform}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    asset_type = "Interactive article"

    def __init__(self, title, author, topics=None, sections=None):
        super().__init__(title, author)
        # New lists are created for missing values so separate objects do not share state.
        self.topics = list(topics) if topics is not None else []
        self.sections = deepcopy(sections) if sections is not None else []

    def add_section(self, heading, paragraphs):
        """Add a valid section and reject empty content as an edge case."""
        if not heading.strip() or not paragraphs:
            raise ValueError("A section needs a heading and at least one paragraph.")
        self.sections.append({"heading": heading, "paragraphs": list(paragraphs)})

    def word_count(self):
        """Student-created extension: count words across all nested paragraphs."""
        return sum(
            len(paragraph.split())
            for section in self.sections
            for paragraph in section["paragraphs"]
        )

    def describe(self):
        # The override extends, rather than duplicates, the parent's description.
        return (
            f"{super().describe()} | Type: {self.asset_type} | "
            f"Topics: {', '.join(self.topics) if self.topics else 'None'}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    first_article = ChildClass("Human-Centered AI", "Tsahai Banks", ["AI ethics"])
    second_article = ChildClass("The Future of Reading", "Tsahai Banks", ["Publishing"])

    print(f"Class variable through ChildClass: {ChildClass.asset_type}")
    print(f"Same class variable through an object: {first_article.asset_type}")

    # This dynamic attribute belongs only to first_article's instance namespace.
    first_article.review_status = "Editor review"
    print(f"First object namespace: {first_article.__dict__}")
    print(f"Second object namespace: {second_article.__dict__}")
    print(
        "Does the second object have review_status? "
        f"{hasattr(second_article, 'review_status')}"
    )

    # Filter out Python's automatic dunder entries to keep class output readable.
    class_namespace = {
        key: value
        for key, value in ChildClass.__dict__.items()
        if not key.startswith("__")
    }
    print(f"ChildClass namespace keys: {list(class_namespace.keys())}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = ChildClass(
        "Responsible AI Guide",
        "Tsahai Banks",
        ["AI", "Writing"],
        [
            {
                "heading": "Principles",
                "paragraphs": ["Keep authors in control."],
            }
        ],
    )
    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # A shallow copy has a new outer object but shares the nested sections list.
    # A deep copy recursively duplicates the nested list and its dictionaries.
    original.sections[0]["paragraphs"].append("Record the source of AI suggestions.")

    print(f"Original paragraphs: {original.sections[0]['paragraphs']}")
    print(f"Shallow-copy paragraphs: {shallow_copy.sections[0]['paragraphs']}")
    print(f"Deep-copy paragraphs: {deep_copy.sections[0]['paragraphs']}")
    print(
        "Original and shallow copy share sections: "
        f"{original.sections is shallow_copy.sections}"
    )
    print(
        "Original and deep copy share sections: "
        f"{original.sections is deep_copy.sections}"
    )


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n--- Parent Object ---")
    base_asset = ParentClass("Editorial Calendar", "Tsahai Banks")
    print(base_asset.describe())

    print("\n--- Child Object and Inheritance ---")
    article = ChildClass(
        "Designing Humane AI",
        "Tsahai Banks",
        ["AI ethics", "Digital publishing"],
    )
    article.add_section(
        "Author agency",
        ["Writers should decide which AI suggestions become part of their work."],
    )
    print(article.describe())
    print(f"Word count from student-created method: {article.word_count()}")

    print("\n--- Edge Case Test ---")
    empty_article = ChildClass("Untitled Draft", "Tsahai Banks")
    print(f"Empty article word count: {empty_article.word_count()}")
    try:
        empty_article.add_section("", [])
    except ValueError as error:
        print(f"Invalid section handled without crashing: {error}")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
