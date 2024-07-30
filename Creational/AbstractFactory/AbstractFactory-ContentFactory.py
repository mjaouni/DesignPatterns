from abc import ABC, abstractmethod


# Abstract Header
class Header(ABC):
    @abstractmethod
    def render(self):
        pass


# Abstract Footer
class Footer(ABC):
    @abstractmethod
    def render(self):
        pass


# Abstract Article
class Article(ABC):
    @abstractmethod
    def render(self):
        pass


# Basic Plan Concreate Header
class BasicHeader(Header):
    def render(self) -> str:
        return "<header><h1>Basic Plan - Welcome!</h1></header>"


# Premium Plan Concreate Header
class PremiumHeader(Header):
    def render(self) -> str:
        return "<header><h1>Premium Plan - Welcome!</h1></header>"


# Basic Plan Concreate Footer
class BasicFooter(Footer):
    def render(self) -> str:
        return "<footer><p>Basic Plan - &copy; 2024 CMS Inc.</p></footer>"


# Premium Plan Concreate Footer
class PremiumFooter(Footer):
    def render(self) -> str:
        return "<footer><p>Premium Plan - &copy; 2024 CMS Inc.</p></footer>"


# Basic Plan Concreate Article
class BasicArticle(Article):
    def render(self) -> str:
        return "<article><p>This is a basic article. Upgrade to Premium for more content.</p></article>"


# Premium Plan Concreate Article
class PremiumArticle(Article):
    def render(self) -> str:
        return ("<article><h2>Premium Content</h2><p>Full access to premium articles with detailed "
                "insights.</p></article>")


# Abstract Factory
class ContentFactory(ABC):
    def create_header(self) -> Header:
        pass

    def create_footer(self) -> Footer:
        pass

    def create_article(self) -> Article:
        pass


# Basic Content Concreate Factory
class BasicContentFactory(ContentFactory):
    def create_header(self) -> Header:
        return BasicHeader()

    def create_footer(self) -> Footer:
        return BasicFooter()

    def create_article(self) -> Article:
        return BasicArticle()


# Premium Content Concreate Factory
class PremiumContentFactory(ContentFactory):
    def create_header(self) -> Header:
        return PremiumHeader()

    def create_footer(self) -> Footer:
        return PremiumFooter()

    def create_article(self) -> Article:
        return PremiumArticle()


def client_code(factory: ContentFactory) -> None:
    header = factory.create_header()
    footer = factory.create_footer()
    article = factory.create_article()

    print(header.render())
    print(footer.render())
    print(article.render())

client_code(BasicContentFactory())
client_code(PremiumContentFactory())
