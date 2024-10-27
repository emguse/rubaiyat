from typing import List

from sqlmodel import Field, Relationship, SQLModel


class Rubaiyat(SQLModel, table=True):
    id: int = Field(primary_key=True)
    is_with_parentheses: bool
    section: str = Field(max_length=1024)
    poem_body: str = Field(max_length=1024)
    poem_body_with_ruby: str = Field(max_length=1024)
    is_boozeism: bool
    footnote: str | None = Field(max_length=1024)

    # Relationship: Rubaiyat has multiple tags
    tags: List["YourTag"] = Relationship(back_populates="rubaiyat")


class YourTag(SQLModel, table=True):
    tag_id: int | None = Field(default=None, primary_key=True)
    rubaiyat_id: int = Field(default=None, foreign_key="rubaiyat.id")
    tag: str = Field(max_length=100)

    # Relationship: A tag is associated with one Rubaiyat
    rubaiyat: "Rubaiyat" = Relationship(back_populates="tags")
